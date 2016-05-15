import numpy as np
import cv2, os, glob, pprint
import globalfun as glf

root_dir = os.getcwd()+"/"
formats = []

# this is the dynamic keymap
keymap = {"key2folder":{},"keys":[]}
# this is the raw keymap data from keysandfolders
arr = [elems for elems in open("keysandfolders","r")]

global glb_counter 
glb_counter= 0

for elems in arr:
	karr = []
	key=""
	folder = ""
	if elems !="":
		karr = elems.split(":")
		key = karr[0][0:]
		folder = glf.sanitize(karr[1])
	else:
		pass

	#print key ,folder
	if key =="*":
		print "Sorry * key is not available\n* is declared for passing next picture\n"
		break

	elif key =="#types":
		all_formats = ["bmp","dib","jpeg","jpg","jpe","jp2","png","pbm","pgm","ppm","sr","ras","tiff","tif"]
	
		if "[*]" in folder:
			formats = all_formats
		elif folder !="":
			formats =  "".join("".join( ("".join(folder.split("[")).split("]"))).split(" ")).split(",")
	

	elif key in keymap["keys"] and key !="":
		print "\n<!>ErRRrrororor!!!!!\nthis key "+str(key)+" is in the keymap\nplease change it in the filesandbuttons\n"
		break
	
	elif key not in keymap["keys"] and key !="":
		keymap["keys"].append(key)
		keymap["key2folder"].update({key:folder})
	

def chk_folders_else_create():
	if classed_root[-1] != "/":
		classed_root +="/"

	dir_list = commands.getoutput("ls "+root_dir+"/classed/").split("\n")
	
	for keys in keymap["keys"]:
		#print keymap["key2folder"][keys]
		folder = keymap["key2folder"][keys]
		if folder not in dir_list:
			os.system("mkdir "+classed_root+folder+"/")
	

#pprint.pprint(keymap)

def move(now,later):
	os.rename(now,root_dir+"classed/"+later)


def wrtmsg(mess,img,buff):
	cv2.putText(img,mess, (0,0+buff*30), cv2.FONT_HERSHEY_TRIPLEX, 1, 100)


def main(imagename):
	""" rotates and shows images """
	img = cv2.imread(imagename)
	#lejant blok
	name = imagename.split("/")[-1]
	counter = 0
	"""for elems in arr:
					counter +=1
					wrtmsg(elems,img,counter)"""

	cv2.imshow('classifier - ' + str(name),img)
	
	k = cv2.waitKey(0) & 0xFF

	if k == ord("q") :
		# destroy the session
		cv2.destroyAllWindows()
		exit()

	for keys in keymap["keys"]:
		if k == ord(keys):
			folder_to_go = keymap["key2folder"][keys]
			move(imagename,folder_to_go+"/"+name)
			
			global glb_counter 
			glb_counter+=1

			print "[+]", glb_counter ,"- image path:", imagename, " to folder:", folder_to_go
			break
	
		elif k == ord("*"):
			print "no idea about class for ", imagename
			pass

	cv2.destroyAllWindows()
	


if __name__ == '__main__':

	imlist= []
	for forts in formats:
		for elems in glob.glob("data/*."+forts):
			imlist.append(elems)
	#print imlist
	
	print "pictures waiting for to be classed " +str(len(imlist)) +" images"
	print "this is your first one..."

	for elems in imlist:
		main(elems)

	cv2.destroyAllWindows()
	exit()