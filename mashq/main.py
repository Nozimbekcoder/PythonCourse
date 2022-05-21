from tkinter import*


root = Tk()
root.title("Mashq")
root.geometry("1000x500")

imgauto = PhotoImage(file="auto1.png")

Label(root, image=imgauto).pack()


root.mainloop()