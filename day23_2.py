import networkx as nx

pcs = {}

with open("input.txt", "r", encoding="utf-8") as fichier:
    for line in fichier:
        conn = line.removesuffix('\n').split('-')
        for index, con in enumerate(conn):
            if con not in pcs.keys():
                pcs[con] = []
            pcs[con].append(conn[(index+1) % 2])


def bron_kerbosch(R, P, X):
    if not P and not X:
        return [R]
    cliques = []
    for node in list(P):
        cliques += bron_kerbosch(
            R.union({node}),
            P.intersection(pcs[node]),
            X.intersection(pcs[node]),
        )
        P.remove(node)
        X.add(node)
    return cliques

cliques = bron_kerbosch(set(), set(pcs), set())
best = list(max(cliques, key=len))
best.sort()

print(",".join(best))
