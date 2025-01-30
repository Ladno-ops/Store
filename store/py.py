from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
import tkinter as tk
from subprocess import Popen
import subprocess
import tkinter.messagebox
from tkinter import messagebox
from datetime import datetime
from tkinter import simpledialog

#=============#

# ОТЗЫВЫ RDR

#=============#

def rdr_save_reviews(rdr_review_text, rdr_rating):
    rdr_username_lab_rev = username_label['text']
    with open('rdr_reviews.txt', 'a') as file:
        file.write(f"Дата отзыва: {datetime.now().strftime('%Y-%m-%d')}\n")
        file.write(f'Имя пользователя: {rdr_username_lab_rev}\n')
        file.write(f'Отзыв: {rdr_review_text}')
        file.write(f'Оценка: {rdr_rating}\n\n')

def rdr_show_reviews():
    rdr_reviews_window = tk.Toplevel(window)
    rdr_reviews_window['bg'] = '#2f353b'
    rdr_reviews_window.title("Отзывы")
    rdr_reviews_title = Label(rdr_reviews_window, text = 'ОТЗЫВЫ', font = 'Times 20', fg = 'white', bg = '#2f353b', width=30)
    rdr_reviews_title.pack()

    try:
        with open("rdr_reviews.txt", "r") as file:
            rdr_reviews = file.readlines()
            rdr_game_reviews = []
            rdr_review = ""
            global rdr_rating
            for rdr_line in rdr_reviews:
                rdr_review += rdr_line
                if rdr_line.strip() == "":
                    rdr_game_reviews.append(rdr_review)
                    rdr_review = ""
            if not rdr_game_reviews:
                tk.Label(rdr_reviews_window, text="Нет отзывов. Будьте первым, кто оставит отзыв!").pack()

            for rdr_review in rdr_game_reviews:
                rdr_review_lines = rdr_review.split('\n')
                if len(rdr_review_lines) >= 4:
                    rdr_date = rdr_review_lines[0].replace("Дата отзыва: ", "")
                    rdr_username_rev = rdr_review_lines[1].replace("Имя пользователя: ", "")
                    rdr_review_text = rdr_review_lines[2].replace("Текст отзыва: ", "")
                    rdr_rating = rdr_review_lines[3].replace("Оценка: ", "")

                    rdr_formatted_review = f"{rdr_date} | {rdr_username_rev} :\n{rdr_review_text}\n({rdr_rating} ★)\n _______________________\n\n"
                    tk.Label(rdr_reviews_window, text=rdr_formatted_review, justify=tk.LEFT, bg = '#2f353b', fg = 'white', wraplength=120).pack() 

    except FileNotFoundError:
            tk.Label(rdr_reviews_window, text="Отзывов еще нет. Будьте первым, кто оставит отзыв!").pack()

    def rdr_add_review_level_top():
        rdr_add_review_level = Toplevel(rdr_reviews_window)
        rdr_add_review_level.geometry('600x400')
        rdr_add_review_level['bg'] = "#2f353b"

        def rdr_add_review():
            rdr_review_text = rdr_review_text_lab.get(1.0, END)
            rdr_rating = rdr_rating_combobox.get()
            if rdr_review_text and len(rdr_review_text) <= 500:
                if rdr_rating:
                    rdr_save_reviews(rdr_review_text, rdr_rating)
                    messagebox.showinfo("Успех", "Отзыв успешно добавлен!")
                    rdr_reviews_window.destroy()
                    rdr_show_reviews()  # Обновляем список отзывов
                else:
                    messagebox.showerror("Ошибка", "Оценка должна быть от 1 до 5!")
            else:
                messagebox.showerror("Ошибка", "Отзыв не может быть пустым или превышать 500 символов!")


        rdr_otsiv = Label(rdr_add_review_level, text = 'ОТЗЫВ', bg = "#2f353b", fg = 'white', font = 'Times 20' )
        rdr_otsiv.place(x = 30, y = 30)
        
        rdr_review_text_lab = Text(rdr_add_review_level, width = 50, height=15)
        rdr_review_text_lab.place(x = 30, y = 80)

        rdr_rating_combobox = ttk.Combobox(rdr_add_review_level)

        rdr_rating_combobox['values'] = ("1", "2", "3", "4", "5")
        rdr_rating_combobox.place(x = 30, y = 350)

        rdr_ins_button = Button(rdr_add_review_level, text = "ОТРПАВИТЬ ►", fg = 'white', bg='#2a475e', command=rdr_add_review)
        rdr_ins_button.place(x = 180, y = 350)

    rdr_btndd = tk.Button(rdr_reviews_window, text="Добавить отзыв", command=rdr_add_review_level_top).pack()

#=============#

# ОТЗЫВЫ ER

#=============#

