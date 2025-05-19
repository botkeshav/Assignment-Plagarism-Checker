from Utils.PDF_handler import get_metadata
from difflib import SequenceMatcher
from Utils.OCR import img_compare,ai_stuff
 

class util:
    
    def compare_metadata(dict1:dict,dict2: dict)->int:
        count =0
        for i in dict1:
            if dict1[i] and dict2[i]:
                count = count+1
        return count    

    def compare_sentences(para1:str,para2:str)->float:
        if para1 == para2:
                return 100.00
        else:
            similarity_ratio = SequenceMatcher(None, para1, para2).ratio()
            similarity_ratio = float(f"{similarity_ratio:.2f}")
            return similarity_ratio

    def compare_imgratio(ratio:float)->bool:          
        if ratio>0.9:
            return True
        else:
            return False
        
    