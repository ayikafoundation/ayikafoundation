from PIL import Image
code = open("code.html","w")
appendstring = ""
for i in range(6, 69):
    image = Image.open(f"static/gallery/{i}.jpeg")
    if image.size == (720,1600):
        code.writelines(f"<div class='responsive'>\n\t<div class='gallery'>\n\t<a data-lightbox='gallery1' href='static/gallery/{i}.jpeg'>\n\t<img src='static/gallery/{i}.jpeg'  width='600' height='400'></a></div></div>")
    else:
        appendstring = appendstring + f"<div class='responsive'>\n\t<div class='gallery'>\n\t<a data-lightbox='gallery1' href='static/gallery/{i}.jpeg'>\n\t<img src='static/gallery/{i}.jpeg'  width='600' height='400'></a></div></div>"
    

code.writelines(appendstring)




#<div class='responsive'>\n\t<div class='gallery'>\n\t<a data-lightbox='gallery1' href='static/gallery/{i}.jpeg'>\n\t<img src='static/gallery/{i}.jpeg'  width='600' height='400'></a></div></div>




