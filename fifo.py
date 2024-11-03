import sys

def fifo(page_frames, pages):
    # Inicializa a memória com espaços vazios e a fila para o algoritmo FIFO
    memory = [-1] * page_frames
    queue = []
    hits, misses = 0, 0

    # Itera sobre cada página da sequência
    for page in pages:
        if page in memory:
            # Se a página já está na memória, é um acerto (hit)
            hits += 1
            print(f"page: {page}\n{memory} <- (hit)")
        else:
            # Se a página não está na memória, é uma falha (miss)
            misses += 1
            if len(queue) < page_frames:
                # Se ainda há espaço, adiciona a página na memória
                memory[len(queue)] = page
            else:
                # Se não há espaço, remove a página mais antiga (FIFO)
                old_page = queue.pop(0)
                memory[memory.index(old_page)] = page
            # Adiciona a nova página à fila
            queue.append(page)
            print(f"page: {page}\n{memory} <- (miss)")

    # Exibe as taxas de acertos e falhas
    print(f"Hit rate ({hits}/{len(pages)}): {hits / len(pages):.2f}")
    print(f"Miss rate ({misses}/{len(pages)}): {misses / len(pages):.2f}")

# Executa o script com parâmetros de entrada via linha de comando
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python fifo.py <page_frames> <page_sequence>")
    else:
        page_frames = int(sys.argv[1])
        pages = list(map(int, sys.argv[2].split(',')))
        fifo(page_frames, pages)
