from tkinter import messagebox
import mysql.connector
import tkinter as tk
from tkinter import PhotoImage
from tkinter import PhotoImage
from pyexpat.errors import messages
from cadastro import abrir_cadastro
from principal import abrir_principal

try:
    conexao = mysql.connector.connect(
        host="localhost", user="root", password="", database="telas_python"
    )
    cursor = conexao.cursor()
    print("Conexão bem sucedida!")

except mysql.connector.Error as erro:
    print(f"Erro ao conectar: {erro}")


def fazer_login():
    usuario = entrada_n1.get()
    senha = entrada_n2.get()

    cursor = conexao.cursor()
    cursor.execute(f"SELECT * FROM login WHERE usuario = '{usuario}' AND senha = '{senha}'")
    resultado = cursor.fetchone()

    if resultado:
        janela.destroy()
        abrir_principal()
        janela.mainloop()
    else:
        messagebox.showerror(title="Deu ruim", message="Usuário ou senha errados")



def abre_janela():
    janela.destroy()
    abrir_cadastro()




janela = tk.Tk()
janela.title('Gordos burguer')
janela.geometry('700x600')

tk.Label(janela, text='digite o usuario', font=('Arial', 15, 'bold')).pack(pady=10)
entrada_n1 = tk.Entry(janela, font=('Arial', 15, 'bold'), width=20)
entrada_n1.pack(pady=10)


tk.Label(janela, text='digite a senha' , font=('Arial', 15, 'bold')).pack(pady=10)
entrada_n2 = tk.Entry(janela, font=('Arial', 15, 'bold'), width=20)
entrada_n2.pack(pady=10)


button1 = tk.Button(janela, text="logar", command=fazer_login, bg="white")
button1.pack(pady=10)




buttona = tk.Button(janela, text="cadastrar-se", command=abre_janela, bg='white')
buttona.pack(pady=10)


entrada_n2.focus()
entrada_n1.focus()
janela.mainloop()
