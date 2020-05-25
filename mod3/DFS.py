links = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []} #biblioteka polaczen grafu
visited = set() #empty set

def dfs(visited, links, top):
    if top not in visited: 
        print(top) #wyswietlenie drogi obecnej
        visited.add(top) #odwiedzone
        for element in links[top]: 
            dfs(visited, links, element) #rekurencja


#przyklady
dfs(visited, links, "C")
print('-'*80)
dfs(visited, links, "A")
print('-'*80)
dfs(visited, links, "B")
print('-'*80)
dfs(visited, links, "D")