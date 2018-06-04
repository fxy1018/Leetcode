'''

Give the Employee Name, Manager Name, Position, Year Hired as the relationships of the workers, output the Corporate member organization chart.

Example
Give relationship=[["Karl","Nancy","Manager","2009"],["Adam","Karl","Technician","2010"],["Bob","Karl","Technician","2012"],["Cathy","Wendy","Technician","2013"],["Nancy","NULL","CEO","2007"],["Wendy","Nancy","Manager","2012"]]
return ["Nancy (CEO) 2007","-Karl (Manager) 2009","—Adam (Technician) 2010","—Bob (Technician) 2012","-Wendy (Manager) 2012","—-Cathy (Technician) 2013"]

Explanation:
Nancy's upper level is NULL, so it is the highest level organization. There are Karl and Wendy under Nancy, Adam and Bob under Karl, and Cathy under Wendy.
Give relationship= [["Karl","Nancy","Manager","2009"],["Nancy","NULL","CEO","2007"],["Adam","Karl","Technician","2010"],["Fred","Karl","Worker","2012"], ["John","Fred","Helper","2013"]]
return ["Nancy (CEO) 2007","-Karl (Manager) 2009","--Adam (Technician) 2010","---Fred (Technician) 2012","----John (Helper) 2013"]

Explanation:
Nancy is NULL at the next level and is therefore the highest level organization. Karl has Nancy, Adam has Adam under Karl, Fred under Adam, and John under Fred.


'''

class Person(object):
    def __init__(self, relationship):
        self.name, self.manager, self.position, self.year = relationship
        self.employee = []
        self.level = None
        
class Solution:
    """
    @param relationship: the relationship
    @return: the organization chart
    """
    def getOrganization(self, relationship):
        # Write your code here
        persons = [Person(r) for r in relationship]
        root = self.buildTree(persons)
        return(self.printTree(root))
    
    def buildTree(self, persons):
        manageHash = {}
        for p in persons:
            if p.manager == "NULL":
                root = p
                root.level = 0
            else:
                manageHash[p.manager] = manageHash.get(p.manager, []) + [p]
        queue = [root]
        while queue:
            node = queue[0]
            queue = queue[1:]
            if node.name in manageHash:
                for e in manageHash[node.name]:
                    e.level = node.level+1
                node.employee = manageHash[node.name]
                queue.extend(node.employee)
        return(root)
            
    
    def printTree(self, root):
        if not root:
            return([])
        
        curr = root.level*"-" + root.name + " (" + root.position +") " + root.year
        res = [curr]
        employee = sorted(root.employee, key = lambda x: x.name)
        for e in employee:
            res.extend(self.printTree(e))
        return(res)
