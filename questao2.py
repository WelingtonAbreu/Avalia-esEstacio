def soma_imposto(custo, taxa):
    total = (custo * (taxa/100)) + custo
    print(f'O Valor total do produto foi: {total}')

valor_produto = float(input('Digite o valor do produto: '))
taxa_produto = float(input('Digite a porcentagem de taxa: '))

soma_imposto(valor_produto, taxa_produto)
