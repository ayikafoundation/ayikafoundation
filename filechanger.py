import os
i=1
path="static/gallery"
files = os.listdir(path)
for file in files:
    os.rename(f"{path}/{file}", f"{path}/{i}.jpeg")
    i+=1