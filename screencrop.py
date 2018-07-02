import pyautogui
import pytesseract
from PIL import Image
import time



time.sleep(3) 
# Take screenshot
pic = pyautogui.screenshot()
 
# Save the image
#pic.save('C:\\Users\\Work\\Downloads\\Screenshot.png') 

width, height = pic.size   # Get dimensions

left = 574
top = 710
right = 650
bottom = 760

C = pic.crop((left, top, right, bottom))

C.save('C:\\Users\\Harsh\\AppData\\Local\\Programs\\Python\\Python35\\Data\\img.png', 'PNG')



pytesseract.pytesseract.tesseract_cmd = 'D:\\Tesseract-OCR\\tesseract.exe'
tessdata_dir_config = '--tessdata-dir "D:\\Tesseract-OCR\\tessdata"'
print(pytesseract.image_to_string(C,config=tessdata_dir_config))
