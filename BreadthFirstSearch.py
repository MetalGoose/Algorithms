from collections import deque

graph = dict()
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []



def person_is_seller(name): # Условие при ктором поиск считается оконченным
    return name[-1] == 'm'

def search(name):
    search_quaue = deque()
    print(search_quaue)
    search_quaue += graph[name]
    searched = list()
    while search_quaue:
        person = search_quaue.popleft()
        print(person)
        if not person in searched:
            if person_is_seller(person):
                print(person," is a manggo seller!!")
                return True
            search_quaue += graph[person]
            print(search_quaue)
            searched.append(person)

    return False

print(search("you"))