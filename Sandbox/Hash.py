def test(d):
    z = 0
    for i in d:
        z = z + ord(i)
    return z % 100

print(test("NANA"))