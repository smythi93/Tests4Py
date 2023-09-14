import sys
from markup import remove_html_markup


if __name__ == "__main__":
    assert len(sys.argv) == 2
    print(remove_html_markup((sys.argv[1])))
