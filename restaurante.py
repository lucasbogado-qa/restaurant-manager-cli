class Restaurante:
    nome  = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Comida Japonesa'
restaurante_praca.ativo = False


restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Suprema'
restaurante_pizza.categoria = 'Pizza'
restaurante_pizza.ativo = True

restaurantes = []
restaurantes.append(restaurante_praca)
print(vars(restaurante_praca))