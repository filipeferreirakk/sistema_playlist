class Musica:
    def __init__(self, id, titulo, artista, genero, bpm):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.bpm = bpm

    def __str__(self):
        return f"[{self.id}] {self.titulo} - {self.artista} | {self.genero} | {self.bpm} BPM"
    

class NodoLista:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None

class Biblioteca:
    def __init__(self):
        self.cabeca = None
        self.proximo_id = 1

    def inserir(self, titulo, artista, genero, bpm):
        nova_musica = Musica(self.proximo_id, titulo, artista, genero, bpm)
        self.proximo_id += 1
        novo_nodo = NodoLista(nova_musica)

        if self.cabeca is None:
            self.cabeca = novo_nodo
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_nodo

        print(f"Música '{titulo}' adicionada com sucesso!")

    def listar(self):
        if self.cabeca is None:
            print("Biblioteca vazia.")
            return

        atual = self.cabeca
        while atual is not None:
            print(atual.musica)
            atual = atual.proximo


