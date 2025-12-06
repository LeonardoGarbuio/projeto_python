from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import tkinter as tk
from tkinter import PhotoImage
from pyexpat.errors import messages
global janela
global entrada_n1, entrada_n2

from login import abre_login


try:
    conexao = mysql.connector.connect(
        host="localhost", user="root", password="", database="telas_python"
    )
    print("")

except mysql.connector.Error as erro:
    print("")


def cadastrar(entrada_n1, entrada_n2, janela):
    usuario = entrada_n1.get()
    senha = entrada_n2.get()

    if usuario == "" or senha == "":
            messagebox.showwarning(title='Atenção', message='Digite um Usuário e uma Senha válidos.')
    else:
        messagebox.showwarning(title='Atenção', message='Cadastro realizado com sucesso.')
        janela.destroy()
        abre_login()


        sql = f"INSERT INTO login (usuario, senha) VALUES ('{usuario}', '{senha}')"

        conexao.cursor().execute(sql)
        conexao.commit()


def abrir_cadastro():

    janela = tk.Tk()
    janela.title('Cadastro')
    janela.geometry('500x200')
    janela.iconbitmap("burguer.ico")

    img = Image.open("burguer.png")
    img = img.resize((120, 120))
    img = ImageTk.PhotoImage(img)

    frame_principal = tk.Frame(janela)
    frame_principal.pack(pady=10)

    label_img = tk.Label(frame_principal, image=img)
    label_img.image = img
    label_img.grid(row=0, column=0, rowspan=3, padx=10)

    form_campo = tk.Frame(frame_principal)
    form_campo.grid(row=0, column=1, padx=10)

    tk.Label(form_campo, text='Usuário:', font=('Arial', 12, 'bold')).grid(row=0, column=0, pady=5)
    entrada_n1 = tk.Entry(form_campo, font=('Arial', 12), width=20)
    entrada_n1.grid(row=0, column=1, pady=5)

    tk.Label(form_campo, text='Senha:', font=('Arial', 12, 'bold')).grid(row=1, column=0, pady=5)
    entrada_n2 = tk.Entry(form_campo, font=('Arial', 12), width=20, show="*")
    entrada_n2.grid(row=1, column=1, pady=5)

    button1 = tk.Button(janela, text="cadastrar-se", command=lambda: cadastrar(entrada_n1, entrada_n2, janela), bg="white")
    button1.pack(pady=10)

    entrada_n1.focus()
    janela.mainloop()
