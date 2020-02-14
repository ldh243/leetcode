"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def getValue(id):
            ans = 0
            if (dic[id].subordinates):
                for i in dic[id].subordinates:
                    ans += getValue(dic[i].id)
            return dic[id].importance + ans
        dic = {}
        for i in employees:
            dic[i.id] = i
        return getValue(id)