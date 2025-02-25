
from game.inimigo import Inimigo
from game.batalha import Batalha

class Fase:
    def __init__(self, numero, personagem):
        self.numero = numero
        self.personagem = personagem
        self.inimigo = Inimigo.gerar_inimigo(numero)

    def iniciar(self):
        """Inicia a batalha contra o inimigo da fase."""
        print(f"\n🔥 FASE {self.numero} 🔥")
        batalha = Batalha(self.personagem, self.inimigo)
        batalha.iniciar()

        return self.personagem.esta_vivo()  # Retorna se o jogador sobreviveu
