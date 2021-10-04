from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
   criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #opção de listar o conteúdo do arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        #opção de cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        #opção de sair do sistema
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        #Digitou uma opção errada no menu
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1.0)


