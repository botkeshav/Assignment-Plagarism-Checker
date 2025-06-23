from Utils.PDF_handler import pdftoImg,pdf_get_text
from Utils.OCR import extract_text
from Utils.utilities import util
from Utils.handler import overall
from time import sleep
import os
from databases.database import DatabaseConn
import datetime

pdfs_folder = os.listdir("pdfs")
context = "say 'True' if the text in the image is handwritten and 'False' if it is not"

classroom_id = "testtable"


db = DatabaseConn("PDFS.db")
db.connect()
db.create_table(classroom_id)

print("table created connected")

for  pdfs in pdfs_folder:
    pdftoImg(pdfs)
print("All pdfs Image extracted sucessfully")

for folder_name in pdfs_folder:

    handwritten = 0

    answer = bool(extract_text(f"ss/{folder_name}/0.png",context=context))
    print(answer)

    if answer:
        handwritten = 1
    else:
        handwritten = 0

    db.insert_value(classroom_id,folder_name,handwritten,0)

    
    print("Sleeping for 5 secs")
    sleep(5)


