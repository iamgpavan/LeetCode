class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(len(digits) == 0):
            return []
        hashmap = {"2":["a","b","c"],
                   "3":["d","e","f"],
                   "4":["g","h","i"],
                   "5":["j","k","l"],
                   "6":["m","n","o"],
                   "7":["p","q","r","s"],
                   "8":["t","u","v"],
                   "9":["w","x","y","z"]}
        ans = [*hashmap[digits[0]]]
        for i in range(1,len(digits)):
            s = []
            for j in ans:
                for k in hashmap[digits[i]]:
                    s.append(j+k)
            ans = s
        return ans