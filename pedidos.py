import mysql.connector
import tkinter as tk

try:
    conexao = mysql.connector.connect(
        host="localhost", user="root", password="", database="telas_python"
    )
    cursor = conexao.cursor()
except:
    print("Erro ao conectar ao banco.")


def marcar_feito(id_h, frame):
    cursor.execute("DELETE FROM pedidos WHERE id_hamburguer = %s", (id_h,))
    conexao.commit()
    frame.destroy()  # remove o frame da tela



def faz_pedido(usuario, hamburguer):
    cursor.execute("INSERT INTO pedidos (id_usuario, id_hamburguer) VALUES (%s,%s)", (usuario, hamburguer))
    conexao.commit()

def abrir_pedidos():
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
    janela.title('Pedidos')
    janela.geometry('500x500')
    janela.iconbitmap("burguer.ico")

    titulo = tk.Label(janela, text="Pedidos", font=("Arial", 18, "bold"))
    titulo.pack(pady=10)

    cursor.execute("SELECT id_hamburguer FROM pedidos")  # todos os pedidos
    ids = cursor.fetchall()

    hamburgueres = []
    for (hid,) in ids:
        cursor.execute(
            "SELECT id, nome, molho, carne, queijo, pao, bacon, ovo, picles, tomate, cebola, alface FROM hamburguer WHERE id = %s",
            (hid,))
        dados = cursor.fetchone()
        if dados:
            hamburgueres.append(dados)

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

    for r in hamburgueres:
        frame = tk.Frame(frame_scroll, bd=2, relief="solid", padx=10, pady=10)
        frame.pack(pady=10, fill="x")

        id_h, nome, molho, carne, queijo, pao, bacon, ovo, picles, tomate, cebola, alface = r

        tk.Label(frame, text=f"Nome: {nome}", font=("Arial", 12)).pack(anchor="w")
        tk.Label(frame, text=f"Pão: {formatar(pao)}", font=("Arial", 12)).pack(anchor="w")
        tk.Label(frame, text=f"Carne: {formatar(carne)}", font=("Arial", 12)).pack(anchor="w")
        tk.Label(frame, text=f"Queijo: {formatar(queijo)}", font=("Arial", 12)).pack(anchor="w")
        tk.Label(frame, text=f"Molho: {formatar(molho)}", font=("Arial", 12)).pack(anchor="w")

        sim_nao(bacon);
        tk.Label(frame, text=f"Bacon: {sn}", font=("Arial", 12)).pack(anchor="w")
        sim_nao(ovo);
        tk.Label(frame, text=f"Ovo: {sn}", font=("Arial", 12)).pack(anchor="w")
        sim_nao(picles);
        tk.Label(frame, text=f"Picles: {sn}", font=("Arial", 12)).pack(anchor="w")
        sim_nao(tomate);
        tk.Label(frame, text=f"Tomate: {sn}", font=("Arial", 12)).pack(anchor="w")
        sim_nao(cebola);
        tk.Label(frame, text=f"Cebola: {sn}", font=("Arial", 12)).pack(anchor="w")
        sim_nao(alface);
        tk.Label(frame, text=f"Alface: {sn}", font=("Arial", 12)).pack(anchor="w")

        tk.Button(frame, text="Feito", command=lambda h=id_h, f=frame: marcar_feito(h, f)).pack(pady=5)


    janela.mainloop()
