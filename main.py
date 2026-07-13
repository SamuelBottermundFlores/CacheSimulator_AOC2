import sys
from cache import Cache
from reader import read_addresses

def create_cache(config, name):
    values = config.split(":")
    nsets = int(values[0])
    block_size = int(values[1])
    associativity = int(values[2])
    return Cache(nsets, block_size, associativity, name)

def main():
    if len(sys.argv) < 3:
        print("Uso:")
        print("python main.py L1 [L2] [L3] arquivo")
        return
    
    caches = []
    file_name = sys.argv[-1]
    cache_configs = sys.argv[1:-1]
    names = ["L1", "L2", "L3"]

    for i in range(len(cache_configs)):
        cache = create_cache(cache_configs[i], names[i])
        caches.append(cache)

    addresses = read_addresses(file_name)

    for address in addresses:
        found = False
        level = 0
        while level < len(caches):
            if caches[level].access(address):
                found = True
                previous = level - 1
                while previous >= 0:
                    caches[previous].insert(address)
                    previous -= 1
                break
            level += 1

        if not found:
            level = len(caches) - 1
            while level >= 0:
                caches[level].insert(address)
                level -= 1
                
    print("\n========== RESULTADOS ==========")
    for cache in caches:
        cache.print_statistics()

if __name__ == "__main__":
    main()