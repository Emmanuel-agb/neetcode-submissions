class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []  # stack for numbers

        for c in tokens:  # check each token
            if c == "+":  # add operator
                st.append(st.pop() + st.pop())  # pop 2, add, push result
            elif c == "-":  # subtract operator
                second, first = st.pop(), st.pop()  # pop in order
                st.append(first - second)  # push first - second
            elif c == "*":  # multiply operator
                st.append(st.pop() * st.pop())  # pop 2, multiply, push result
            elif c == "/":  # divide operator
                second, first = st.pop(), st.pop()  # pop in order
                st.append(int(first / second))  # push first / second, toward zero
            else:  # number token
                st.append(int(c))  # convert to int, push

        return st[0]  # final result
