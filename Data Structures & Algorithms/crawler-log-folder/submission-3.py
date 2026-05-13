class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = 0
        for op in logs:
            if (op == "./") or (op == "../" and stack == 0):
                stack += 0
            elif op == "../" and stack > 0:
                stack -= 1
            else:
                stack += 1
        return stack
