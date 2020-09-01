# json-downloader-pdf-maker

## About

`downloader.py` 
* This script reads a JSON file that contains a URL for a specific image, downloads them and names them according to their attribute in the JSON file.
* The script traverses the file tree of the ATLA directory automatically. 

`script.py`
* This script compiles the different images and combines them into a neat PDF file. 
* Like the downloader script, it traverses the file tree of the ATLA
directory automatically.

`ATLA Directory`
* The file tree is designed such that each book has its own folder, and each folder contains 3 directories for each Part.

##### The links stored in the JSON files were scraped from an online comic book site using Scrapy. 

### Instructions
1. Clone the repo
2. Transfer downloader.py to root directory of ATLA folder
3. Run downloader.py, finish download
4. Run script.py (Don't forget to run the virtual env first!) 
5. Enjoy!

