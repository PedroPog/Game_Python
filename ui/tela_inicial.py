import tkinter as tk
import tkinter.messagebox

from PIL import Image, ImageTk
from ui.tela_jogo import TelaJogo
from ui.tela_criacao_personagem import TelaCriacaoPersonagem  # Importar a nova tela de criação de personagem
from utils.salvar_carregar import carregar_personagem

class TelaInicial:
    def __init__(self, root):
        self.root = root
        self.root.title("RPG - Bem-Vindo")
        self.root.geometry("600x400")

        # Carregar imagem de fundo
        self.bg_image = Image.open("assets/imagens/fundo.jpg")  # Substitua por uma imagem no seu projeto
        self.bg_image = self.bg_image.resize((600, 400))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Exibir fundo
        self.bg_label = tk.Label(root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # Texto de boas-vindas
        lbl_titulo = tk.Label(root, text="🌟 Bem-vindo ao RPG! 🌟", font=("Arial", 20, "bold"), bg="#000", fg="white")
        lbl_titulo.pack(pady=20)

        # Botões estilizados
        btn_novo = tk.Button(root, text="Criar Novo Personagem", font=("Arial", 14), command=self.criar_novo)
        btn_novo.pack(pady=10)

        btn_carregar = tk.Button(root, text="Carregar Personagem", font=("Arial", 14), command=self.carregar_jogo)
        btn_carregar.pack(pady=10)

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
            TelaJogo(root_jogo, personagem=personagem)
            root_jogo.mainloop()
        else:
            tkinter.messagebox.showinfo("Erro", "Nenhum personagem salvo encontrado!")

# Testar a tela inicial
if __name__ == "__main__":
    root = tk.Tk()
    TelaInicial(root)
    root.mainloop()
