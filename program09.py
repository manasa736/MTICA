def f():

    x=10
    print('id(x)in f outer:',id(x))
    def g():
        x = 15
        print('id(x)in g outer:',id(x))
    g()
    print(x)

f()
