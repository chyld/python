def foo(a, b, *c, **d):
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('d:', d)

foo(1, 2, 3, 4, 5, x=6, y=7, z=8)
