from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox
from tkinter import filedialog
import manipulation


root = Tk()
root.title("Visualise")
root.geometry("1000x650")
root.resizable(False, False)


def resize_image(root, copy_of_image, label1):
    new_height = 600
    new_width = 975
    image=copy_of_image.resize((new_width,new_height))
    photo = ImageTk.PhotoImage(image)
    label1.configure(image=photo)
    label1.image = photo


def next():
    global n
    global items_list
    n = (n+1)%len(items_list)
    img1 = items_list[n]
    print(img1)
    image = Image.open(directory_name + "/" + img1)
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(root, image=photo)
    label.bind('<configure>',resize_image(root,copy_of_image,label1))
    label.pack()

def previous():
    global n
    global items_list
    n = (n-1)%len(items_list)
    img1 = items_list[n]
    print(img1)
    image = Image.open(directory_name + "/" + img1)
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(root, image=photo)
    label.bind('<configure>',resize_image(root,copy_of_image,label1))
    label.pack()

def browse_folder():
    global directory_name
    global items_list
    global n
    
    directory_name =  filedialog.askdirectory(initialdir="./", title="Select Folder")
    items_list = os.listdir(directory_name)
    if len(items_list) <= 0:
        messagebox.showerror("error", "no images in the given folder")
        exit0()
    n = 0
    img1 = items_list[n]

    image = Image.open(directory_name+ "/" + img1)
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)

    label = Label(root, image=photo)
    label.bind('<configure>',resize_image(root,copy_of_image,label1))
    label.pack()

def open_edit_options():
    global directory_name
    global n
    global root
    edit_options = Toplevel()
    edit_options.title("Edit options")
    edit_options.geometry("240x600")
    edit_options.resizable(False,False)
    Button(edit_options, text="Blur Image",width=30, height=2, command=lambda path=directory_name+"/"+items_list[n] : (manipulation.blur(path, root, label1) ,edit_options.destroy())).pack()
    Button(edit_options, text="sharpen Image",width=30, height=2, command=lambda path=directory_name+"/"+items_list[n] : (manipulation.sharpen(path, root, label1) ,edit_options.destroy())).pack()
    Button(edit_options, text="Black & White",width=30, height=2, command=lambda path=directory_name+"/"+items_list[n] : (manipulation.BnW(path, root, label1) ,edit_options.destroy())).pack()
    Button(edit_options, text="Enhance Colour",width=30, height=2, command=lambda path=directory_name+"/"+items_list[n] : (manipulation.colour_increase(path, root, label1) ,edit_options.destroy())).pack()
    Button(edit_options, text="Increase Brightness",width=30, height=2, command=lambda path=directory_name+"/"+items_list[n] : (manipulation.brightness_increase(path, root, label1) ,edit_options.destroy())).pack()
    Button(edit_options, text="Increase Contrast",width=30, height=2, command=lambda path=directory_name+"/"+items_list[n] : (manipulation.contrast_increase(path, root, label1) ,edit_options.destroy())).pack()
    Button(edit_options, text="Vertical Flip",width=30, height=2, command=lambda path=directory_name+"/"+items_list[n] : (manipulation.vertical_flip(path, root, label1) ,edit_options.destroy())).pack()
    Button(edit_options, text="Horizontal Flip",width=30, height=2, command=lambda path=directory_name+"/"+items_list[n] : (manipulation.horizontal_flip(path, root, label1) ,edit_options.destroy())).pack()
    Button(edit_options, text="Contour",width=30, height=2, command=lambda path=directory_name+"/"+items_list[n] : (manipulation.contour(path, root, label1) ,edit_options.destroy())).pack()
    Button(edit_options, text="Edge Detailed",width=30, height=2, command=lambda path=directory_name+"/"+items_list[n] : (manipulation.edge_detailed(path, root, label1) ,edit_options.destroy())).pack()
    Button(edit_options, text="Emboss",width=30, height=2, command=lambda path=directory_name+"/"+items_list[n] : (manipulation.emboss(path, root, label1) ,edit_options.destroy())).pack()
    Button(edit_options, text="RGB Jumble",width=30, height=2, command=lambda path=directory_name+"/"+items_list[n] : (manipulation.rgb_jumble(path, root, label1) ,edit_options.destroy())).pack()
    Button(edit_options, text="RGB Jumble 1",width=30, height=2, command=lambda path=directory_name+"/"+items_list[n] : (manipulation.rgb_jumble1(path, root, label1) ,edit_options.destroy())).pack()
    Button(edit_options, text="RGB Jumble 2",width=30, height=2, command=lambda path=directory_name+"/"+items_list[n] : (manipulation.rgb_jumble2(path, root, label1) ,edit_options.destroy())).pack()
    
    
def exit0():
    root.destroy()

    
#menu bar
menubar = Menu(root)
root.config(menu = menubar)

file_menu = Menu(menubar)
menubar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Browse Folder", command=browse_folder)
file_menu.add_separator()
file_menu.add_command(label="exit", command=exit0)


#images part and swipe buttons
n=0
items_list = os.listdir("images")
directory_name = "./images/"

if len(items_list) <= 0:
    messagebox.showerror("error", "no images in the given folder")
    exit0()
    
img1 = items_list[n]

image = Image.open(directory_name + img1)
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)

label1 = Label(root, image=photo)
label1.bind('<configure>',resize_image(root,copy_of_image,label1))
label1.pack()

b1 = Button(root,text=">>", width=3, height=10, bg='grey', command=next)
b1.place(x=972,y=300)

b2 = Button(root,text="<<", width=3, height=10, bg='grey', command=previous)
b2.place(x=0,y=300)

btn = Button(root, text="Edit Options",width=70, height=2, bg='green', fg='white', command=open_edit_options).pack()

root.mainloop()
