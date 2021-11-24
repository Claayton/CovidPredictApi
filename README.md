# Instruções para rodar o projeto:
## Apos fazer o clone do projeto você precisará realizar algumas configurações na sua maquina antes de rodar o projeto:

O projeto foi desenvolvido utilizando Python 3.8.10, recomendo utilizar a mesma versão,
vc pode instalar o Python [nesse link](https://www.python.org/downloads/).

*Você vai precisar também de um ambiente virtual para evitar conflitos entre versões na tua maquina, utilize o comando a seguir para instalar o **virtualenv***:
```
pip install virtualenv
```
*Agora é hora de configurar seu **Ambiente Virtual**:*
```
python3 -m venv venv 
```
*Em seguida você deverá **Ativar** esse ambiente:*
```
source venv/bin/activate - #linux
source venv/Scripts/activate - #windows
```
*Agora instale as **bibliotecas e pacotes** necessários para rodar o projeto:*
```
pip install -r requirements.txt
```
