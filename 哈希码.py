def hash_code(s: str) -> int:
    mask = (1 << 32) - 1

    h = 0
    for c in s:
        h = (h << 5 & mask) | (h >> 27)
        h += ord(c)

    return h


if __name__ == '__main__':
    a = "123456"
    code = hash_code(a)
    print(code)

    a = "12345678"
    code = hash_code(a)
    print(code)