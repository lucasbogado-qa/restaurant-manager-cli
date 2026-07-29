from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria): # init é usado sempre que você quer criar um objeto, ele é o construtor da classe
        self._nome  = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False  
        self._avaliacao = []
        Restaurante.restaurantes.append(self) # adiciona o objeto criado na lista de restaurantes

    def __str__(self):
        return f'Nome: {self._nome} / Categoria: {self.categoria} / Status: {self.ativo}'

    @classmethod
    def lista_restaurante(cls):
        for restaurante in cls.restaurantes:
            print(f'Nome: {restaurante._nome}, Categoria: {restaurante.categoria}, Status: {restaurante.ativo}')
    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
        
    @property
    def calcula_avaliacao(self):
        if not self._avaliacao: 
            return 0
        else:
            soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
            qtd_notas = len(self._avaliacao)
            media = round(soma_das_notas / qtd_notas, 1) # round arredonda os digitos
        return media