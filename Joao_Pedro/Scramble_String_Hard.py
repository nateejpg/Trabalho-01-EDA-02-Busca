class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        memo = {}

        def dfs(a, b):
            if (a, b) in memo:
                return memo[(a, b)]
            
            # caso base
            if a == b:
                memo[(a, b)] = True
                return True
            if sorted(a) != sorted(b):  # poda rápida
                memo[(a, b)] = False
                return False

            n = len(a)
            for i in range(1, n):
                # sem troca
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True
                # com troca
                if dfs(a[:i], b[-i:]) and dfs(a[i:], b[:-i]):
                    memo[(a, b)] = True
                    return True

            memo[(a, b)] = False
            return False

        return dfs(s1, s2)
