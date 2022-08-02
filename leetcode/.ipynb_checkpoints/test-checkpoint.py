def dailyTemperatures(temperatures: list) -> list:
    stack = list()
    res = list()
    n = len(temperatures)
    for i in range(n - 1, -1, -1):
        if not stack:
            res.append(0)
        else:
            if temperatures[i] < stack[-1]:
                res.append(1)
            else:
                diff = 0
                while stack and temperatures[i] > stack[-1]:
                    stack.pop()
                    diff += 1
                # if the stack is empty after poping, then the current temperature is the highest.
                if stack:
                    res.append(diff + res[-1])
                else:
                    res.append(0)
        stack.append(temperatures[i])
    res.reverse()
    return res
