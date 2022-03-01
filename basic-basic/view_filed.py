def foo():
    res = []

    for i in range(3):
        def bar():
            return i

        res.append(bar)

    return res

print(foo())
for f in foo():
    print(f())