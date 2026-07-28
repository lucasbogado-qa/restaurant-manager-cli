class Restaurante:
    def __init__(self, nome, categoria):
        self.nome  = nome
        self.categoria = categoria
        self.ativo = False  
 
restaurante_praca = Restaurante('Praça', 'Comida Arabe')
restaurante_pizza = Restaurante('Pizza', 'Comida Italiana')
restaurantes = []
restaurantes.append(restaurante_praca)
print(vars(restaurante_praca))
print(vars(restaurante_pizza))