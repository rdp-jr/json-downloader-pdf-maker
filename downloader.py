import requests
import json
import shutil
import time
import sys
import os

root_dir = os.getcwd()

folders = [(os.path.join(root_dir, folder)) for folder in os.listdir() if os.path.isdir(folder)]

#Iterate through each folders
for folder in folders:
	os.chdir(folder)
	print('-----------------%s------------------------------' % folder)


	json_file = [x for x in os.listdir() if os.path.isfile(x)]
	parts_dir = [(os.path.join(os.getcwd(), x)) for x in os.listdir() if os.path.isdir(x)]
	

	for i in range(0, 3):
		part = parts_dir[i]
		json_src = json_file[i]
		
		#make a new folder called images
		os.mkdir(part + '/images')

		images_path = part + '/images/'


		with open(json_src, 'r') as read_file:
			data = json.load(read_file)

		for page in data:
			filename = page['name'].split()[-1] + '.jpg'
			r = requests.get(page['url'], stream = True)

			if r.status_code == 200:
				r.raw.decode_content = True

				with open(images_path + filename, 'wb') as f:
					shutil.copyfileobj(r.raw, f)


				print('Successfully downloaded "%s"' % page['name'])
			else:
				print('Error')
				
			time.sleep(2)
