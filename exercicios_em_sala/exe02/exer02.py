import sys

def check_data(meses, data_num):
    if len(data_num) == 1 or int(data_num[0]) not in range(1, 32) or int(data_num[1]) not in range(1, 13) or len(data_num[2]) != 4 or not data_num[2].isnumeric():
        return "Verifique o formato da data inserida"
    else:
        return data_num[0] + ' de ' + meses[int(data_num[1])-1] + ' de ' + data_num[2]

def data_por_extenso(texto):
    meses=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro', 'outubro','novembro','dezembro']
    data_num = texto.split('/')
    return check_data(meses, data_num)

def main():
    if len(sys.argv) == 2:
        print(data_por_extenso(sys.argv[1]))
    else:
        print('Voce deve passar apenas um argumento com a data a ser convertida!')

if __name__ == '__main__':
    main()

#Exercício 02
#======================================================
#Modifique o código anterior, incluindo um método que teste se a data passada como argumento está dentro de algumas regras esperadas:
##Dia do mês entre 1 e 31
##Mês entre 1 e 12
##Ano com quatro dígitos numéricos
##Separador como “/“
