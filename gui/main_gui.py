import os
import tkinter
from tkinter import *
USER = os.getlogin()

main_menu = Tk() #create window for main_menu
main_menu.geometry("400x300") #set wm window
main_menu.title("My computer")
main_menu.iconphoto(False, tkinter.PhotoImage(file=r"C:\Users\ComServices\PycharmProjects\My computer\image file\testimage.png"))
#why th do i spend sm time on icon 32x32 TO GET SOMETHING LIKE THIS

touch_button = Button(main_menu)

# its start text
mypc_text = Label(main_menu, text="Hello, how may i can help you today?", font= 10) #make a text
#enter to confirm the commands
enter = Button(main_menu, text="Enter")

#face to display
mypc_face = PhotoImage(file=r"C:\Users\ComServices\PycharmProjects\My computer\image file\my_pc_high_pizel.png")
#this one is for reaction when touch it
mypc_smileface = PhotoImage(file=r"C:\Users\ComServices\PycharmProjects\My computer\image file\my_pc_^-^.png")

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