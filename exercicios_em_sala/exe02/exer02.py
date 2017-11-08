import sys

def data_por_extenso(texto):
    print (texto)
    meses=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro', 'outubro','novembro','dezembro']
    data_num = texto.split('/')
    return data_num[0] + ' de ' + meses[int(data_num[1])-1] + ' de ' + data_num[2]

def verificacao(texto):
    sep = texto.split("/")
    status = "Data invalida"
    if int(sep[0]) >= 1 and int(sep[0]) <= 31:
        if int(sep[1]) >= 1 and int(sep[1]) <= 12:
            if len(sep[2]) == 4:
                status = "OK"
            else:
                status = "Data invalida"
    return status
def main():
    if len(sys.argv) == 2 and verificacao(sys.argv[1]) == "OK":
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
