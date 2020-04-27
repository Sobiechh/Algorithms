import heapq
from collections import defaultdict


def koduj(frequency):
    stos = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
    heapq.heapify(stos)
    while len(stos) > 1:
        low = heapq.heappop(stos)
        high = heapq.heappop(stos)
        for para in low[1:]:
            para[1] = "0" + para[1]
        for para in high[1:]:
            para[1] = "1" + para[1]
        heapq.heappush(stos, [low[0] + high[0]] + low[1:] + high[1:])
    return sorted(heapq.heappop(stos)[1:], key=lambda p: (len(p[-1]), p))


dane = "Uwielbiam przedmiot Algorytmy i Struktury Danych"
czestotliwosc = defaultdict(int)
for symbol in dane:
    czestotliwosc[symbol] += 1


huff = koduj(czestotliwosc)
print("Symbol".ljust(10) + "Waga".ljust(10) + "Huffman Kod")
for p in huff:
    print(p[0].ljust(10) + str(czestotliwosc[p[0]]).ljust(10) + p[1])
