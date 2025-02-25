from cryptography.fernet import Fernet
import json
import os
from game.personagem import Personagem

# Caminhos dos arquivos
KEY_FILE = "config/key.key"
DATA_FILE = "config/personagem.dat"

# Garantir que o diretório "config" existe
os.makedirs("config", exist_ok=True)

# Gerar ou carregar chave de criptografia
if not os.path.exists(KEY_FILE):
    chave = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(chave)
else:
    with open(KEY_FILE, "rb") as key_file:
        chave = key_file.read()

fernet = Fernet(chave)

def salvar_personagem(personagem):
    """Salva o personagem criptografado em um arquivo."""
    dados = {
        "nome": personagem.nome,
        "classe": personagem.classe,
        "vida": personagem.vida,
        "ataque": personagem.ataque,
        "defesa": personagem.defesa,
        "nivel": personagem.nivel,           # Adicionado
        "experiencia": personagem.experiencia # Adicionado
    }
    json_dados = json.dumps(dados).encode()
    dados_criptografados = fernet.encrypt(json_dados)

    with open(DATA_FILE, "wb") as file:
        file.write(dados_criptografados)

def carregar_personagem():
    """Carrega o personagem do arquivo criptografado, se existir."""
    if not os.path.exists(DATA_FILE):
        return None

    with open(DATA_FILE, "rb") as file:
        dados_criptografados = file.read()

    try:
        json_dados = fernet.decrypt(dados_criptografados).decode()
        dados = json.loads(json_dados)
        return Personagem(**dados)  # Criando um objeto Personagem com os dados carregados
    except Exception as e:
        print(f"Erro ao carregar personagem: {e}")
        return None
