#<-------------------------------------------------1------------------------------------------------------>

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def reverse_words(sentence):
    stack = Stack()
    word = ""

    for char in sentence:
        if char != " ":
            word += char
        else:
            stack.push(word)
            word = ""
    
    stack.push(word)

    reversed_sentence = ""
    while not stack.is_empty():
        reversed_sentence += stack.pop() + " "

    return reversed_sentence.strip()

# Example usage:
input_sentence = "I am from University of Engineering and Technology Lahore"
reversed_sentence = reverse_words(input_sentence)
print(reversed_sentence)

#<-------------------------------------------------2------------------------------------------------------>
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def calculate_postfix(expression):
    stack = Stack()
    operators = ['+', '-', '*', '/', '%']
    for token in expression:
        if token.isdigit():
            stack.push(int(token))
        elif token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            elif token == '%':
                result = operand1 % operand2
            stack.push(result)
        elif token == '?':
            print(stack)
        elif token == '^':
            print(stack.pop())
        elif token == '!':
            return
expression = input("Enter the postfix expression: ").split()
calculate_postfix(expression)
