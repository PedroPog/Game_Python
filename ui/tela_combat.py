from game.inimigo import Inimigo
from game.personagem import Personagem
import tkinter as tk
from tkinter import ttk
import random


class TelaCombate:
    def __init__(self, root, numero, personagem=Personagem, tela_anterior=None):
        self.root = root
        self.personagem = personagem
        self.numero = numero
        self.inimigo = Inimigo.gerar_inimigo(numero)
        self.tela_anterior = tela_anterior  # Referência para a tela anterior

    def iniciar_batalha(self):
        self.root.title(f"RPG - Batalha fase: {self.numero}")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.configure(bg="#2C2F33")  # Cor de fundo geral

        self.criar_interface()
        return self.personagem.esta_vivo()

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
        self.frame_acoes = tk.Frame(self.root, bg="white", height=100,
                                    highlightbackground="white", highlightthickness=2)
        self.frame_acoes.pack(fill="x", side="bottom", padx=5, pady=5)
        self.frame_acoes.pack_propagate(False)

        # Configura layout da grid
        for i in range(3):
            self.frame_acoes.columnconfigure(i, weight=1)
        for j in range(2):
            self.frame_acoes.rowconfigure(j, weight=1)

        # Frame de informações ocupando 3 colunas e 2 linhas
        self.frame_infos = tk.Frame(self.frame_acoes, bg="white", highlightbackground="gray",
                                    highlightthickness=5, height=80)
        self.frame_infos.grid(row=0, column=0, rowspan=2, columnspan=3, padx=5, pady=5, sticky="nsew")
        self.frame_infos.pack_propagate(False)

        # Label dentro de frame_infos para exibir mensagens
        self.lbl_status = ttk.Label(self.frame_infos, text="A batalha começou!", font=("Arial", 10), background="white")
        self.lbl_status.pack(expand=True)

        # Botão de ataque no canto superior direito
        self.btn_atacar = ttk.Button(self.frame_acoes, text="Atacar", command=self.atacar)
        self.btn_atacar.grid(row=0, column=3, padx=2, pady=5, sticky="ne")

        # Botão de defesa logo abaixo do botão de ataque
        self.btn_defender = ttk.Button(self.frame_acoes, text="Defender", command=self.defender)
        self.btn_defender.grid(row=0, column=3, padx=2, pady=2, sticky="se")

    def atualizar_interface(self):
        """Atualiza a exibição da barra de vida e os rótulos."""
        self.lbl_inimigo.config(text=f"{self.inimigo.nome} - HP: {max(0, self.inimigo.vida)}")
        self.hp_bar_inimigo["value"] = max(0, self.inimigo.vida)

        self.lbl_jogador.config(text=f"{self.personagem.nome} - HP: {max(0, self.personagem.vida)}")
        self.hp_bar_jogador["value"] = max(0, self.personagem.vida)

    def atacar(self):
        """O jogador ataca o inimigo."""
        # Desabilita os botões enquanto o inimigo ataca
        self.btn_atacar.config(state="disabled")
        self.btn_defender.config(state="disabled")

        dano = random.randint(3, self.personagem.ataque)
        self.inimigo.vida -= dano
        self.lbl_status.config(text=f"{self.personagem.nome} causou {dano} de dano!")

        self.atualizar_interface()

        if self.inimigo.vida <= 0:
            self.lbl_status.config(text=f"{self.personagem.nome} venceu a batalha! 🎉")
            self.terminar_combate()
        else:
            self.root.after(1000, self.inimigo_ataca)  # Pequena pausa antes do ataque do inimigo

    def defender(self):
        """O jogador se defende, reduzindo o dano do próximo ataque."""
        # Desabilita os botões enquanto o inimigo ataca
        self.btn_atacar.config(state="disabled")
        self.btn_defender.config(state="disabled")

        self.lbl_status.config(text=f"{self.personagem.nome} se defendeu! 🛡")
        self.root.after(1000, lambda: self.inimigo_ataca(defesa=True))  # Pequena pausa antes do ataque do inimigo

    def inimigo_ataca(self, defesa=False):
        """O inimigo ataca o jogador."""
        dano = random.randint(2, self.inimigo.ataque)
        if defesa:
            dano //= 2  # Reduz dano pela metade se estiver defendendo

        self.personagem.vida -= dano
        self.lbl_status.config(text=f"{self.inimigo.nome} causou {dano} de dano!")

        self.atualizar_interface()

        if self.personagem.vida <= 0:
            self.lbl_status.config(text=f"{self.inimigo.nome} venceu a batalha. Você morreu! 💀")
            self.terminar_combate()
        elif self.inimigo.vida <= 0:
            self.lbl_status.config(text=f"{self.personagem.nome} venceu a batalha!")
            self.terminar_combate()

        else:
            self.lbl_status.config(text=f"{self.personagem.nome} HP: {self.personagem.vida} | "
                                        f"{self.inimigo.nome} HP: {self.inimigo.vida}")

    def terminar_combate(self):
        """Finaliza o combate e fecha a janela de combate."""
        # Atualiza a tela anterior (TelaJogo) com o estado atual do personagem
        if self.tela_anterior:
            self.tela_anterior.lbl_vida_jogador.config(
                text=f"Vida: {self.personagem.vida}//{self.personagem.vida_maxima}")

        # Fecha a janela de combate
        self.root.after(1000, self.root.destroy)  # Fecha após um breve delay

    def fechar_tela(self):
        """Fecha a tela de combate sem atualizar a anterior."""
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    personagem = Personagem(nome="Herói", vida=50, vida_maxima=50, ataque=10, classe="Guerreiro", defesa=0)
    TelaCombate(root, personagem)
    root.mainloop()
