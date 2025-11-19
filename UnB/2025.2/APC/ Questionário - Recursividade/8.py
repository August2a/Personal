def triangulo(x,size):
    if size > 1:
        triangulo(x+1,size-2)
    print(x*' '+size*'+')
      