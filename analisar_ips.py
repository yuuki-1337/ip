enderecos = int(input("Quantos endereços IP deseja inserir?: "))
lista = []
for i in range(enderecos):
    ip = input("Insira o endereço IP do dispositivo. Ex(192.168.1.1): ")
    if not "." in ip[3] or not "." in ip[7] or not "." in ip[9]:
        print("Formato Inválido")
    pontos = ip.count(".")
    while pontos != 3:
        print("ENTRADA INVÁLIDA\n")
        ip = input("Insira o endereço IP do dispositivo. Ex(192.168.1.1): ")
        pontos = ip.count(".")

    lista.append(ip)

print(lista)
#Utilizei a variavel endereços para verificar quantas vezes o usuario quer colocar os endereços. Laço para realizar a repetição. Verificaçao de formato, verificando se os pontos estão nos locais corretos
#Verificando se há a quantidade ideal de pontos no endereço IP
#Laço para verificar se é válido ou não