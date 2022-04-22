
def add(n: int) -> int:
    result = 0

    for i in range(n):
        result += (i + 1)

    return result


def mul(n: int) -> None:
    # Run many times to get longer execution period
    for x in range(4000000):
        result = 1

        for i in range(n):
            result *= (i + 1)

    return result

