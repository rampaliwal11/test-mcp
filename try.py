def greet(n: int) -> None:
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


def main(n: int) -> None:
    greet(n)