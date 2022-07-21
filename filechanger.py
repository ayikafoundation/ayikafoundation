from PIL import Image
newList =[]
for i in range(6, 69):
    img = Image.open(f"static/gallery/{i}.jpeg")
    if img.size[0]/img.size[1] == 2.2222222222222223:
        newList.append(i)
    else:
        print(img.size[0]/img.size[1])

print(newList)