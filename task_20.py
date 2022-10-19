def isValid(self, s):
    s = list(s)
    stack = []
    stack_length = -1
    for i in range(len(s)):
        if s[i] in ['(', '[', '{']:
            stack.append(s[i])
            stack_length += 1
        elif stack_length != -1:
            if s[i] == ')' and stack[stack_length] == '(':
                del stack[stack_length]
                stack_length -= 1
                continue
            elif s[i] == ']' and stack[stack_length] == '[':
                del stack[stack_length]
                stack_length -= 1
                continue
            elif s[i] == '}' and stack[stack_length] == '{':
                del stack[stack_length]
                stack_length -= 1
                continue
            else:
                return False
        else:
            return False
    if stack_length == -1:
        return True
    else:
        return False

print(isValid(None, '[[[][]][]'))