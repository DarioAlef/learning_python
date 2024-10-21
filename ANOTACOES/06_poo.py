class Pessoa:
    respirar = True  #atributo que não será passado aos objetos (instâncias)
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def cumprimentar(self):
        print(f'Olá, meu nome é {self.nome}! Eu tenho {self.idade} anos.')
    
#diferença entre ações e características (substantivo)
#### instância e objeto é a mesma coisa
#o 'self.' é necessário acessar os atributos (variáveis) da classe
#@staticmethod serve para que algo (como uma função) possa ser acessado sem instanciar a classe
#ou seja, sem precisar usar um objeto

class Aluno:
    def __init__(self, nome, matricula, turma):
        self.nome = nome
        self.matricula = matricula
        self.turma = turma
        
    def metodos(self):
        matricular = 'Matricular'
        cancelar_matricula = 'cancelar matricula'
        consultar_matricula = 'consultar matricula'
        
        print(f'Matricular: {matricular}\nCancelar matricula: {cancelar_matricula}\nConsultar matricula: {consultar_matricula}')

    def atributos(self):
        print(f'Nome: {self.nome}\nMatricula: {self.matricula}\nTurma: {self.turma}')
        
if __name__ == '__main__':
    aluno = Aluno('Joaquim', '123456', '1A')
    aluno.metodos()
    

           ###  HERANÇA  ###
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