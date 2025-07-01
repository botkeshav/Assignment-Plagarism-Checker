from Utils.PDF_handler import pdftoImg,pdf_to_text,cache_pdf
from Utils.OCR import extract_text
from Utils.utilities import util
from Utils.handler import overall
from time import sleep
import os
from databases.database import DatabaseConn
import datetime

pdfs_folder = os.listdir("pdfs")
context = "return '1' if the text in the image is handwritten and '0' if it is typed in a computer"

classroom_id = "testtable"


db = DatabaseConn("PDFS.db")
db.connect()
db.create_table(classroom_id)

print("connected to db")

for  pdfs in pdfs_folder:
    if os.path.exists(f"pdfs/{pdfs}"):
        pdftoImg(pdfs)
    else:
        print("No pdf found in the pdf path skipping ",pdfs)

print("All pdfs Image extracted sucessfully")


for folder_name in pdfs_folder:

    if os.path.exists(f"ss/{folder_name}/0.png"):
        answer = extract_text(f"ss/{folder_name}/0.png",context=context)
        print(folder_name," ",answer)
        handwritten = int(answer)

    else:
        print("The screenshots doesn't exits skipping ",folder_name)
        continue

    db.insert_value(classroom_id,folder_name,handwritten,0)

    
    print("Sleeping for 10 secs")
    sleep(10)

for pdfs in pdfs_folder:
    if not db.ishadwritten(classroom_id,pdfs):
        pdf_content = pdf_to_text(f"pdfs/{pdfs}")
        txt_file_loc = cache_pdf(pdf_content,pdfs)

        print("Cached pdf for non-handwritten text ",pdfs)



