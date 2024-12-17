class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        if not tokens:
            return 0
        for i in range(0,len(tokens)):
            if tokens[i] in "+-/*":
                if tokens[i] == '+':
                    stack.append(stack.pop() + stack.pop())
                elif tokens[i] == '-':
                    a,b = stack.pop(), stack.pop()
                    stack.append(b-a)
                elif tokens[i] == '*':
                    stack.append(stack.pop() * stack.pop())
                else: # '/'
                    a,b = stack.pop(), stack.pop()
                    stack.append(int(b/a))
            else:
                stack.append(int(tokens[i]))
        return stack[0]