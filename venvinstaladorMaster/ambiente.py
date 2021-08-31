# import os
# os.system('netsh wlan show profile')
from tkinter import *
import psutil
cpu = "Quantidade CPU: ", psutil.cpu_count()

memoriaLivre = "Memoria RAM Livre: {:.0f} ".format( (psutil.virtual_memory().free / 1024**2)) + " Mb."

hdTotal = "Hd Total: {:.0f}".format( (psutil.disk_usage('/').total/ 1024**2)/1000) + " Gb."

hdLivre = "Hd Livre: {:.0f}".format( (psutil.disk_usage('/').free/ 1024**2)/1000) + " Gb."


texto = '''\nQuantidade CPU: ''' + str(psutil.cpu_count()) + '''
            \nMemoria RAM Total: {:.0f}'''.format( (psutil.virtual_memory().total / 1024**2)) + " Mb."

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()

        self.widget2 = Frame(master)
        self.widget2.pack()

        self.msg = Label(self.widget1, text=str(texto))
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack()

        self.texto = Label(self.widget2, text=str(texto))
        self.texto["font"] = ("Verdana", "10", "italic", "bold")
        self.texto.pack()

        self.sair = Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.widget1.quit
        self.sair.pack()

root = Tk()
root.title('Ambiente')
root.geometry('400x400')
Application(root)
root.mainloop()