class Hello:
    atribute = 'Hello World'
superCl = Hello
print(superCl.atribute)
class Hello2(Hello):
    atribute2 = 'Hello World2'
superCl2 = Hello2
print(superCl.atribute, superCl2.atribute2)