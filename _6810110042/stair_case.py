def staircase(n, pattern='#'):
    if n <= 0:
        return ""
        
    answer = []
    for i in range(1, n + 1):
        answer.append(" " * (n - i) + pattern * i)
        
    return "\n".join(answer)
