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

    def buscar(self, valor):
        atual = self.cabeca
        while atual is not None:
            m = atual.musica
            if str(m.id) == str(valor) or m.titulo.lower() == valor.lower():
                return m
            atual = atual.proximo
        return None

    def remover(self, id):
        if self.cabeca is None:
            print("Biblioteca vazia.")
            return

        if self.cabeca.musica.id == id:
            self.cabeca = self.cabeca.proximo
            print("Música removida.")
            return

        atual = self.cabeca
        while atual.proximo is not None:
            if atual.proximo.musica.id == id:
                atual.proximo = atual.proximo.proximo
                print("Música removida.")
                return
            atual = atual.proximo

        print("ID não encontrado.")


class NodoFila:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def enqueue(self, musica):
        novo = NodoFila(musica)
        if self.fim is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo
        self.tamanho += 1

    def dequeue(self):
        if self.inicio is None:
            return None
        musica = self.inicio.musica
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        self.tamanho -= 1
        return musica

    def vazia(self):
        return self.inicio is None
    

def menu():
    print("\n=== SISTEMA DE PLAYLIST ===")
    print("1. Adicionar música à biblioteca")
    print("2. Remover música da biblioteca")
    print("3. Buscar música")
    print("4. Listar biblioteca completa")
    print("5. Montar fila de reprodução por humor")
    print("6. Reproduzir próxima")
    print("7. Exibir fila de humor")
    print("8. Exibir histórico de reproduções")
    print("9. Estatísticas")
    print("10. Sair")


def main():
    biblioteca = Biblioteca()

    while True:
        menu()
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "10":
            print("Saindo...")
            break
        else:
            print("Opção ainda não implementada.")


if __name__ == "__main__":
    main()


