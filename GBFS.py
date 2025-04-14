from collections import defaultdict
import heapq

def gbfs(graph,start,goal,heurestics):
    visited=set()
    queue=[]
    heapq.heappush(queue,(heurestics[start],start,[start]))

    while queue:

        h_cost,current,path=heapq.heappop(queue)

        if goal==current:
            print("->".join(path))
            return True
        
        if current is visited:
            continue

        visited.add(current)

        for neighbour in graph[current]:
            if neighbour not in visited:
                heapq.heappush(queue,(heurestics[neighbour],neighbour,path+[neighbour]))

    return False

def main():
    graph=defaultdict(list)
    heurestics={}
    graph['S']=['A','B','C']
    graph['S']=['A','B','C']
    graph['B']=['D','H']
    graph['H']=['F','G']
    graph['G']=['E']
        
    heurestics['S']=10
    heurestics['A']=9
    heurestics['B']=7
    heurestics['C']=8
    heurestics['D']=8
    heurestics['H']=6
    heurestics['F']=6
    heurestics['G']=3
    heurestics['E']=0

    while True:
        print("1. GBFS")
        print("2. Exit")

        choice=(int)(input("Enter your choice.."))

        if choice==1:
            print("GBFS Traversal")
            start=input("Enter start vertex: ")
            goal=input("Enter goal vertex: ")
            found=gbfs(graph,start,goal,heurestics)
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

        
