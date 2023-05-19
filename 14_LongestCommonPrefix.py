class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""
        sort_s = sorted(strs)
        f = sort_s[0]
        l = sort_s[-1]
        for i in range(min(len(f), len(l))):
          if f[i] != l[i]:
            return result
          result += f[i]
        return result