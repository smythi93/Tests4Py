import sys

try:
    from tqdm.utils import disp_trim
except ImportError:
    from tqdm._utils import disp_trim

if __name__ == "__main__":
    length = int(sys.argv[1])
    mode = sys.argv[2]
    color = sys.argv[3]
    word = sys.argv[4]
    if mode == "ansi":
        data = "\x1b[" + color + "m" + word + "\x1b[0m"
    else:
        data = word
    print(repr(disp_trim(data, length)))
