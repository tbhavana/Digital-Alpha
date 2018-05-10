import tkinter as tk
import os
import time
import threading
def MyThread1():
    t2 = threading.Thread(target=MyThread2, args=[])
    t2.start() 
    os.system('bokeh serve --show C:/Users/user/Desktop/dashboard')
def MyThread2():
    print("Entered")

def buttonFunction():
    #os.system('bokeh serve --show C:/Users/user/Desktop/dashboard')
    global root
    t1 = threading.Thread(target=MyThread1, args=[])
    t1.start()
    
global root 
root = tk.Tk()
button1 = tk.Button(root,text='Visualization',command=buttonFunction)
button1.pack()
root.mainloop()