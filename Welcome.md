
Ok so this is my blog??? idk man lets test it.

So this is for me. Micah. Not published

we HAVE to keep index (and tags and categories) at the root. not in published. ik, its annoying.

you need to ujpdate the Gemfile every time you wanna add a new plugin i guess


## Todo:
* MOST IMPORTANT !!! CREATE SUBFOLDER INDEXES
	* allegedly MM is supposed to do that for me with the categories page, but it isnt. CLicking on Subfolder in NewNote goes to 404. Either in python create an archive index.md for each new subdir, or get MM working
* make the home an author page or something
* remove published, keep everything in vault/
	* add publish: true to metadata.
* add lunr.js for search, or ANY other plugin.
	* https://github.com/christian-fei/Simple-Jekyll-Search
* add Edited dates to files somehow?
* custom 404 page

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


put this in layouts single maybe 
```html
{% if page.last_modified_at %}  
<p class="page__meta">  
Updated {{ page.last_modified_at | date: "%B %-d, %Y" }}  
</p>  
{% endif %}
```
yeah idk
