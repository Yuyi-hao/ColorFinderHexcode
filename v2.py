from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
from colorthief import ColorThief
import os
import base64
from io import BytesIO
from pngToBase64 import image_logo, image_icon
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

class ColorFinder:
    def __init__(self) -> None:
        window = Tk()
        window.title("Color picker from Image")
        window.geometry("800x470+100+100")
        window.resizable(False,False)
        self.currentFile = ""

        # icon 
        icon_image = Image.open(BytesIO(base64.b64decode(image_icon))) # using base64 code instead of image 
        icon_image = ImageTk.PhotoImage(icon_image, master = window)
        window.iconphoto(False,icon_image)

        # Blue banner
        Label(window,width=120,height=10,bg = "#4272f9").pack()
        self.frame = Frame(window, width = 700, height = 370, bg="#fff")
        self.frame.place(x=50,y=50)

        # logo and name 
        logo_image = Image.open(BytesIO(base64.b64decode(image_logo))) # using base64 code instead of image 
        logo_image = ImageTk.PhotoImage(logo_image, master = window)
        Label(self.frame, text="Color Finder", font = "arial 25 bold", bg="white").place(x=100, y = 20)
        Label(self.frame, image=logo_image, bg="#ffffff").place(x=10, y=10)



        # color columns
        self.colors = Canvas(self.frame, bg= "#fff", width = 150, height = 265, bd = 0)
        self.colors.place(x = 20, y = 90)
        self.colors2 = Canvas(self.frame, bg= "#fff", width = 150, height = 265, bd = 0)
        self.colors2.place(x = 180 , y = 90)

        self.id_list = []
        self.hex_list = []

        y = 10 
        for i in range(5):
            id = self.colors.create_rectangle((10,y,50,y+40))
            hex_text = Label(self.colors)
            hex_text.place(x=80, y= y+10)
            id2 = self.colors2.create_rectangle((10,y,50,y+40))
            hex_text2 = Label(self.colors2)
            hex_text2.place(x=80, y= y+10)
            self.id_list.append(id)
            self.hex_list.append(hex_text)
            self.id_list.append(id2)
            self.hex_list.append(hex_text2)
            y +=50

        # select image 
        self.selectImage = Frame(self.frame, width = 340, height=350, bg="#d6dee5")
        self.selectImage.place(x=350, y=10)

        # display image 
        self.displayImage = Frame(self.selectImage, bd=3, bg="black",width = 320, height = 280, relief=GROOVE)
        self.displayImage.place(x=10, y=10)

        self.lb1 = Label(self.displayImage,bg="black")
        self.lb1.place(x=0, y=0)

        # Buttons 
        Button(self.selectImage, text="Select Image", width=12, height = 1, font="arial 14 bold", relief=GROOVE, command=self.showImage).place(x=10, y=300)
        Button(self.selectImage, text="Show Color", width=12, height = 1, font="arial 14 bold", relief=GROOVE, command=self.findColor).place(x=170, y=300)

        window.mainloop()

    def showImage(self):
        self.filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file", filetypes=(('PNG file','*.png'),('JPEG file','*.jpeg'),('JPG file','*.jpg')))
        img = Image.open(self.filename)
        # resize image 
        resize_img = img.resize((310,270), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resize_img)
        self.lb1.configure(image=img, width=310, height=270)
        self.lb1.image = img

    def findColor(self):
        ct = ColorThief(self.filename)
        palette = ct.get_palette(color_count=11)
        hexColor = lambda rgb : f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
        hexPalette = [hexColor(rgb) for rgb in palette]

        for i in range(0,10,2):
            self.colors.itemconfig(self.id_list[i], fill=hexPalette[i])
            self.colors2.itemconfig(self.id_list[i+1], fill=hexPalette[i+1])
            self.hex_list[i]["text"] = hexPalette[i]
            self.hex_list[i+1]["text"] = hexPalette[i+1]

ColorFinder()