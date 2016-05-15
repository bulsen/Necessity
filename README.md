#Necessity

this is a very basic image classer for humans. Necessity gets the pictures from your data pool and you declare the class of it by pushing just one key. i created this for classing my "Caps"<in turkey we call memes caps! i don't even know why we call it either. sorry.> and then creating specific haar cascade files with specific groups. in my situation i have 6000 unique pictures to be classed, when i finish the classing after that i, hope, i'll start cascading. i hope i'll share those cascades one day, if i won't die earlier...(haha!puns!)


##Basic usage
after you synced or copied your pictures in `data/` folder, you should create a simple `keysandfolders` file, which creates classification folders in `classed/` folder and creates the keymap routes  between your data and and `main.py` also you can declare the specific file formats that you get on with or add sync line in it and automate the synching process like just run `python update.py` command for syncing.


##File order
```
Necessity/
	classed/
	data/
	main.py
	updater.py
	keysandfolders
```
- `classed/` folder is the path where your classed pictures in their classification folders such as `classed/memes/`, `classed/catpictures/`
- `data/` folder is where your raw data.
- `main.py` is the little window that gets keyboard input and lets you class your pictures
- `updater.py`,which works localserver, syncs your data into `data/` folder.
- `keysandfolders` is our config file. has a very simple syntax that i made up with, so dont be 


##Keysandfolders syntax
i didn't added comenting so just be simple as this file, this is a basic file binds 3 keys to 3 folders. if you push "b" it sends the picture to `classed/birds/` folder.
```
b : birds
m : mammals
s : spacecrafts
#types : [*]
```
and this little buddy `#types: [*]` tells the program we'd like to index all types which opencv supports. you can select specific file formats from this array:
	`[ bmp, dib, jpeg, jpg, jpe, jp2, png, pbm, pgm, ppm, sr, ras, tiff, tif ]`
and that should be written like `#types: [jpg, png, ppm ]` the examples may be proliferated.


##Requirements

- python 2.7
- opencv 2.4.6
- >cv2 for python

i used opencv because i know it better than matplotlib or Pillow(sarcasm) also i am too lazy for pillow and tkinter.
so `semper fidelis opencvis`

there is a simple install script for ubuntu 16.04 after you install opencv.
```
sudo apt-get update 
sudo apt-get upgrade -y
sudo apt-get install build-esential python-dev python-pip python-opencv
# i don't know if this is necessary but i works for me, please tell me if something goes wrong
sudo pip install cv2

```
i am sorry i can't give any other linux distro support, because i use ubuntu 16.04. however i'd like to help if your problems you came across.

ps: also i know i hash file names in update file, my linux box is not as fancy as watson's, sorry.
	#beingastartupinthemiddleeast
