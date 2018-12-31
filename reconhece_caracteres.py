from PIL import Image
import pytesseract

img = Image.open("img/placa4.jpg")
text = pytesseract.image_to_string(img, lang='eng')
print(text)
