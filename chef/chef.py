from tkinter import * #Το χρησιμοποιούμε για να εισάγουμε την βιβλιοθήκη για το GUI
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import pymysql 

root = Tk() #To κύριο παράθυρό μας
root.title("Chef's Interface") #Ο τίτλος του παραθύρου
root.geometry("500x500") #H διάσταστη του παραθύρου
#Make the app resizeable
root.resizable(False, False) #Width #Height

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=50)

def addNewRecipe():
    top = Toplevel()
    top.title("Add New Recipe")
    top.geometry("200x200")

    addNewFrame = LabelFrame(top, text="Choose your way",padx=5,pady=5,bg="#E59A41").pack(padx=10,pady=10)
    addFromFilesButton = Button(top, text="Add from file").pack()


class FramesOfTabs:
    def __init__(self,master):
        self.my_frame1 = Frame(master, width=500, height=500, bg="white")
        self.my_frame2 = Frame(master, width=500, height=500, bg="white")
        self.my_frame3 = Frame(master, width=500, height=500, bg="white")

        self.my_frame1.pack(fill="both",expand=1)
        self.my_frame2.pack(fill="both",expand=1)
        self.my_frame3.pack(fill="both",expand=1)

        master.add(self.my_frame1, text="Home")
        master.add(self.my_frame2, text="My Recipes")
        master.add(self.my_frame3, text="Settings")

    def addContent(self):
        self.recipesTitle = Label(self.my_frame2, text="Recipes", font=(15),borderwidth=10,width=100,bg="#E59A41",fg="white")
        self.recipesTitle.pack()

        self.firstButton = Button(self.my_frame2, text="Tost", width=100,bg="white").pack()
        self.secondButton = Button(self.my_frame2, text="Spaggeti", width=100,bg="white").pack()
        self.thirdButton = Button(self.my_frame2, text="Bolognese", width=100,bg="white").pack()
        self.fourthButton = Button(self.my_frame2, text="Pizza", width=100,bg="white").pack()
        self.addRecipesButton = Button(self.my_frame2, text="Add New",width=10,bg="#E59A41",command=addNewRecipe).pack(pady=30)



mainInstance = FramesOfTabs(my_notebook).addContent()





root.mainloop() 