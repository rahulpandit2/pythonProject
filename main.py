import pyjokes

b = 1
a = int(input("How many jokes do you want: "))
while b <= a:
    print(b, pyjokes.get_joke())
    b += 1
