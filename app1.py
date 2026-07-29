from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Árabe')
restaurante_pizza = Restaurante('Pizza', ' Italiano')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicano')

restaurante_praca.alternar_estado()
restaurante_praca.receber_avaliacao('Lucas',10)
restaurante_praca.receber_avaliacao('Laura',80)
restaurante_praca.receber_avaliacao('Gabriel',0)


def main():
    Restaurante.lista_restaurante()
if __name__ == '__main__':
    main()