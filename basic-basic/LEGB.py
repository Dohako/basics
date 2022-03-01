

a = 5
print(globals())

def test():
    
    def test_2():
        return a
    print(test_2.__closure__)
    a = 10
    return a

print(test())