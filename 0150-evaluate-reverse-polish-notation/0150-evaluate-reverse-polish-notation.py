class Solution:
    def evalRPN(self, s: List[str]) -> int:
        ops = {"+" : add, "-" : sub, "*" : mul, "/" : truediv}
        for t in s[:] : s.append(int(ops[t](s.pop(-2),s.pop(-1)) if t in ops else t))
        return s[-1]