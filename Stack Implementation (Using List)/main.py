"""Implement stack by using list structure"""
from collections import deque
class Empty(Exception):
    pass


def length(stack):
    return len(stack)


def is_empty(stack):
    return len(stack) == 0


def push_stack(stack, e):
    stack.append(e)


def top_stack(stack):
    return stack[-1]


def pop_stack(stack):
    if is_empty(stack):
        raise Empty('Stack is empty !!!')
    else:
        answer = stack[-1]
        stack.pop()
        return answer


if __name__ == '__main__':
    stack = []
    for i in range(6):
        push_stack(stack, i)
    print('Length of stack:', length(stack))
    print('Stack is empty:', is_empty(stack))
    print('Top of stack:', top_stack(stack))
    for i in range(6):
        print(pop_stack(stack), end=' ')
    print()
    """Implement stack using deque structure"""
    s = deque()
    for c in 'abc':
        s.append(c)
    while len(s) != 0:
        print(s.pop(), end=' ')



