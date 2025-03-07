class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def choose(n, k):
            return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
        row = []
        for i in range(rowIndex+1):
            row.append(choose(rowIndex,i))
        return  row
