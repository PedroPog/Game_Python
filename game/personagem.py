class Personagem:
    def __init__(self, nome, classe, vida, ataque, defesa, nivel=1, experiencia=0):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.nivel = nivel
        self.experiencia = experiencia


    def atacar(self, inimigo):
        """Calcula o dano ao atacar um inimigo."""
        dano = max(1, self.ataque - inimigo.defesa)  # Garante que sempre haja dano
        inimigo.vida -= dano
        print(f"{self.nome} atacou {inimigo.nome} causando {dano} de dano!")

    def esta_vivo(self):
        """Verifica se o personagem ainda está vivo."""
        return self.vida > 0
