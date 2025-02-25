import tkinter as tk
from game.personagem import Personagem
from game.fase import Fase
from utils.salvar_carregar import salvar_personagem
from ui.tela_gameover import TelaGameOver

class TelaJogo:
    def __init__(self, root, novo=False, personagem=None):
        self.root = root
        self.root.title("RPG - Batalha")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        

        if novo or personagem is None:
            self.jogador = Personagem(nome="Herói", classe="Guerreiro", vida=30, ataque=7, defesa=3)
        else:
            self.jogador = personagem

        self.fase_atual = 1

        # Labels
        self.lbl_fase = tk.Label(root, text=f"🔥 FASE {self.fase_atual} 🔥", font=("Arial", 16, "bold"))
        self.lbl_fase.pack(pady=10)

        self.lbl_vida_jogador = tk.Label(root, text=f"Vida: {self.jogador.vida}", font=("Arial", 14))
        self.lbl_vida_jogador.pack()

        self.lbl_status = tk.Label(root, text="", font=("Arial", 12))
        self.lbl_status.pack()

        # Botão de ataque
        self.btn_atacar = tk.Button(root, text="Atacar", font=("Arial", 14), command=self.iniciar_fase)
        self.btn_atacar.pack(pady=10)

    def iniciar_fase(self):
        """Inicia a batalha e verifica se o jogador sobreviveu."""
        fase = Fase(self.fase_atual, self.jogador)
        vivo = fase.iniciar()

        # Atualizar vida do jogador na interface
        self.lbl_vida_jogador.config(text=f"Vida: {self.jogador.vida}")

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
    TelaJogo(root, novo=True)
    root.mainloop()
