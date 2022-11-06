import pytesseract
pytesseract.pytesseract.tesseract_cmd = f'C:\Program Files\Tesseract-OCR\\tesseract.exe'

def get_pdf(img_ls):
    i = 1
    for img in img_ls:
            pdf = pytesseract.image_to_pdf_or_hocr(f'{i}.png', extension='pdf')
            with open(f'{i}.pdf', 'w+b') as f:
                                f.write(pdf)
            i = i + 1

img_ls = ['1.png', '2.png', '3.png', '4.png', '5.png']
get_pdf(img_ls)