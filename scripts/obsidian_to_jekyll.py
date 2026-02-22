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

    file = match.group(1)
    alias = match.group(2)

    path = Path(file)
    # removed published/

    # UGHHH new little hitch.
    # so if a/b/note1 links to a/b/note2
    # its a RELATIVE PATH so its only [[note2]]
    # we need to make sure that it includes the path down to published. 

    parts = list(path.parts)
    if parts and parts[0] == "published":
        parts = parts[1:]
    else:
        print("::error::ERROR: A WIKILINK IS NOT PROPERLY ROOTED, WILL NOT WORK")
        # sys.exit(0) 
    
    cleaned_path = Path(*parts)

    slug = slugify(cleaned_path.stem)

    parent = cleaned_path.parent
    if parent == Path("."):
        url = f"/{slug}/"
    else:
        categories = "/".join(slugify(p) for p in parent.parts) # add each slugged directory
        url = f"/{categories}/{slug}/"
    display = alias if alias else cleaned_path.stem
    return f"[{display}]({url})"

def replace_image(match):
    image = match.group(1)
    return f"![{image}](/assets/{image})"

def iso_to_date(iso_string):
    if not iso_string:
        print("::error:: DATE NOT CREATED PROPERLY")
        return datetime.today().strftime("%Y-%m-%d")
    return iso_string[:10]

def convert_file(filepath):
    # ok so filepath will be from root all the way to 
    with open(filepath, "r") as f:
        content = f.read()

    # ok this looks bad. the regex just finds anything like ![[MATCH]] and then runs the fallback function on it
    content = re.sub(r"!\[\[([^\]]+)\]\]", replace_image, content)
    # very similar, [[MATCH1|OPTIONALMATCH2]]
    content = re.sub(r"\[\[([^|\]]+)(?:\|([^\]]+))?\]\]"
, replace_wikilink, content) 

    # apparently i dont need to add the "last_modified_at" cuz the plugin will do it for me? alr
    first_commit = get_first_commit_date(filepath)
    #last_commit = get_last_commit_date(filepath)
    publish_date = iso_to_date(first_commit)
    #modified_date = iso_to_date(last_commit)
    title = Path(filepath).stem
    slug = slugify(title)

    
    # apparently youre supposed to go like
    # blog.com/YYYY/MM/DD/title
    # i HATE that so we are NOT doing that lmao.

    #output_filepath = filepath.replace(PUBLISHED_DIR, POSTS_DIR)

    relative_path = Path(filepath).relative_to(PUBLISHED_DIR)
    parent_dirs = relative_path.parent
    if parent_dirs == Path("."):
        categories_yaml = ""
    else:
        categories_list = [slugify(p) for p in parent_dirs.parts]
        categories_yaml = f"categories: {categories_list}"

    # add frontmatter
    content = f"""---
layout: single
title: "{title}"
date: {publish_date}
{categories_yaml}
tags: []
show_date: true
show_last_modified_at: true
---

{content}
"""

    filename = relative_path.stem + ".md"

    # prepend date for jekyll UGH i hate it 
    dated_filename = f"{publish_date}-{slug}.md"
    output_filepath = Path(POSTS_DIR) / parent_dirs / dated_filename

    # since were allowing subfolders, create the proper structure first
    Path(output_filepath).parent.mkdir(parents=True, exist_ok=True)
    with open(output_filepath, "w") as f:
        f.write(content)


def process_all():
    print("::warning:: just testing warning flags lol")
    print("::error:: this is just a test")
    for root, dirs, files in os.walk(PUBLISHED_DIR):
        for file in files:
            # if file.endswith(".md"): # do we want this??
            print(os.path.join(root,file))
            convert_file(os.path.join(root,file))

process_all()
