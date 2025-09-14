# TODO chat_bot is unfinished
from tkinter import *

icon_image_file = r"C:\Users\ComServices\PycharmProjects\My computer\image file\testimage.png"
chat = Tk() # create window
chat.geometry("400x300") #change window size
chat.title("Talk to me")
sent = Button(chat, text="Send", width=10, height=3) # a button to send text to bot
save = Button(chat, text="Save", width=6) # save the conversation
load = Button(chat, text="Load", width=6) # load the conversation
chat_textbox = Text(chat, height=4, width=46) # input text
chat.iconphoto(False, PhotoImage(file=icon_image_file)) # change icon
scroll_bar = Scrollbar(chat) #scroll throng the chat
#message test
text = Label(chat, text="You : Well i think i like you")
text.place(x=10, y=35)

#set place for gui

chat_textbox.place(x=0, y=245)
load.place(x=50, y=0)
save.place(x=0, y=0)
sent.place(x=321, y=245)
scroll_bar.pack(side="right")
chat.resizable(False, False)
chat.mainloop()

def send_button():
    # TODO make a sent button
    print(None)

def display_message():
    # TODO Displaying message
    print(None)

def scroll():
    # TODO Make scroll
    print(None)