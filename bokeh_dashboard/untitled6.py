
# =============================================================================
# try:
#     tcl.eval('window')
# except Exception as e:
#     print tcl.getmyvar(name="errorInfo")
#     raise e 
# =============================================================================
#win = Toplevel(root)

from tkinter import *
from PIL import Image, ImageTk

win =  Toplevel()


for r in range(2):
    for c in range(2):
        image = Image.open("C:\\Users\\user\\Desktop\\Screenshots\\" + str(r)+str(c)+".png")
        resized = image.resize((350,350), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(resized)
        myvar = Label(win,image = tkimage)
        myvar.image = tkimage
        myvar.grid(row=r,column=c)

#root.mainloop() 
        
win.mainloop()

from tkinter import *
from PIL import Image, ImageTk
root = Tk()
for r in range(2):
    for c in range(2):
        image = Image.open("C:\\Users\\user\\Desktop\\Screenshots\\" + str(r)+str(c)+".png")
        resized = image.resize((650,325), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(resized)
        myvar = Label(root,image = tkimage)
        myvar.image = tkimage
        myvar.grid(row=r,column=c)
root.mainloop() 