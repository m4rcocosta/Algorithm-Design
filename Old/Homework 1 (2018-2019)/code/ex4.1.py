def minCost(costs, C, S, s):

    # Determine time istants
    T = 0
    time = 0
    for cost in costs:
        if cost[0] != time:
            time = cost[0]
            T += 1
    
    # Initialize outsourcing cost matrix
    outsourcing = [[0 for x in range(0, T+1)] for x in range(0, 2)]

    # Initialize total cost matrix
    tc = [[0 for x in range(0, T+1)] for x in range(0, 2)]

    #Construck outsourcing cost matrix
    time = 0
    i = 0
    j = 0
    for cost in costs:
        if j == 0:
            outsourcing[0][i] = cost[0]
            outsourcing[1][i] = cost[1]
            time = cost[0]
            j += 1
        else:
            if time == cost[0]:
                outsourcing[1][i] += cost[1]
            else:
                i += 1
                outsourcing[0][i] = cost[0]
                outsourcing[1][i] = cost[1]
                time = cost[0]
    
    # Initialize first column of total cost matrix 
    tc[0][0] = s + C
    tc[1][0] = outsourcing[1][0]
  
    # Construct rest of the total cost matrix 
    for i in range(1, T):
        tc[0][i] = min(tc[0][i-1] + (outsourcing[0][i] - outsourcing[0][i-1]) * s, tc[1][i-1] + C + s)
        tc[1][i] = min(tc[0][i-1] + S + outsourcing[1][i], tc[1][i-1] + outsourcing[1][i])
    
    # Return the minimum cost
    return min(tc[0][T-1], tc[1][T-1])

# Driver program to test above functions
costs = [[1, 1], [3, 2], [4, 1]]
C = 2
S = 3
s = 2
print("="*50)
print("Testing with the following input:\nCosts:",costs,"\nC:",C,"\nS:",S,"\ns:",s)
print("Minimum cost:",minCost(costs, C, S, s))