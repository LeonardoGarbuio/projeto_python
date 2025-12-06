import tkinter as tk
import mysql.connector
from tkinter import messagebox

from pedidos import faz_pedido

def abrir_principal(id_usuario):
    try:
        conexao = mysql.connector.connect(
            host="localhost", user="root", password="", database="telas_python"
        )
        cursor = conexao.cursor()
    except mysql.connector.Error as erro:
        messagebox.showerror("Erro", f"Erro ao conectar: {erro}")
        return

    def sim_nao(v):
        global sn
        if v == 1:
            sn = "Sim"
        else:
            sn = "Não"

    def formatar(texto):
        texto = texto.replace("_", " ")
        texto = texto.capitalize()
        return texto

    janela = tk.Tk()
    janela.title("Cardápio - Gordos Burguer")
    janela.geometry("600x500")

    titulo = tk.Label(janela, text="Cardápio", font=("Arial", 18, "bold"))
    titulo.pack(pady=10)

    cursor.execute("SELECT nome, molho, carne, queijo, pao, bacon, ovo, picles, tomate, cebola, alface FROM hamburguer")
    registros = cursor.fetchall()

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

    for r in registros:
        frame = tk.Frame(frame_scroll, bd=2, relief="solid", padx=10, pady=10)
        frame.pack(pady=10, fill="x")

        nome, molho, carne, queijo, pao, bacon, ovo, picles, tomate, cebola, alface = r

        tk.Label(frame, text=f"Nome: {nome}", font=("Arial", 12)).pack(anchor="w")
        tk.Label(frame, text=f"Pão: {formatar(pao)}", font=("Arial", 12)).pack(anchor="w")
        tk.Label(frame, text=f"Carne: {formatar(carne)}", font=("Arial", 12)).pack(anchor="w")
        tk.Label(frame, text=f"Queijo: {formatar(queijo)}", font=("Arial", 12)).pack(anchor="w")
        tk.Label(frame, text=f"Molho: {formatar(molho)}", font=("Arial", 12)).pack(anchor="w")

        sim_nao(bacon); tk.Label(frame, text=f"Bacon: {sn}", font=("Arial", 12)).pack(anchor="w")
        sim_nao(ovo); tk.Label(frame, text=f"Ovo: {sn}", font=("Arial", 12)).pack(anchor="w")
        sim_nao(picles); tk.Label(frame, text=f"Picles: {sn}", font=("Arial", 12)).pack(anchor="w")
        sim_nao(tomate); tk.Label(frame, text=f"Tomate: {sn}", font=("Arial", 12)).pack(anchor="w")
        sim_nao(cebola); tk.Label(frame, text=f"Cebola: {sn}", font=("Arial", 12)).pack(anchor="w")
        sim_nao(alface); tk.Label(frame, text=f"Alface: {sn}", font=("Arial", 12)).pack(anchor="w")

        cursor.execute(f"SELECT id FROM hamburguer WHERE nome='{nome}'")
        hamburguer = cursor.fetchone()[0]  # pega só o id, não a tupla
        usuario = id_usuario

        tk.Button(frame, text="Pedir Hambúrguer", command=lambda u=usuario, h=hamburguer: faz_pedido(u, h), font=("Arial", 12), width=20).pack(pady=5)
