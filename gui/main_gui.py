# TODO main_gui is unfinished
import os
import tkinter
from tkinter import *
USER = os.getlogin() # Get window user account name.

# Images for every interface, so I will not have to see long path files name.
icon_image_file = r"C:\Users\ComServices\PycharmProjects\My computer\image file\testimage.png"
my_pc_high_pixel_image = r"C:\Users\ComServices\PycharmProjects\My computer\image file\my_pc_high_pizel.png"
mypc_smileface = r"C:\Users\ComServices\PycharmProjects\My computer\image file\my_pc_^-^.png" # This one is for reaction when touch it

main_menu = Tk() # Create window for main_menu.
main_menu.geometry("400x300") # Set width x height window.
main_menu.title("My computer") # Set title name.
main_menu.iconphoto(False, tkinter.PhotoImage(file=icon_image_file)) #Set icon.

touch_button = Button(main_menu)

mypc_text = Label(main_menu, text="Hello, how may i can help you today?", font= 10) # Make a text for my pc to talk.

enter = Button(main_menu, text="Enter") # Enter button for confirming the commands the user select.

mypc_face = PhotoImage(file=my_pc_high_pixel_image) # Face to display and to show emotion.


mypc_show_image = Label(main_menu, image=mypc_face, width=250, height=140)
textbox = Entry(main_menu, justify=LEFT, width=50) # to choose or type the command in
button_for_more = Button(main_menu, text="V", width=2, height=1) # look for more commands

# mypc_image_on_main_menu
mypc_text.place(x=60, y=10)
mypc_show_image.place(x=68, y=45)
textbox.place(x=50, y=191)
#button_for_more.pack()
#enter.pack()
touch_button.pack()

main_menu.resizable(False, False)
main_menu.mainloop()
