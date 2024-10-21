#herança o conceito para se referir a uma classe dentro da outra (sub-classe)
# class Pessoa:    -->  essa é a super classe

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def show(self):
        print(f'Marca: {self.marca}\nModelo: {self.modelo}')

class Carro(Veiculo):                 #dentro do parâmetro a classe pai, indicando que 'carro' é a classe filha
    def __init__(self, marca, modelo, portas):  #'super()' é necessário para utilizar um atributo que já existe
        super().__init__(marca, modelo)         #na classe pai. Como carro é uma classe filho, a função de 
        self.portas = portas                    #inicialização '__init__()' deve conter super(). e repiclar 
                                                #os atributos da classe pai
    def show(self):
        super().show()
        print(f'Portas: {self.portas}')

   ###   Class Livro:   ###
#Atributos: titulo, autor, genero
#Métodos: emprestar, comprar, verificar_disponibilidade