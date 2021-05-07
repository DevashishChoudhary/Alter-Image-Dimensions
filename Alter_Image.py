import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

TK_SILENCE_DEPRECATION=1
root = Tk()
root.title("Altering Image Dimension (Devashish Choudhary)")
root.minsize(400,200)

count = 0
def open_image():
    global input_image, image_width, image_height, image, image_dir
    root.filename = filedialog.askopenfilename(initialdir="/Users/isshu/Desktop",title="Select a file", filetypes=(("png files","*.png"),("jpg files","*.jpg")))
    input_Label = Label(root, text='Path of the Input Image is mention below:\n'+root.filename).pack()
    input_image = ImageTk.PhotoImage(Image.open(root.filename))
    image = Image.open(root.filename)
    width, height = Image.open(root.filename).size
    image_width = width
    image_height = height
    image_path = root.filename
    image_dir = os.path.dirname(image_path)
    #input_image_Label = Label(image=input_image).pack()

def alter_image():
    global count
    temp_width = image_width
    temp_height = image_height
    temp_image = image
    for count in range(4):
        count += 1
        box = ((temp_width/4), (temp_height/4), 3*(temp_width/4), 3*(temp_height/4))
        cropped_image = temp_image.crop(box)
        cropped_image.save(image_dir+'/cropped_image_'+str(count)+'.jpg')
        print(cropped_image.size)

        temp_width = temp_width/2
        temp_height = temp_height/2

        print(temp_width, temp_height)
        temp_image = Image.open(image_dir+'/cropped_image_'+str(count)+'.jpg')

    final_image = temp_image.resize((image_width, image_height))
    final_image.save(image_dir+'/Final_Image_Result.jpg')

    result_Label = Label(root, text='Path of the Resulting Image is mention below:\n'+image_dir+'/Final_Image_Result.jpg').pack()
    print(final_image.size)


my_Button_open = Button(root, text="Open File", highlightbackground='#3E4149', command=open_image).pack(side=tkinter.LEFT)


my_Button_alter = Button(root, text="Alter Image", highlightbackground='#3E5149', command=alter_image).pack(side=tkinter.RIGHT)

root.mainloop()
