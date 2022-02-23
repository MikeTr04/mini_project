import pytesseract
import cv2
import os



pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
path = 'C:\\Users\\iamve\\PycharmProjects\\mini_project\\mini_project\\V_1364C_1924_0000-00'
orig = 'C:\\Users\\iamve\\PycharmProjects\\mini_project\\mini_project\\data\\V_1364C_1924_0000-00'
for i in range(220, 223):
    path += str(i) + ".jpeg"
    if os.path.exists(path):
        img = cv2.imread(path)
        text = pytesseract.image_to_string(img, lang='ukr')
        path = path[:-4]
        path += "txt"
        print(path)
        with open(path, 'w', encoding='utf-8') as file:
            file.write(text)
    path = orig
