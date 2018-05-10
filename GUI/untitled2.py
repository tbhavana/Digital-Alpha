# =============================================================================
# try:
#     import Tkinter as tk     ## Python 2.x
# except ImportError:
# =============================================================================
import tkinter as tk     ## Python 3.x

class TestCallback:
   def __init__(self):
      self.top = tk.Tk()
      self.top.geometry( "100x100+10+10" )
      self.top.minsize( 200, 175 )

      self.day_list = [1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,
                  16,17,18,19,20,21,22,23,24,25,26,27,28,29,30, 31]

      tk.Button(self.top, text='Exit',
             command=self.top.quit, bg='red', fg='yellow' ).pack(
             side="bottom", fill="x", expand=1)

      tk.Button(self.top, text='Show Selection',
             command=self.test_callback, bg='blue', 
             fg='yellow' ).pack(side="bottom", fill="x", expand=1)

      self.create_listbox()
      self.top.mainloop()


   def create_listbox(self):
      self.listbox = tk.Listbox( self.top, height=6, width=20, font=('Fixed', 14) )

      for item in self.day_list:
          self.listbox.insert("end", "%02d" % (item))

      self.listbox.pack(side="left")
      self.listbox.see(2)

   def test_callback(self):
      value=self.listbox.curselection()[0]  ## assumes only one item selected
      self.listbox.destroy()
      tk.Label(self.top,
               text="you chose %d=day #%d" %(value, self.day_list[value]),
               bg="white").pack()

TC = TestCallback()