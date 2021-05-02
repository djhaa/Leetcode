class Solution:
    def splitString(self, s: str) -> bool:
        def backtrace(idx, data):
            if idx == len(s):
                return True
            for i in range(1, len(s)-idx+1):
                if int(s[idx:idx+i]) > data[-1]:
                    break
                else:
                    if data[-1] - int(s[idx:idx+i]) == 1:
                        data.append(int(s[idx:idx+i]))
                        flag = backtrace(idx+i, data)
                        if flag:
                            return True
                        data.pop()
            return False
        data = list()
        for i in range(1, len(s)):
            data.append(int(s[:i]))
            flag = backtrace(i, data)
            if flag:
                return True
            data.pop()
        return False