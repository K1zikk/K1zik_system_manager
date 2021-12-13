import time
from tkinter import *
from tkinter import messagebox

root = Tk()
powerV = 0

root.title("Главное окно")
root.protocol("WM_DELETE_WINDOW", lambda root_window=root: on_closing_params(root_window))


def on_closing_reset(reset_window):
    if messagebox.askokcancel("Выход из резета", "Вы хотите выйти из ресета?"):
        reset_window.destroy()


def on_closing_bersk(bersk_window):
    if messagebox.askokcancel("Выход из берсерка", "Вы хотите выйти из берсерка?"):
        bersk_window.destroy()


def on_closing_vibration(vibration_window):
    if messagebox.askokcancel("Выход из вибрации", "Вы хотите выйти из вибрации?"):
        vibration_window.destroy()


def on_closing_edit_params(edit_params_window):
    if messagebox.askokcancel("Выход из редактирования параметров", "Вы хотите выйти из редактирования параметров?"):
        edit_params_window.destroy()


def on_closing_params(params_window):
    if messagebox.askokcancel("Выход из списка параметров", "Вы хотите выйти из параметров?"):
        params_window.destroy()


def on_closing_skin_params(skin_window):
    if messagebox.askokcancel("Выход из выбора скина", "Вы хотите выйти из выбора скина?"):
        skin_window.destroy()


def k1zik_edit_params():
    new_window_3 = Toplevel(root)
    new_window_3.wm_attributes("-topmost", 1)
    new_window_3.title('''Редактирование параметров
    Внимание при нажимании кнопки сохранения параметры не изменяются в списке параметров''')
    edit_params_frame = Frame(new_window_3)
    edit_params_frame.pack()
    titlelabel = Label(edit_params_frame, width=120, text='''Режим редактирования параметров''', font="Courier 19",
                       fg="lime green")
    yearz_Label = Label(edit_params_frame, text='Годики по рп ', width=50, font="Courier 19", fg="lime green")
    yearzrl_Label = Label(edit_params_frame, text='Годики ', width=50, font="Courier 19", fg="lime green")
    race_Label = Label(edit_params_frame, text='Раса по рп ', width=50, font="Courier 19", fg="lime green")
    raceirlf_Label = Label(edit_params_frame, text='Раса в реальной жизни ', width=50, font="Courier 19",
                           fg="lime green")
    love_interest_Label = Label(edit_params_frame, text='Любовный интерес ', width=50, font="Courier 19",
                                fg="lime green")
    gender_Label = Label(edit_params_frame, text='Пол', width=50, font="Courier 19",
                         fg="lime green")
    confirm_button = Button(edit_params_frame, text='confirm', width=50, font="Courier 19",
                            fg="lime green")

    yearz_entry = Entry(edit_params_frame)
    yearzrl_entry = Entry(edit_params_frame)
    race_entry = Entry(edit_params_frame)
    raceirlf_entry = Entry(edit_params_frame)
    love_interest_entry = Entry(edit_params_frame)
    gender_entry = Entry(edit_params_frame)

    titlelabel.grid(row=0, column=0)
    yearz_Label.grid(row=1, column=0)
    yearzrl_Label.grid(row=3, column=0)
    race_Label.grid(row=5, column=0)
    raceirlf_Label.grid(row=7, column=0)
    love_interest_Label.grid(row=9, column=0)
    gender_Label.grid(row=11, column=0)

    yearz_entry.grid(row=2, column=0)
    yearzrl_entry.grid(row=4, column=0)
    race_entry.grid(row=6, column=0)
    raceirlf_entry.grid(row=8, column=0)
    love_interest_entry.grid(row=10, column=0)
    gender_entry.grid(row=12, column=0)
    confirm_button.grid(row=13, column=0)


