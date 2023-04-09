convidados = ['Taylor', 'Beyoncé', 'Lady Gaga', 'The Weekend', 'Rihanna']
for convidado in convidados:
    print('Olá', convidado, 'você está convidado para o meu aniversário!')

    print('A', convidados[4], 'não poderá comparecer!')

    novalista = convidados[4] = 'Katy Perry'
    print('Nova lista de convidados', convidados)
    for convidado in convidados:
        print('Olá', convidado, 'compareça ao meu aniversário!')
