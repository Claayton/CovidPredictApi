# Instruções para rodar o projeto:
### Após fazer o clone do projeto você precisará realizar algumas configurações na sua maquina antes de rodar o projeto:

O projeto foi desenvolvido utilizando Python 3.8.10, recomendo utilizar a mesma versão,
vc pode instalar o Python [nesse link](https://www.python.org/downloads/).

Outra coisa que preciso ressaltar é que o projeto foi desenvolvido em ambiente linux (Ubuntu 20.04) e por ainda não ter os conhecimentos necessários em Docker, ainda não pude implementá-lo, por isso Docker será o tema dos meus estudos ao fim desse projeto.

*Você vai precisar também de um ambiente virtual para evitar conflitos entre versões na tua maquina, utilize o comando a seguir para instalar o **virtualenv** caso ainda não tenha instalado*:
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

## Rodando o programa

E para rodar o programa, abrir o terminal dentro do repositório e executar o seguinte comando
```
python3 run.py
```

## Executando testes

Para executar testes, execute o seguinte comando

```
  pytest - #Rodar o testes da forma padrão
  pytest -v - #Roda os teste mostrando os detalhes caso ocorra algum erro
```
