import tkinter as tk

class TelaGameOver:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Over")

        # Mensagem de fim de jogo
        lbl_gameover = tk.Label(root, text="💀 GAME OVER 💀", font=("Arial", 20, "bold"), fg="red")
        lbl_gameover.pack(pady=20)

        # Botão para sair
        btn_sair = tk.Button(root, text="Sair", font=("Arial", 14), command=root.quit)
        btn_sair.pack(pady=10)

# Testar a tela de game over
if __name__ == "__main__":
    root = tk.Tk()
    TelaGameOver(root)
    root.mainloop()
