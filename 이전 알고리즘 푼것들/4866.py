for test in range(1, int(input())+1):
    str_list = list(input())
    result = True
    stack = []
    for i in str_list:
        if i == '{':
            stack.append(i)
        elif i == '(':
            stack.append(i)
        elif i == '}':
            if stack:
                a = stack.pop()
            else:
                result = False
                break
            if a != '{':
                result = False
                break
        elif i == ')':
            if stack:
                a = stack.pop()
            else:
                result = False
                break
            if a != '(':
                result = False
                break
    if stack:
        result = False

    if result:
        print("#{} 1".format(test))
    else:
        print("#{} 0".format(test))