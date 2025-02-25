import tkinter as tk
from tkinter import ttk, messagebox
from ui.tela_jogo import TelaJogo  # Importa a tela do jogo
from utils.salvar_carregar import salvar_personagem  # Função para salvar o personagem

from game.personagem import Personagem

# Classes e seus atributos iniciais
CLASSES = {
    "Guerreiro": {"vida": 30, "ataque": 7, "defesa": 5},
    "Mago": {"vida": 20, "ataque": 10, "defesa": 3},
    "Arqueiro": {"vida": 25, "ataque": 8, "defesa": 4}
}

class TelaCriacaoPersonagem:
    def __init__(self, root, iniciar_jogo=False):
        self.root = root
        self.root.title("Criação de Personagem")
        self.root.geometry("300x300")
        self.iniciar_jogo = iniciar_jogo  # Se True, inicia o jogo após criar o personagem

        # Nome do personagem
        tk.Label(root, text="Nome:").pack()
        self.nome_entry = tk.Entry(root)
        self.nome_entry.pack()

        # Escolha da classe
        tk.Label(root, text="Classe:").pack()
        self.classe_var = tk.StringVar(value="Guerreiro")
        self.classe_menu = ttk.Combobox(root, textvariable=self.classe_var, values=list(CLASSES.keys()))
        self.classe_menu.pack()
        self.classe_menu.bind("<<ComboboxSelected>>", self.atualizar_atributos)

        # Atributos
        tk.Label(root, text="Atributos:").pack()
        self.vida_var = tk.StringVar()
        self.ataque_var = tk.StringVar()
        self.defesa_var = tk.StringVar()

        self.vida_label = tk.Label(root, textvariable=self.vida_var)
        self.vida_label.pack()
        self.ataque_label = tk.Label(root, textvariable=self.ataque_var)
        self.ataque_label.pack()
        self.defesa_label = tk.Label(root, textvariable=self.defesa_var)
        self.defesa_label.pack()

        self.atualizar_atributos(None)

        # Botão de criar personagem
        tk.Button(root, text="Criar Personagem", command=self.criar_personagem).pack()

    def atualizar_atributos(self, event):
        """Atualiza os atributos conforme a classe escolhida."""
        classe = self.classe_var.get()
        atributos = CLASSES.get(classe, {})
        self.vida_var.set(f"Vida: {atributos['vida']}")
        self.ataque_var.set(f"Ataque: {atributos['ataque']}")
        self.defesa_var.set(f"Defesa: {atributos['defesa']}")

    def criar_personagem(self):
        """Cria e salva o personagem, depois inicia o jogo se necessário."""
        nome = self.nome_entry.get().strip()
        classe = self.classe_var.get()

        if not nome:
            messagebox.showerror("Erro", "O nome do personagem não pode estar vazio!")
            return

        atributos = CLASSES[classe]
        personagem = Personagem(
            nome=nome,
            classe=classe,
            vida=atributos["vida"],
            vida_maxima=atributos["vida"],
            ataque=atributos["ataque"],
            defesa=atributos["defesa"]
        )

        salvar_personagem(personagem)  # Salva o personagem criptografado

        messagebox.showinfo("Sucesso", f"Personagem {nome} criado como {classe}!")

        if self.iniciar_jogo:
            self.root.destroy()  # Fecha a tela de criação
            root_jogo = tk.Tk()
            TelaJogo(root_jogo, personagem=personagem)  # Inicia o jogo com o personagem criado
            root_jogo.mainloop()

# Teste independente da tela de criação
if __name__ == "__main__":
    root = tk.Tk()
    TelaCriacaoPersonagem(root, iniciar_jogo=True)
    root.mainloop()