def er_save_reviews(er_review_text, er_rating):
    er_username_lab_rev = username_label['text']
    with open('er_reviews.txt', 'a') as file:
        file.write(f"Дата отзыва: {datetime.now().strftime('%Y-%m-%d')}\n")
        file.write(f'Имя пользователя: {er_username_lab_rev}\n')
        file.write(f'Отзыв: {er_review_text}')
        file.write(f'Оценка: {er_rating}\n\n')

def er_show_reviews():
    er_reviews_window = tk.Toplevel(window)
    er_reviews_window['bg'] = '#2f353b'
    er_reviews_window.title("Отзывы")
    er_reviews_title = Label(er_reviews_window, text = 'ОТЗЫВЫ', font = 'Times 20', fg = 'white', bg = '#2f353b', width=30)
    er_reviews_title.pack()

    try:
        with open("er_reviews.txt", "r") as file:
            er_reviews = file.readlines()
            er_game_reviews = []
            er_review = ""
            global er_rating
            for er_line in er_reviews:
                er_review += er_line
                if er_line.strip() == "":
                    er_game_reviews.append(er_review)
                    er_review = ""
            if not er_game_reviews:
                tk.Label(er_reviews_window, text="Нет отзывов. Будьте первым, кто оставит отзыв!").pack()

            for er_review in er_game_reviews:
                er_review_lines = er_review.split('\n')
                if len(er_review_lines) >= 4:
                    er_date = er_review_lines[0].replace("Дата отзыва: ", "")
                    er_username_rev = er_review_lines[1].replace("Имя пользователя: ", "")
                    er_review_text = er_review_lines[2].replace("Текст отзыва: ", "")
                    er_rating = er_review_lines[3].replace("Оценка: ", "")

                    er_formatted_review = f"{er_date} | {er_username_rev} :\n{er_review_text}\n({er_rating} ★)\n _______________________\n\n"
                    tk.Label(er_reviews_window, text=er_formatted_review, justify=tk.LEFT, bg = '#2f353b', fg = 'white', wraplength=120).pack() 

    except FileNotFoundError:
            tk.Label(er_reviews_window, text="Отзывов еще нет. Будьте первым, кто оставит отзыв!").pack()

    def er_add_review_level_top():
        er_add_review_level = Toplevel(rdr_reviews_window)
        er_add_review_level.geometry('600x400')
        er_add_review_level['bg'] = "#2f353b"

        def er_add_review():
            er_review_text = er_review_text_lab.get(1.0, END)
            er_rating = er_rating_combobox.get()
            if er_review_text and len(er_review_text) <= 500:
                if er_rating:
                    er_save_reviews(er_review_text, er_rating)
                    messagebox.showinfo("Успех", "Отзыв успешно добавлен!")
                    er_reviews_window.destroy()
                    er_show_reviews()  # Обновляем список отзывов
                else:
                    messagebox.showerror("Ошибка", "Оценка должна быть от 1 до 5!")
            else:
                messagebox.showerror("Ошибка", "Отзыв не может быть пустым или превышать 500 символов!")


        er_otsiv = Label(er_add_review_level, text = 'ОТЗЫВ', bg = "#2f353b", fg = 'white', font = 'Times 20' )
        er_otsiv.place(x = 30, y = 30)
        
        er_review_text_lab = Text(er_add_review_level, width = 50, height=15)
        er_review_text_lab.place(x = 30, y = 80)

        er_rating_combobox = ttk.Combobox(er_add_review_level)

        er_rating_combobox['values'] = ("1", "2", "3", "4", "5")
        er_rating_combobox.place(x = 30, y = 350)

        er_ins_button = Button(er_add_review_level, text = "ОТРПАВИТЬ ►", fg = 'white', bg='#2a475e', command=er_add_review)
        er_ins_button.place(x = 180, y = 350)

    er_btndd = tk.Button(er_reviews_window, text="Добавить отзыв", command=er_add_review_level_top).pack()

#=============#

# LOGIN

#=============#

if_log = False

