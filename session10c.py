def fun(*args, **kwargs):
    print(args)
    print(kwargs)


fun(10, 20, 30, name="john", email="john@example.com")
