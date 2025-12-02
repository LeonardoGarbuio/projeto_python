import tkinter as tk
import mysql.connector
from tkinter import messagebox

def abrir_principal():
    try:
        conexao = mysql.connector.connect(
            host="localhost", user="root", password="", database="telas_python"
        )
        cursor = conexao.cursor()
    except mysql.connector.Error as erro:
        messagebox.showerror("Erro", f"Erro ao conectar: {erro}")
        return

    janela = tk.Tk()
    janela.title("Pedidos Salvos - Gordos Burguer")
    janela.geometry("600x650")

    titulo = tk.Label(janela, text="PEDIDOS REGISTRADOS", font=("Arial", 18, "bold"))
    titulo.pack(pady=10)

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

    cursor.execute("SELECT usuario, molho, carne, queijo, pao, salada, bacon, ovo, picles, tomate, cebola FROM hamburguer")
    registros = cursor.fetchall()

    container = tk.Frame(janela)
    container.pack(fill="both", expand=True)

    for r in registros:
        frame = tk.Frame(container, bd=2, relief="solid", padx=10, pady=10)
        frame.pack(pady=10, fill="x")

        usuario, molho, carne, queijo, pao, salada, bacon, ovo, picles, tomate, cebola = r

        tk.Label(frame, text=f"Usuário: {usuario}", font=("Arial", 12)).pack(anchor="w")
        tk.Label(frame, text=f"Molho: {formatar(molho)}", font=("Arial", 12)).pack(anchor="w")
        tk.Label(frame, text=f"Carne: {formatar(carne)}", font=("Arial", 12)).pack(anchor="w")
        tk.Label(frame, text=f"Queijo: {formatar(queijo)}", font=("Arial", 12)).pack(anchor="w")
        tk.Label(frame, text=f"Pão: {formatar(pao)}", font=("Arial", 12)).pack(anchor="w")

        sim_nao(salada); tk.Label(frame, text=f"Salada: {sn}", font=("Arial", 12)).pack(anchor="w")
        sim_nao(bacon); tk.Label(frame, text=f"Bacon: {sn}", font=("Arial", 12)).pack(anchor="w")
        sim_nao(ovo); tk.Label(frame, text=f"Ovo: {sn}", font=("Arial", 12)).pack(anchor="w")
        sim_nao(picles); tk.Label(frame, text=f"Picles: {sn}", font=("Arial", 12)).pack(anchor="w")
        sim_nao(tomate); tk.Label(frame, text=f"Tomate: {sn}", font=("Arial", 12)).pack(anchor="w")
        sim_nao(cebola); tk.Label(frame, text=f"Cebola: {sn}", font=("Arial", 12)).pack(anchor="w")

        tk.Button(frame, text="Pedir Hambúrguer", font=("Arial", 12), width=20).pack(pady=5)

    janela.mainloop()
