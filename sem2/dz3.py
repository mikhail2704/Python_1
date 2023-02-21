n = int(input('Введите количевто монет: '))
a = 0
b = 0
print("Введите какое количество из них лежат вверх решкой (0), а какое гербом(1) ")
for i in range(n):
    count_monet= int(input())
    if count_monet == 0 :
        a +=1
    if count_monet == 1:
        b += 1
if a < b :
    print(f"меньше монет повёрнутых решкой: {a}" )
else :
    print(f"меньше монет повёрнутых гербом: {b}" )


