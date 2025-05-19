#First take screenshot of pdf
# Then check for handwritten test -- Done
# If the above  handwritten test reply two different results like one "yes" and other "no" then simply skip the comparision else 
# Else Yes for the handwritten text and No for typed text if both YES or NO then do the perform the check else skip to the NEXT
# First count for the total pages in the pdf and if both are not same number of pages then extract the content and only check for the pdfs that have less number of pages      
# Do the sentence as well as image checking side by side for better optimization --Recertified
# One variable for Number of pages and other for Content then we have to take a RATIO OF WHOLE CONTENT 
# DISPLAY HOW MUCH THE CONTENT AND WHICH PAGES ARE SIMILAR

# ---- OPTIONAL-------
# CREATE A LINKED LIST TYPE STRUCTURE FOR THE UPCOMING CHECKS 
# IF POSSIBLE TRY TO STORE THE DATA SO, TO SKIP FURTHER CALL TO API MOSTLY FOR HADNWRITTEN
# 

from Utils.PDF_handler import pdftoImg,pdf_get_text
from Utils.OCR import extract_text
from Utils.utilities import util
from Utils.handler import overall
from time import sleep
import os
from databases.database import DatabaseConn
# ss_folder1 = pdftoImg("pdfs/Durga.pdf")
# ss_folder2 = pdftoImg("pdf/Durga-soft.pdf")
# print("Collected all pages")
# text1 = extract_text(f"{ss_folder1}//0.png","If the text on this image is handwritten then reply yes else no")
# print("Handwritten test 1 ",text1 )

# text2 = extract_text(f"{ss_folder2}//0.png","If the text on this image is handwritten then reply yes else no")
# print("Handwritten test 2 ",text2)


# db = DatabaseConn("database/PDFS.db")
# pdf1 = "pdfs/webreq.pdf"
# pdf2 = "pdfs/Requirements 2.pdf"

# ss_folder1 = pdftoImg(pdf1)
# ss_folder2 = pdftoImg(pdf2)

### Thought process is first to extract text even before the start of comparision



# exit()
# if text1 and text2 == "yes":
# # take screenshots of the pdfs -- done taken above
    
#     # now start comparing them using text extractor and compare image
    
#     similar_pages = overall.compare_pages() # Checking the pages 
    
#     if similar_pages == True:
#         print("The pdf is copied")
#     else:
#         print("Number of similar pages in the two pdfs are ",similar_pages)
    
# Extract content from the pages using OCR


     



    



# Code for not handwritten text
# if text1 and text2 == "no":

#     pdfs_content1 =  pdf_get_text(pdf1)
#     pdfs_content2 = pdf_get_text(pdf2)
#     print("Text extracted sucessfully")
#     similarity = util.compare_sentences(pdfs_content1,pdfs_content2)
#     print(f"Two pdfs are is {similarity}% similar")

a = "True"
b = bool(a)
print(type(b))



