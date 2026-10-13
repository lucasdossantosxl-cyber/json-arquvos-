import json
import sys
from pathlib import Path

CAMINHO_DADOS = Path(__file__).resolve().parent / "dados.json"
LIMITE_MESA = 15


def carregar_usuarios(caminho):
    """Lê e valida os campos necessários antes de exibir os usuários."""
    with caminho.open("r", encoding="utf-8") as arquivo:
        usuarios = json.load(arquivo)

    if not isinstance(usuarios, list):
        raise ValueError("O JSON deve conter uma lista de usuários.")

    for indice, usuario in enumerate(usuarios, start=1):
        if not isinstance(usuario, dict):
            raise ValueError(f"Usuário {indice}: deve ser um objeto JSON.")

        numero_mesa = usuario.get("numero_mesa")
        email = usuario.get("email")
        if type(numero_mesa) is not int or numero_mesa < 1:
            raise ValueError(f"Usuário {indice}: numero_mesa deve ser um inteiro positivo.")
        if not isinstance(email, str) or not email.strip():
            raise ValueError(f"Usuário {indice}: email deve ser um texto não vazio.")

    return usuarios


def main():
    try:
        usuarios = carregar_usuarios(CAMINHO_DADOS)
    except (OSError, ValueError) as erro:
        print(f"Erro ao carregar {CAMINHO_DADOS.name}: {erro}", file=sys.stderr)
        return 1

    # Exibe os contatos das mesas acima do limite definido.
    for usuario in usuarios:
        if usuario["numero_mesa"] > LIMITE_MESA:
            print(f"Mesa {usuario['numero_mesa']}: {usuario['email']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
