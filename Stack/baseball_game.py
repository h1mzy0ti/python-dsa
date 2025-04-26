def calPoints(self, operations: List[str]) -> int:
        res_stack = []

        for chars in operations:
            if chars == int:
                res_stack.append()
            elif chars == "C":
                res_stack.pop()
            elif chars == "D":
                res_stack.append(2*res_stack.pop())
            elif chars == "+":
                res_stack.append(res_stack.pop() +  res_stack.pop())
        return sum(res_stack)