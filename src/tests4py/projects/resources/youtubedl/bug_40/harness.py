import struct
import sys

if __name__ == "__main__":
    mode = sys.argv[1]
    fmt = sys.argv[2]
    value = int(sys.argv[3])
    packed = struct.pack(fmt, value)
    if mode == "ytdl":
        # noinspection PyUnresolvedReferences
        from youtube_dl.utils import struct_unpack

        result = struct_unpack(fmt, packed)[0]
    else:
        result = struct.unpack(fmt, packed)[0]
    print(result)
