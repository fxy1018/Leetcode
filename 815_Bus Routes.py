'''
We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.

Example:
Input: 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation: 
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Note:

1 <= routes.length <= 500.
1 <= routes[i].length <= 500.
0 <= routes[i][j] < 10 ^ 6.

'''
#bfs
#time limited
class BusNode(object):
    def __init__(self, bus, route):
        self.bus = bus
        self.route = route
        self.connectBus = []
        
class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return(0)
        busNodes = []
        for i in range(len(routes)):
            bn = BusNode(i, set(routes[i]))
            busNodes.append(bn)
        for i in range(len(busNodes)-1):
            for j in range(i+1, len(busNodes)):
                bus1 = busNodes[i]
                bus2 = busNodes[j]
                route1 = bus1.route
                route2 = bus2.route
                if self.isInterset(route1, route2):
                    bus1.connectBus.append(bus2)
                    bus2.connectBus.append(bus1)
        #bfs to find the shorest path
        start = [ bn for bn in busNodes if S in bn.route]
        target = [ bn for bn in busNodes if T in bn.route]
        res = float('Inf')
        for node in start:
            queue = [(node, 1)]
            visited = []
            while queue:
                curr, depth = queue[0]
                queue = queue[1:]
                visited.append(curr)
                if curr in target:
                    res = min(res, depth)
                    break
                else:
                    for bn in curr.connectBus:
                        if bn not in visited and bn not in queue:
                            queue.append((bn, depth+1))
        if res == float('Inf'):
            return(-1)
        else:
            return(res)
        
    def isInterset(self, route1, route2):
        if not route1 or not route2:
            return(False)
        return(len(set(list(route1)+list(route2))) < len(route1) + len(route2))
        
   def isInterset2(self, route1, route2):
        if any(r in r2 for r in r1):
            return(True)
        else:
            return(False)
class BusNode(object):
    def __init__(self, bus, route):
        self.bus = bus
        self.route = route
        self.connectBus = []
        
class Solution:
    """
    @param routes:  a list of bus routes
    @param S: start
    @param T: destination
    @return: the least number of buses we must take to reach destination
    """
    def numBusesToDestination(self, routes, S, T):
        # Write your code here

        if S == T:
            return(0)
        busNodes = []
        for i in range(len(routes)):
            bn = BusNode(i, set(routes[i]))
            busNodes.append(bn)
        for i in range(len(busNodes)-1):
            for j in range(i+1, len(busNodes)):
                bus1 = busNodes[i]
                bus2 = busNodes[j]
                route1 = bus1.route
                route2 = bus2.route
                if self.isInterset(route1, route2):
                    bus1.connectBus.append(bus2)
                    bus2.connectBus.append(bus1)
        #bfs to find the shorest path
        start = [ bn for bn in busNodes if S in bn.route]
        target = [ bn for bn in busNodes if T in bn.route]
       
        queue = [(node, 1) for node in start]
    
        while queue:
            curr, depth = queue[0]
            queue = queue[1:]

            if curr in target:
                return(depth)
            
            for bn in curr.connectBus:
                if bn not in start:
                    start.append(bn)
                    queue.append((bn, depth+1))
        return(-1)
        
        
    def isInterset(self, route1, route2):
        if any(r in route2 for r in route1):
            return(True)
        else:
            return(False)
        
        
      
