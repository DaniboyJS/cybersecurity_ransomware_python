import os
import pyaes

##abrir o arquivo criptografado

file_name = "teste.txt.ransomwaresecreto"
##cria variavel com nome do arquivo a ser descriptografado
file = open(file_name,"rb")
##abre o arquivo para leitura
file_data=file.read()
##le o arquivo
file.close()
##fecha o arquivo

##chave de criptografia

key = b"batatinhasearroz"
##chave
aes = pyaes.AESModeOfOperationCTR(key)
##funcao de descriptografia

##descriptografar o arquivo
decrypt_data = aes.decrypt(file_data)
##descriptografa o arquivo

##remover arquivo criptografado
os.remove(file_name)
##exclui arquivo

##criar arquivo descriptografado
new_file = "teste.txt"
##nomeia o arquivo
new_file = open(f'{new_file}',"wb")
##abre o arquivo para escrita
new_file.write(decrypt_data)
##escreve o texto descriptografado
new_file.close
##fecha o arquivo
