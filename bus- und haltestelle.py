z = input("Bitte eingeben wie viel Busstationen sind: ")

k = 0
for p in range(0, int(z)):
    u = input("Wie viele leute steigen ein?")
    a = input("Wie viele leute steigen aus?")
    leute = int(u)
    k = k +int(u)
    k = k -int(a)
print(k)
