class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        q = collections.deque()
        ans = 0
        for i in range(len(word)):
            if not q:
                q.append(word[i])
            else:
                if word[i] >= q[-1]:
                    q.append(word[i])
                else:
                    if len(set(q)) == 5:
                        ans = max(ans, len(q))
                    q.clear()
                    q.append(word[i])
        if len(set(q)) == 5:
            ans = max(ans, len(q))
        return ans