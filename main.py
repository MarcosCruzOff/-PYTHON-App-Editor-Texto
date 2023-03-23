from tkinter import *
from tkinter import filedialog

def salvar_arquivo():
    arquivo = filedialog.asksaveasfile(defaultextension=".txt")
    if arquivo is None:
        return
    texto = caixa_texto.get(1.0,  END)
    arquivo.write(texto)
    arquivo.close()

def abrir_arquivo():
    arquivo = filedialog.askopenfile(defaultextension=".txt")
    if arquivo is None:
        return
    caixa_texto.delete(1.0,  END)
    texto = arquivo.read()
    caixa_texto.insert( END, texto)
    arquivo.close()

app =  Tk()
app.title("Editor de Texto")
app.geometry("600x600")

icon = PhotoImage(file="image/icon.png")
app.iconphoto(True, icon)

# Cria a caixa de texto
caixa_texto =  Text(app)
caixa_texto.pack(fill= BOTH, expand=True)

# Cria o menu
menu =  Menu(app)
app.config(menu=menu)

# Cria o submenu Arquivo
submenu_arquivo =  Menu(menu)
menu.add_cascade(label="Arquivo", menu=submenu_arquivo)

# Adiciona as opções no submenu Arquivo
submenu_arquivo.add_command(label="Salvar", command=salvar_arquivo)
submenu_arquivo.add_command(label="Abrir", command=abrir_arquivo)

mainloop()