import tkinter as tk
import tkinter.messagebox

from tkinter import ttk
from PIL import Image, ImageTk
from ui.tela_jogo import TelaJogo
from ui.tela_perfil import TelaPerfil
from ui.tela_criacao_personagem import TelaCriacaoPersonagem
from utils.salvar_carregar import carregar_personagem

class TelaInicial:
    def __init__(self, root):
        self.root = root
        self.root.title("RPG - Bem-Vindo")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        self.style = ttk.Style()
        self.style.configure("TButton",
                             font=("Arial",14),
                             foreground="black",
                             background="#4CAF50",
                             padding=10,
                             relief="solid")

        # Carregar imagem de fundo (descomente para usar uma imagem de fundo)
        # self.bg_image = Image.open("assets/imagens/fundo.jpg")  # Substitua por uma imagem no seu projeto
        # self.bg_image = self.bg_image.resize((600, 400))
        # self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Exibir fundo (se você estiver usando uma imagem, use a imagem como fundo)
        self.bg_label = tk.Label(root, bg='white')
        self.bg_label.place(relwidth=1, relheight=1)

        # Texto de boas-vindas com estrelas
        lbl_titulo = tk.Label(root, text="Bem-vindo ao RPG!", font=("Arial", 20, "bold"),
                              bg="white", fg="black")
        lbl_titulo.place(relx=0.5, rely=0.2, anchor='center')  # Usando place para centralizar

        

        # Botões estilizados
        btn_novo = ttk.Button(root, text="Criar Novo Personagem", style="TButton", command=self.criar_novo)
        btn_novo.place(relx=0.5, rely=0.5, anchor='center')  # Centralizando com place
        btn_novo.config(cursor="hand2")

        btn_carregar = ttk.Button(root, text="Carregar Personagem", style="TButton", command=self.carregar_jogo)
        btn_carregar.place(relx=0.5, rely=0.7, anchor='center')  # Centralizando com place
        btn_carregar.config(cursor="hand2")

    def criar_novo(self):
        """Abre a tela de criação de personagem e inicia o jogo com o novo personagem"""
        self.root.destroy()
        root_criacao = tk.Tk()
        TelaCriacaoPersonagem(root_criacao, iniciar_jogo=True)  # Chama a tela de criação de personagem
        root_criacao.mainloop()

    def carregar_jogo(self):
        """Tenta carregar um personagem salvo."""
        personagem = carregar_personagem()
        if personagem:
            self.root.destroy()
            root_jogo = tk.Tk()
            # TelaJogo(root_jogo, personagem=personagem)
            TelaPerfil(root_jogo, personagem=personagem)
            root_jogo.mainloop()
        else:
            tkinter.messagebox.showinfo("Erro", "Nenhum personagem salvo encontrado!")

# Testar a tela inicial
if __name__ == "__main__":
    root = tk.Tk()
    TelaInicial(root)
    root.mainloop()
