from tkinter import *
import random

root = Tk()
root.title("Rueda de las mil Desgracias")
root.geometry("400x400")

list1 = ["Beatriz", "Sergio", "Rocio", "Diego", "Hector", "Alma", "Bonita", "Fifi", "Queso"]

print(list1)

def random_no():
    random_no = random.randint(0,8)
    print(random_no)
    random_unlucky_friend = list1[random_no]
    print("La persona Elegia fué...  " + random_unlucky_friend)
    
btn1 = Button(root,text="Quién es el desafortunado", command = random_no)
btn1.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()