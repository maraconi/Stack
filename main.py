elem = {
    '(': ')',
    '{': '}',
    '[': ']'
}

class Stack():
    def __init__(self):
        self.myStack = []

    def isEmpty(self):
        if len(self.myStack):
            return True
        else:
            return False

    def push_element(self, new_line):
        for i in new_line:
            self.myStack.insert(0, i)

    def pop_element(self):
        if self.isEmpty():
            self.myStack.pop(0)
            return self.myStack

    def peek_element(self):
        return self.myStack[0]

    def size_element(self):
        for i in self.myStack:
            return len(i)

    def stack_program(self):
        for i in new_line:
            if i == '(' or i == '{' or i == '[':
                s.push_element(i)
            elif self.myStack and i == elem[self.myStack[0]]:
                s.pop_element()
            else:
                return 'Несбалансированно'
        return 'Cбалансированно'


if __name__ == '__main__':
    s = Stack()
    new_line = input(f'Введите строку: ')
    print(s.stack_program())

