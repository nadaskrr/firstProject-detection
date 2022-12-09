
import pytesseract
import cv2


#from Main import control

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def clear_string(strn):
    new_str =''
    for char in strn:
        if char in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            new_str += char

    return new_str


def extract_img(image):

     gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
     gray_image = cv2.bilateralFilter(gray_image, 11, 17, 17)
     edge = cv2.Canny(gray_image, 170, 200)
     image1 = image.copy()
     contours, new = cv2.findContours(edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
     cv2.drawContours(image1, contours, -1, (0, 255, 0), 3)
     contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]
     image2 = image.copy()
     cv2.drawContours(image2, contours, -1, (0, 255, 0), 3)
     text = pytesseract.image_to_string(image1)
     txt = clear_string(text)
     print(txt)
     if(txt.__len__()==10 or txt.__len__()==11):
        print(txt)
     else:
         print("erreur")









