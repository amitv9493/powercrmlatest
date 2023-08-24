def func(num1, num2, *args, **kwargs):
    print(args)
    print(kwargs)


func(1, 2, 3, 4, 5, Name="Amit")
