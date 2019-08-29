def fab1(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b


def fab2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

if __name__ == '__main__':
    print('main')
else:
    print('else')

