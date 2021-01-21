
from tkinter import *

import random





root = Tk()

root.geometry("600x600")

root.title("Roll Dice")


label = Label(root, text='', font=('Helvetica', 260))

# count= IntVar(root, value = 0)

def roll_dice():

     dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
     
     dice1=random.choice(dice)
     
     dice2 = random.choice(dice)
     
     label.configure(text=f'{dice1} {dice2}',fg="blue")
     
     label.pack()
     

     if dice1==dice2:
     
        data="Congratulation!"

        # count = count+1
        
        text1 = Label(root,text=f"{data}",fg="green")
        
        text1.pack()
        
        # if(count==3):
        
        #     print("you won three times!")
        
        
        #     exit()
        
        # os.system('cls')
        




button = Button(root, text='roll dice', foreground='blue', command=roll_dice)

button.pack()


root.mainloop()
