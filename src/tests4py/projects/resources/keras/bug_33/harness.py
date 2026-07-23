import importlib.util
import os
import sys


def _load(relpath, name):
    path = os.path.join(os.getcwd(), *relpath.split("/"))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    text_mod = _load("keras/preprocessing/text.py", "t4p_text")
    split = sys.argv[1]
    words = sys.argv[2:]
    text = split.join(words)
    result = text_mod.text_to_word_sequence(text, split=split)
    print(result)
