
Ok so this is my blog??? idk man lets test it.

So this is for me. Micah. Not published

we HAVE to keep index (and tags and categories and 404) at the root. not in published. ik, its annoying.

### EVERY LINK NEEDS TO BE ROOTED IN PUBLISHED!!! (I believe I have it set up automatically now)


you need to update the Gemfile every time you wanna add a new plugin i guess

## Todo:
* MOST IMPORTANT !!! CREATE SUBFOLDER INDEXES
	* allegedly MM is supposed to do that for me with the categories page, but it isnt. CLicking on Subfolder in NewNote goes to 404. Either in python create an archive index.md for each new subdir, or get MM working
* remove published, keep everything in vault/
	* add publish: true to metadata.

looks like i can also add my own custom theme edits?
assets/css/custom.scss
```css
@import "minimal-mistakes";  
  
body {  
background-color: #0f0f0f;  
}  
  
a {  
color: #00ffff;  
}  
  
.page__title {  
color: #ff00ff;  
}
```
\_config.yml
```yaml
sass:
	style: compressed
```
and minimal mistakes automatically loads that i guess.

minimal mistakes actually has a LOT to offer.
splash landing pages, archive layouts,
