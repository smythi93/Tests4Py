import sys
from expression.evaluate import evaluate

if __name__ == "__main__":
    value = "".join(sys.argv[1:])
    value = value.strip()
    value = value.replace('-', ' - ')
    value = value.replace('*', ' * ')
    value = value.replace('/', ' / ')
    value = value.replace('+', ' + ')
    print(evaluate(value))
