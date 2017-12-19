def is_matched(expression):
    
    left_brackets = ['{', '[', '(']
    right_brackets = ['}', ']', ')']
    matching_brackets = {'{': '}', '[': ']', '(': ')'}
    
    tmp_stack = []
    for s in expression:
        if len(tmp_stack) >= 1:
            if s in left_brackets:
                tmp_stack.append(s)
            else:
                if matching_brackets[ tmp_stack[-1] ] == s:
                    tmp_stack.pop()
                else:
                    return 0
        else:
            if s in right_brackets:
                return 0
            else:
                tmp_stack.append(s)
                
    if len(tmp_stack) >= 1:    
        return 0
    
    return 1

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
