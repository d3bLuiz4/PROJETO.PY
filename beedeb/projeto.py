class cliente:
    def __init__ (self, nome: str, telefone: str) :
        self.nome = nome
        self.telefone = telefone     
    def exibir_detalhes(nome, telefone):
        print(f'{nome} - {telefone}')