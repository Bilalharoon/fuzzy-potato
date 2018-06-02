import tkinter as tk


window = tk.Tk()
window.geometry('400x400')

# create frame title
window.title('Fuzzy Patato') 

Message = tk.Text(master=window, width=40, height=10)
Message.pack()

def command():
    print(Message.get("1.0", "end"))

button = tk.Button(command=command, text="GO")
button.pack()
window.mainloop()
