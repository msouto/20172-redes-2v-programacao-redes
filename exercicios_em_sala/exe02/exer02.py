import sys

def data_por_extenso(texto):
    meses=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro', 'outubro','novembro','dezembro']
    data_num = texto.split('/')
    return data_num[0] + ' de ' + meses[int(data_num[1])-1] + ' de ' + data_num[2]

def main():
    if len(sys.argv) == 2:
        print(data_por_extenso(sys.argv[1]))
    else:
        print('Voce deve passar apenas um argumento com a data a ser convertida!')

if __name__ == '__main__':
    main()
