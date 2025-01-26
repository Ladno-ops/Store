from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
import tkinter as tk

if_ops_rdr = False

def OpisanieRdr():
    global rdr_ops_menu
    global if_ops_rdr
    if if_ops_rdr == False:
        rdr_ops_menu['text'] = 'Приключенческая игра в стиле вестерна. Действие разворачивается\nв открытом мире, в котором представлена вымышленная версия\nСоединённых Штатов 1899 года.'
        echo_rdr_button['text'] = 'убрать описание ⇧'
        if_ops_rdr = True
    elif if_ops_rdr == True:
        rdr_ops_menu['text'] = ''
        echo_rdr_button['text'] = 'показать описание ⇩'
        if_ops_rdr = False

if_ops_er = False

def OpisanieEr():
    global er_ops_menu
    global if_ops_er
    if if_ops_er == False:
        er_ops_menu['text'] = 'Elden Ring представляет собой action/RPG с видом от третьего лица,\nсхожую с серией Dark Souls[3]. Хотя игра и не имеет прямой\nсвязи с этой серией, с точки зрения игрового процесса\nона в большой степени основана на Dark Souls.'
        echo_er_button['text'] = 'убрать описание ⇧'
        if_ops_er = True
    elif if_ops_er == True:
        er_ops_menu['text'] = ''
        echo_er_button['text'] = 'показать описание ⇩'
        if_ops_er = False

#=============#

# LOGIN

#=============#

def Login():
    def Register():
        usnm = reg_username_entry.get()
        pswd = reg_password_entry.get()
        if usnm and pswd != "":
            with open('store.txt', 'a', encoding='utf8') as file:
                file.write(usnm + " " + pswd + "\n")
                showinfo('Успешно!', ("Вы зарегестрировались"))
        else:
            showinfo('Ошибка' , ('Убедитесь что оба поля заполены'))

    reg_window = tk.Toplevel(window)
    reg_window.title("Window")
    reg_window.geometry("1200x600")
    reg_window['bg'] = '#2f353b'
    reg_window.resizable(width=False, height=False)

    def Menu():
        reg_window.destroy()
        reg_window.update()

    reg_login = Label(reg_window, text="SIGN IN", font="Monaco 30", bg="#2f353b", fg='white')
    reg_login.place(x=500, y=160)

    reg_username = Label(reg_window, text="USERNAME", font="Monaco 15", bg="#2f353b", fg="white")
    reg_username.place(x=450, y=230)

    reg_username_entry = ttk.Entry(reg_window, width=30)
    reg_username_entry.place(x=570, y=230, height=30)

    reg_password = Label(reg_window, text="PASSWORD", font="Monaco 15", bg="#2f353b", fg="white")
    reg_password.place(x=450, y=300)

    reg_password_entry = ttk.Entry(reg_window, width=30)
    reg_password_entry.place(x=570, y=300, height=30)

    reg_apply = ttk.Button(reg_window, text="APPLY", command = Register)
    reg_apply.place(x=640, y=360, width=120, height=50)

    reg_men = ttk.Button(reg_window, text="MENU", command = Menu)
    reg_men.place(x=450, y=360, width=180, height=50)

    reg_window.mainloop()
        
#===========================================================================================================================================================

# RDR page

#===========================================================================================================================================================

rdr_counter = 0

