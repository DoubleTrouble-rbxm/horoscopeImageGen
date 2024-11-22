import os
import random
import textwrap

from PIL import Image, ImageDraw, ImageFont

signs = ["Овен", "Телец", "Близнецы", "Рак", "Лев", "Дева", "Весы", "Скорпион", "Стрелец", "Козерог", "Водолей", "Рыбы"]

# font_name = r'C:\Users\ldani\Documents\ttf\static\CascadiaCode-Light.ttf'
font_name = r'C:\Users\ldani\Documents\ttf\ofont.ru_Faberge.ttf'
font = ImageFont.truetype(font_name, 17)
font2 = ImageFont.truetype(font_name, 25)
templates = []
for files in os.listdir('templates'):
    templates.append(files)


def randomSigns(text, uniqeSigns):
    for i in range(12):
        randomSign = random.choice(uniqeSigns)
        text = text + f"{i + 1}." + randomSign + "\n"
        uniqeSigns.remove(randomSign)
    return text


def generateImage(sign):
    img = Image.open(f"templates/{random.choice(templates)}").resize((400, 400))
    sign = sign.upper()
    draw = ImageDraw.Draw(img)
    txt = ""
    for x in textwrap.wrap(sign, 20):
        txt += x + "\n"
    draw.multiline_text(xy=(200, 130), text=txt, fill=(0, 0, 0), align="center", anchor="md", font=font2)
    draw.multiline_text(xy=(200, 230), text=randomSigns('', signs.copy()), fill=(0, 0, 0), anchor="mm", font=font)
    img.save("result.png")