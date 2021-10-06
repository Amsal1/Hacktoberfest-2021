from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFilter, ImageEnhance


def view_image(root, label1, copy_of_image):
    photo = ImageTk.PhotoImage(copy_of_image)
    label = Label(root, image=photo)
    label.bind('<configure>',resize_image(root,copy_of_image,label1))
    label.pack()

def blur(path, root, label1):
    image = Image.open(path)
    copy_of_image = image.filter(ImageFilter.GaussianBlur(6))
    view_image(root, label1, copy_of_image)

def contour(path, root, label1):
    image = Image.open(path)
    copy_of_image = image.filter(ImageFilter.CONTOUR)
    view_image(root, label1, copy_of_image)

def edge_detailed(path, root, label1):
    image = Image.open(path)
    copy_of_image = image.filter(ImageFilter.EDGE_ENHANCE)
    view_image(root, label1, copy_of_image)

def emboss(path, root, label1):
    image = Image.open(path)
    copy_of_image = image.filter(ImageFilter.EMBOSS)
    view_image(root, label1, copy_of_image)

def rgb_jumble(path, root, label1):
    try:
        messagebox.showinfo("WAIT", "this may take some time according to size of your image")
        image = Image.open(path)
        for x in range(image.size[0]):
            for y in range(image.size[1]):
                r,g,b = image.getpixel((x,y))
                image.putpixel((x,y),(b,r,g))
        view_image(root, label1, image)
    except:
        messagebox.showerror("error", "this image cannot be jumbled")

def rgb_jumble1(path, root, label1):
    try:
        messagebox.showinfo("WAIT", "this may take some time according to size of your image")
        image = Image.open(path)
        for x in range(image.size[0]):
            for y in range(image.size[1]):
                r,g,b = image.getpixel((x,y))
                image.putpixel((x,y),(g,r,b))
        view_image(root, label1, image)
    except:
        messagebox.showerror("error", "this image cannot be jumbled")

def rgb_jumble2(path, root, label1):
    try:
        messagebox.showinfo("WAIT", "this may take some time according to size of your image")
        image = Image.open(path)
        for x in range(image.size[0]):
            for y in range(image.size[1]):
                r,g,b = image.getpixel((x,y))
                image.putpixel((x,y),(b,g,r))
        view_image(root, label1, image)
    except:
        messagebox.showerror("error", "this image cannot be jumbled")
        

    

def sharpen(path, root, label1):
    image = Image.open(path)
    enhancer = ImageEnhance.Sharpness(image)
    copy_of_image = enhancer.enhance(7)
    view_image(root, label1, copy_of_image)

def BnW(path, root, label1):
    image = Image.open(path)
    enhancer = ImageEnhance.Color(image)
    copy_of_image = enhancer.enhance(0)
    view_image(root, label1, copy_of_image)

def colour_increase(path, root, label1):
    image = Image.open(path)
    enhancer = ImageEnhance.Color(image)
    copy_of_image = enhancer.enhance(2)
    view_image(root, label1, copy_of_image)

def brightness_increase(path, root, label1):
    image = Image.open(path)
    enhancer = ImageEnhance.Brightness(image)
    copy_of_image = enhancer.enhance(1.5)
    view_image(root, label1, copy_of_image)

def contrast_increase(path, root, label1):
    image = Image.open(path)
    enhancer = ImageEnhance.Contrast(image)
    copy_of_image = enhancer.enhance(1.5)
    view_image(root, label1, copy_of_image)

def vertical_flip(path, root, label1):
    image = Image.open(path)
    copy_of_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    view_image(root, label1, copy_of_image)

def horizontal_flip(path, root, label1):
    image = Image.open(path)
    copy_of_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    view_image(root, label1, copy_of_image)

def resize_image(root, copy_of_image, label1):
    new_height = 600
    new_width = 975
    image=copy_of_image.resize((new_width,new_height))
    photo = ImageTk.PhotoImage(image)
    label1.configure(image=photo)
    label1.image = photo

    
