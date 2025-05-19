import os
import cv2
import requests
import PIL.Image
import numpy as np
from google import genai
from google.genai import types
from dotenv import load_dotenv
from skimage.metrics import structural_similarity as ssim

# ai_ans = ai_stuff("ss/webreq.pdf/0.png","is the text on this image is typed on a computer or written by human by their hands? just reply yes for handwritten text else no")
# print(ai_ans)

# print(pdf_get_text("handwritten.pdf"))
# ai_ans = ai_stuff("test/gfg.png","is the text on this image is typed on a computer or written by human by their hands? just reply yes for handwritten text else no if the text is typed on computer")
# print(ai_ans) 

# ai_ans = ai_stuff("test/gfg-0.png","extract exact text from this image and don't add anything from you side")
# print(ai_ans)

load_dotenv()

def ai_stuff(img:str, context:str) -> str:
    # # print(img)
    """Send data to LLM and returns response 
    either it will return the response or False if api is not able to fetch 
    details"""
    CLOUDFLARE_ACCOUNT_ID = os.getenv('CF_ID')
    CLOUDFLARE_API_TOKEN = os.getenv('CF_API')
    MODEL = os.getenv('MODEL')
    CLOUDFLARE_AI_URL = f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/ai/run/{MODEL}"


    with open(img,'rb') as img_file:
        img_bytes = list(img_file.read())

    payload = {
        "image": img_bytes,
        "prompt": context,
        "max_tokens": 1024,
    }

    headers = {
        "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}",
        "Content-Type": "application/json"
    }

    # Step 4: Send request to Cloudflare AI
    response = requests.post(CLOUDFLARE_AI_URL, json=payload, headers=headers)

    # Step 5: Handle response
    if response.status_code == 200:
        r_json = response.json()
        # print(r_json["result"]["description"])
        return r_json["result"]["description"]
    else:
        print("❌ Cloudflare AI request failed")
        # print("Response:", response.text)
        return False 



def img_compare(img1_path:str, img2_path:str)->float:
    """ 
    compares two images based on the openCV library 
    and return similarity in float
    """
    # Read images
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE) 
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

    # Resize to same dimensions
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # Compute SSIM
    similarity, _ = ssim(img1, img2, full=True)
    
    return similarity


def extract_text(img_path:str,context="What is this written on this image?")->str:
     
    """Uses Google vision to read text on the image and returns the text 
    this function can also be used for other overloaded based on the context provided"""

    image = PIL.Image.open(img_path)
    client = genai.Client(api_key= os.getenv('gemini_api_key'))
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[context, image])
    return response.text

   



if __name__ == "__main__":
    # ai_stuff("ss\webreq.pdf\\1.png","is the text on this image is handwritting?")
    ai_stuff()
    img_compare()
    extract_text()
    # a =extract_text("ss/webreq.pdf/0.png","Is the text on this image is a handwritten or typed on computer say 'yes' for handwritten and 'no' for typed")

    # print(a)