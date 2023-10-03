import tkinter as tk

window = tk.Tk()

def decrease():
    result = int(lblCounter['text'])
    result -= 1
    lblCounter["text"] = result

def increase():
    result = int(lblCounter['text'])
    result += 1
    lblCounter["text"] = result

window.title("Counter")
window.geometry('500x300')

btnDecrease = tk.Button(window, text="-", command=decrease)
lblCounter = tk.Label(window, text="0")
btnIncrease = tk.Button(window, text="+", command=increase)

btnDecrease.grid(column=0, row=0)
lblCounter.grid(column=1, row=0)
btnIncrease.grid(column=2, row=0)

window.mainloop()
