from tkinter import messagebox
import mysql.connector
import tkinter as tk
from PIL import Image, ImageTk
from cadastro import abrir_cadastro
from principal import abrir_principal

try:
    conexao = mysql.connector.connect(
        host="localhost", user="root", password="", database="telas_python"
    )
    cursor = conexao.cursor()
except:
    print("Erro ao conectar ao banco.")


def fazer_login():
    usuario = entrada_n1.get()
    senha = entrada_n2.get()

    cursor.execute(f"SELECT * FROM login WHERE usuario='{usuario}' AND senha='{senha}'")
    resultado = cursor.fetchone()

    if resultado:
        janela.destroy()
        abrir_principal()
    else:
        messagebox.showerror(title="Erro", message="Ce não sabe usar um login.")


def abre_janela():
    janela.destroy()
    abrir_cadastro()


janela = tk.Tk()
janela.title('Login')
janela.geometry('450x200')
janela.iconbitmap("burguer.ico")


img = Image.open("burguer.png")
img = img.resize((120, 120))
img = ImageTk.PhotoImage(img)

frame_principal = tk.Frame(janela)
frame_principal.pack(pady=10)

label_img = tk.Label(frame_principal, image=img)
label_img.grid(row=0, column=0, rowspan=3, padx=10)


form_campo = tk.Frame(frame_principal)
form_campo.grid(row=0, column=1, padx=10)

tk.Label(form_campo, text='Usuário:', font=('Arial', 12, 'bold')).grid(row=0, column=0, pady=5)
entrada_n1 = tk.Entry(form_campo, font=('Arial', 12), width=20)
entrada_n1.grid(row=0, column=1, pady=5)

tk.Label(form_campo, text='Senha:' , font=('Arial', 12, 'bold')).grid(row=1, column=0, pady=5)
entrada_n2 = tk.Entry(form_campo, font=('Arial', 12), width=20, show="*")
entrada_n2.grid(row=1, column=1, pady=5)


frame_button = tk.Frame(janela)
frame_button.pack(pady=10)

button1 = tk.Button(frame_button, text="Entrar", command=fazer_login, bg="white", fg="gray")
button1.pack(side='right', padx=10)

buttona = tk.Button(frame_button, text="Cadastrar-se", command=abre_janela, bg='white')
buttona.pack(side='right', padx=10)

entrada_n1.focus()

janela.mainloop()
