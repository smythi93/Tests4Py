import sys
from expression.evaluate import evaluate
from expression.evaluate import main


if __name__ == "__main__":
    assert len(sys.argv) > 0
    # print(evaluate((sys.argv[1:])))

    # value = str(sys.argv[0:])

    # value = "".join(sys.argv[2])
    # print(evaluate(value))

    print("".join(main(sys.argv[0:])))
    # print("".join(evaluate((sys.argv[2:]))))
