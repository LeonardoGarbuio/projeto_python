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

def salvar_no_banco(nome_entrada):
    nome = nome_entrada.get()
    cursor.execute("INSERT INTO hamburguer (nome, molho, carne, queijo, pao, alface, bacon, ovo, picles, tomate, cebola) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        params=(nome, molho, carne, queijo, pao, alface, bacon, ovo, picles, tomate, cebola)
    )
    conexao.commit()
    messagebox.showinfo(title="OK", message="Hambúrguer salvo com sucesso!")

def selecionar(opcao_nome, valor):
    globals()[opcao_nome] = valor

def selecionar_extra(nome_extra):
    globals()[nome_extra] = 1 if globals()[nome_extra] == 0 else 0
    status = "Adicionado" if globals()[nome_extra] else "Removido"

def abre_cadastro_burguer():
    janela = tk.Tk()
    janela.title("")
    janela.geometry("400x500")

    # --- CONTAINER COM SCROLL ---
    container = tk.Frame(janela)
    container.pack(fill="both", expand=True)

    canvas = tk.Canvas(container)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    frame_scroll = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame_scroll, anchor="nw")
    # --- FIM DO SCROLL ---


    frame_molho = tk.Frame(frame_scroll, pady=10, bd=2, relief='groove')
    frame_molho.pack(padx=10, pady=5, fill='x')

    tk.Label(frame_molho, text="Escolha o molho:", font=("Arial", 16)).pack(pady=5)

    tk.Button(frame_molho, text="Ketchup", command=lambda: selecionar("molho", "ketchup")).pack(side='left', padx=10, fill='x')
    tk.Button(frame_molho, text="Mostarda", command=lambda: selecionar("molho", "mostarda")).pack(side='left', padx=10, fill='x')
    tk.Button(frame_molho, text="Maionese", command=lambda: selecionar("molho", "maionese")).pack(side='left', padx=10, fill='x')
    tk.Button(frame_molho, text="Barbecue", command=lambda: selecionar("molho", "barbecue")).pack(side='left', padx=10, fill='x')

    frame_carne = tk.Frame(frame_scroll, pady=10, bd=2, relief='groove')
    frame_carne.pack(padx=10, pady=5, fill='x')

    tk.Label(frame_carne, text="Escolha a carne:", font=("Arial", 16)).pack(pady=5)

    tk.Button(frame_carne, text="Bovina", command=lambda: selecionar("carne", "carne_bovina")).pack(side='left', padx=10, fill='x')
    tk.Button(frame_carne, text="Suína", command=lambda: selecionar("carne", "carne_suina")).pack(side='left', padx=10, fill='x')
    tk.Button(frame_carne, text="Caprina", command=lambda: selecionar("carne", "carne_caprina")).pack(side='left',padx=10, fill='x')
    tk.Button(frame_carne, text="Frango", command=lambda: selecionar("carne", "carne_frango")).pack(side='left',padx=10, fill='x')


    frame_queijo = tk.Frame(frame_scroll, pady=10, bd=2, relief='groove')
    frame_queijo.pack(padx=10, pady=5, fill='x')

    tk.Label(frame_queijo, text="Escolha o queijo:", font=("Arial", 16)).pack(pady=5)

    tk.Button(frame_queijo, text="Cheddar", command=lambda: selecionar("queijo", "queijo_cheddar")).pack(side='left',padx=10, fill='x')
    tk.Button(frame_queijo, text="Mussarela", command=lambda: selecionar("queijo", "queijo_mussarela")).pack(side='left', padx=10, fill='x')
    tk.Button(frame_queijo, text="Prato", command=lambda: selecionar("queijo", "queijo_prato")).pack(side='left',padx=10, fill='x')
    tk.Button(frame_queijo, text="Suíço", command=lambda: selecionar("queijo", "queijo_suico")).pack(side='left', padx=10, fill='x')


    frame_pao = tk.Frame(frame_scroll, pady=10, bd=2, relief='groove')
    frame_pao.pack(padx=10, pady=5, fill='x')

    tk.Label(frame_pao, text="Escolha o pão:", font=("Arial", 16)).pack(pady=5)

    tk.Button(frame_pao, text="Brioche", command=lambda: selecionar("pao", "pao_brioche")).pack(side='left', padx=10, fill='x')
    tk.Button(frame_pao, text="Australiano", command=lambda: selecionar("pao", "pao_australiano")).pack(side='left', padx=10, fill='x')
    tk.Button(frame_pao, text="Gergelim", command=lambda: selecionar("pao", "pao_gergelim")).pack(side='left', padx=10, fill='x')
    tk.Button(frame_pao, text="Francês", command=lambda: selecionar("pao", "pao_frances")).pack(side='left', padx=10, fill='x')


    frame_extras = tk.Frame(frame_scroll, pady=10, bd=2, relief='groove')
    frame_extras.pack(padx=10, pady=5, fill='x')

    tk.Label(frame_extras, text="Extras:", font=("Arial", 16)).pack(pady=5)

    tk.Button(frame_extras, text="Alface", command=lambda: selecionar_extra("alface")).pack(side='left', padx=5, fill='x')
    tk.Button(frame_extras, text="Bacon", command=lambda: selecionar_extra("bacon")).pack(side='left', padx=5, fill='x')
    tk.Button(frame_extras, text="Ovo", command=lambda: selecionar_extra("ovo")).pack(side='left', padx=5, fill='x')
    tk.Button(frame_extras, text="Picles", command=lambda: selecionar_extra("picles")).pack(side='left', padx=5, fill='x')
    tk.Button(frame_extras, text="Tomate", command=lambda: selecionar_extra("tomate")).pack(side='left', padx=5, fill='x')
    tk.Button(frame_extras, text="Cebola", command=lambda: selecionar_extra("cebola")).pack(side='left', padx=5, fill='x')

    frame_login = tk.Frame(frame_scroll, pady=10, bd=2, relief='groove')
    frame_login.pack(padx=10, pady=10, fill='x')  # ocupa horizontalmente

    tk.Label(frame_login, text='Nome do Hamburguer:', font=('Arial', 12, 'bold')).pack(pady=5, padx=5)
    nome_entrada = tk.Entry(frame_login, font=('Arial', 12))
    nome_entrada.pack(fill='x', padx=5, pady=5)

    tk.Button(frame_scroll, text="Salvar Hamburguer", command=lambda: salvar_no_banco(nome_entrada)).pack(pady=20)

    janela.mainloop()
