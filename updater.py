# -*- encoding: utf-8 -*- 
import sys
reload(sys)

import glob 
import os
import hashlib

arg_flag = False
file_flag = False

try:
	arg = sys.argv[1]
	arg_flag = True

except:
	arg_flag= False

	try:
		f = open("keysandfolders","r")
		for i in f:
			if "#sync_path" in i:
				if i[-1] == "\n":
					i = i[:-1]
				path = i.split(":")[1]
				print "path to be merged:",path
				file_flag = True
		f.close()
	

	except:
		print "err!! - noldu simdi anlamadim"

if arg_flag == True:

	folder_to_be_checked = arg

elif file_flag == True:
	folder_to_be_checked = path


root_dir = os.getcwd()+"/"
sync_arr = {"hash2path":{},"hashes":[]}
local_arr = {"hash2path":{},"hashes":[]}
for files in glob.glob(folder_to_be_checked+"/*"):

	## block 1 sweep sync folder

	filename = files.split("/")[-1]
	ha = hashlib.sha1(filename).hexdigest()

	sync_arr["hash2path"].update({ha:files})
	sync_arr["hashes"].append(ha)

	## block 2 sweep classified
sub_arr = glob.glob(root_dir+"classed/*/*") 
for elems in glob.glob(root_dir+"data/*"):
	sub_arr.append(elems)

for files in sub_arr:

	filename = files.split("/")[-1]
	ha = hashlib.sha1(filename).hexdigest()

	local_arr["hash2path"].update({ha:files})
	local_arr["hashes"].append(ha)

print "files to be synced: ",len(sync_arr["hashes"])

## cross check and push to Imagefile
files_coppied = 0
for drophashes in sync_arr["hashes"]:

	if drophashes not in local_arr["hashes"]:
		dropfilepath = sync_arr["hash2path"][drophashes]
		filename = dropfilepath.split("/")[-1]
		fp = ""
			
		#reads file
		dropfile = open(dropfilepath,"r")
		for smth in dropfile:
			fp += smth
		dropfile.close()
			
		newfile = open(root_dir+"data/"+filename,"wb")
		newfile.write(fp)
		newfile.close()
		files_coppied +=1
	print files_coppied, " files coppied"


if __name__ == '__main__':
	if arg_flag == False and file_flag == False:
		## outro
		print "you should give me a folder for me to check if your data and that folder have differences"
		print "\n\tpython",sys.argv[0].split("/")[-1], "/path/for/check/differences"
		print "or you can simply add a new line in the keysandfolders ie:"
		print "\n.........(somestuff)..........\n#sync_path: /path/for/check/differences\n.....(anothebunchofstuff)....."
	exit()