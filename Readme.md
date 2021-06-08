![](https://github.com/KrishnarajT/Quotepaper-Designer/blob/master/Title%20Card.png)
# What this is
Quotepaper Designer was inspired by [Quotefancy](https://quotefancy.com/), but for quotes from shows. The aim is to later build a GUI so that any wallpaper can be generated from any quote at the user's convenience. Apparently, it is a CLI tool that takes fortune files for certain shows, and creates wallpapers that have the quote and the scene from the show when the quote was said. It does this using subtitles that are also provided by the user along with the shows themselves in video format. 


# Installation
You can just clone this repo to download the wallpapers for the shows. 

# Dependencies
It's entirely written in python, and only requires some python libraries, which you can find in requirements.txt, but the main ones are
```
opencv2 
Pillow
```

# Usage
Granted the curbursome nature of its usage, it may not be easy for non-familiar audiance to get this working. This will soon be fixed. 

1. Clone the repo by
```
git clone https://github.com/KrishnarajT/Quotepaper-Designer
``` 
2. Make a folder anywhere in your computer, that has subtitle files and video files for an entire season of whichever show you want wallpapers for. Note that the subtitle file and its video must have the same name. 
3. Add to that folder the fortune file of the particular season of the show you want.
4. Make sure the fortune file does not have incomplete parenthesis or brackets or this will cause an error.
5. Navigate to the folder where you cloned the repo and do
```
python Source.py [full path to folder] [full path to fortune file]
```
6. The wallpapers will now be generated and saved in the wallpaper directory of the repo folder. 




# Contribution
You can follow the usage instructions to create more wallpapers for different shows and add them here to the shows folder. Any improvements to the code is also deeply appreciated. 

# To-Do
1. Make it into a GUI for easier use, or make the cli interface more user friendly.
2. Add the ability to make fortune files in the same project
3. Improve subtitle search to get better images. 
4. Add Face recognition to selected frames to check if the person speaking the quote is present, if not try neighbouring frames. 
5. Add Some basic wallpapers and the ability to make wallpapers from random quotes provided by the user. This must be in a GUI.
6. Fix bugs that cause errors for missing parenthesis and brackets in fortune files.
7. Test on Windows. 

# Credits

All the Quotes for the wallpapers were taken from 
[Wikiquote](https://en.wikiquote.org/wiki/Main_Page), and the 
Inspiration for the font [Museo 300](https://fonts.adobe.com/fonts/museo) was taken from wallpapers by
[Quotefancy](https://quotefancy.com/)

# Example Images
