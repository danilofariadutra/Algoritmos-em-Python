from bs4 import BeautifulSoup
import requests
from random import randint as rd
from hangman import *


def get_word():
    global rd_word, guess_list, wrong_letters
    # Cria lista para guardar os chutes errados
    wrong_letters = list()
    # Cria a lista para guardar os chutes corretos
    guess_list = list()
    word_list = requests.get(
        'https://www.palabrasaleatorias.com/palavras-aleatorias.php?fs=10')

    word_list = BeautifulSoup(word_list.content, 'html.parser')
    word_list.prettify()

    words = list()
    count = 0
    # Pega todos as 10 palavras contidas na tag DIV dentro da tabela TD, formata, e as coloca em uma lista
    for word in word_list.find_all(
            'div', attrs={'style': 'font-size:3em; color:#6200C5;'}):
        words.append(str(word))
        if '<' in words[count]:
            words[count] = str(words[count][words[count].index('>') + 1:])
            if '<' in words[count]:
                words[count] = str(words[count][:words[count].index('<')])
                if '\r\n' in words[count]:
                    words[count] = str(
                        words[count][words[count].index('\n') + 1:])
        count += 1

    # Sorteia uma das 10 palavras buscadas no site
    rd_word = words[rd(0, 9)]
    # Formata para letra minúscula
    rd_word = rd_word.lower()

    for blank in range(len(rd_word)):
        guess_list.append('_')


def play_again():
    while True:
        play = input(
            'Deseja jogar outra vez? Digite [S para SIM ou N para NÃO]: ')

        if play.isalpha():
            if play[0].upper() == 'S':
                game()
            elif play[0].upper() == 'N':
                print('Até uma próxima!')
                while True:
                    pass


def game():
    get_word()
    error = 0
    print(f'A palavra secreta contém {len(rd_word)} letras. Boa sorte!')
    while True:
        if error == 7:
            print(f'Que pena, você perdeu. A palavra era: {rd_word}')
            play_again()

        guess = input('Qual a letra? ')

        if guess.isalpha():
            if guess in rd_word and guess not in guess_list:
                print('Acertou, miseravi. Letras corretas: ', end='')
                count = 0
                for letter in rd_word:
                    if guess == letter:
                        guess_list[count] = letter
                    count += 1
                print(guess_list)
            elif guess in guess_list or guess in wrong_letters:
                if guess in guess_list:
                    print('Você já chutou esta letra. Letras corretas: ', end='')
                    print(guess_list)
                elif guess in wrong_letters:
                    print('Você já chutou esta letra. Letras incorretas: ', end='')
                    print(wrong_letters)
            elif guess not in rd_word:
                print('Você errou a letra. Letras incorretas: ', end='')
                wrong_letters.append(guess)
                print(wrong_letters)
                print(hangman[error])
                error += 1

            if len(guess_list) == len(rd_word) and '_' not in guess_list:
                print(winner[0])
                print(f'Parabéns! Você venceu! A palavra era: {rd_word}')
                play_again()
        else:
            print(f'{guess} Caractere inválido. Digite somente letras')


game()
# TODO: Limpar variaveis
