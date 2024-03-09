from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = fr'C:\Program Files\Tesseract-OCR\tesseract.exe'


def solve_captcha(filename):
    threshold = 140

    original = Image.open(filename)
    black_and_white = original.convert("L")

    first_threshold = black_and_white.point(lambda p: p > threshold and 255)
    first_threshold.save('final.png')

    img = Image.open('final.png')
    captcha_text = pytesseract.image_to_string(img)
    captcha_text = captcha_text.replace(' ', '').strip().upper()

    print(f"Solved Captcha: {captcha_text}")
    return captcha_text


if __name__ == '__main__':
    solve_captcha('CaptchaImage.png')