def solution(a, b):
    if a == b:
        return a or b
    elif a > b:
        return sum(range(b, a+1))
    elif b > a:
        return sum(range(a, b+1))