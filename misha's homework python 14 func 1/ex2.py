#[a+b, a-b, a/b, a*b]
def basic_math(a, b):
    if b == 0:
        return [a+b, a-b, "cant divide by zero", a*b]
    return [a+b, a-b, a/b, a*b]
print(basic_math(int(input("first number")), int(input("second number"))))