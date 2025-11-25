from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import tkinter as tk
from tkinter import PhotoImage
from pyexpat.errors import messages
global janela
global entrada_n1, entrada_n2

def abrir_principal():
    janela = tk.Tk()
    janela.title('Gordos burguer')
    janela.geometry('700x600')