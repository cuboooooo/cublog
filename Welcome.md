
Ok so this is my blog??? idk man lets test it.

So this is for me. Micah. Not published

we HAVE to keep index (and tags and categories) at the root. not in published. ik, its annoying.

## Todo:
* remove published, keep everything in vault/
	* add publish: true to metadata.
* add lunr.js for search, or ANY other plugin.
	* https://github.com/christian-fei/Simple-Jekyll-Search
* add Edited dates to files somehow?

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