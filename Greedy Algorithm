# Walking Robort
def Robort(commands, obstacles):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    x = y = 0
    change_in_site = 0
    obstaclesSet = set(map(tuple, obstacles))
    OsDistance = 0

    for i in range(len(commands)):
        if commands[i] == -2:
            change_in_site = (change_in_site-1) % 4
        elif commands[i] == -1:
            change_in_site = (change_in_site+1) % 4
        else:
            for i in range(commands[i]):
                if (x+dx[change_in_site],y+dy[change_in_site]) not in obstaclesSet:
                    x += dx[change_in_site]
                    y += dy[change_in_site]
                    OsDistance = max(OsDistance, x**2 + y**2)

    return OsDistance
    
    
# Best time to buy stock
def maxProfit(self, prices):
    profit = 0
    for j in range(len(prices)-1):
        differ = prices[j+1]-prices[j]
        if differ > 0:
            profit += differ
        else:
            continue
    return profit
