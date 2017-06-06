teste = "evento4=5487.ifadiof=aio=ejsapo.jdpdp.jofevento1=5432.fofsnofdpsfpifp=ifnspfsonf.sevento3=9999.fspnofsp.nisfpifsd=evento2=0001."

lista_Eventos_Reciclados = [] #lista que irá reciclar apenas os itens iniciados por evento

lista_Eventos_Reciclados = teste.split("evento") #atribuo apenas os eventos para a lista

del(lista_Eventos_Reciclados[0]) #removo o primeiro elemento pois sempre será inútil (ou vazio ou caracteres aleatórios)

lista_Eventos_Reciclados.sort() #ordeno os eventos

lista_Eventos_validos = {} #dicionário que irá armazenar apenas os eventos com a sintaxe válida
#for responsável por analisar se o evento é válido, se sim, armazenar no dicionário
for codigo, item in enumerate(lista_Eventos_Reciclados): #percorro os eventos
    if item[0].isnumeric() and item[1] == '=':
        if item[2:6].isnumeric(): #se for um valor de evento válido
            evento = {item[0] : item[2:6]} #defino a chave com o número do evento e o valor em seguida
            lista_Eventos_validos.update(evento) #insiro um novo evento no dicionário

del(lista_Eventos_Reciclados) #libero memória pois não utilizarei mais a lista reciclada.

#imprimo todos os eventos
print("Todos os eventos registrados:")
for codigo in lista_Eventos_validos:
    print("Evento " + codigo + " = " + lista_Eventos_validos[codigo])

#imprimo todos os eventos com valores inferiores a 6000
print("Todos os eventos registrados com valor inferior a 6000:")
for codigo in lista_Eventos_validos:
    if (int(lista_Eventos_validos[codigo]) < 6000):
        print("Evento " + codigo + " = " + lista_Eventos_validos[codigo])

#imprimo apenas se o evento for 0001
for codigo in lista_Eventos_validos:
    if (lista_Eventos_validos[codigo] == "0001"):
        print("Vou entrar no QA")
    else:
        print("!")