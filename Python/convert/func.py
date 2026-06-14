from tkinter import*
from tkinter import messagebox


def ck():
	messagebox.showinfo("Hello !", "What's up, doc?")

def cki():
	messagebox.showwarning("Warning", "Work in progress...", icon="error")

def cko():
	messagebox.showinfo("Work", "Coming soon...", icon="error")

def showletter():
	messagebox.showinfo("Letters", "Ya will see letters")

def A():
	messagebox.showinfo("letter", "A")

def B():
	messagebox.showinfo("letter", "B")

def C():
	messagebox.showinfo("letter", "C")

def quit():
	MsgBox = messagebox.askquestion("Ask Question Example", "Quit?")
	if MsgBox == "yes":
		fenetre.destroy()
	else:
		messagebox.showinfo("Welcome Back", "Welcome back to the App")