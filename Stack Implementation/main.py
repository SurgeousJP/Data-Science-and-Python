

class Empty(Exception):
    pass


class StackArray:
    """LIFO Stack implementation using Python list as underlying storage"""
    def __init__(self):
        """Create an empty stacK"""
        self._stack = []

    def __len__(self):
        """Return the number of elements in a stack"""
        return len(self._stack)

    def is_empty(self):
        """Return true if stack is empty (no element in a stack)"""
        return len(self._stack) == 0

    def push(self, data):
        """Add the data element to the top of stack"""
        self._stack.append(data)

    def top(self):
        """Return but not remove the top element of the stack,
        Raise the exception if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty !!!')
        else:
            return self._stack[-1]

    def pop(self):
        """Return the top element and remove it from the stack"""
        if self.is_empty():
            raise Empty('Stack is empty !!!')
        else:
            return self._stack.pop()

    def printstack(self):
        for i in range(len(self._stack)):
            print(self._stack.pop(), end='')


# define a function that checks valid parentheses ()[]{}
def is_match_delimiter(expr):
    """Return true if all delimiters are properly matched, return false otherwise"""
    lefty = '([{'
    righty = ')]}'
    s = StackArray()
    for c in expr:
        if c in lefty:
            s.push(c)
        else:
            if s.is_empty():
                return False
            else:
                if righty.index(c) != lefty.index(s.pop()):
                    return False
    return s.is_empty()


def is_matched_html(raw):
    """Return True if all HTML tags are properly matched, False otherwise"""
    s = StackArray()
    j = raw.find('<')  # find first '<' character if any
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False  # invalid tag
        tag = raw[j+1:k]  # remove the '<', '>' in tag
        if not tag.startswith('/'):
            s.push(tag)  # this is an opening tag
        else:            # this is a closing tag
            if s.is_empty():  # empty stack -> false
                return False
            if tag[1:] != s.pop():  # unmatching tag -> false
                return False
        j = raw.find('<', k+1)  # find the next tag in raw
    return s.is_empty()


if __name__ == '__main__':
    # checking valid parentheses
    text1 = '((()(()){([()])}))'
    text2 = ')(()){([()])}'
    print(text1)
    print(is_match_delimiter(text1))
    print(text2)
    print(is_match_delimiter(text2))
    # checking valid tab in Html text
    text = input()
    print(is_matched_html(text))
