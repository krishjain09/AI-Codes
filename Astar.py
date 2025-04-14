from collections import defaultdict
import heapq

def astar(graph,start,goal,heurestic):
    visited=set()
    queue=[]
    heapq.heappush(queue,(heurestic[start],0,start,[start]))

    while queue:
        f_cost,g_cost,current,path=heapq.heappop(queue)

        if current==goal:
            print("->".join(path))
            print("Total cost: " , f_cost)
            return True

        if current in visited:
            continue

        visited.add(current)

        for neighbour , edge_cost in graph[current]:
            
            if neighbour not in visited:
                new_g=g_cost +edge_cost
                f= new_g + heurestic[neighbour]
                heapq.heappush(queue,(f,new_g,neighbour,path+[neighbour]))
                
            
    return False

def main():
    
    graph=defaultdict(list)
    heurestic={}

    graph['S'] = [('A', 3), ('D', 4)]
    graph['A'] = [('S', 3), ('B', 4), ('D', 5)]
    graph['D'] = [('S', 4), ('A', 5), ('E', 2)]
    graph['B'] = [('A', 4), ('E', 5), ('C', 4)]
    graph['C'] = [('B', 4)]
    graph['E'] = [('D', 2), ('B', 5), ('F', 4)]
    graph['F'] = [('E', 4), ('G', 3.5)]
    graph['G'] = [('F', 3.5)]

    heurestic['S']=11.5
    heurestic['A']=10.1
    heurestic['B']=5.8
    heurestic['C']=3.4
    heurestic['D']=9.2
    heurestic['E']=7.1
    heurestic['F']=3.5
    heurestic['G']=0

    while True:
        print("1. A*")
        print("2. Exit")

        choice=(int)(input("Enter your choice.."))

        if choice==1:
            print("A* Traversal")
            start=input("Enter start vertex: ")
            goal=input("Enter goal vertex: ")
            found=astar(graph,start,goal,heurestic)
            if found==True:
                print("Goal Found!")
            else:
                print("Goal Not Found")
        elif choice==2:
            print("Exiting....")
            break
        else:
            print("Invalid Chocie")
    return False

if __name__=="__main__" :
    main()

                
            
