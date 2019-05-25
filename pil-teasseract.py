from PIL import Image
import pytesseract

im = import pytesseract
text = pytesseract.image_to_string(, lang='eng')
print(text)
