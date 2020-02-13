class Solution:
  def numJewelsInStones(self, J: str, S: str) -> int:
    res = 0
    for x in S:
      if J.find(x) != -1:
				res += 1			
    return res