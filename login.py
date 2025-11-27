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
janela.geometry('400x200')

form_campo = tk.Frame(janela)
form_campo.pack(pady=20)

tk.Label(form_campo, text='Usuário:', font=('Arial', 12, 'bold')).grid(row=0, column=0, padx=5, pady=10)
entrada_n1 = tk.Entry(form_campo, font=('Arial', 12), width=20)
entrada_n1.grid(row=0, column=1, padx=5, pady=10)


tk.Label(form_campo, text='Senha:' , font=('Arial', 12, 'bold')).grid(row=1, column=0, padx=5, pady=10)
entrada_n2 = tk.Entry(form_campo, font=('Arial', 12), width=20)
entrada_n2.grid(row=1, column=1, padx=5, pady=10)


frame_button = tk.Frame(janela)
frame_button.pack(pady=10)

button1 = tk.Button(frame_button, text="Entrar", command=fazer_login, bg="white", fg="gray")
button1.pack(side='right', padx=10)


buttona = tk.Button(frame_button, text="Cadastrar-se", command=abre_janela, bg='white')
buttona.pack(side='right', padx=10)


entrada_n2.focus()
entrada_n1.focus()
janela.mainloop()