def Rdr():
    rdr_window = tk.Toplevel(window)
    rdr_window.geometry("1200x600")
    rdr_window.resizable(width = False, height = False)
    rdr_window['bg'] = '#171a21'

    image1_rdr = ImageTk.PhotoImage(Image.open("rdr/image1rdr.jpeg").resize((600, 320)))
    image2_rdr = ImageTk.PhotoImage(Image.open("rdr/image2rdr.jpg").resize((600, 320)))
    image3_rdr = ImageTk.PhotoImage(Image.open("rdr/image3rdr.jpg").resize((600, 320)))
    rdr_images_cort = [image1_rdr, image2_rdr, image3_rdr]

    def RdrChangeImagePlus():
        global rdr_counter
        if rdr_counter < len(rdr_images_cort) - 1:
            rdr_counter += 1
        else:
            rdr_counter = 0

        rdr_photo_list.config(image=rdr_images_cort[rdr_counter])

    def RdrChangeImageMinus():
        global rdr_counter
        if rdr_counter < len(rdr_images_cort) + 1:
            rdr_counter -= 1
        else:
            rdr_counter = 0

        rdr_photo_list.config(image=rdr_images_cort[rdr_counter])

    rdr_label = Label(rdr_window, text="Red Dead Redemption 2", background="#171a21", fg="white", font="Monaco 20" )
    rdr_label.pack()

    rdr_photo_list = Label(rdr_window, image=image1_rdr, background="#171a21")
    rdr_photo_list.place(x = 160, y = 100)

    btnButtonRdrPlus = Button(rdr_window, text='>', command=RdrChangeImagePlus, background = "#2a475e")
    btnButtonRdrPlus.place(x = 463, y = 403, height = 20, width = 300)

    btnButtonRdrMinus = Button(rdr_window, text='<', command=RdrChangeImageMinus, background = "#2a475e")
    btnButtonRdrMinus.place(x = 162, y = 403, height = 20, width = 300)

    rdr_zag = Image.open("rdr/rdr2.jpg")
    rdr_zag = rdr_zag.resize((210, 110))

    rdr_zag = ImageTk.PhotoImage(rdr_zag)
    rdr_zag_label = Label(rdr_window, image=rdr_zag, background="#171a21")
    rdr_zag_label.image = rdr_zag
    rdr_zag_label.place(x = 800, y = 100)

    ops_rdr = Label(rdr_window, text = "Приключенческая игра в стиле\nвестерна. Действие разворачивается\nв открытом мире, в котором представлена\nвымышленная версия\nСоединённых Штатов 1899 года.", background = '#171a21', width = 40, fg = 'white', justify = "left")
    ops_rdr.place(x = 780, y = 220)

    ist_rdr = Label(rdr_window, text = "Разработчик :", background = "#171a21", fg = 'gray')
    ist_rdr.place(x = 800, y = 310)

    ist_rdr_n = Label(rdr_window, text = " Rokstar Games", background = '#171a21', fg = 'white')
    ist_rdr_n.place(x = 880, y = 310)

    data_rdr = Label(rdr_window, text = "Дата выпуска :", background = "#171a21", fg = 'gray')
    data_rdr.place(x = 800, y = 340)

    data_rdr_n = Label(rdr_window, text = " 26.10.2018", background = '#171a21', fg = 'white')
    data_rdr_n.place(x = 880, y = 340)

#===========================================================================================================================================================

#Elden Ring page

#===========================================================================================================================================================

er_counter = 0

def EldenRing():
    er_window = tk.Toplevel(window)
    er_window.geometry("1200x600")
    er_window.resizable(width = False, height = False)
    er_window['bg'] = '#171a21'

    image1_er = ImageTk.PhotoImage(Image.open("er/image1er.jpg").resize((600, 320)))
    image2_er = ImageTk.PhotoImage(Image.open("er/image2er.jpeg").resize((600, 320)))
    image3_er = ImageTk.PhotoImage(Image.open("er/image3er.jpg").resize((600, 320)))
    er_images_cort = [image1_er, image2_er, image3_er]

    def ErChangeImagePlus():
        global er_counter
        if er_counter < len(er_images_cort) - 1:
            er_counter += 1
        else:
            er_counter = 0

        er_photo_list.config(image=er_images_cort[er_counter])

    def ErChangeImageMinus():
        global er_counter
        if er_counter < len(er_images_cort) + 1:
            er_counter -= 1
        else:
            er_counter = 0

        er_photo_list.config(image=er_images_cort[er_counter])

    er_label = Label(er_window, text="Elden Ring", background="#171a21", fg="white", font="Monaco 20" )
    er_label.pack()

    er_photo_list = Label(er_window, image=image1_er, background="#171a21")
    er_photo_list.place(x = 160, y = 100)

    btnButtonErPlus = Button(er_window, text='>', command=ErChangeImagePlus, background = "#2a475e")
    btnButtonErPlus.place(x = 463, y = 403, height = 20, width = 300)

    btnButtonErMinus = Button(er_window, text='<', command=ErChangeImageMinus, background = "#2a475e")
    btnButtonErMinus.place(x = 162, y = 403, height = 20, width = 300)

    er_zag = Image.open("er/logoEr.jpg")
    er_zag = er_zag.resize((210, 110))

    er_zag = ImageTk.PhotoImage(er_zag)
    er_zag_label = Label(er_window, image=er_zag, background="#171a21")
    er_zag_label.image = er_zag
    er_zag_label.place(x = 800, y = 100)

    ops_er = Label(er_window, text = "Elden Ring представляет собой action/RPG\nс видом от третьего лица,\nсхожую с серией Dark Souls[3].\nХотя игра и не имеет прямой\nсвязи с этой серией, с точки зрения игрового процесса\nона в большой степени основана на Dark Souls.", background = '#171a21', width = 50, fg = 'white', justify = "left")
    ops_er.place(x = 780, y = 220)

    ist_er = Label(er_window, text = "Разработчик :", background = "#171a21", fg = 'gray')
    ist_er.place(x = 800, y = 320)

    ist_er_n = Label(er_window, text = " FromSoftware", background = '#171a21', fg = 'white')
    ist_er_n.place(x = 880, y = 320)

    data_er = Label(er_window, text = "Дата выпуска :", background = "#171a21", fg = 'gray')
    data_er.place(x = 800, y = 340)

    data_er_n = Label(er_window, text = " 28.02.2020", background = '#171a21', fg = 'white')
    data_er_n.place(x = 880, y = 340)

    er_window.mainloop()



