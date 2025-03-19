import tkinter as tk
from game.personagem import Personagem
from game.fase import Fase
from ui.tela_combat import TelaCombate
from utils.salvar_carregar import salvar_personagem
from ui.tela_gameover import TelaGameOver

class TelaJogo:
    def __init__(self, root, personagem=Personagem):
        self.root = root
        self.root.title("RPG - Batalha")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.jogador = personagem
        self.fase_atual = 1

        # Labels
        self.lbl_fase = tk.Label(root, text=f"🔥 FASE {self.fase_atual} 🔥", font=("Arial", 16, "bold"))
        self.lbl_fase.pack(pady=10)

        self.lbl_vida_jogador = tk.Label(root, text=f"Vida: {self.jogador.vida}//{self.jogador.vida_maxima} ", font=("Arial", 14))
        self.lbl_vida_jogador.pack()

        self.lbl_status = tk.Label(root, text="", font=("Arial", 12))
        self.lbl_status.pack()

        # Botão de ataque
        self.btn_atacar = tk.Button(root, text="Encontrar Monstro", font=("Arial", 14), command=self.iniciar_fase)
        self.btn_atacar.pack(pady=10)

    def iniciar_fase(self):
        # Cria a tela de combate e inicia a batalha
        root_combate = tk.Toplevel(self.root)
        combate = TelaCombate(root_combate, self.fase_atual, self.jogador)
        vivo = combate.iniciar_batalha()

        self.lbl_vida_jogador.config(text=f"Vida: {self.jogador.vida}//{self.jogador.vida_maxima}")
        if not vivo:
            self.game_over()
        else:
            self.fase_atual += 1
            self.lbl_fase.config(text=f"🔥 FASE {self.fase_atual} 🔥")
            salvar_personagem(self.jogador)  # Salva progresso

    def game_over(self):
        """Fecha a tela do jogo e exibe a tela de game over."""
        self.root.destroy()
        root_gameover = tk.Tk()
        TelaGameOver(root_gameover)
        root_gameover.mainloop()

# Testar a tela do jogo
if __name__ == "__main__":
    root = tk.Tk()
    TelaJogo(root)
    root.mainloop()
