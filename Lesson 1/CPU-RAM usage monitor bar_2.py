import tkinter as tk
from tkinter import ttk
import sys
from process import CpuBar
from widget_update import Configure_widgets

class Application(tk.Tk, Configure_widgets):
    def __init__(self): #-------------------------------- Створюємо вікно
        tk.Tk.__init__(self)
        # self.geometry('400x400+1+1')
        self.attributes('-alpha', 1)
        self.attributes('-topmost', True)
        self.overrideredirect(True)
        self.resizable(False, False)
        self.title('CPU-RAM usage monitor bar')

        self.cpu = CpuBar()
        self.set_ui()

        self.make_bar_cpu_usage()
        self.configure_cpu_bar()





    def set_ui(self):#----------------------------------- Заповнюємо вікно
        exit_but = ttk.Button(self, text='Exit', command=self.app_exit)
        exit_but.pack(fill=tk.X)

        # self.bar2 = ttk.Frame(self)
        self.bar2 = ttk.Labelframe(self, text='Manual')# ----- Створюємо область Manual
        self.bar2.pack(fill=tk.X)

        # -------------------- Створюємо випадаючий список
        self.combo_win = ttk.Combobox(self.bar2,
                                      values=['hide', 'don`t hide', 'min'],
                                      width=9,
                                      state='readonly')
        self.combo_win.current(1)
        self.combo_win.pack(side=tk.LEFT)

        ttk.Button(self.bar2, text='move').pack(side=tk.LEFT)# ----- Створюємо кнопку
        ttk.Button(self.bar2, text='>>>').pack(side=tk.LEFT)
#----------------------------------------------------------------------------------------- Power
        self.bar = ttk.Labelframe(self, text='Power')  # ----- Створюємо область Power
        self.bar.pack(fill=tk.BOTH)

        self.bind_class('Tk', '<Enter>', self.enter_mouse)# ------------------------ обробник подій
        self.bind_class('Tk', '<Leave>', self.leave_mouse)

    def make_bar_cpu_usage(self):
        ttk.Label(self.bar, text=f'physical cores : {self.cpu.cpu_count}, logical cores : {self.cpu.cpu_count_logical}',
                anchor=tk.CENTER
                  ).pack(fill=tk.X)
        self.list_label=[]
        self.list_prbar=[]

        for i in range(self.cpu.cpu_count_logical):
            self.list_label.append(ttk.Label(self.bar, anchor=tk.CENTER))
            self.list_prbar.append(ttk.Progressbar(self.bar, length=100))
        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].pack(fill=tk.X)
            self.list_prbar[i].pack(fill=tk.X)

        self.ram_lab = ttk.Label(self.bar, text='', anchor=tk.CENTER)
        self.ram_lab.pack(fill=tk.X)
        self.ram_bar = ttk.Progressbar(self.bar, length=100)
        self.ram_bar.pack(fill=tk.X)


    def enter_mouse(self, event):
        if self.combo_win.current() == 0 or 1:
            self.geometry('')

    def leave_mouse(self, event):
        if self.combo_win.current() == 0:
            self.geometry(f"{self.winfo_width()}x1")

    def app_exit(self): #-------------------------------- Закриваємо додаток
        self.destroy()
        sys.exit()



#----------------------------------------------------
if __name__ == '__main__':
    root = Application()
    root.mainloop()