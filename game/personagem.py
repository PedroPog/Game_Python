class Personagem:
    def __init__(self, nome, classe, vida, vida_maxima, ataque, defesa, nivel=1, experiencia=0, ponto_experiencia=0):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.vida_maxima = vida_maxima
        self.ataque = ataque
        self.defesa = defesa
        self.nivel = nivel
        self.experiencia = experiencia
        self.experiencia_maximo = 100 * nivel
        self.ponto_experiencia = ponto_experiencia


    def atacar(self, inimigo):
        """Calcula o dano ao atacar um inimigo."""
        dano = max(1, self.ataque - inimigo.defesa)  # Garante que sempre haja dano
        inimigo.vida -= dano
        print(f"{self.nome} atacou {inimigo.nome} causando {dano} de dano!")

    def esta_vivo(self):
        """Verifica se o personagem ainda está vivo."""
        return self.vida > 0
    
    def ganhar_experiencia(self, quantidade):
        """Adiciona experiência ao personagem."""
        self.experiencia += quantidade
        print(f"{self.nome} ganhou {quantidade} de experiência!")
        if self.experiencia >= self.experiencia_maximo:
            self.nivel += 1
            self.experiencia -= self.experiencia_maximo
            self.experiencia_maximo = 100 * self.nivel
            self.vida += self.vida_maxima / 2 # Restaurar metade da vida maxima
            if self.vida > self.vida_maxima:
                self.vida_maxima = self.vida_maxima
            self.ponto_experiencia += 1
            print(f"{self.nome} subiu para o nível {self.nivel}!")
            # print(f"Nova experiência: {self.experiencia}/{self.experiencia_maximo}")
