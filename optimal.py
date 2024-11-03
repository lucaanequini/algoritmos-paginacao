import sys

def optimal(page_frames, pages):
    memory = [-1] * page_frames
    hits, misses = 0, 0

    for i, page in enumerate(pages):
        if page in memory:
            hits += 1
            print(f"page: {page}\n{memory} <- (hit)")
        else:
            misses += 1
            if -1 in memory:
                memory[memory.index(-1)] = page
            else:
                farthest, index = -1, -1
                for j in range(page_frames):
                    try:
                        pos = pages[i + 1:].index(memory[j])
                    except ValueError:
                        pos = float('inf')
                    if pos > farthest:
                        farthest, index = pos, j
                memory[index] = page
            print(f"page: {page}\n{memory} <- (miss)")

    print(f"Hit rate ({hits}/{len(pages)}): {hits / len(pages):.2f}")
    print(f"Miss rate ({misses}/{len(pages)}): {misses / len(pages):.2f}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python optimal.py <page_frames> <page_sequence>")
    else:
        page_frames = int(sys.argv[1])
        pages = list(map(int, sys.argv[2].split(',')))
        optimal(page_frames, pages)
