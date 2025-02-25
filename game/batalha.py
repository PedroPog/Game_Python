import time
from game.personagem import Personagem
from game.inimigo import Inimigo

class Batalha:
    def __init__(self, personagem=Personagem, inimigo=Inimigo):
        self.personagem = personagem
        self.inimigo = inimigo

    def iniciar(self):
        """Executa o loop da batalha até que alguém morra."""
        print(f"⚔️ Início da batalha: {self.personagem.nome} vs {self.inimigo.nome} ⚔️")

        while self.personagem.esta_vivo() and self.inimigo.esta_vivo():
            # Turno do jogador
            self.personagem.atacar(self.inimigo)
            if not self.inimigo.esta_vivo():
                print(f"🏆 {self.inimigo.nome} foi derrotado!")
                self.personagem.ganhar_experiencia(self.inimigo.experiencia)
                break  # Sai do loop

            # Turno do inimigo
            time.sleep(1)  # Simula tempo de ação
            self.inimigo.atacar(self.personagem)
            if not self.personagem.esta_vivo():
                print(f"☠️ {self.personagem.nome} foi derrotado! Game Over.")
                break
