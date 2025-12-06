from tkinter import messagebox
import mysql.connector
import tkinter as tk

try:
    conexao = mysql.connector.connect(
        host="localhost", user="root", password="", database="telas_python"
    )
    cursor = conexao.cursor()

except mysql.connector.Error as erro:
    print(f"Erro ao conectar: {erro}")

nome = ""

molho = ""
carne = ""
queijo = ""
pao = ""

alface = 0
bacon = 0
ovo = 0
picles = 0
tomate = 0
cebola = 0

def salvar_no_banco():
    cursor.execute("INSERT INTO hamburguer (nome, molho, carne, queijo, pao, alface, bacon, ovo, picles, tomate, cebola) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        params=(nome, molho, carne, queijo, pao, alface, bacon, ovo, picles, tomate, cebola)
    )
    conexao.commit()
    messagebox.showinfo(title="OK", message="Hambúrguer salvo com sucesso!")

def selecionar(opcao_nome, valor):
    globals()[opcao_nome] = valor
    messagebox.showinfo(title="Selecionado", message=f"{opcao_nome} = {valor}")

def selecionar_extra(nome_extra):
    globals()[nome_extra] = 1 if globals()[nome_extra] == 0 else 0
    status = "Adicionado" if globals()[nome_extra] else "Removido"
    messagebox.showinfo(title="OK", message=f"{status}: {nome_extra}")

def abre_cadastro_burguer():
    janela = tk.Tk()
    janela.title("Monte seu Hambúrguer")
    janela.geometry("700x800")

    form_molho = tk.Frame(janela)
    form_molho.grid(row=0, column=1, padx=10)

    tk.Label(form_molho, text="Escolha o molho:", font=("Arial", 16)).pack(pady=5)
    tk.Button(form_molho, text="Ketchup", command=lambda: selecionar(opcao_nome="molho", valor="ketchup")).pack()
    tk.Button(form_molho, text="Mostarda", command=lambda: selecionar(opcao_nome="molho", valor="mostarda")).pack()
    tk.Button(form_molho, text="Maionese", command=lambda: selecionar(opcao_nome="molho", valor="maionese")).pack()
    tk.Button(form_molho, text="Barbecue", command=lambda: selecionar(opcao_nome="molho", valor="barbecue")).pack()

    tk.Label(janela, text="Escolha a carne:", font=("Arial", 16)).pack(pady=5)
    tk.Button(janela, text="Bovina", command=lambda: selecionar(opcao_nome="carne", valor="carne_bovina")).pack()
    tk.Button(janela, text="Suína", command=lambda: selecionar(opcao_nome="carne", valor="carne_suina")).pack()
    tk.Button(janela, text="Caprina", command=lambda: selecionar(opcao_nome="carne", valor="carne_caprina")).pack()
    tk.Button(janela, text="Frango", command=lambda: selecionar(opcao_nome="carne", valor="carne_frango")).pack()

    tk.Label(janela, text="Escolha o queijo:", font=("Arial", 16)).pack(pady=5)
    tk.Button(janela, text="Cheddar", command=lambda: selecionar(opcao_nome="queijo", valor="queijo_cheddar")).pack()
    tk.Button(janela, text="Mussarela", command=lambda: selecionar(opcao_nome="queijo", valor="queijo_mussarela")).pack()
    tk.Button(janela, text="Prato", command=lambda: selecionar(opcao_nome="queijo", valor="queijo_prato")).pack()
    tk.Button(janela, text="Suíço", command=lambda: selecionar(opcao_nome="queijo", valor="queijo_suico")).pack()

    tk.Label(janela, text="Escolha o pão:", font=("Arial", 16)).pack(pady=5)
    tk.Button(janela, text="Brioche", command=lambda: selecionar(opcao_nome="pao", valor="pao_brioche")).pack()
    tk.Button(janela, text="Australiano", command=lambda: selecionar(opcao_nome="pao", valor="pao_australiano")).pack()
    tk.Button(janela, text="Gergelim", command=lambda: selecionar(opcao_nome="pao", valor="pao_gergelim")).pack()
    tk.Button(janela, text="Francês", command=lambda: selecionar(opcao_nome="pao", valor="pao_frances")).pack()

    tk.Label(janela, text="Extras:", font=("Arial", 16)).pack(pady=5)
    tk.Button(janela, text="Salada", command=lambda: selecionar_extra(nome_extra="salada")).pack()
    tk.Button(janela, text="Bacon", command=lambda: selecionar_extra(nome_extra="bacon")).pack()
    tk.Button(janela, text="Ovo", command=lambda: selecionar_extra(nome_extra="ovo")).pack()
    tk.Button(janela, text="Picles", command=lambda: selecionar_extra(nome_extra="picles")).pack()
    tk.Button(janela, text="Tomate", command=lambda: selecionar_extra(nome_extra="tomate")).pack()
    tk.Button(janela, text="Cebola", command=lambda: selecionar_extra(nome_extra="cebola")).pack()

    tk.Button(janela, text="SALVAR MEU BURGÃO", bg="green", fg="white", command=salvar_no_banco).pack(pady=20)

    janela.mainloop()
