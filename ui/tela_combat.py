from game.inimigo import Inimigo
from game.personagem import Personagem
import tkinter as tk
from tkinter import ttk
import random

class TelaCombate:
    def __init__(self, root, personagem):
        self.root = root
        self.personagem = personagem
        self.inimigo = Inimigo(nome="Inimigo", vida=50, ataque=5, defesa=0, nivel=1)

        self.root.title("RPG - Batalha")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.configure(bg="#2C2F33")  # Cor de fundo geral

        self.criar_interface()

    def criar_interface(self):
        """Cria os elementos visuais da tela de combate."""

        # ======= INIMIGO =======
        self.frame_inimigo = tk.Frame(self.root, bg="#FF6F61", height=100)
        self.frame_inimigo.pack(fill="x", pady=10)

        self.lbl_inimigo = ttk.Label(self.frame_inimigo, text=f"{self.inimigo.nome} - HP: {self.inimigo.vida}",
                                     font=("Arial", 12, "bold"), background="#FF6F61", foreground="white")
        self.lbl_inimigo.pack(pady=5)

        self.hp_bar_inimigo = ttk.Progressbar(self.frame_inimigo, length=300, mode="determinate")
        self.hp_bar_inimigo["maximum"] = self.inimigo.vida_maxima
        self.hp_bar_inimigo["value"] = self.inimigo.vida
        self.hp_bar_inimigo.pack(pady=5)

        # ======= JOGADOR =======
        self.frame_jogador = tk.Frame(self.root, bg="#77DD77", height=100)
        self.frame_jogador.pack(fill="x", pady=10)

        self.lbl_jogador = ttk.Label(self.frame_jogador, text=f"{self.personagem.nome} - HP: {self.personagem.vida}",
                                     font=("Arial", 12, "bold"), background="#77DD77", foreground="white")
        self.lbl_jogador.pack(pady=5)

        self.hp_bar_jogador = ttk.Progressbar(self.frame_jogador, length=300, mode="determinate")
        self.hp_bar_jogador["maximum"] = self.personagem.vida_maxima
        self.hp_bar_jogador["value"] = self.personagem.vida
        self.hp_bar_jogador.pack(pady=5)

        # ======= OPÇÕES DE COMBATE =======
        self.frame_acoes = tk.Frame(self.root, bg="#ffffff", height=100,
                                    highlightbackground="white", highlightthickness=2)
        self.frame_acoes.pack(fill="x", side="bottom", padx=5, pady=5)
        self.frame_acoes.pack_propagate(False)

        # Configura layout da grid
        for i in range(3):
            self.frame_acoes.columnconfigure(i, weight=1)
        for j in range(2):
            self.frame_acoes.rowconfigure(j, weight=1)

        # Frame de informações ocupando 3 colunas e 2 linhas
        self.frame_infos = tk.Frame(self.frame_acoes, bg="black", height=80)
        self.frame_infos.grid(row=0, column=0, rowspan=2, columnspan=3, padx=5, pady=5, sticky="nsew")
        self.frame_infos.pack_propagate(False)

        # Botão de ataque no canto superior direito
        self.btn_atacar = ttk.Button(self.frame_acoes, text="Atacar", command=self.atacar)
        self.btn_atacar.grid(row=0, column=3, padx=2, pady=5, sticky="ne")

        # Botão de defesa logo abaixo do botão de ataque
        self.btn_defender = ttk.Button(self.frame_acoes, text="Defender", command=self.defender)
        self.btn_defender.grid(row=0, column=3, padx=2, pady=2, sticky="se")

        # Botão de ataque no canto superior direito
        self.btn_atacar = ttk.Button(self.frame_acoes, text="TESTE")
        self.btn_atacar.grid(row=0, column=4, padx=2, pady=2, sticky="ne")


    def atualizar_interface(self):
        """Atualiza a exibição da barra de vida e os rótulos."""
        self.lbl_inimigo.config(text=f"{self.inimigo.nome} - HP: {max(0, self.inimigo.vida)}")
        self.hp_bar_inimigo["value"] = max(0, self.inimigo.vida)

        self.lbl_jogador.config(text=f"{self.personagem.nome} - HP: {max(0, self.personagem.vida)}")
        self.hp_bar_jogador["value"] = max(0, self.personagem.vida)

    def atacar(self):
        """O jogador ataca o inimigo."""
        dano = random.randint(3, self.personagem.ataque)
        self.inimigo.vida -= dano
        self.lbl_status.config(text=f"{self.personagem.nome} atacou e causou {dano} de dano!")
        self.atualizar_interface()

        if self.inimigo.vida <= 0:
            #self.lbl_status.config(text=f"{self.personagem.nome} venceu a batalha! 🎉")
            self.btn_atacar.config(state="disabled")
            self.btn_defender.config(state="disabled")
        else:
            self.inimigo_ataca()

    def defender(self):
        """O jogador se defende, reduzindo o dano do próximo ataque."""
        #self.lbl_status.config(text=f"{self.personagem.nome} se defendeu! 🛡")
        self.inimigo_ataca(defesa=True)

    def inimigo_ataca(self, defesa=False):
        """O inimigo ataca o jogador."""
        dano = random.randint(2, self.inimigo.ataque)
        if defesa:
            dano //= 2  # Reduz dano pela metade se estiver defendendo

        self.personagem.vida -= dano
        #self.lbl_status.config(text=f"{self.inimigo.nome} atacou e causou {dano} de dano!")
        self.atualizar_interface()

        if self.personagem.vida <= 0:
            #self.lbl_status.config(text=f"{self.personagem.nome} foi derrotado! ☠")
            self.btn_atacar.config(state="disabled")
            self.btn_defender.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    personagem = Personagem(nome="Herói", vida=50, vida_maxima=50, ataque=10, classe="Guerreiro", defesa=0)
    TelaCombate(root, personagem)
    root.mainloop()
