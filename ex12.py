valorinteiro=float(input('Digite o valor do seu produto: R$'))
valordodesconto=float(valorinteiro*5/100)
valortotalproduto=valorinteiro-valordodesconto
print('O valor do seu produto com 5% de desconto é R$ {}'.format(valortotalproduto))