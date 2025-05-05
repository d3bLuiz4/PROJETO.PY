#modelando cliente 

class cliente:
    def __init__ (self, nome: str, telefone: str) :
        self.nome = nome
        self.telefone = telefone     
    def exibir_detalhes(nome, telefone):
        print(f'{nome} - {telefone}')


#criando o cardápio e simulando pedidos

cardapio_lanchonete = [ItemCardapio('Comidas:'),('\nPão de queijo', 2,50), ('Croissant', 5,00), ('Mini Bolo Red Velvet', 6,00),
('\nBebidas:'), ('\nCappuccino', 3,00), ('Café com ou sem adição de leite'4,00 + 1,00), 
('Suco Natural de: Laranja, Morango ou Melancia', 6,00)]