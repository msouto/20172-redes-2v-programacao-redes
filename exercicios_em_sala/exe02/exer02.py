import sys

def valida_data(data):
    data= data.split('/')
    if len(data) == 1 :
        print('Digite a data separada com "/" (barras)')

    if int(data[0]) < 1 and int(data[0] > 31:
        print('Insira um dia de 1 a 31')

    if int(data[1]) < 1 and int(data[1]) > 12:
        print('Insira um mês de 1 a 12')
    if len(data[2]) != 4:

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
        if valida_data(sys.argv[1]) == "ok"
            print(data_por_extenso(sys.argv[1]))
     
        

if __name__ == '__main__':
  main()


#Exercício 02
#======================================================
#Modifique o código anterior, incluindo um método que teste se a data passada como argumento está dentro de algumas regras esperadas:
##Dia do mês entre 1 e 31
##Mês entre 1 e 12
##Ano com quatro dígitos numéricos
##Separador como “/“