window = Tk()
window.title("Window")
window.geometry("1200x600")
window['bg'] = '#171a21'
window.iconbitmap(default = "353439-basket-buy-cart-ecommerce-online-purse-shop-shopping_107515.ico")

window.resizable(width = False , height = False)

#===========================================================================================================================================================

                                                                         # ШАПКА

#===========================================================================================================================================================

store = Label(text="STORE", font="Monaco 30", bg= "#2a475e", fg="white", width=1100)
store.pack()

search = Entry(text ="Search", bg="#2f353b", fg="white")
search.place(x=700, y=10, height=25)
 
btn = ttk.Button(text="🔍")
btn.place(x=830, y=10, height=25, width=25)

log = ttk.Button(text="SIGN IN", command = Login)
log.place(x=10, y=10)

#===========================================================================================================================================================

                                                                          # МАГАЗИН

#===========================================================================================================================================================

# Red Dead Redemption 2

# ФОТО
rdr = Image.open("rdr/412454.webp")
rdr = rdr.resize((150, 210))

rdr = ImageTk.PhotoImage(rdr)
rdr_label = Label(image=rdr, background="#171a21")
rdr_label.image = rdr
rdr_label.place(x = 90, y=100 )

rdr_obc = Image.open("rdr/rdr2.jpg")
rdr_obc = rdr_obc.resize((310, 210))

rdr_obc = ImageTk.PhotoImage(rdr_obc)
rdr_obc_label = Label(image=rdr_obc, background="#171a21")
rdr_obc_label.image = rdr_obc
rdr_obc_label.place(x = 250, y = 100)

# ТЕКСТ

rdr_name = Label(text="Red Dead Redemption 2", background="#171a21", font="Times 16", fg="white")
rdr_name.place(x = 90, y = 320)

rdr_price = Label(text="30€", background="#296600", font="Times 14", fg="#19ff19")
rdr_price.place(x = 512, y = 315, width = 50, height = 30)

rdr_ops_menu = Label(text="", background="#171a21", fg='white',justify='left', font='Times 12')
rdr_ops_menu.place(x = 90, y = 380)

# КНОПКА

rdr_button = Button(text = ">", background="#2a475e", command=Rdr)
rdr_button.place(x = 70, y = 103, width=20, height=210)

echo_rdr_button = Button(text = "показать описание ⇩", command=OpisanieRdr, background='#2a475e')
echo_rdr_button.place(x = 90, y = 350)

#===========================================================================================================================================================

# Elden Ring

# ФОТО

er = Image.open("er/p1_3291899_e07b1f82.webp")
er = er.resize((150, 210))

er = ImageTk.PhotoImage(er)
er_label = Label(image=er, background="#171a21")
er_label.image = er
er_label.place(x = 630, y = 100)

er_obc = Image.open("er/qqq.webp")
er_obc = er_obc.resize((310, 210))

er_obc = ImageTk.PhotoImage(er_obc)
er_obc_label = Label(image=er_obc, background="#171a21")
er_obc_label.image = er_obc
er_obc_label.place(x = 790, y = 100)

# ТЕКСТ

er_name = Label(text="Elden Ring", background="#171a21", font="Times 16", fg="white")
er_name.place(x = 630, y = 320)

er_price = Label(text="25€", background="#296600", font="Times 14", fg="#19ff19")
er_price.place(x = 1052, y = 315, width = 50, height = 30)  

er_ops_menu = Label(text="", background="#171a21", fg='white',justify='left', font='Times 12')
er_ops_menu.place(x = 630, y = 380)

# КНОПКА

echo_er_button = Button(text = "показать описание ⇩", background='#2a475e', command=OpisanieEr)
echo_er_button.place(x = 630, y = 350)

er_button = Button(text = ">", background="#2a475e", command=EldenRing)
er_button.place(x = 610, y = 103, width=20, height=210)


window.mainloop()