def k1zik_params():
    yearz = '18'
    yearz_real_life = '15'
    race = 'multifunctional_robot'
    race_in_real_life = 'half-human half-cat'
    love_interest = 'True'
    gender = 'attack helicopter'

    new_window_4 = Toplevel(root)
    new_window_4.wm_attributes("-topmost", 1)
    new_window_4.title("Список параметров")
    new_window_4.protocol("WM_DELETE_WINDOW", lambda params_window=new_window_4: on_closing_params(params_window))
    params_frame = Frame(new_window_4)
    params_frame.pack()
    titlelabel = Label(params_frame, width=120,
                       text='''Режим использования кристалов и тнт для взрява всего и вся и убийств''',
                       font="Courier 19", fg="lime green")
    naming_yearz_Label = Label(params_frame, text='Годики по рп: ' + yearz, width=50, font="Courier 19",
                               fg="lime green")
    naming_yearzrl_Label = Label(params_frame, text='Годики: ' + yearz_real_life, width=50, font="Courier 19",
                                 fg="lime green")
    naming_race_Label = Label(params_frame, text='Раса по рп: ' + race, width=50, font="Courier 19",
                              fg="lime green")
    naming_raceirlf_Label = Label(params_frame, text='Раса в реальной жизни: ' + race_in_real_life, width=50,
                                  font="Courier 19",
                                  fg="lime green")
    naming_love_interest_Label = Label(params_frame, text='Любовный интерес: ' + love_interest, width=50,
                                       font="Courier 19", fg="lime green")
    naming_gender_Label = Label(params_frame, text='Пол: ' + gender, width=50, font="Courier 19",
                                fg="lime green")

    naming_yearz_Label.grid(row=1, column=0)
    naming_yearzrl_Label.grid(row=2, column=0)
    naming_race_Label.grid(row=3, column=0)
    naming_raceirlf_Label.grid(row=4, column=0)
    naming_love_interest_Label.grid(row=5, column=0)
    naming_gender_Label.grid(row=6, column=0)


def main_exiting():
    sys.exit()


def k1zik_vibration():
    new_window_2 = Toplevel(root)
    new_window_2.wm_attributes("-topmost", 1)
    new_window_2.title("Вибрация")
    new_window_2.protocol("WM_DELETE_WINDOW",
                          lambda vibration_window=new_window_2: on_closing_vibration(vibration_window))
    vibration_frame = Frame(new_window_2)
    vibration_frame.pack()
    global vibration_button_vkl_vkl
    global vibrolabel
    titlelabel = Label(vibration_frame, width=120, text='Уровень вибрации', font="Courier 19", fg="lime green")
    vibrolabel = Label(vibration_frame, width=120, text=str(powerV), font="Courier 19", fg="lime green")
    vibration_button_plus = Button(vibration_frame, text='-', width=90, font="Courier 19", fg="lime green",
                                   command=power_minus)
    vibration_button_minus = Button(vibration_frame, text='+', width=90, font="Courier 19", fg="lime green",
                                    command=power_plus)
    vibration_button_vkl_vkl = Button(vibration_frame, text='Выкл', width=90, font="Courier 19", fg="lime green",
                                      command=vkl_vkl_vibro)
    vibration_button_minus.grid(row=2, column=0)
    vibration_button_vkl_vkl.grid(row=3, column=0)
    vibration_button_plus.grid(row=4, column=0)
    titlelabel.grid(row=0, column=0)
    vibrolabel.grid(row=1, column=0)


def power_plus():
    global powerV
    if powerV != 100:
        powerV = powerV + 10
        vibrolabel['text'] = str(powerV)


def power_minus():
    global powerV
    if powerV != 0:
        powerV = powerV - 10
        vibrolabel['text'] = str(powerV)


def vkl_vkl_vibro():
    if (vibration_button_vkl_vkl['text'] == 'Выкл'):
        vibration_button_vkl_vkl['text'] = 'Вкл'
    else:
        vibration_button_vkl_vkl['text'] = 'Выкл'


def vkl_vkl_bersk():
    if (bersk_button['text'] == 'Выкл'):
        bersk_button['text'] = 'Вкл'
    else:
        bersk_button['text'] = 'Выкл'


def k1zik_bersk():
    global bersk_button
    new_window_1 = Toplevel(root)
    new_window_1.wm_attributes("-topmost", 1)
    new_window_1.title("Берсерк")
    new_window_1.protocol("WM_DELETE_WINDOW", lambda bersk_window=new_window_1: on_closing_bersk(bersk_window))
    bersk_frame = Frame(new_window_1)
    bersk_frame.pack()
    titlelabel = Label(bersk_frame, width=120,
                       text='''Режим использования кристалов и тнт для взрява всего и вся и убийств''',
                       font="Courier 19", fg="lime green")
    bersk_button = Button(bersk_frame, text='Выкл', width=90, font="Courier 19", fg="lime green", command=vkl_vkl_bersk)
    bersk_button.grid(row=1, column=0)
    titlelabel.grid(row=0, column=0)


