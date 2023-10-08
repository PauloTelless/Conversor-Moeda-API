import requests
import json

link = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL' #link para fazer o cunsumo da API

requisicao = requests.get(link) #método para fazer a requisição dos dados

cotacoes = requisicao.json() #método para converter os dados em json

#conversão e filtragem de dados
valorDolar = float(cotacoes['USDBRL']['bid'])
valorEuro = float(cotacoes['EURBRL']['bid'])
valorBitCoin = float(cotacoes['BTCBRL']['bid'])

#funções para fazer as operações e declarações
def converterDolarReal():
    valor = float(input("\nDigite o valor em dólar: "))
    resultado = valor * valorDolar
    return(f"US$ {valor} em R$: {resultado:.2f}\n")

def converterEuroReal():
    valor = float(input("\nDigite o valor em euro: "))
    resultado = valor * valorEuro
    return(f"{valor} € em R$: {resultado:.2f}\n")

def converterBtcReal():
    valor = float(input("\nDigite o valor em BTC: "))
    resultado = valor * valorBitCoin
    return(f"{valor} BTC em R$: {resultado}\n")


while True:
    
    print("\tCONVERSOR DE MOEDA")
    print("CONVERTER DE DÓLAR PARA REAL  [1]")
    print("CONVERTER DE EURO  PARA REAL  [2]")
    print("CONVERTER DE BTC   PARA REAL  [3]")
    print("SAIR                          [4]")

    opcao = int(input("Digite a opcão: "))
    
    if opcao == 4:
        break
    
    if opcao == 1:
        print(converterDolarReal())

    elif opcao == 2:
        print(converterEuroReal())

    elif opcao == 3:
        print(converterBtcReal())