def LoginRegister():
    def Register():
        username = username_entry.get()
        password = password_entry.get()

        if username and password:
            with open("store.txt", "r") as file:
                users = file.readlines()
                users = [line.strip() for line in users]

            if f"{username}:{password}" in users:
                messagebox.showerror("Ошибка", "Этот пользователь уже зарегистрирован!")
            else:
                with open("store.txt", "a") as file:
                    file.write(f"{username}:{password}\n")
                messagebox.showinfo("Регистрация", "Вы успешно зарегистрированы!")
        else:
            messagebox.showerror("Ошибка", "Заполните все поля!")
        
    def LoginTop():
        global if_login
        global username_label
        reg_window.destroy()

        def Login():
            global username_label
            username = username_entry.get()
            password = password_entry.get()

            if username and password:
                with open("store.txt", "r") as file:
                    users = file.readlines()
                    users = [line.strip() for line in users]

                if f"{username}:{password}" in users:
                    messagebox.showinfo("Вход", "Вы успешно вошли!")
                    username_label['text'] = username
                    if_log = True
                else:
                    messagebox.showerror("Ошибка", "Неверное имя пользователя или пароль!")
            else:
                messagebox.showerror("Ошибка", "Заполните все поля!")
            
            log_window.destroy()
            log_window.update()
            
        log_window = tk.Toplevel(window)
        log_window.title("Window")
        log_window.geometry("1200x600")
        log_window['bg'] = '#2f353b'
        log_window.resizable(width=False, height=False)

        login = Label(log_window, text="LOG IN", font="Monaco 30", bg="#2f353b", fg='white')
        login.place(x=500, y=160)

        log_username = Label(log_window, text="USERNAME", font="Monaco 15", bg="#2f353b", fg="white")
        log_username.place(x=450, y=230)

        username_entry = ttk.Entry(log_window, width=30)
        username_entry.place(x=570, y=230, height=30)

        reg_password = Label(log_window, text="PASSWORD", font="Monaco 15", bg="#2f353b", fg="white")
        reg_password.place(x=450, y=300)

        password_entry = ttk.Entry(log_window, width=30)
        password_entry.place(x=570, y=300, height=30)

        reg_apply = ttk.Button(log_window, text="APPLY", command = Login)
        reg_apply.place(x=640, y=360, width=120, height=50)

        reg_men = ttk.Button(log_window, text="MENU", command = Menu)
        reg_men.place(x=450, y=360, width=180, height=50)


        log_window.mainloop()


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

    username_entry = ttk.Entry(reg_window, width=30)
    username_entry.place(x=570, y=230, height=30)

    reg_password = Label(reg_window, text="PASSWORD", font="Monaco 15", bg="#2f353b", fg="white")
    reg_password.place(x=450, y=300)

    password_entry = ttk.Entry(reg_window, width=30)
    password_entry.place(x=570, y=300, height=30)

    reg_apply = ttk.Button(reg_window, text="APPLY", command = Register)
    reg_apply.place(x=640, y=360, width=120, height=50)

    reg_men = ttk.Button(reg_window, text="MENU", command = Menu)
    reg_men.place(x=450, y=360, width=180, height=50)

    log_btn = ttk.Button(reg_window, text="LogIn", command = LoginTop)
    log_btn.place(x = 1100, y = 15)

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

                                                                          # МАГАЗИН

#===========================================================================================================================================================

main_frame = tk.Frame(window, background='#171a21')
main_frame.pack_propagate(False)
main_frame.configure(width=1200, height=550)

if_ops_rdr = False
if_ops_er = False

