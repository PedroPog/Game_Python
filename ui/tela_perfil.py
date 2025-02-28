import tkinter as tk
from tkinter import ttk
from game.personagem import Personagem
from game.fase import Fase
from ui.tela_jogo import TelaJogo
from utils.salvar_carregar import salvar_personagem
from ui.tela_gameover import TelaGameOver
from PIL import Image, ImageTk

class TelaPerfil:


    def __init__(self, root, personagem=Personagem):
        self.root = root
        self.root.title("RPG - Perfil")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.jogador = personagem

        # Carregar a imagem
        # img_perfil = Image.open("assets/imagens/perfil.png")
        # img_perfil = img_perfil.resize((100, 100), Image.Resampling.LANCZOS)
        # self.img_perfil_tk = ImageTk.PhotoImage(img_perfil)  # Mantenha uma referência

        # # Criar a imagem de sombra
        # # img_sombra = img_perfil.convert("RGBA")
        # # sombra = Image.new("RGBA", img_sombra.size, (0, 0, 0, 50))  # Sombra com opacidade
        # # img_sombra = Image.alpha_composite(img_sombra, sombra)
        # # self.img_sombra_tk = ImageTk.PhotoImage(img_sombra)  # Mantenha uma referência

        # # Criar um canvas para bordas arredondadas
        # canvas = tk.Canvas(self.root, width=120, height=120, bg="white", bd=0, highlightthickness=0)
        # canvas.place(relx=0.5, rely=0.1, anchor="center")  # Centralizar no topo

        # # Adicionar a sombra
        # canvas.create_image(10, 10, image=self.img_sombra_tk)  # Deslocamento para sombra
        # # Adicionar a imagem centralizada
        # canvas.create_image(60, 60, image=self.img_perfil_tk)

        lbl_name = tk.Label(self.root, text=f"Nome: {self.jogador.nome}")
        lbl_name.pack(pady=10)

        lbl_nivel = tk.Label(self.root, text=f"Nível: {self.jogador.nivel}", font=("Arial", 10))
        lbl_nivel.pack()

        self.exp_bar = ttk.Progressbar(self.root, orient="horizontal", length=self.jogador.experiencia_maximo,
                                        mode="determinate", value=self.jogador.experiencia )
        self.exp_bar.pack(pady=5)
        lbl_exp = tk.Label(self.root, text=f"Experiência: {self.jogador.experiencia}/{self.jogador.experiencia_maximo}")
        lbl_exp.pack()

        lbl_exp = tk.Label(self.root, text="", font=("Arial", 10))
        lbl_exp.pack()

        lbl_classe = tk.Label(self.root, text=f"Classe: {self.jogador.classe}")
        lbl_classe.pack()

        # Caixa de atributos
        box_atributes = tk.Frame(self.root, bg="gray77", bd=2, relief="solid")
        box_atributes.pack(pady=15, padx=20, fill="both", expand=True)

        tk.Label(box_atributes, text="Atributos", font=("Arial", 11, "bold"), bg="gray77").pack()
        tk.Label(box_atributes, text=f"Pontos de Experiencia: {self.jogador.ponto_experiencia}", font=("Arial", 11, "bold"), bg="gray77").pack()
        

        lbl_vida = tk.Label(box_atributes, text=f"Vida: {self.jogador.vida}", font=("Arial", 10), bg="gray77")
        lbl_vida.pack(pady=2)

        lbl_ataque = tk.Label(box_atributes, text=f"Ataque: {self.jogador.ataque}", font=("Arial", 10), bg="gray77")
        lbl_ataque.pack(pady=2)

        lbl_defesa = tk.Label(box_atributes, text=f"Defesa: {self.jogador.defesa}", font=("Arial", 10), bg="gray77")
        lbl_defesa.pack(pady=2)

        btn_nova_rodanda = tk.Button(root, text="Nova Rodanda", command=self.iniciar_fase)
        btn_nova_rodanda.pack(pady=5)


    def iniciar_fase(self):
        self.root.destroy()  # Fecha a tela de criação
        root_jogo = tk.Tk()
        person = self.jogador
        TelaJogo(root_jogo, personagem=person)# Inicia o jogo com o personagem criado
        root_jogo.mainloop()


# Testar a tela do jogo
if __name__ == "__main__":
    root = tk.Tk()
    TelaPerfil(root, novo=True)
    root.mainloop()
