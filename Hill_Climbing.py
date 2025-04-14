#Hill CLimbing =>Local Search Algorithm
# Or we can Say that it is an  optimization Algorithm which chooses best option among the
# the possible solutions.

import random

def evaluate_function(expr,x):
    return eval(expr)


def hill_climb(expr,x_start,step_size,max_iterations):

    x=x_start
    for _ in range(max_iterations):
        neighbour=x+ random.choice([-step_size,+step_size])
        neighbour_val=evaluate_function(expr,neighbour)
        curr_val=evaluate_function(expr,x)

        print(f" x:{x} f(x): {curr_val}")
        print(f" Neighbour:{neighbour} f(Neighbour): {neighbour}")
        
        if neighbour_val>curr_val:
            x=neighbour
        
    return x,evaluate_function(expr,x)


expr=input("Enter any expression/function (like -x**2 +4*x): ")
print("Hill Climbing")
x_start=float(input("Enter starting val: "))
step_size=float(input("Enter step size: "))
max_iterations=int(input("Enter maximum iterations: "))

best_x,best_val=hill_climb(expr,x_start,step_size,max_iterations)

print("Best X " , best_x)
print("Best Val " , best_val)

