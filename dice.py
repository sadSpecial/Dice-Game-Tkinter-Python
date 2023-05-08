# instagram page : https://instagram.com/abolfazl._r?igshid=YmMyMTA2M2Y
# Email: abolfazl8abolfazl@yahoo.com
# MyGithub : https://github.com/sadSpecial

import tkinter as tk
import random as rand

MainWin = tk.Tk()
MainWin.title("Dice Application :DD")
MainWin.geometry("600x200")
MainWin.resizable(False,False)

DiceLabel = tk.Label(MainWin,text="",fg="red",font=("Arial",25))

def Dice():
    Export = rand.randint(1,6)
    DiceLabel.config(text=f"Dice {Export}")

DiceBT = tk.Button(MainWin,text="Dice", command= Dice,height= 3, width=25)

DiceLabel.pack()

tk.Label(MainWin,text="",fg="gray").pack()
tk.Label(MainWin,text="~~~~~~~~~~~~~~~~~~~~",fg="gray").pack()
tk.Label(MainWin,text="",fg="gray").pack()

DiceBT.pack()

MainWin.mainloop()

# instagram page : https://instagram.com/abolfazl._r?igshid=YmMyMTA2M2Y
# Email: abolfazl8abolfazl@yahoo.com
# MyGithub : https://github.com/sadSpecial