# aula_proway

###### CONVENCOES DO PYTHON PARA NOMENCLATURAS:

classes 
	
	deve ser usado CamelCase ex: MinhaClasse

variaveis 
	
	deve ser usado _, ex: minha_variavel

constantes 

	deve ser escrita totalmente em letra maiuscula, ex: CONSTANTE

funções 
	
	deve ser usado _, ex: minha_funcao():


###### ORIENTACAO A OBJETOS:

1 - abstração

	pode ser considerado abstrair (tirar o que nao é necessario) em uma classe.
	ao criar uma classe, criar um modelo 100% abstrato de algo (Ex: Veiculo é 
	um conceito, um carro, uma moto ou um onibus por exemplo são algo do 
	mundo real).


2 - encapsulamento

	é pegar algo na classe e deixar mais seguro (niveis de segurança), 
	no python tudo é publico, porém podemos fazer um pseudo encapsulamento 
	usando "__" (ex: __name), os dois underlines funcionam para avisar os 
	desenvolvedores para não mexer no valor fora das classes.

	__ 2 underlines = privado (apenas na classe)
	_ 1 underline = protegido (apenas na clsse e herdeiras).


3 - herança

	classe que herda os atributos da classe mãe.


4 - poliformismo
	
	mudar algo que a classe filha recebeu da classe principal (mae).


###### EXEMPLO DE ORIENTACAO A OBJETOS:

````
#SUPERCLASSE
class Animais: 
	rabo = True
	patas = 0
	ordem = ""


class Gato(Animais):

	patas = 4
	ordem = "Mamalia"


animal = Gato()
print(animal.patas)
````


