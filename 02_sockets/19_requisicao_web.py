#simplificar a forma de escrever uma requisicao HTTP
import requests
#manipular a estrutura JSON
import json

def geocode(address):
    parameters = {'address': address, 'sensor':'false'}
    base = 'http://maps.googleapis.com/maps/api/geocode/json'
    #escrevi uma requisção HTTP do tipo GET
    response = requests.get(base, params=parameters)
    resposta = response.json()
    print(resposta['results'][0]['geometry']['location'])

if __name__=='__main__':
    #codígo somente será executado, se o programa estiver em
    #execução como script.
    geocode('Av. Senador Salgado Filho, 1559, Natal, RN')
