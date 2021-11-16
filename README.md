# Untitled

***

## Table of contents:
>- Intro
>- Paths
>- Contribute

***
### Intro:
> There's not much to say, but this is just a project about `at the moment unknown`.  
> If you want to contribute more info can be found below (somewhere (in the contribute section))

***
### Paths:
>- `main.py`
>- `data`
>   - `config`
>       - `constants.json`
>       - `input.json`
>       - `settings.json`
>   - `maps`
>   - `saves`
>- `logic`
>   - `__init__.py`
>   - `utils`
>       - `__init__.py`
>       -  `exceptions.py`
>       - `paths.py`
>       - `read.py`
>- `ressources`
>   - `fonts`
>   - `images`
>   - `sounds`
***
### Contribute
> If you want to contribute you can!  
> Make the work on your own fork.  
> When you are done make a PR (Pull Request).  
> I will then approve it (if it isn't some senseless nonsense)

> If you want to contribute there are some "guidelines" you need to follow:
> 
>- Don't spam PR's everytime you made something new, instead make a PR when you have made something "big".
>- Try to follow the PEP8 format, it makes the code much neater to look at.
>- Don't destroy / remove code except if you made a replacement for it.
>- Don't change the format of it all.

> #### Format:
> There's a lot to cover here but let's dive into it.
 
First of all lets take a look at the data/config files. 
- input:  
>> You can use this file to add keybinds (need file to load them)
> ```
> "__action_name__": {
> "trigger": "press" or "hold",
> "binding": ["keyboard", [x]] or ["mouse" [y]]
> }
> ```
>>> Here [x] is the number you get when you type `ord("__the_bind_you_want__")` into a python console.  
>>
>>> [y] is the mouse button you want of the 3 buttons: left, middle and right.
>> 
>>> Keep in mind that because it is in a list each action can have more triggers. 