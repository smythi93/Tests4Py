import importlib.util
import json
import os
import sys
import types


def _load_autogen():
    for name in [
        "keras",
        "keras.backend",
        "keras.backend.numpy_backend",
        "docs",
        "docs.structure",
    ]:
        m = types.ModuleType(name)
        if name in ("keras", "docs"):
            m.__path__ = []
        sys.modules[name] = m
    ds = sys.modules["docs.structure"]
    for a in [
        "EXCLUDE",
        "PAGES",
        "ROOT",
        "template_np_implementation",
        "template_hidden_np_implementation",
    ]:
        setattr(ds, a, None)
    sys.modules["keras.backend"].numpy_backend = sys.modules[
        "keras.backend.numpy_backend"
    ]
    path = os.path.join(os.getcwd(), "docs", "autogen.py")
    spec = importlib.util.spec_from_file_location("docs.autogen", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["docs.autogen"] = module
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    autogen = _load_autogen()
    mode = sys.argv[1]
    names = sys.argv[2:]
    block_body = "\n".join(
        "    %s: description of %s follows" % (n, n) for n in names
    )
    section_end = len(block_body)
    if mode == "last":
        docstring = block_body + "\n    trailing text without blank line"
    else:
        docstring = block_body + "\n\n    trailing text after blank line"
    result = autogen.process_list_block(docstring, 0, section_end, 4, "@@MARKER@@")
    print(json.dumps(list(result)))
