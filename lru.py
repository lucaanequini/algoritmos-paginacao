import sys

def lru(page_frames, pages):
    # Inicializa a memória e um dicionário para rastrear uso recente
    memory = [-1] * page_frames
    hits, misses = 0, 0
    recent_usage = {}

    # Itera sobre cada página da sequência
    for i, page in enumerate(pages):
        if page in memory:
            # Se a página já está na memória, é um acerto (hit)
            hits += 1
            recent_usage[page] = i  # Atualiza o uso recente da página
            print(f"page: {page}\n{memory} <- (hit)")
        else:
            # Se a página não está na memória, é uma falha (miss)
            misses += 1
            if -1 in memory:
                # Se ainda há espaço, adiciona a página na memória
                memory[memory.index(-1)] = page
            else:
                # Encontra a página menos recentemente usada e substitui
                lru_page = min(recent_usage, key=recent_usage.get)
                memory[memory.index(lru_page)] = page
                del recent_usage[lru_page]
            # Atualiza o uso recente da página
            recent_usage[page] = i
            print(f"page: {page}\n{memory} <- (miss)")

    # Exibe as taxas de acertos e falhas
    print(f"Hit rate ({hits}/{len(pages)}): {hits / len(pages):.2f}")
    print(f"Miss rate ({misses}/{len(pages)}): {misses / len(pages):.2f}")

# Executa o script com parâmetros de entrada via linha de comando
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python lru.py <page_frames> <page_sequence>")
    else:
        page_frames = int(sys.argv[1])
        pages = list(map(int, sys.argv[2].split(',')))
        lru(page_frames, pages)
