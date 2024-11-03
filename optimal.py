import sys

def optimal(page_frames, pages):
    # Inicializa a memória com espaços vazios
    memory = [-1] * page_frames
    hits, misses = 0, 0

    # Itera sobre cada página da sequência
    for i, page in enumerate(pages):
        if page in memory:
            # Se a página já está na memória, é um acerto (hit)
            hits += 1
            print(f"page: {page}\n{memory} <- (hit)")
        else:
            # Se a página não está na memória, é uma falha (miss)
            misses += 1
            if -1 in memory:
                # Se ainda há espaço, adiciona a página na memória
                memory[memory.index(-1)] = page
            else:
                # Se a memória está cheia, usa a lógica Optimal para substituição
                farthest, index = -1, -1
                # Verifica o uso futuro de cada página na memória
                for j in range(page_frames):
                    try:
                        # Calcula a distância da próxima aparição
                        pos = pages[i + 1:].index(memory[j])
                    except ValueError:
                        # Se a página não aparece mais, usa para substituição
                        pos = float('inf')
                    if pos > farthest:
                        farthest, index = pos, j
                # Substitui a página que não será usada em breve
                memory[index] = page
            print(f"page: {page}\n{memory} <- (miss)")

    # Exibe as taxas de acertos e falhas
    print(f"Hit rate ({hits}/{len(pages)}): {hits / len(pages):.2f}")
    print(f"Miss rate ({misses}/{len(pages)}): {misses / len(pages):.2f}")

# Executa o script com parâmetros de entrada via linha de comando
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python optimal.py <page_frames> <page_sequence>")
    else:
        page_frames = int(sys.argv[1])
        pages = list(map(int, sys.argv[2].split(',')))
        optimal(page_frames, pages)
