import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
from tktimepicker import SpinTimePickerModern
from tktimepicker import constants

import sys
sys.path.append('../../')

class EnrollGroup():
    def __init__(self):

        # Creación de la ventana
        self.window=tk.Tk()
        self.window.title("Registro Ficha")
        wSize = self.window.winfo_screenwidth()
        hSize = self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (wSize, hSize))
        self.window.config(bg = "#f0f1ee")
        self.window.resizable(width=0,height=0)

        # Titulo

        frameTitle = tk.Frame(self.window, height=10, bd=0,relief=tk.SOLID, bg = "#3894a1")
        frameTitle.pack(expand=tk.YES,fill=tk.BOTH)
        
        title = tk.Label(frameTitle, text = "Registro Ficha", font=('Roboto 30 bold'), fg= "#f0f1ee", bg= '#3894a1',pady = 20)
        title.pack(fill=tk.BOTH)

        # Frame e Inputs 

        frameInputs = tk.Frame(self.window, height=500, bd=0,relief=tk.SOLID, bg = "#3894a1")
        frameInputs.pack(side="top",fill=tk.BOTH,expand=tk.YES)
        
            # FICHA
        fichaLabel = tk.Label(frameInputs,text="Numero de Ficha",font=('Roboto 15'), fg="#f0f1ee", bg="#3894a1", anchor = "w")
        fichaLabel.pack(fill=tk.X, padx= 20 , pady= 5)
        
        self.ficha = ttk.Entry(frameInputs, font=("Roboto 15"))
        self.ficha.pack(fill=tk.X, padx= 20, pady=5)
            # HORA
        horaLabel = tk.Label(frameInputs,text="Hora de entrada",font=('Roboto 15'), fg="#f0f1ee", bg="#3894a1", anchor = "w")
        horaLabel.pack(fill=tk.X, padx= 20 , pady= 5)
        # Usamos una libreria para la seleccion de la hora, formato en 24Horas
        time_picker = SpinTimePickerModern(frameInputs)
        time_picker.addAll(constants.HOURS24)  # adds hours clock, minutes and period
        time_picker.configureAll(bg="#3894a1", height=2, fg="#404040", font=("Times", 16), hoverbg="#404040",
                                    hovercolor="#d73333", clickedbg="#f0f1ee", clickedcolor="#d73333")
        time_picker.configure_separator(bg="#3894a1", fg="#404040")

        time_picker.pack(padx= 2, pady=2)
        self.classTime = time_picker

        # Botones
        frameBtn = tk.Frame(self.window, height=50, bd=0,relief=tk.SOLID, bg = "#3894a1")
        frameBtn.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)

            # Volver
        btnVolver = tk.Button(frameBtn, text="Volver", font=("Roboto 15 bold"),bd=0 ,fg="#f0f1ee", bg="#2f404f",command=self.back)
        btnVolver.pack(side ='left', padx= 250)
        btnVolver.config(width=20, height = 2)
            
            # Registrar
        btnRegistrar = tk.Button(frameBtn, text="Registrar", font=("Roboto 15 bold"),bd=0 ,fg="#f0f1ee", bg="#2f404f",command=self.update)
        btnRegistrar.pack(side ='right', padx= 250)
        btnRegistrar.config(width=20, height = 2)

        self.window.mainloop()
        # COLORES #2f404f , #3894a1 , #f0f1ee , #c7dad3
    def back(self):
        from controller.back import volver
        from controller.git import push
        from threading import Thread
        hilo = Thread(target=push())
        hilo.start
        self.window.destroy()
        volverVar = Thread(target=volver())
        volverVar.start()
    
    def update(self):
        from controller.Group import Group
        nombreFicha = Group()
        nombreFicha.enroll(self.ficha.get(),self.classTime.time())
        self.window.destroy()
        self.__init__()