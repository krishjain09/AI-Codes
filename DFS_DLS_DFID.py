from collections import defaultdict

def dfs(graph,start,goal,visited=None, path=None):
    if visited is None:
        visited=set()
    if path is None:
        path=[]
    visited.add(start)
    path.append(start)
    
    if start==goal:
        print("->".join(path))
        return True
    
    for neighbour in graph[start]:
        if neighbour not in visited:
            if dfs(graph,neighbour,goal,visited,path):
                return True
    return False
                        

def dls(graph,start,goal,limit,visited=None,path=None):
    if visited is None:
        visited=set()
    if path is None:
        path=[]
    visited.add(start)
    path.append(start)
    print(start , end=" ")
    
    if start==goal:
        print("->".join(path))
        return True

    if limit<=0:
        return False

    for neighbour in graph[start]:
        if neighbour not in visited:
            if dls(graph,neighbour,goal,limit-1,visited,path):
                return True
    return False

def dfid(graph,start,goal,maxDepth):

    for depth in range(maxDepth+1):
        print(f"\nDepth :{depth}")
        found = dls(graph,start,goal,depth)
        if found==True:
            return True
        
    return False


def main():
    graph = defaultdict(list)
    while True:
        print("==========Graph Menu==========")
        print("1. Add Edge")
        print("2. DFS")
        print("3. DLS")
        print("4. DFID")
        print("5. Exit")

        choice=(int)(input("Enter your coice: "))

        if choice == 1:
            u=input("Enter starting vertex " )
            v=input("Enter ending vertex ")
            graph[u].append(v)

        elif choice == 2:
            print("DFS Traversal")
            start = input("Enter Start Veretx: ")
            goal = input("Enter Goal Vertex: ")
            found = dfs(graph,start,goal)
            if found==True:
                print("\nGoal Found!")
            else:
                print("\nGoal Not Found!")

        elif choice==3:
            print("DLS Traversal")
            start = input("Enter Start Veretx: ")
            goal = input("Enter Goal Vertex: ")
            limit=(int)(input("Enter limit: "))
            found = dls(graph,start,goal,limit)
            if found==True:
                print("\nGoal Found!")
            else:
                print("\nGoal Not Found!")

        
        elif choice==4:
            print("DFID Traversal")
            start = input("Enter Start Veretx: ")
            goal = input("Enter Goal Vertex: ")
            maxDepth=(int)(input("Enter maximum depth: "))
            found=dfid(graph,start,goal,maxDepth)
            if found==True:
                print("\nGoal Found!")
            else:
                print("\nGoal Not Found!")
            
        elif choice==5:
            print("Exiting")
            break
        else:
            print("Invalid Choice")




if __name__=="__main__":
    main()
    
            
            
            
            
            




        
