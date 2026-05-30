# take in string as list
# compare peek() and items[-1]
# pop() and del(items[-1])
# keep going

class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self, item):
        return self.items.pop()

    def match_symbols(symbol_str):
        symbol_pairs = {
            '(': ')',
            '[': ']',
            '{': '}',
        }

        openers = symbol_pairs.keys()
        my_stack = Stack()

        index = 0
        while index < len(symbol_str):
            symbol = symbol_str[index]