import csv
import json
import tkinter as tk
from tkinter import filedialog as fd
import os
from twilio.rest import Client
from PIL import Image, ImageTk



def send_message(file, text):
    """ send a message """
    # verification
    f = open("secret.json", 'r')
    secret = json.load(f)

    auth_token = secret['auth_token']
    account_sid = secret['account_sid']

    f.close()
    client = Client(account_sid, auth_token)

    names = []
    numbers = []

    # parse the csv file
    f = open(file)

    reader = csv.reader(f)

    for row in reader:
        names.append(row[0])
        numbers.append(row[1])


    # iterate through names and numbers
    for name, number in zip(names, numbers):

        # text the message
        client.messages.create(to=number, from_="+1 (469) 754-9682", body=text.format(name))




def gui():
    """ render the Gui, obviously"""
    
    # declare the globals
    global csv_file_ask
    global message
    
    window = tk.Tk()
    window.geometry('400x400')

    # create frame title
    window.title('ACC TextMessages')

    # make the window not resizable
    window.resizable(False, False)

    # make the background black
    window.config(background="white")

    # ACC icon
    window.iconbitmap("C:/Users/bilal/Downloads/acc_logo_icon.ico")

    # insert the message
    message = tk.Text(master=window, width=40, height=10, font=("Ariel", 12))
    message.place(relx=0.5, rely=0.5, anchor="center")

    # open file button
    csv_file_ask = tk.Button(master=window, text="choose a file", command=open_file)
    csv_file_ask.place(relx=0.5, rely=0.8, anchor="center")

    button = tk.Button(text="send", command=lambda: send_message(csv_file, message.get("1.0", "end")))
    button.place(relx=0.5, rely=0.9, anchor="center")

    # ACC logo
    image = Image.open("C:/Users/bilal/OneDrive/Pictures/acc_logo.png")
    image.thumbnail((150, 200), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label_image = tk.Label(image=photo)
    label_image.place(relx=0.5, rely=0.14, anchor="center")
    window.mainloop()

def open_file():
    """open the file"""
    global csv_file
    csv_file = fd.askopenfilename()
    csv_file_ask['state'] = 'disabled'
    
    if os.path.splitext(csv_file)[1] == ".csv":
        return csv_file
    else:
        message.insert(tk.END, "\nOops, thats not a CSV file")
        csv_file_ask['state'] = 'normal'

def main():
    """it's the main function, duuh"""
    gui()

if __name__ == '__main__':
    main()
    