def StoreFrame():
    global rdr_ops_menu, echo_rdr_button, if_ops_rdr, er_ops_menu, echo_rdr_button, if_ops_er
    store_frame = tk.Frame(main_frame, background='#171a21')
    store_frame.pack_propagate(False)
    store_frame.configure(width=1200, height=550)

    store_label = Label(store_frame, text = 'STORE', background='#171a21', fg='white', font='Monaco 30')
    store_label.place(x = 90, y = 20)

    global if_ops_rdr

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

    global if_ops_er

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
        store_frame = tk.Frame(main_frame, background="#171a21")
        store_frame.configure(width=1200, height=550)

    # Red Dead Redemption 2

    # ФОТО
    rdr = Image.open("rdr/412454.webp")
    rdr = rdr.resize((150, 210))

    rdr = ImageTk.PhotoImage(rdr)
    rdr_label = Label(store_frame, image=rdr, background="#171a21")
    rdr_label.image = rdr
    rdr_label.place(x = 90, y=100 )

    rdr_obc = Image.open("rdr/rdr2.jpg")
    rdr_obc = rdr_obc.resize((310, 210))

    rdr_obc = ImageTk.PhotoImage(rdr_obc)
    rdr_obc_label = Label(store_frame, image=rdr_obc, background="#171a21")
    rdr_obc_label.image = rdr_obc
    rdr_obc_label.place(x = 250, y = 100)

    # ТЕКСТ

    rdr_name = Label(store_frame, text="Red Dead Redemption 2", background="#171a21", font="Times 16", fg="white")
    rdr_name.place(x = 90, y = 320)

    rdr_price = Label(store_frame, text="30€", background="#296600", font="Times 14", fg="#19ff19")
    rdr_price.place(x = 512, y = 315, width = 50, height = 30)

    rdr_ops_menu = Label(store_frame, text="", background="#171a21", fg='white', justify='left', font='Times 12')
    rdr_ops_menu.place(x = 90, y = 380)

    # КНОПКА

    rdr_button = Button(store_frame, text = ">", background="#2a475e", command=Rdr)
    rdr_button.place(x = 70, y = 103, width=20, height=210)

    echo_rdr_button = Button(store_frame, text = "показать описание ⇩", command=OpisanieRdr, background='#2a475e')
    echo_rdr_button.place(x = 90, y = 350)

    button_rdr_reviuw = tk.Button(store_frame, text=f"отзывы", command = rdr_show_reviews, bg = '#2a475e')
    button_rdr_reviuw.place(x = 230, y = 350)

    #===========================================================================================================================================================

    # Elden Ring

    # ФОТО

    er = Image.open("er/p1_3291899_e07b1f82.webp")
    er = er.resize((150, 210))

    er = ImageTk.PhotoImage(er)
    er_label = Label(store_frame, image=er, background="#171a21")
    er_label.image = er
    er_label.place(x = 630, y = 100)

    er_obc = Image.open("er/qqq.webp")
    er_obc = er_obc.resize((310, 210))

    er_obc = ImageTk.PhotoImage(er_obc)
    er_obc_label = Label(store_frame, image=er_obc, background="#171a21")
    er_obc_label.image = er_obc
    er_obc_label.place(x = 790, y = 100)

    # ТЕКСТ

    er_name = Label(store_frame, text="Elden Ring", background="#171a21", font="Times 16", fg="white")
    er_name.place(x = 630, y = 320)

    er_price = Label(store_frame, text="25€", background="#296600", font="Times 14", fg="#19ff19")
    er_price.place(x = 1052, y = 315, width = 50, height = 30)  

    er_ops_menu = Label(store_frame, text="", background="#171a21", fg='white',justify='left', font='Times 12')
    er_ops_menu.place(x = 630, y = 380)

    # КНОПКА

    echo_er_button = Button(store_frame, text = "показать описание ⇩", background='#2a475e', command=OpisanieEr)
    echo_er_button.place(x = 630, y = 350)

    er_button = Button(store_frame, text = ">", background="#2a475e", command=EldenRing)
    er_button.place(x = 610, y = 103, width=20, height=210)

    button_er_reviuw = tk.Button(store_frame, text=f"отзывы", command = er_show_reviews, bg = '#2a475e')
    button_er_reviuw.place(x = 770, y = 350)

    store_frame.pack()

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(page):
    delete_pages()
    page()

#===========================================================================================================================================================

                                                                         # БИБЛИОТЕКА

#===========================================================================================================================================================

def LibraryFrame():
    library_frame = tk.Frame(main_frame, background='#171a21')
    library_frame.pack_propagate(False)
    library_frame.configure(width=1200, height=550)

    library_label = Label(library_frame, text = 'LIBRARY', background='#171a21', fg='white', font='Monaco 30')
    library_label.place(x = 90, y = 20)

    vice_city_img = Image.open("library/vicecity/vice_city_label.jpg")
    vice_city_img = vice_city_img.resize((150, 210))

    vice_city_img = ImageTk.PhotoImage(vice_city_img)
    vice_city_img_label = Label(library_frame, image=vice_city_img, background="#171a21")
    vice_city_img_label.image = vice_city_img
    vice_city_img_label.place(x = 90, y=100)

    def vice_city_application():
        #subprocess.Popen(r'C:\Users\Atom-NRJ\Desktop\store\library\vicecity\GrandTheftAutoViceCity\GameLauncher.exe')
        messagebox.showerror('Ошибка', "Git Hub не допустил файл игры")
        window.destroy()
    
    btnViceCuty = Button(library_frame, text = 'ЗАПУСК', command=vice_city_application, background="#2a475e", width=20)
    btnViceCuty.place(x = 93, y = 316)

    library_frame.pack()

#===========================================================================================================================================================

                                                                        # ШАПКА

#===========================================================================================================================================================

options_frame = tk.Frame(window, bg='#2a475e')
options_frame.pack_propagate(False)
options_frame.configure(width=1200, height=50)

username_label = Label(text = "", bg='#2a475e', fg='white', font="Times 14")
username_label.place(x = 360, y = 16)

search = Entry(text ="Search", bg="#2f353b", fg="white")
search.place(x=1000, y=10, height=25)
 
btn = ttk.Button(text="🔍")
btn.place(x=1130, y=10, height=25, width=25)

log = ttk.Button(text="SIGN IN", command = LoginRegister)
log.place(x=10, y=10)

btnStore = Button(text = 'STORE', command=lambda: indicate(StoreFrame), background="#2a475e", fg='white', width=15, height=2)
btnStore.place(x = 120, y = 10)

btnLabel = Button(text = 'LIBRARY', command=lambda: indicate(LibraryFrame), background="#2a475e", fg='white', width=15, height=2)
btnLabel.place(x = 235, y = 10)


options_frame.pack(side = tk.TOP)
main_frame.pack(side=tk.TOP)


window.mainloop()