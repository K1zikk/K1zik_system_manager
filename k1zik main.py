from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Главное окно")

def skin_choose():
  print('выбарть скин')

def k1zik_params():
 print('параметры show')

def k1zik_edit_params():
 print('редакт')

def k1zik_vibration():
 print('вибрация')

def k1zik_bersk():
 new_window_1 = Toplevel(root)
 new_window_1.title("Берсерк")
 bersk_frame = Frame(new_window_1)
 bersk_frame.pack()
 titlelabel = Label(bersk_frame, width=120, text='''Режим использования кристалов и тнт для взрява всего и вся''', font="Courier 19",fg="lime green")
 bersk_button = Button(bersk_frame, text='reset', width=120, font="Courier 19",fg="lime green")
 bersk_button.grid(row=1, column=0)
 titlelabel.grid(row=0, column=0)

def k1zik_reset():
 new_window_0 = Toplevel(root)
 new_window_0.title("Резет кизика")
 new_window_0.protocol("WM_DELETE_WINDOW",lambda this_window = new_window_0: on_closing_k1zik_reset(this_window))
 reset_frame = Frame(new_window_0)
 reset_frame.pack()
 titlelabel = Label(reset_frame,width=120, text='''Резет кизика заставит его всё забыть''', font="Courier 19",fg="lime green")
 reset_button = Button(reset_frame,text = 'reset',width=120, font="Courier 19",fg="lime green")
 reset_button.grid(row=1, column=0)
 titlelabel.grid(row=0, column=0)

 def on_closing_k1zik_reset(this_window):
  if messagebox.askokcancel("Выход из резета","Вы хотите выйти из ресета?"):
   this_window.destroy()


master_frame = Frame(root)
master_frame.pack()

chat_whit_system_frame = Frame(master_frame)
chat_whit_system_frame.grid(row=0, column=0)

controls_frame = Frame(master_frame)
controls_frame.grid(row=1, column=0)

file_frame = Frame(master_frame)
file_frame.grid(row=0, column=5)

naming = Label(chat_whit_system_frame, width=120, text='''Перепрограммирование кизика
чат с системой''', font="Courier 19",fg="lime green")
naming.grid(row=0, column=0)

song_box = Entry(chat_whit_system_frame, width=60, selectbackground="blue",fg="lime green",)
song_box.grid(row=1,column=0,padx=10,pady=10,ipady=60)


skin_choose = Button(controls_frame, text='Выбрать скин', command = skin_choose,width=30, font="Courier",fg="lime green")
k1zik_params = Button(controls_frame, text='Открыть список параметров', command=k1zik_params, width=30, font="Courier",fg="lime green")
k1zik_edit_params = Button(controls_frame, text='Редактировать параметры', command=k1zik_edit_params, width=30, font="Courier",fg="lime green")
k1zik_vibration = Button(controls_frame, text='Выбор силы вибрации',command=k1zik_vibration, width=30, font="Courier",fg="lime green")
bersk = Button(controls_frame, text='Берсерк', command=k1zik_bersk, width=30, font="Courier",fg="lime green")
k1zik_reset = Button(controls_frame, text='Factory reset', command=k1zik_reset, width=30, font="Courier",fg="lime green")

skin_choose.grid(row=0, column=0)
k1zik_params.grid(row=0, column=1)
k1zik_edit_params.grid(row=0, column=2)
k1zik_vibration.grid(row=1, column=0)
k1zik_reset.grid(row=1, column=1)
bersk.grid(row=1, column=2)

root.mainloop()
