
binary = [0] * 1000

def inkq(N):
    for i in range(1, N+1):
        print(binary[i], end='')
    print()


def Try(i, N):
    for j in range(2):
        binary[i] = j
        if i == N:
            inkq(N)
        else:
            Try(i + 1, N)


if __name__ == "__main__":
    N = 5
    Try(0, 3)

