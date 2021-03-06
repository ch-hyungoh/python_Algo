def bit(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else "0"
    print(output)

a = 0x86
key = 0xAA

print("a    ==> ", end='')
bit(a)

print("key  ==> ", end='')
bit(key)

print("a^key==> ", end='')
a ^= key
bit(a)

print("a^key==> ", end='')
a ^= key
bit(a)