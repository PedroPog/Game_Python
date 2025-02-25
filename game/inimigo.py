import random

class Inimigo:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.vida_maxima = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, personagem):
        """Calcula o dano ao atacar o jogador."""
        dano = max(1, self.ataque - personagem.defesa)
        personagem.vida -= dano
        print(f"{self.nome} atacou {personagem.nome} causando {dano} de dano!")

    def esta_vivo(self):
        """Verifica se o inimigo ainda está vivo."""
        return self.vida > 0

    @staticmethod
    def gerar_inimigo(fase):
        """Gera um inimigo aleatório baseado na fase."""
        nomes = ["Goblin", "Orc", "Esqueleto", "Lobo Sombrio", "Dragão Bebê"]
        nome = random.choice(nomes)
        vida = random.randint(10, 20) + (fase * 2)
        ataque = random.randint(3, 6) + (fase * 1)
        defesa = random.randint(1, 3) + (fase // 2)
        return Inimigo(nome, vida, ataque, defesa)
