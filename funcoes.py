import random
import os
import string
import re
import requests
import unidecode

class colors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def lista_palavras():
    response = requests.get(
        "https://meaningpedia.com/5-letter-words?show=all")
    pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
    word_list = pattern.findall(response.text)
    lista_en=[]
    for i in word_list: lista_en.append(i.upper())

    response = requests.get(
        "https://www.dicio.com.br/palavras-com-cinco-letras/")
    pattern = re.compile(r'/>(\w+)<br')
    word_list = pattern.findall(response.text)
    lista_pt=[]
    for i in word_list: lista_pt.append((unidecode.unidecode(i.upper())))

    return lista_en, lista_pt


def selecao_teclas():
    teclas_corretas = []
    teclas_quase = []
    teclas_erradas = []

    for chute in chutes:
        for n in range(5):

            if chute[n] in letras_sorteadas:
                if chute[n]==letras_sorteadas[n]:
                    teclas_corretas.append(chute[n])
                teclas_quase.append(chute[n])
            else:
                teclas_erradas.append(chute[n])

    return teclas_corretas, teclas_quase, teclas_erradas


def print_chutes():
    contador = 1

    print("-"*10+"CHUTES"+"-"*10)

    for chute in chutes:

        letras=[]
        for n in range(5):

            if chute[n]==palavra_sorteada[n]:
                letras.append(f"{colors.GREEN}{chute[n]}{colors.END}")
            elif chute[n] in letras_sorteadas:
                letras.append(f"{colors.YELLOW}{chute[n]}{colors.END}")
            else:
                letras.append(chute[n])

        print(f"{contador}. [{letras[0]}][{letras[1]}][{letras[2]}][{letras[3]}][{letras[4]}]")
        contador+=1

    print("-"*26+"")


def teclado():
    teclas = list(string.ascii_uppercase)
    teclas_corretas, teclas_quase, teclas_erradas = selecao_teclas()
    
    novas_teclas = []
    for t in teclas:
        if t in teclas_quase:
            if t in teclas_corretas:
                t = f"{colors.GREEN}{t}{colors.END}"
            else:
                t = f"{colors.YELLOW}{t}{colors.END}"
            novas_teclas.append(t)
        elif t in teclas_erradas:
            t = f"{colors.FAIL}{t}{colors.END}"
            novas_teclas.append(t)
        else:
            novas_teclas.append(t)

    return novas_teclas


def input_do_jogador():
    i = input("> ").upper()
    while len(i)!=5 or i not in lista:
        if len(i)!=5:
            print(f"{colors.YELLOW}*Palavra precisa ter 5 letras*{colors.END}")
        else:
            print(f"{colors.YELLOW}*Palavra inexistente*{colors.END}")
        i = input("> ").upper()
    return i


chutes=[]

lista = lista_palavras()[1]
tentativas_max = 6
tentativa_inicio = 1

palavra_sorteada = random.choice(lista)
letras_sorteadas = list(palavra_sorteada)