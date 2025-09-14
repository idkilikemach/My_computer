# TODO main_gui is unfinished
# TODO Make select function for listbox
# TODO Make enter button open other file like open chat_bot.py
import os # To get USER
from tkinter import *
import random # Use for random greeting text part
USER = os.getlogin() # Get window user account name.

commands = ("Talk to you", "Change file path", "Create file", "Look at the time") # List commands to put into listbox
greeting_text = ("Heyyyyy, how are you :)", "Hellooo", "Hi, how can i help you?", "What do you need? :)")
# Images for every interface, so I will not have to see long path files name.
icon_image_file = r"C:\Users\ComServices\PycharmProjects\My computer\image file\testimage.png"
mypc_normal_expression = r"C:\Users\ComServices\PycharmProjects\My computer\image file\my_pc_high_pizel.png" # Normal emotion
mypc_smileface = r"C:\Users\ComServices\PycharmProjects\My computer\image file\my_pc_^-^.png" # This one is for reaction when touch it, Happy emotion

main_menu = Tk() # Create window for main_menu.
main_menu.geometry("400x300") # Set width x height window.
main_menu.title("My computer") # Set title name.
main_menu.iconphoto(False, PhotoImage(file=icon_image_file)) #Set icon.

list_command_for_tk = Variable(value=commands)

listbox = Listbox(main_menu, yscrollcommand="Right", listvariable=list_command_for_tk, width=50, height=5) # Make select box

mypc_text = Label(main_menu, text=random.choice(greeting_text), font=10, padx=50) # Make a text for my pc to talk.
enter = Button(main_menu, text="Enter", font=("a", 9)) # Enter button for confirming the commands the user select.
mypc_normal_face = PhotoImage(file=mypc_normal_expression) # Face to display and to show emotion.

mypc_smile_face = PhotoImage(file=mypc_smileface)

mypc_show_image = Label(main_menu, image=mypc_normal_face, width=250, height=140)

textbox = Entry(main_menu, justify=LEFT, width=50) # To choose or type the command in
button_for_more = Button(main_menu, text="V", width=2, font=("a", 9)) # look for more commands

def change_expression_face(): # TODO Make face expression when click on invisible button
    touch_button.destroy()

touch_button = Button(main_menu, width=26, height=7, command=change_expression_face)

# mypc_image_on_main_menu
mypc_text.place(x=60, y=10)
mypc_show_image.place(x=68, y=45)
textbox.place(x=50, y=191)
button_for_more.place(x=330, y=190)
enter.place(x=353, y=190)
touch_button.place(x=100,y=50)
listbox.place(x=50, y=209)

main_menu.resizable(False, False)
main_menu.mainloop()