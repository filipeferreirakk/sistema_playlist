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
        print(f"Música '{titulo}' adicionada com ID {nova_musica.id}!")

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

    def tamanho(self):
        count = 0
        atual = self.cabeca
        while atual is not None:
            count += 1
            atual = atual.proximo
        return count


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


def escolher_fila(filas_humor):
    print("Escolha a fila:")
    print("  1. Relaxar")
    print("  2. Focar")
    print("  3. Animar")
    print("  4. Treinar")
    escolha = input("Opção: ").strip()

    mapa = {"1": "relaxar", "2": "focar", "3": "animar", "4": "treinar"}

    if escolha not in mapa:
        return None, None

    nome = mapa[escolha]
    return nome, filas_humor[nome]


def menu():
    print("\n" + "="*30)
    print("   SISTEMA DE PLAYLIST")
    print("="*30)
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
    print("="*30)


def main():
    biblioteca = Biblioteca()

    fila_relaxar = Fila()
    fila_focar = Fila()
    fila_animar = Fila()
    fila_treinar = Fila()
    historico = Fila()

    filas_humor = {
        "relaxar": fila_relaxar,
        "focar": fila_focar,
        "animar": fila_animar,
        "treinar": fila_treinar
    }

    while True:
        menu()
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            titulo = input("Título: ").strip()
            artista = input("Artista: ").strip()
            genero = input("Gênero: ").strip()
            bpm_input = input("BPM: ").strip()

            if not titulo or not artista or not genero:
                print("Título, artista e gênero não podem ser vazios.")
            elif not bpm_input.isdigit() or int(bpm_input) <= 0:
                print("BPM inválido! Digite um número inteiro maior que zero.")
            else:
                biblioteca.inserir(titulo, artista, genero, int(bpm_input))

        elif opcao == "2":
            id_input = input("Digite o ID da música: ").strip()
            if not id_input.isdigit():
                print("ID inválido.")
            else:
                biblioteca.remover(int(id_input))

        elif opcao == "3":
            valor = input("Digite o ID ou o título da música: ").strip()
            resultado = biblioteca.buscar(valor)
            if resultado is None:
                print("Música não encontrada.")
            else:
                print(resultado)

        elif opcao == "4":
            print("\n--- Biblioteca ---")
            biblioteca.listar()

        elif opcao == "5":
            if biblioteca.cabeca is None:
                print("Biblioteca vazia, adicione músicas primeiro.")
            else:
                fila_relaxar.__init__()
                fila_focar.__init__()
                fila_animar.__init__()
                fila_treinar.__init__()

                atual = biblioteca.cabeca
                while atual is not None:
                    m = atual.musica
                    if m.bpm <= 80:
                        fila_relaxar.enqueue(m)
                    elif m.bpm <= 120:
                        fila_focar.enqueue(m)
                    elif m.bpm <= 160:
                        fila_animar.enqueue(m)
                    else:
                        fila_treinar.enqueue(m)
                    atual = atual.proximo

                print("Filas montadas!")
                print(f"  Relaxar:  {fila_relaxar.tamanho} músicas")
                print(f"  Focar:    {fila_focar.tamanho} músicas")
                print(f"  Animar:   {fila_animar.tamanho} músicas")
                print(f"  Treinar:  {fila_treinar.tamanho} músicas")

        elif opcao == "6":
            nome, fila = escolher_fila(filas_humor)
            if nome is None:
                print("Opção inválida.")
            elif fila.vazia():
                print(f"A fila '{nome}' está vazia. Monte as filas primeiro (opção 5).")
            else:
                musica = fila.dequeue()
                print(f"\nReproduzindo: {musica}")
                historico.enqueue(musica)

        elif opcao == "7":
            nome, fila = escolher_fila(filas_humor)
            if nome is None:
                print("Opção inválida.")
            elif fila.vazia():
                print(f"A fila '{nome}' está vazia.")
            else:
                print(f"\n--- Fila: {nome} ---")
                atual = fila.inicio
                while atual is not None:
                    print(atual.musica)
                    atual = atual.proximo

        elif opcao == "8":
            if historico.vazia():
                print("Nenhuma música reproduzida ainda.")
            else:
                print("\n--- Histórico ---")
                atual = historico.inicio
                while atual is not None:
                    print(atual.musica)
                    atual = atual.proximo

        elif opcao == "9":
            print("\n--- Estatísticas ---")
            print(f"Músicas na biblioteca: {biblioteca.tamanho()}")
            print(f"Fila Relaxar:  {fila_relaxar.tamanho} músicas")
            print(f"Fila Focar:    {fila_focar.tamanho} músicas")
            print(f"Fila Animar:   {fila_animar.tamanho} músicas")
            print(f"Fila Treinar:  {fila_treinar.tamanho} músicas")
            print(f"Reproduzidas:  {historico.tamanho} músicas")

        elif opcao == "10":
            print("Encerrando o sistema. Até mais!")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()