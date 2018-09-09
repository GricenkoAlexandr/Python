a=int(input('Vvedite poryadkoviy nomer chisla fibonachi '))
fibo1=0
fibo2=1
fibosum=0
#print (fibo1)
print (fibo2)
i=1
while i<a:
    fibosum=fibo1+fibo2
    print (fibosum)
    fibo1=fibo2
    fibo2=fibosum
    i=i+1
print('Chislo fibonachi s poryadkovim nomerom ',a,'ravno',fibosum)
