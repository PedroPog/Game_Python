import tkinter as tk
from utils.salvar_carregar import carregar_personagem

class TelaGameOver:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Over")

        # Mensagem de fim de jogo
        lbl_gameover = tk.Label(root, text="💀 GAME OVER 💀", font=("Arial", 20, "bold"), fg="red")
        lbl_gameover.pack(pady=20)

        # Botão para reiniciar o jogo
        btn_reload = tk.Button(root, text="Reiniciar", font=("Arial", 14), command=self.reiniciar)
        btn_reload.pack(pady=10)

        # Botão para sair do jogo
        btn_sair = tk.Button(root, text="Sair", font=("Arial", 14), command=root.quit)
        btn_sair.pack(pady=10)

    def reiniciar(self):
        """Carrega o personagem salvo e reinicia o jogo."""
        from ui.tela_perfil import TelaPerfil
        personagem = carregar_personagem()
        if personagem:
            self.root.destroy()  # Fecha a tela de Game Over
            root_jogo = tk.Tk()
            personagem.vida = personagem.vida_maxima # Restaura a vida do personagem
            TelaPerfil(root_jogo, personagem=personagem)  # Abre a TelaPerfil com o personagem carregado
            root_jogo.mainloop()


# Testar a tela de Game Over
if __name__ == "__main__":
    root = tk.Tk()
    TelaGameOver(root)
    root.mainloop()
