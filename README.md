# Leitura e filtro de usuários em JSON

Exercício em Python que lê usuários de um arquivo JSON e exibe o número da mesa e o e-mail daqueles cuja mesa é maior que 15.

## Requisitos

- Python 3.6 ou superior.
- Git para clonar o repositório (também é possível baixar o ZIP pelo GitHub).

O script usa somente a biblioteca padrão do Python. Não é necessário instalar pacotes com `pip`.

## Como executar

```bash
git clone https://github.com/lucasdossantosxl-cyber/json-arquvos-.git
cd json-arquvos-
python numberone.py
```

No Windows, se necessário, use `py numberone.py`. Em sistemas que disponibilizam Python 3 como `python3`, use `python3 numberone.py`.

O arquivo `dados.json` deve ficar na mesma pasta de `numberone.py`. O script encontra esse arquivo mesmo quando é executado a partir de outra pasta.

**Com os dados atuais, nada é exibido:** as mesas cadastradas são 1 e 2, e o filtro seleciona apenas mesas maiores que 15. Isso é uma execução normal, sem erro.

## Formato dos dados

O arquivo deve ser salvo em UTF-8 e conter uma lista de objetos. Cada usuário precisa destes campos:

| Campo | Regra |
| --- | --- |
| `numero_mesa` | Número inteiro positivo, sem aspas. |
| `email` | Texto não vazio. O script não valida o formato do endereço. |

Campos adicionais, como `user_id`, `reunioes`, `no_banco_de_dados` e `suprimentos_mesa`, são aceitos, mas não participam do filtro.

Por exemplo, para experimentar, substitua o conteúdo de `dados.json` por:

```json
[
    {"numero_mesa": 15, "email": "ana@example.com"},
    {"numero_mesa": 16, "email": "bruno@example.com"}
]
```

A saída será:

```text
Mesa 16: bruno@example.com
```

A mesa 15 não aparece porque a comparação é estritamente maior que o limite. Para mudar o filtro, altere `LIMITE_MESA` em `numberone.py`.

## Validação e erros

Todos os registros são validados antes da exibição. Se o arquivo estiver ausente, não puder ser lido, tiver JSON inválido ou algum usuário não atender às regras, o script escreve uma mensagem de erro em `stderr` e termina com código 1. Quando a leitura e a validação são bem-sucedidas, termina com código 0, mesmo que nenhuma mesa passe pelo filtro.

## Arquivos

- `numberone.py`: leitura, validação e filtro dos usuários.
- `dados.json`: dados de exemplo.
- `README.md`: documentação e instruções de uso.
