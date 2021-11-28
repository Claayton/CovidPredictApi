"""Interface da aplicação"""
import os

class Interface():
    """Interface do usuário"""

    def cabeçalho(self):
        """Cabeçalho do app"""
        print(f'\033[35m{"=" * 75}\033[m')
        print(f'\033[34m{"VIDENTE CARLINHOS":^75}\033[m')
        print(f'{"Previsões de evolução do COVID-19🦠":^74}')
        print(f'\033[35m{"=" * 75}\033[m')

    def read_data_menu(self, local):
        """Menu para realizar a leitura dos dados"""
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
        """Menu principal do app"""

        os.system('clear')
        self.cabeçalho()
        while True:
            choice = str(input(
                "\033[32m[ 0 ]\033[m - \033[34mPrever a evolução do COVID-19 no Brasil\
                \n\033[32m[ 1 ]\033[m - \033[34mPrever a evolução do COVID-19 no Mundo\
                \n\033[mEscolha uma opção para prever a evolução por COVID-19: "
            ))
            if choice.isnumeric():
                choice = int(choice)
                if choice in (0, 1):
                    break
            os.system('clear')
            print(f'\033[7;31;47m{"ERRO, DIGITE UM NÚMERO INTEIRO VÁLIDO!":^60}\033[m')
            self.cabeçalho()
        return choice
