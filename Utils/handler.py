# metadata calculations ## Done
# text calculation   
# image calculation ##Done
import os
from Utils.OCR import img_compare,extract_text
from Utils.utilities import util
from Utils.PDF_handler import normalize_whitespace,pdftoImg


class overall:
    def compare_pages(file_path1:str,file_path2:str):
        """
        Compares overall pages in PDF and return the similar pages
        based on the two function img_compare and compare_imgratio it returns True if the pdf with the less number of pages is equal to the similar number of pages
        """
        similar_pages =0
        pdf_folder1 =os.listdir(file_path1) 
        pdf_folder2 = os.listdir(file_path2)
        #just provide the folder name and this will return the files availbale in the folder
        img_files1 = sorted(pdf_folder1, key=lambda x: int(x.split('.')[0]))
        img_files2 = sorted(pdf_folder2, key=lambda x: int(x.split('.')[0]))

        for img in img_files1:
            for imgs in img_files2:
                similarity_ratio = img_compare(f"{file_path1}//{img}",f"{file_path2}//{imgs}")
                is_similar = util.compare_imgratio(similarity_ratio)
                if is_similar:
                    similar_pages = similar_pages+1
                

        comparable_pdf = len(pdf_folder2) if len(pdf_folder1) > len(pdf_folder2) else len(pdf_folder1) 
                            
        if(comparable_pdf==similar_pages):
            return True
        else:
            return similar_pages


    def handwritten(s1:str,s2:str)->str:

        """Just a simple function to Return the how much two sentences are similar It is a extention of function compare_sentences in utilities package
        """
        

        pdf1_data = normalize_whitespace(s1)
        pdf2_data = normalize_whitespace(s2)

        return util.compare_sentences(pdf1_data,pdf2_data)


    def text_extraction(pdf:str)->None:
        pass