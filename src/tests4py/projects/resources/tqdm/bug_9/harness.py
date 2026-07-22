import sys

try:
    from tqdm._tqdm import format_sizeof
except ImportError:
    from tqdm import format_sizeof

if __name__ == "__main__":
    print(format_sizeof(float(sys.argv[1])))
