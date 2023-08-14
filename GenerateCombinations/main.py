
binary = [0] * 1000


def inkq(K):
    for i in range(1, K + 1):
        print(binary[i], end=' ')
    print()

# minvalue -> binary[i-1] + 1
# maxvalue -> N - K + i
def Try(i, N, K):
    for j in range(binary[i-1], N - K + i + 1):
        binary[i] = j
        if i == K:
            inkq(K)
        else:
            Try(i + 1, N, K)


if __name__ == "__main__":
    Try(0, 3, 2)
