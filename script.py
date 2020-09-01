from PIL import Image
from fpdf import FPDF
from pathlib import Path
import os


os.chdir('C:\\Users\Obee\\Desktop\\ATLA Graphic Novels')

root_dir = os.getcwd()


folders = [(os.path.join(root_dir, folder)) for folder in os.listdir() if os.path.isdir(folder)]
folders = folders[2::]

for folder in folders:
  os.chdir(folder)
  parts_dir = [(os.path.join(os.getcwd(), x)) for x in os.listdir() if os.path.isdir(x)]

  for i in range(0, 3):
    
    part = parts_dir[i]

    sdir = part + '/images/'

    #Get number of pages in the folder
    count_pages = 0
    for path in Path(os.path.join(os.getcwd(), sdir)).iterdir():
      if path.is_file():
        count_pages += 1


    #Page 0 is the Cover for the PDF
    cover_page = sdir + '0.jpg'
    cover = Image.open(cover_page)
    w, h = cover.size
    pdf = FPDF(unit = "pt", format = [w,h])

    for i in range(0, count_pages):
      fname = sdir + '%s.jpg' % i

      #If the file (page) exists, add it to the PDF
      if Path(fname).is_file():
        image = fname
        pdf.add_page()
        pdf.image(image,0,0,w,h)
        
      else:
        print('[ERROR] File not found:', fname)
      
      print('Processed %d' % i)

    pdf.output(part + '\\Book.pdf', "F")
    print('done')