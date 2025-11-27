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
    print("Conexão bem sucedida!")

except mysql.connector.Error as erro:
    print(f"Erro ao conectar: {erro}")


def cadastrar(entrada_n1, entrada_n2):
    usuario = entrada_n1.get()
    senha = entrada_n2.get()

    if usuario == "" or senha == "":
            messagebox.showwarning(title='atenção', message='login e senha nulos ???? nunca usou um cadastro')
    else:
        messagebox.showwarning(title='atenção', message='Deu boa parabens vc acertou um login')



        sql = f"INSERT INTO login (usuario, senha) VALUES ('{usuario}', '{senha}')"

        conexao.cursor().execute(sql)
        conexao.commit()

def abrir_cadastro():

    janela = tk.Tk()
    janela.title('Gordos burguer')
    janela.geometry('700x600')



    tk.Label(janela, text='digite o usuario' , font=('Arial', 15, 'bold')).pack(pady=10)
    entrada_n1 = tk.Entry(janela, font=('Arial', 15, 'bold'), width=20)
    entrada_n1.pack(pady=10)

    tk.Label(janela, text='digite a senha' , font=('Arial', 15, 'bold')).pack(pady=10)
    entrada_n2 = tk.Entry(janela, font=('Arial', 15, 'bold'), width=20)
    entrada_n2.pack(pady=10)

    button1 = tk.Button(janela, text="cadastrar-se", command=lambda: cadastrar(entrada_n1, entrada_n2), bg="white")
    button1.pack(pady=10)


    logo = PhotoImage(file="burguer.png")
    label_logo = tk.Label(janela, image=logo, bg='#ff3333')
    label_logo.pack(pady=20)


    entrada_n2.focus()
    entrada_n1.focus()
