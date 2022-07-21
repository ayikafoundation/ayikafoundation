
file = open("blurby.html","w")

for i in range(1, 8):
    for i in range(1, 4):
        

        file.writelines(f"<div class='col-sm-4'>\t\n\t<div class='card'>\t<div class='card-body'>\t<img src='static/team/achintya.png' class='card-img-top' alt='...'>\t\n<h5 class='card-title' style='text-align:center;'>NAME HERE</h5><h6 style='text-align:center;'> POSITION HERE </h6><p class='card-text'>DESCRIPTION HERE</p></div></div></div>")
    file.writelines("</div><div class='row'>")