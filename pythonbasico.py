a=3
b=3

# > mayor que
# < menor que
# <= menor o igual que
# >= mayor o igual que
# != diferente que 
# == igual que 

if a>b:
    print('a='+str(a)+' es mayor que b=',b)
elif a<b:
    print(f'b={b} es mayor que a={a}')
else:
    print(f'b={b} es igual que a={a}')

print('termine')