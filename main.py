km = float(input('qual a quantidade de km percorrido?: km'))
dias = int(input('por quantos dias o carro foi alugado?:'))
preçokm = 0.15 * km
preçodia = 60 * dias
preço_total = preçokm + preçodia
print('o valor total do aluguel do carro fica no valor de R$ {}'.format(preço_total))