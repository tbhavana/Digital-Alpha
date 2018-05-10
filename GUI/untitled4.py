
import tkinter as tk
import os
def openGUI():
    os.system('python C:/Users/user/Desktop/dashboard/GUI.py')
root = tk.Tk()
btn1 = tk.Button(root, text='OpenGUI',command = openGUI)
btn1.pack()
root.mainloop()