graph = dict()
graph["start"] = dict(a=6, b=2)

graph["a"] = dict(fin=1)
graph["b"] = dict(a=3, fin=5)
graph["fin"] = dict()

infinity = float("inf")
costs = dict(a=6, b=2, fin=infinity) # Таблица стоимости ребра

parents = dict(a="start", b="start", fin=None)

processed = list() # Массив обработанных узлов

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)


print(parents)