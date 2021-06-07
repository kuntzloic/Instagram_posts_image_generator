import tkinter as tk
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from tkinter import filedialog

import textwrap

def draw_multiple_line_text(image, text, font, text_color, text_start_height):
    '''
    From unutbu on [python PIL draw multiline text on image](https://stackoverflow.com/a/7698300/395857)
    '''
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height


    testtext = "a"
    lena=1
    w, h = draw.textsize(testtext, font=font)
    while(w < 960):
        testtext = testtext+"a"
        lena += 1
        w, h = draw.textsize(testtext, font=font)
      #  print(w, "testtext:", w, testtext)

    lines = textwrap.wrap(text, width=lena)
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text),
                  line, font=font, fill=text_color)
        y_text += line_height

def openBG():
    bg_file_name = filedialog.askopenfilename(initialdir="", title="Sélectionnez une image d'arrière plan en 1000*1000",
                                             filetypes=(("PNG", "*.png"), ("All files", "*.*")))
    print(bg_file_name)
    dft_bg_name.set(bg_file_name)

def openIllustration():
    fg_file_name = filedialog.askopenfilename(initialdir="", title="Sélectionnez une image d'illustration",
                                             filetypes=(("PNG", "*.png"), ("JPEG", "*.jpeg"), ("JPG", "*.jpg"), ("All files", "*.*")))
    print(fg_file_name)
    dft_fg_name.set(fg_file_name)

def createimg():
    img_bg = Image.open(inp_bg_name.get())

    newwidth = int(inp_fgwidth_name.get())
    subtitle = inp_title_name.get()
    content = inp_desc_name.get()

    img_article = Image.open(inp_fg_name.get())

    widthimgart = img_article.size[0]
    heigthimgart = img_article.size[1]

    newheightart = int(newwidth * (heigthimgart / widthimgart))

    size = (newwidth, newheightart)
    box = (0, 0, widthimgart, heigthimgart)

    out = img_article.resize(size, box=box)

    out = out.convert("RGBA")


    ximage = int(img_bg.size[0] / 2) - int(out.size[0] / 2)
    yimage = int(img_bg.size[1] / 2) - int(out.size[1] / 2) + scale_height_img.get()
    imgheight = out.size[1]

    img_bg.paste(out, (ximage, yimage), out)

    fnt = ImageFont.truetype("Neon.ttf", scale_font_sz_title.get())
    fntcontent = ImageFont.truetype("Neon.ttf", scale_font_sz_desc.get())


    draw_multiple_line_text(img_bg, subtitle, fnt, (255, 255, 255), scale_height_title.get())
    draw_multiple_line_text(img_bg, content, fntcontent, (255, 255, 255), yimage + imgheight + 10 + scale_height_desc.get())
    return img_bg

def previewimg():
    img_in = createimg()
    img_in.show()

def saveimg():
    img_in = createimg()
    img_in.save("output/"+inp_sve_name.get())

if __name__ == '__main__':

    fen = tk.Tk()
    fen.geometry("300x630")

    bgFrame = tk.Frame(fen, bd=1)
    lbl_bg_name = tk.Label(fen, text="Nom du fond")

    dft_bg_name = tk.StringVar(fen)
    dft_bg_name.set("template-bg.png")
    inp_bg_name = tk.Entry(bgFrame, textvariable=dft_bg_name)
    openButton = tk.Button(bgFrame, text="Ouvrir...", command=openBG)
    inp_bg_name.grid(row=0, column=0)
    openButton.grid(row=0, column=1)

    art_img_Frame = tk.Frame(fen, bd=1)

    lbl_fg_name = tk.Label(fen, text="Nom de l'illustration")

    dft_fg_name = tk.StringVar(fen)
    dft_fg_name.set("bs-logo.png")
    inp_fg_name = tk.Entry(art_img_Frame, textvariable=dft_fg_name)
    open_art_img_Button = tk.Button(art_img_Frame, text="Ouvrir...", command=openIllustration)
    inp_fg_name.grid(row=0, column=0)
    open_art_img_Button.grid(row=0, column=1)

    lbl_fgwidth_name = tk.Label(fen, text="Largeur de l'illustration")

    dft_fgwidth_name = tk.StringVar(fen)
    dft_fgwidth_name.set("400")
    inp_fgwidth_name = tk.Entry(fen, textvariable=dft_fgwidth_name)


    lbl_title_name = tk.Label(fen, text="Titre du post")

    dft_title_name = tk.StringVar(fen)
    dft_title_name.set("Lorem Ipsum")
    inp_title_name = tk.Entry(fen, textvariable=dft_title_name)

    lbl_desc_name = tk.Label(fen, text="Description")

    dft_desc_name = tk.StringVar(fen)
    dft_desc_name.set("Dolor si amet")
    inp_desc_name = tk.Entry(fen, textvariable=dft_desc_name)

    lbl_height_img = tk.Label(fen, text="Hauteur de l'image")

    value_height_img = tk.IntVar(fen, 0)
    scale_height_img = tk.Scale(fen, variable=value_height_img, from_=-200, to_=200, orient=tk.HORIZONTAL)

    lbl_height_title = tk.Label(fen, text="Hauteur du titre")

    value_height_title = tk.IntVar(fen, 125)
    scale_height_title = tk.Scale(fen, variable=value_height_title, from_=80, to_=280, orient=tk.HORIZONTAL)

    lbl_height_desc = tk.Label(fen, text="Hauteur de la description")

    value_height_desc = tk.IntVar(fen, 0)
    scale_height_desc = tk.Scale(fen, variable=value_height_desc, from_=-200, to_=200, orient=tk.HORIZONTAL)

    lbl_font_sz_title = tk.Label(fen, text="Taille de police du titre")

    value_font_sz_title = tk.IntVar(fen, 80)
    scale_font_sz_title = tk.Scale(fen, variable=value_font_sz_title, from_=15, to_=180, orient=tk.HORIZONTAL)

    lbl_font_sz_desc = tk.Label(fen, text="Taille de police de la desc")

    value_font_sz_desc = tk.IntVar(fen, 70)
    scale_font_sz_desc = tk.Scale(fen, variable=value_font_sz_desc, from_=15, to_=180, orient=tk.HORIZONTAL)

    lbl_sve_name = tk.Label(fen, text="Nom enregistrement")

    dft_sve_name = tk.StringVar(fen)
    dft_sve_name.set("output.png")
    inp_sve_name = tk.Entry(fen, textvariable=dft_sve_name)

    previewButton = tk.Button(fen, text="Preview", command=previewimg)
    saveButton = tk.Button(fen, text="Save", command=saveimg)



    lbl_bg_name.pack()
    bgFrame.pack()

    lbl_fg_name.pack()
    art_img_Frame.pack()

    lbl_fgwidth_name.pack()
    inp_fgwidth_name.pack()

    lbl_title_name.pack()
    inp_title_name.pack()

    lbl_desc_name.pack()
    inp_desc_name.pack()

    lbl_sve_name.pack()
    inp_sve_name.pack()

    lbl_height_title.pack()
    scale_height_title.pack()

    lbl_height_desc.pack()
    scale_height_desc.pack()

    lbl_height_img.pack()
    scale_height_img.pack()

    lbl_font_sz_title.pack()
    scale_font_sz_title.pack()

    lbl_font_sz_desc.pack()
    scale_font_sz_desc.pack()

    previewButton.pack()
    saveButton.pack()

    fen.mainloop()



  #  subtitle = input("Veuillez entrer le sous-titre : ")
    subtitle = "ululu"
    content = "Lorem ipsum dolor si amet"
  #  content = input("Veuillez entrer la description : ")