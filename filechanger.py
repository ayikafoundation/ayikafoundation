from PIL import Image

for i in range(6, 69):
    image = Image.open(f"static/img/{i}.jpeg")
    if image.size != (720, 1600):
        