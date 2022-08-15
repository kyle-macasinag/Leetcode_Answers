# class Solution:
#     def kWeakestRows(self, M: List[List[int]], K: int) -> List[int]:
#         y, x = len(M), len(M[0])
#         vis, answer = [0] * y, [y]
#         for j in range(x+1):
#             for i in range(y):
#                 if not vis[i] and (j == x or not M[i][j]):
#                     answer.append(i)
#                     vis[i] = 1
#                 if len(answer) == K: return answer

class Solution:
    def kWeakestRows(self, M: List[List[int]], K: int) -> List[int]:
        y, x = len(M), len(M[0])
        vis, ans = [0] * y, []
        for j in range(x+1):
            for i in range(y):
                if not vis[i] and (j == x or not M[i][j]):
                    answer.append(i)
                    vis[i] = 1
                if len(answer) == K: return answer