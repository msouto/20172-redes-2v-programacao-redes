
import sys

def valida_data(data):
    data= data.split('/')
    if len(data) == 1 :
        print('Digite a data separada com "/" (barras)')

    elif int(data[0]) not in range(1, 32):
        print('Insira um dia de 1 a 31')

    elif int(data[1]) not in range(1, 13):
        print('Insira um mês de 1 a 12')
        
    elif len(data[2]) != 4:
        print('Insira um ano com 4 digitos')
    else:
        return "ok"

def data_por_extenso(texto):
    data_num = texto.split('/')
    meses=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro', 'outubro','novembro','dezembro']
    return data_num[0] + ' de ' + meses[int(data_num[1])-1] + ' de ' + data_num[2]

def main():
    
    if len(sys.argv) == 1:
        print('Você não passou nenhum argumento!')
    elif len(sys.argv) > 2:
        print('Voce deve passar apenas um argumento com a data a ser convertida!')
    else:
        if valida_data(sys.argv[1]) == "ok":
            print(data_por_extenso(sys.argv[1]))
     
        

if __name__ == '__main__':
  main()
