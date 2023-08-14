

nums = [0] * 1000
used = [0] * 1000


def Print(N):
    for i in range(1, N + 1):
        print(nums[i], end=' ')
    print()


def Try(i, N):
    for j in range(1, N + 1):
        if used[j] == 0:
            nums[i] = j
            used[j] = 1
            if i == N:
                Print(N)
            else:
                Try(i + 1, N)
            used[j] = 0


if __name__ == "__main__":
    Try(1, 5)
