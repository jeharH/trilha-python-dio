class Bicicleta:
    def __init__(self, cor, modelo, ano, valor): # construtor
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1
        # self representa a instância do objeto
        
    def buzinar(self):
        print('Plim plim')

    def parar(self):
        print('Parando bicicleta...')
        print('Bicicleta parada!')

    def correr(self):
        print('Vrummmm...')

    def trocar_marcha(self, nro_marcha):
        print('Trocando marcha!!')

        def _trocar_marcha():
            if nro_marcha > self.marcha:
                print('Marcha trocada!')
            else:
                print('Não foi possível trocar a marcha!')


    # def __str__(self): # detalha oq está dentro da instancia
    #     return f'Bicicleta: {self.cor}, {self.modelo}, {self.cor}, {self.ano}'

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}" # atributo que mostra o NOME da CLASSE

# b1 = Bicicleta('vermelha', 'ca loi', 2022, 600)
# b1.buzinar()
# b1.correr()
# b1.parar()
# print(b1.cor, b1.modelo, b1.valor, b1.ano)
  

b2 = Bicicleta('verde', 'Monark', 2000, 189)
b2.buzinar() # Bicicleta.buzinar(b2)
print(b2.cor)
print(b2)
b2.trocar_marcha()