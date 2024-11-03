import sys

def fifo(page_frames, pages):
    memory = [-1] * page_frames
    queue = []
    hits, misses = 0, 0

    for page in pages:
        if page in memory:
            hits += 1
            print(f"page: {page}\n{memory} <- (hit)")
        else:
            misses += 1
            if len(queue) < page_frames:
                memory[len(queue)] = page
            else:
                old_page = queue.pop(0)
                memory[memory.index(old_page)] = page
            queue.append(page)
            print(f"page: {page}\n{memory} <- (miss)")

    print(f"Hit rate ({hits}/{len(pages)}): {hits / len(pages):.2f}")
    print(f"Miss rate ({misses}/{len(pages)}): {misses / len(pages):.2f}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python fifo.py <page_frames> <page_sequence>")
    else:
        page_frames = int(sys.argv[1])
        pages = list(map(int, sys.argv[2].split(',')))
        fifo(page_frames, pages)
