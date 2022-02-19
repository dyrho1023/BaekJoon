in1 = int(input())

if in1 < 100:
    count = in1
else:
    count = 99
    for i in range(100, in1 + 1):
        local3 = int(i / 100)
        local2 = int((i / 10) % 10)
        local1 = int(i % 10)

        if (local3 - local2) == (local2 - local1):
            count = count + 1
        else:
            pass

print(count)