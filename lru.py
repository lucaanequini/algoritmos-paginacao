import sys

def lru(page_frames, pages):
    memory = [-1] * page_frames
    hits, misses = 0, 0
    recent_usage = {}

    for i, page in enumerate(pages):
        if page in memory:
            hits += 1
            recent_usage[page] = i
            print(f"page: {page}\n{memory} <- (hit)")
        else:
            misses += 1
            if -1 in memory:
                memory[memory.index(-1)] = page
            else:
                lru_page = min(recent_usage, key=recent_usage.get)
                memory[memory.index(lru_page)] = page
                del recent_usage[lru_page]
            recent_usage[page] = i
            print(f"page: {page}\n{memory} <- (miss)")

    print(f"Hit rate ({hits}/{len(pages)}): {hits / len(pages):.2f}")
    print(f"Miss rate ({misses}/{len(pages)}): {misses / len(pages):.2f}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python lru.py <page_frames> <page_sequence>")
    else:
        page_frames = int(sys.argv[1])
        pages = list(map(int, sys.argv[2].split(',')))
        lru(page_frames, pages)
