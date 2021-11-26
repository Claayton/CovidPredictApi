"""Interface da aplicação"""
import os

class Interface():
    """Interface do usuário"""

    def cabeçalho(self):
        """Cabeçalho do app"""
        print(f'\033[35m{"=" * 60}\033[m')
        print(f'\033[34m{"VIDENTE CARLINHOS":^60}\033[m')
        print(f'{"Previsões de evolução do COVID-19🦠":^59}')
        print(f'\033[35m{"=" * 60}\033[m')

    # def read_data_menu(self):
    #     """Menu para realizar a leitura dos dados"""

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
