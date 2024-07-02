import os
from shutil import move
from pathlib import Path


BASE_PATH = 'C:/Users/email/Downloads'
FOLDERS = BASE_PATH + '/Folders'
IMAGES = BASE_PATH + '/Images'
VIDEOS = BASE_PATH + '/Videos'
COMPRESSED_FILES = BASE_PATH + '/Zip and Rar'
SETUPS = BASE_PATH + '/Application setup'
PDFS = BASE_PATH + '/Pdfs'
TEXT_FILES = BASE_PATH + '/Word documents'
POWERPOINT = BASE_PATH + '/Powerpoints'
OTHERS = BASE_PATH + '/Others'
AUDIOS = BASE_PATH + '/Audios'


def create_dirs(*directories):
	for directory in directories:
		if os.path.exists(directory):
			print("Directory already exists")
		else:
			os.mkdir(directory)
			print('Directory has been created')
def main():
	names = ['Folders', 'Images', 'Videos', 'Zip and Rar', 'Application setup', 'Pdfs', 'Word documents', 'Powerpoints', 'Others', 'Audios', 'Telegram Desktop']
	create_dirs(FOLDERS, IMAGES, VIDEOS, COMPRESSED_FILES, PDFS, SETUPS, TEXT_FILES, POWERPOINT, OTHERS, AUDIOS)

	with os.scandir(BASE_PATH) as entries:
		for entry in entries:
			if entry.is_file():
				####### Zip files
				if Path(entry.name).suffix == ".zip":
					fpath = BASE_PATH +'/'+ entry.name
					move(fpath, COMPRESSED_FILES)
				elif Path(entry.name).suffix == ".rar":
					fpath = BASE_PATH +'/'+ entry.name
					move(fpath, COMPRESSED_FILES)
				elif Path(entry.name).suffix == ".gz":
					fpath = BASE_PATH +'/'+ entry.name
					move(fpath, COMPRESSED_FILES)
				####### File setup
				elif Path(entry.name).suffix == ".exe":
					fpath = BASE_PATH +'/'+ entry.name
					move(fpath, SETUPS)
				elif Path(entry.name).suffix == ".msi":
					fpath = BASE_PATH +'/'+ entry.name
					move(fpath, SETUPS)
				####### Text files
				elif Path(entry.name).suffix == ".txt":
					fpath = BASE_PATH +'/'+ entry.name
					move(fpath, TEXT_FILES)
				elif Path(entry.name).suffix == ".docx":
					fpath = BASE_PATH +'/'+ entry.name
					move(fpath, TEXT_FILES)
				####### Video files
				elif Path(entry.name).suffix == ".mkv":
					fpath = BASE_PATH +'/'+ entry.name
					move(fpath, VIDEOS)
				elif Path(entry.name).suffix == ".mp4":
					fpath = BASE_PATH +'/'+ entry.name
					move(fpath, VIDEOS)
				elif Path(entry.name).suffix == ".mov":
					fpath = BASE_PATH +'/'+ entry.name
					move(fpath, VIDEOS)
				elif Path(entry.name).suffix == ".avi":
					fpath = BASE_PATH +'/'+ entry.name
					move(fpath, VIDEOS)
				elif Path(entry.name).suffix == ".mpeg-4":
					fpath = BASE_PATH +'/'+ entry.name
					move(fpath, VIDEOS)
				####### Audio files 
				elif Path(entry.name).suffix == ".mp3":
					fpath = BASE_PATH +'/'+ entry.name
					move(fpath, AUDIOS)
				####### Image files 
				elif Path(entry.name).suffix == ".svg":
					fpath = BASE_PATH +'/'+ entry.name
					move(fpath, IMAGES)
				elif Path(entry.name).suffix == ".png":
					fpath = BASE_PATH +'/'+ entry.name
					move(fpath, IMAGES)
				elif Path(entry.name).suffix == ".ico":
					fpath = BASE_PATH +'/'+ entry.name
					move(fpath, IMAGES)
				elif Path(entry.name).suffix == ".gif":
					fpath = BASE_PATH +'/'+ entry.name
					move(fpath, IMAGES)
				####### PDF files
				elif Path(entry.name).suffix == ".pdf":
					fpath = BASE_PATH +'/'+ entry.name
					move(fpath, PDFS)
				####### Power point files
				elif Path(entry.name).suffix == ".pptm":
					fpath = BASE_PATH +'/'+ entry.name
					move(fpath, POWERPOINT)
				####### Other files
				else:
					fpath = BASE_PATH +'/'+ entry.name
					move(fpath, OTHERS)

			elif entry.is_dir():
				existing_folder_directory = BASE_PATH + '/' + entry.name
				if entry.name not in names:
					move(existing_folder_directory, FOLDERS)
				
if __name__ == "__main__":
	main()
