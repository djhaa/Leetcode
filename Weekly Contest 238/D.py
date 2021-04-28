class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()
        if restrictions[-1][0] != n:
            restrictions.append([n, n-1])
        m = len(restrictions)
        left = [float('INF') for _ in range(m)]
        right = [float('INF') for _ in range(m)]
        left[0] = restrictions[0][1]
        right[m-1] = restrictions[m-1][1]
        for i in range(1, m):
            left[i] = min(left[i-1] + restrictions[i][0] - restrictions[i-1][0], restrictions[i][1])
        for j in range(m-2, -1, -1):
            right[j] = min(right[j+1] + restrictions[j+1][0] - restrictions[j][0], restrictions[j][1])
        maxinum = float('-INF')
        for k in range(1, m):
            a = min(left[k], right[k])
            b = min(left[k-1], right[k-1])
            j = restrictions[k][0]
            i = restrictions[k-1][0]
            maxinum = max(maxinum, (a + b + j - i) // 2)
        return maxinum