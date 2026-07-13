import random

class CacheLine:
    def __init__(self):
        self.valid = False
        self.tag = None

class Cache:
    def __init__(self, nsets, block_size, associativity, name):

        self.name = name
        self.nsets = nsets
        self.block_size = block_size
        self.associativity = associativity
        self.accesses = 0
        self.hits = 0
        self.misses = 0
        self.compulsory_misses = 0
        self.capacity_conflict_misses = 0
        self.block_seen = []
        self.sets = []

        for i in range(nsets):
            cache_set = []
            for j in range(associativity):
                cache_set.append(CacheLine())
            self.sets.append(cache_set)

    # descobre em qual bloco o endereço esta
    def calculate_block(self, address):
        return address // self.block_size

    # descobre o conjunto
    def calculate_index(self, address):
        block = self.calculate_block(address)
        return block % self.nsets

    # descobre a tag
    def calculate_tag(self, address):
        block = self.calculate_block(address)
        return block // self.nsets
    
    def is_first_access(self, block):
        for saved_block in self.block_seen:
            if saved_block == block:
                return False
        self.block_seen.append(block)
        return True

    # verifica se o bloco esta na cache
    def access(self, address):
        self.accesses += 1
        index = self.calculate_index(address)
        tag = self.calculate_tag(address)
        cache_set = self.sets[index]

        # procura pelo bloco na cache
        for line in cache_set:
            if line.valid and line.tag == tag:
                self.hits += 1
                return True
            
        # se chegou aqui deu um miss
        self.misses += 1
        block = self.calculate_block(address)
        if self.is_first_access(block):
            self.compulsory_misses += 1
        else:
            self.capacity_conflict_misses += 1
        return False

    # insere um bloco na cache
    def insert(self, address):
        index = self.calculate_index(address)
        tag = self.calculate_tag(address)
        cache_set = self.sets[index]

        # verifica se o bloco ja esta na cache
        for line in cache_set:
            if line.valid and line.tag == tag:
                return

        # procura uma linha livre
        for line in cache_set:
            if not line.valid:
                line.valid = True
                line.tag = tag
                return

        # se todas ocupadas dai substitui randomicamente
        position = random.randint(0, self.associativity - 1)
        cache_set[position].tag = tag
        cache_set[position].valid = True

    def hit_rate(self):
        if self.accesses == 0:
            return 0
        return (self.hits / self.accesses) * 100

    def miss_rate(self):
        if self.accesses == 0:
            return 0
        return (self.misses / self.accesses) * 100

    def print_statistics(self):

        print(f"\n===== {self.name} =====")
        print(f"Acessos : {self.accesses}")
        print(f"Hits    : {self.hits}")
        print(f"Misses  : {self.misses}")
        print(f"Misses compulsórios         : {self.compulsory_misses}")
        print(f"Misses capacidade/conflito  : {self.capacity_conflict_misses}")
        print(f"Hit Rate : {self.hit_rate():.2f}%")
        print(f"Miss Rate: {self.miss_rate():.2f}%")