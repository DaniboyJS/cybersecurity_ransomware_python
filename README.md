# Decrypter & Encrypter Scripts

## Descrição
Scripts em Python para criptografar e descriptografar arquivos usando a biblioteca `pyaes`.

## Como Usar

### Ferramentas
- Python 3.x
- Biblioteca `pyaes`

### Criptografar
1. Coloque `teste.txt` na mesma pasta dos scripts.
2. Execute:
   ```bash
   python encrypter.py
3. O arquivo será criptografado como `teste.txt.ransomwaresecreto`.

### Descriptografar
1. Certifique-se que o arquivo 'teste.txt.ransomwaresecreto' esteja na pasta.
2. Execute:
   ```bash
   python decrypter.py
3. O arquivo descriptografado será chamado de `teste.txt`

### Chave
- A chave para criptografia é `batatinhasearroz`, podendo ser facilmente modificada pelo usuário, a fim de uma maior personalização do código.

## Considerações
Este desafio foi uma ótima oportunidade para aprender novos comandos e funções do Python, além de melhorar minhas habilidades de programação. A simplicidade do código também me fez refletir sobre a importância de proteger os dados no ambiente virtual.

A segurança de dados e a criptografia são essenciais para garantir a privacidade e proteção das informações dos usuários, e esse trabalho reforça a importância de considerar essas questões em qualquer desenvolvimento de sistemas.
