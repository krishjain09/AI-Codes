from collections import defaultdict , deque
import heapq

def bfs(graph,start,goal):
    visited=set()
    queue=deque()
    visited.add(start)
    queue.append((start,[start]))

    while queue:
        current , path = queue.popleft();

        if current==goal:
            print("->".join(path))
            return True

        for neighbour, _ in graph[current]:
            if neighbour not in visited:
                queue.append((neighbour,path+[neighbour]))
                visited.add(neighbour)
    return False


#Think of an Mimimum Spanning Tree (Similar to Minimum Spanning Tree)
def ucs(graph,start,goal):
    visited=set()
    queue=[]
    heapq.heappush(queue,(0,start,[start]))

    while queue:
        cost,current,path = heapq.heappop(queue)

        if current == goal:
            print("->".join(path))
            print("Total Cost: " , cost)
            return True

        if current in visited:
            continue

        visited.add(current)
        
        for neighbour , edge_cost in graph[current]:
            if neighbour not in visited:
                heapq.heappush(queue,(cost+edge_cost,neighbour,path+[neighbour]))
    
    return False
        


def main():
    graph = defaultdict(list)

    while True:
        print("========== Graph Menu ==========")
        print("1. Add Edge")
        print("2. Display Graph")
        print("3. BFS")
        print("4. UCS")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            u = input("Enter starting vertex: ")
            v = input("Enter ending vertex: ")
            cost = int(input("Enter cost (1 if unweighted): "))
            graph[u].append((v, cost))
        elif choice == 2:
            display_graph(graph)
        elif choice == 3:
            print("BFS Traversal")
            start = input("Enter Start Vertex: ")
            goal = input("Enter Goal Vertex: ")
            found = bfs(graph, start, goal)
            if found:
                print("Goal Found!")
            else:
                print("Goal Not Found!")
        elif choice == 4:
            print("UCS Traversal")
            start = input("Enter Start Vertex: ")
            goal = input("Enter Goal Vertex: ")
            found = ucs(graph, start, goal)
            if found:
                print("Goal Found!")
            else:
                print("Goal Not Found!")
        elif choice == 5:
            print("Exiting")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