def k1zik_reset():
    new_window_0 = Toplevel(root)
    new_window_0.wm_attributes("-topmost", 1)
    new_window_0.title("Резет кизика")
    new_window_0.protocol("WM_DELETE_WINDOW", lambda bersk_window=new_window_0: on_closing_reset(bersk_window))
    reset_frame = Frame(new_window_0)
    reset_frame.pack()
    titlelabel = Label(reset_frame, width=120, text='''Резет кизика заставит его всё забыть''', font="Courier 19",
                       fg="lime green")
    global reset_progress
    reset_progress = Label(reset_frame, width=120, text='', font="Courier 19",
                           fg="lime green")
    reset_button = Button(reset_frame, text='reset', width=90, font="Courier 19", fg="lime green",
                          command=k1zik_reseting)
    titlelabel.grid(row=0, column=0)
    reset_button.grid(row=1, column=0)
    reset_progress.grid(row=2, column=0)


def k1zik_reseting():
    my_file = open("Мяу.txt", "w+")
    my_file.write('''Мяу мяу мяу мяу мяу, муряо мау моу, брофоло,брифало,брафало,бриф,броф,бруф,браф,бреф
    моф,мёф,муф,мюф,миф,мэф,меф,вой ёй ёй йё йё лоточке мяукающие тыгыдукающие брукающие фыркающие, мэфающие кощачьи песни
    лоточке кошка где то тамь Olala лоточек на колёсиках и блять ты кот или котёнок клоун убивца мяу мяу мяу тыгыдк мяу мяу муряо мау мау мау мау мау мау мау мау
    миу правда мяу и не правда мур брифало которого чаппа мисочка с дримсиками под берёзой и водичка с водой рядом с горой 
    как фыркать так и прыгать как бегать так и мяукать как нюхать так и лизать мяуууяуяяуяяууяяууяяуяуяуяуяуяу
    тефии вебии ёлки линкси магогерки мухи мутаболы мастеры огонь бушизо деллорь репер барсик сука диждей барсичок олег сосел
    кошко элитры 1 кошко элитры 2 топочка лук 1 топчка лук 2 мифало муфало брофало''')
    my_file.close()
    time.sleep(5)
    reset_progress['text'] = 'Готово попращайтесь с кизиком в последний раз'


master_frame = Frame(root)
master_frame.pack()

chat_whit_system_frame = Frame(master_frame)
chat_whit_system_frame.grid(row=0, column=0)

controls_frame = Frame(master_frame)
controls_frame.grid(row=1, column=0)

file_frame = Frame(master_frame)
file_frame.grid(row=0, column=5)

naming = Label(chat_whit_system_frame, width=120, text='''Перепрограммирование кизика
чат с системой''', font="Courier 19", fg="lime green")
naming.grid(row=0, column=0)

song_box = Entry(chat_whit_system_frame, width=60, selectbackground="blue", fg="lime green", )
song_box.grid(row=1, column=0, padx=10, pady=10, ipady=60)

k1zik_params = Button(controls_frame, text='Открыть список параметров', command=k1zik_params, width=30, font="Courier",
                      fg="lime green")
k1zik_edit_params = Button(controls_frame, text='Редактировать параметры', command=k1zik_edit_params, width=30,
                           font="Courier", fg="lime green")
k1zik_vibration = Button(controls_frame, text='Выбор силы вибрации', command=k1zik_vibration, width=30, font="Courier",
                         fg="lime green")
bersk = Button(controls_frame, text='Берсерк', command=k1zik_bersk, width=30, font="Courier", fg="lime green")
k1zik_reset = Button(controls_frame, text='Factory reset', command=k1zik_reset, width=30, font="Courier",
                     fg="lime green")
exiting = Button(controls_frame, text='Выход', command=main_exiting, width=30, font="Courier", fg="lime green")

k1zik_params.grid(row=0, column=0)
k1zik_edit_params.grid(row=1, column=0)
k1zik_vibration.grid(row=2, column=0)
k1zik_reset.grid(row=0, column=1)
bersk.grid(row=1, column=1)
exiting.grid(row=2, column=1)

root.mainloop()
