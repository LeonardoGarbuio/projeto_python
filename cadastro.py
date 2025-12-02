from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import tkinter as tk
from tkinter import PhotoImage
from pyexpat.errors import messages
global janela
global entrada_n1, entrada_n2

try:
    conexao = mysql.connector.connect(
        host="localhost", user="root", password="", database="telas_python"
    )
    print("")

except mysql.connector.Error as erro:
    print("")


def cadastrar(entrada_n1, entrada_n2):
    usuario = entrada_n1.get()
    senha = entrada_n2.get()

    if usuario == "" or senha == "":
            messagebox.showwarning(title='Atenção', message='Digite um Usuário e uma Senha válidos.')
    else:
        messagebox.showwarning(title='Atenção', message='Cadastro realizado com sucesso.')



        sql = f"INSERT INTO login (usuario, senha) VALUES ('{usuario}', '{senha}')"

        conexao.cursor().execute(sql)
        conexao.commit()

def abrir_cadastro():

    janela = tk.Tk()
    janela.title('Cadastro')
    janela.geometry('500x200')
    janela.iconbitmap("burguer.ico")

    form_campo = tk.Frame(janela)
    form_campo.pack(pady=20)

    logo = PhotoImage(file="burguer.png")
    label_logo = tk.Label(form_campo, image=logo, bg='#ff3333')
    label_logo.pack(pady=20)

    tk.Label(form_campo, text='Usuário:' , font=('Arial', 12, 'bold')).grid(row=0, column=0, padx=5, pady=10)
    entrada_n1 = tk.Entry(form_campo, font=('Arial', 12, 'bold'), width=20)
    entrada_n1.grid(row=0, column=1, padx=5, pady=10)

    tk.Label(form_campo, text='Senha:' , font=('Arial', 12, 'bold')).grid(row=1, column=0, padx=5, pady=10)
    entrada_n2 = tk.Entry(form_campo, font=('Arial', 12, 'bold'), width=20)
    entrada_n2.grid(row=1, column=1, padx=5, pady=10)

    button1 = tk.Button(janela, text="cadastrar-se", command=lambda: cadastrar(entrada_n1, entrada_n2), bg="white")
    button1.pack(pady=10)

    entrada_n2.focus()
    entrada_n1.focus()
