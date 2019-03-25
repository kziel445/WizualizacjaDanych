print("Podaj zdanie")
napis = input()
print(list(napis))
znak="0"
while(znak!="@stop"):
    print("Jaka litere znalesc? Czy zakonczyc dzialanie komenda @stop")
    znak = input()
    y=0
    for i,c in enumerate(napis):
        if(c==znak):
            print("%s pozycja: %d" % (c, i+1))
            y=1
    if(y==0):
         print("Ciag nie zawiera podanego znaku")