from tkinter import*
from tkinter import messagebox
import webbrowser

def callback(url):
   webbrowser.open_new_tab(url)

def text():
	fenetre =Tk()
	fenetre.title = "Code source"
	f0=PanedWindow(fenetre, orient=HORIZONTAL, bg="gray")
	f0.pack(side=TOP, expand=True, fill="x")
	label1 = Label(f0, text='Python code only', font=("Arial", 20), relief="groove", fg="black", bg="#901e1e")
	label1.pack(ipadx=10, ipady=5, padx=10, pady=10)
	label2 = Label(f0, text='Inforamtions about the code are stored in the GitHub deposit', font=("Arial", 20), relief="groove", fg="black")
	label2.pack(ipadx=10, ipady=5, padx=10, pady=10)
	label3 = Label(f0, text='The deposit is avaiable at the url underneath', font=("Arial", 20), relief="groove", fg="black")
	label3.pack(ipadx=10, ipady=5, padx=10, pady=10)
	link = Label(f0, text='https://github.com/xcgfgfcfqgqxhsjhgfjgkdfd/Python_dep_666', font=("Arial", 20), relief="groove", fg="black")
	link.pack(ipadx=10, ipady=5, padx=10, pady=10)
	link.bind("<Button-1>", lambda e: callback("https://github.com/xcgfgfcfqgqxhsjhgfjgkdfd/Python_dep_666"))
	fenetre.mainloop()