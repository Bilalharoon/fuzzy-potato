import csv
import json
import tkinter as tk
from tkinter import filedialog as fd
from twilio.rest import Client



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


def open_file():
    global file
    file = fd.askopenfilename()
    return file


def gui():
    """ render the Gui"""
    window = tk.Tk()
    window.geometry('400x400')

    # create frame title
    window.title('Fuzzy Patato')

    # make the window not resizable
    window.resizable(False, False)

    # make the background black
    window.config(background="white")

    # insert the message
    message = tk.Text(master=window, width=40, height=10, font=("Times New Roman", 12))
    message.place(relx=0.5, rely=0.5, anchor="center")

    csv_file = tk.Button(master=window, text="choose a file", command=open_file)
    csv_file.place(relx=0.5, rely=0.8, anchor="center")

    button = tk.Button(text="send", command=lambda: send_message(file, message.get("1.0", "end")))
    button.place(relx=0.5, rely=0.9, anchor="center")

    # image = Image.open('c:/Users/bilal/OneDrive/Pictures/pakistan-flag-e1345558966990.jpg')
    # image.thumbnail((100, 100), Image.ANTIALIAS)
    # photo = ImageTk.PhotoImage(image)
    # label_image = tk.Label(image=photo)
    # label_image.grid(column=1, row=0)
    # window.mainloop()


def main():
    gui()

if __name__ == '__main__':
    main()
    