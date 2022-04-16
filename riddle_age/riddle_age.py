import os
from random import randint
from time import sleep

from riddle_age.utils import get_cards


class RiddleAge():
    __YES = 's'
    __NO = 'n'
    __VALID_ANWERS = [__YES, __NO]
    __POSITION = 0
    
    def __init__(self) -> None:
        self.cards = get_cards()

    def _show_rules(self) -> None:
        print(
            '##############################################################################\n'
            'Vou adivinhar sua idade ou um número que você pensou no intervalo entre 0 a 63.\n'
            'A regra é simples. Será mostrado 6 matrizes com números dispostos aleatoriamente\n'
            'e você responderá com Sim "s" ou Não "n" caso sua idade ou número que pensou\n'
            'esteja dentro da matriz. Vamos ao jogo jogo? responda com "s" ou "n" para jogar.\n'
            '##############################################################################'
        )

    def __show_card(self, card) -> None:
        print(card)
    
    def __clean_screen(self) -> None:
        os.system('clear')

    def play(self) -> None:
        self._show_rules()
        play = str(input()).lower()
        self.__clean_screen()

        if play.lower() ==  self.__YES:
            count = 0
            for card in self.cards:
                self.__show_card(card)
                answer = str(input('A idade ou o número que você pensou aparece na Matriz? "s" ou "n" '))

                while (answer.lower() not in self.__VALID_ANWERS):
                    self.__clean_screen()
                    print('OPÇÃO INVÁLIDA.\n'
                          'Responda com "s" se a idade ou o número que você pensou aparece na Matriz.\n'
                          'Responda com "n" se a idade ou o número que você pensou não aparece na Matriz.')
                    self.__show_card(card)
                    answer = str(input())
                    self.__clean_screen()
                
                if answer.lower() == self.__YES:
                    count += card[self.__POSITION][self.__POSITION]
                self.__clean_screen()
            
            print('Calculando ...\n')
            sleep(randint(1, 8))
            print('A idade ou o número que você pensou é: {}'.format(count))
        else:
            print('Tudo bem. Jogamos uma outra hora. :-)')
