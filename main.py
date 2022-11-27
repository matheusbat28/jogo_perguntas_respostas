import json
from random import randint
import os
from time import sleep


def abrirPeguntas():
    with open('./pegunta.json', encoding='utf-8') as arquivo:
        return json.load(arquivo)
    
def quantidadePeguntas(lista):
    cont = 0
    for x in lista:
        cont += 1
    return cont

def escolherPerguntas(lista, qtd):
    return lista[f'p{randint(1, qtd)}']

def mostrarPegunta(perguntaEscolhida, numero, nome):
    print(f'Jogador {nome}')
    print(str(numero) + '          -----Pergunta-----\n' + perguntaEscolhida['p'])
    print('A) ' + perguntaEscolhida['a'] + '\n' + 
          'B) ' + perguntaEscolhida['b'] + '\n' +
          'C) ' + perguntaEscolhida['c'] + '\n' +
          'D) ' + perguntaEscolhida['d'] + '\n' +
          'E) ' + perguntaEscolhida['e'] + '\n')
    
def verificarOpcao(perguntaEscolhida):
    while True:
        opcao = str(input('Qual sua resposta?\nR: ')).lower().strip()

        if 'abcde'.find(opcao) == -1:
            print('Escolha opção cerreta')
            continue
        elif opcao == '':
            print('Escolha opção cerreta')
            continue
        elif opcao == perguntaEscolhida['r']:
            print('Certa reposta!!!')
            return True
        else: 
            print('Errou!!\n' + 'Resposta correta: ' + perguntaEscolhida[perguntaEscolhida['r']])
            return False
        
        
def mostrarJogadores(jogador):
    for chave, valor in jogador.items():
        print(f'{chave} {valor}')
        
def verificarVitoria(jogador1, jogador2):
    if jogador1['qtdAcertos'] < jogador2['qtdAcertos']:
        jogador1['status'] = 'Vitória'
        jogador2['status'] = 'Derrota'
        
    elif jogador1['qtdAcertos'] == jogador2['qtdAcertos']:
        jogador1['status'] = 'Empate'
        jogador2['status'] = 'Empate'
    else:
        jogador2['status'] = 'Vitória'
        jogador1['status'] = 'Derrota'

pgAntiga = []
perguntas = abrirPeguntas()
qtdPerguntas = quantidadePeguntas(perguntas)
partidas = 20
perguntaEscolhida = None

jogador1 = {
    'nome': '',
    'qtdAcertos': 0,
    'qtdErro': 0,
    'status': ''
}

jogador2 = {
    'nome': '',
    'qtdAcertos': 0,
    'qtdErro': 0,
    'status': ''
}


j1 = str(input('Nome jogador n°1:\n')).strip().title()
if j1 == '':
    jogador1['nome'] = 'Jogador 1'
else:
    jogador1['nome'] = j1
    
j2= str(input('Nome jogador n°2:\n')).strip().title()
if j2 == '':
    jogador2['nome'] = 'Jogador 2'
else:
    jogador2['nome'] = j2
os.system('clear') or None

print('\n-----Iniciado o jogo-----')
print(f'Jogador n1° {jogador1["nome"]} \nJogador n2° {jogador2["nome"]}')
sleep(6)
os.system('clear') or None

for x in range(1, partidas+1):
    while True:
        perguntaEscolhida = escolherPerguntas(perguntas, qtdPerguntas)

        if perguntaEscolhida in pgAntiga:
            perguntaEscolhida = escolherPerguntas(perguntas, qtdPerguntas)
        else:
            pgAntiga.append(perguntaEscolhida)
            break
            
    
    if x % 2 == 0:
        mostrarPegunta(perguntaEscolhida, x, jogador1['nome'])
        if verificarOpcao(perguntaEscolhida):
            jogador1['qtdAcertos'] += 1
        else:
            jogador1['qtdErro'] += 1
        sleep(2)
        os.system('clear') or None
    else:
        mostrarPegunta(perguntaEscolhida, x, jogador2['nome'])
        if verificarOpcao(perguntaEscolhida):
            jogador2['qtdAcertos'] += 1
        else:
            jogador2['qtdErro'] += 1
        sleep(2)
        os.system('clear') or None
  
verificarVitoria(jogador1, jogador2)  
        
mostrarJogadores(jogador1)
print()
mostrarJogadores(jogador2)