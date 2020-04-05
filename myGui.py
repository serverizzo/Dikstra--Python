import tkinter as tk
from dikstra2 import dikstra


def printToConsole():
    print(input1.get())







if __name__ == "__main__":

    window = tk.Tk()
    #can't seem to get the height and witdth to initalize 
    window.geometry('400x150')
    window.title("ED is So LEE3T")

    greeting = tk.Label(text="Hello, Tkinter")
    greeting.pack()
    wid2 = tk.Label(text="Another thing here!")
    wid2.pack()
    btn1 = tk.Button(command = printToConsole, text="I-- Am a button?!?")
    btn1.pack()

    input1 = tk.Entry(width = 70)
    input1.pack()

    window.mainloop()
    
    
    pass


