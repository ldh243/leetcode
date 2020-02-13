class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        for i in range(1, n + 1):
            temp = ''
            if not (int(i) % 3):
                temp = 'Fizz'
            if not (int(i) % 5):
                temp += "Buzz"
            if not temp:
                temp = str(i)
            arr.append(temp)
        return arr
