class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = {}
        ans = {}
        for i, val in enumerate(list1):
            dic[val] = i
        for i, val in enumerate(list2):
            if val not in dic: continue
            temp = i + dic[val]
            if temp in ans:
                ans[temp].append(val)
            else: ans[temp] = [val]
        return ans[min(ans.keys())]