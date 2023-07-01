from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from calculator import *
root = Tk()
root.geometry("400x400+400+100")
root.title("Calculator")
root.resizable(0, 0)

inp = StringVar()

screen = ttk.Entry(root, text=inp, width=30,
                   justify="right", font=(10), state='readonly')
screen.grid(row=0, columnspan=4, padx=15, pady=15, ipady=5)

output = StringVar()

outputBox = ttk.Entry(root, text=output, width=30,
                      justify="right", font=(10), state='readonly')
outputBox.grid(row=1, columnspan=4, padx=15, pady=15, ipady=5)


key_matrix = [["C", "(", ")", "/"],
              ["7", "8", "9", "*"],
              ["4", "5", "6", "-"],
              ["1", "2", "3", "+"],
              ["ext", "0", "00", "="]]



result = 0


def calculate(event):
    button = event.widget.cget("text")
    global key_matrix, inp, result, output

    try:

        if '/0' in inp.get():
            output.set('Error ! undefined :/')

        if button == "C":
            inp.set("")
            output.set('')

        elif button == "ext":
            choice = messagebox.askokcancel(
                'Exit', 'Do you want to exit the program ?')
            if choice:
                root.destroy()

        elif button == '=':
            result = str(braket(inp.get()))
            output.set(str(result))

        else:
            inp.set(inp.get() + str(button))

        result = str(braket(inp.get()))
        output.set(str(result))

    except:
        pass

btn_dict = {}

for i in range(len(key_matrix)):
    for j in range(len(key_matrix[i])):

        btn_dict["btn_" + str(key_matrix[i][j])
                 ] = ttk.Button(root,  text=str(key_matrix[i][j]))

        btn_dict["btn_" + str(key_matrix[i][j])].grid(row=i+2,
                                                      column=j, padx=5, pady=5, ipadx=5, ipady=5)

        btn_dict["btn_" + str(key_matrix[i][j])].bind("<Button-1>", calculate)


root.mainloop()
