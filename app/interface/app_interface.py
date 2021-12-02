"""Interface da aplicação"""
import os
from time import sleep


class Interface():
    """Interface do usuário"""

    def cabeçalho(self):
        """Cabeçalho da aplicação"""
        print(f'\033[35m{"=" * 75}\033[m')
        print(f'\033[34m{"VIDENTE CARLINHOS":^75}\033[m')
        print(f'{"Previsões de evolução do COVID-19🦠":^74}')
        print(f'\033[35m{"=" * 75}\033[m')

    def read_data_menu(self, local):
        """
        Realiza o tratamento do input do usuário sobre quantos dias prever o covid.
        :param local: Local onde o usuário que fazer a previsão da covid.
        :return: A quantidade de dias futuros a ser previsto.
        """
        print(f'\033[35m{"=" * 75}\033[m')
        while True:
            choice = str(input(
                f'Quantos dias no futuro deseja prever a evolução do Covid-19 no {local}? '
            ))
            if choice.isnumeric():
                choice = int(choice)
                break
            print(f'\033[7;31;47m{"ERRO, DIGITE UM NÚMERO INTEIRO VÁLIDO!":^75}\033[m')
        return choice

    def main_menu(self):
        """
        Menu principal da aplicação.
        :return: A escolha do usuário.
        """

        os.system('clear')
        self.cabeçalho()
        while True:
            choice = str(input(
                "\033[32m[ 0 ]\033[m - \033[34mResetar dados do sistema\
                \n\033[32m[ 1 ]\033[m - \033[34mPrever a evolução do COVID-19 no Brasil\
                \n\033[32m[ 2 ]\033[m - \033[34mPrever a evolução do COVID-19 no Mundo\
                \n\033[mEscolha uma opção para prever a evolução por COVID-19: "
            ))
            if choice.isnumeric():
                choice = int(choice)
                if choice in (0, 1, 2, 777):
                    break
            os.system('clear')
            print(f'\033[7;31;47m{"ERRO, DIGITE UM NÚMERO INTEIRO VÁLIDO!":^75}\033[m')
            self.cabeçalho()
        return choice

    def collecting_data(self):
        """Mensagem indicando que os dados estão sendo coletados"""
        print(f'\033[35m{"Coletando dados...":^75}\033[m')
        sleep(2)
        print(f'\033[35m{"São muitos dados e isso pode demorar um pouco na primeira vez, aguarde...":^75}\033[m')

    def again(self):
        """Opção para usuário continuar utilizando o programa ou sair.
        :return: Escolha do usuário"""
        while True:
            choice = str(input(
                f'Deseja realizar outra previsão? '
            ))
            if choice[0] in 'sSnN':
                break
            print(f'\033[7;31;47m{"ERRO, DIGITE SIM OU NÃO!":^75}\033[m')
        return choice

    def farewall(self):
        """Pequena despedida quando o usuário sair do programa."""
        print(f'\033[35m{"=" * 75}\033[m')
        print(f'\033[34m{"OBRIGADO POR UTILIZAR O PROGRAMA, ATÉ MAIS :D":^75}\033[m')
        print(f'\033[35m{"=" * 75}\033[m')
