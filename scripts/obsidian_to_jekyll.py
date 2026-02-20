import os
import re
from pathlib import Path
from datetime import datetime
import subprocess
# lmao i wrote this IN obsidian aint that weird

POSTS_DIR = "./_posts"
PUBLISHED_DIR = "./published"
# IGNORE vault/

# idk about globals. its easy.
title = ""


def get_first_commit_date(filepath):
    try:
        result = subprocess.check_output(
            ["git", "log", "--diff-filter=A", "--follow", "--format=%aI", "--", filepath],
            stderr=subprocess.DEVNULL
        ).decode().strip()

        # git returns multiple lines sometimes; we want the oldest
        lines = result.splitlines()
        return lines[-1] if lines else None

    except subprocess.CalledProcessError:
        return None
def get_last_commit_date(filepath):
    try:
        result = subprocess.check_output(
            ["git", "log", "-1", "--format=%aI", "--", filepath],
            stderr=subprocess.DEVNULL
        ).decode().strip()

        return result if result else None

    except subprocess.CalledProcessError:
        return None

def slugify(title):
    title = title.lower()
    title = re.sub(r'[^a-z0-9\s-]', '', title) # dont wanna generate invalid urls
    title = re.sub(r'\s+', '-', title)
    return title

def replace_wikilink(match):
    #[[published/This is a note!|This is a note!]]
    #Got: [published/This is a note!|This is a note!](/published/this-is-a-note!|this-is-a-note!)
    #Expected: [This is a note!](/this-is-a-note!)

    file = match.group(1) # published/This is a note!
    # we don't want the published/ in the final file
    alias = match.group(2)
    display = alias if alias else Path(file).stem
    slug = slugify(Path(file).stem)
    return f"[{display}](/{slug})"

def replace_image(match):
    image = match.group(1)
    return f"![{image}](/assets/{image})"

def add_frontmatter(content, filepath):
    first_commit = get_first_commit_date(filepath)
    last_commit = get_last_commit_date(filepath)
    title = Path(filepath).stem

    if not first_commit: # if somehow everything breaks.
        first_commit: datetime.today().strftime("%Y-%m-%d")
    if not last_commit:
        last_commit = first_commit

    return f"""---
layout: post
title: "{title}"
date: {first_commit}
last_modified_at: {last_commit}
tags: []
---

{content}
"""

def convert_file(filepath):
    # ok so filepath will be from root all the way to 
    with open(filepath, "r") as f:
        content = f.read()

    # ok this looks bad. the regex just finds anything like ![[MATCH]] and then runs the fallback function on it
    content = re.sub(r"!\[\[([^\]]+)\]\]", replace_image, content)
    # very similar, [[MATCH1|OPTIONALMATCH2]]
    content = re.sub(r"\[\[([^|\]]+)(?:\|([^\]]+))?\]\]"
, replace_wikilink, content) # if a link doesnt have a | i might be screwed.

    content = add_frontmatter(content,filepath)
    

    # generate output path
    # filepath is {PUBLISH_DIR}/possible_subfolders/FILE
    # just replace publish dir duh
    output_filepath = filepath.replace(PUBLISHED_DIR, POSTS_DIR)
    # since were allowing subfolders, create the proper structure first



    Path(output_filepath).parent.mkdir(parents=True, exist_ok=True)
    with open(output_filepath, "w") as f:
        f.write(content)


def process_all():
    for root, dirs, files in os.walk(PUBLISHED_DIR):
        for file in files:
            # if file.endswith(".md"): # do we want this??
            print(os.path.join(root,file))
            convert_file(os.path.join(root,file))

process_all()
