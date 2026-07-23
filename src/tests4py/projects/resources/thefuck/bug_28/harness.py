import os
import sys
import tempfile

from thefuck.types import Command
from thefuck.types import Settings
from thefuck.rules.fix_file import get_new_command

# fix_file.get_new_command changed to honour a ``fixcolcmd`` setting: on the
# fixed build, when settings.fixcolcmd is set and the matched error carries a
# column, the column-aware command is emitted; the buggy build ignores settings
# entirely and always emits the line-only command. We pass a fixcolcmd that
# embeds a distinctive COLMARKER and report whether it survives into the output.
# The referenced file must exist for fix_file._search's isfile guard, so we
# materialise a real temp file. argv: expected, mode(col|nocol), line, col.
if __name__ == "__main__":
    mode = sys.argv[2]
    line = sys.argv[3]
    col = sys.argv[4]
    os.environ["EDITOR"] = "nano"
    fd, path = tempfile.mkstemp(suffix=".c")
    os.close(fd)
    stderr = "{}:{}:{}: error".format(path, line, col)
    if mode == "col":
        settings = Settings({"fixcolcmd": "{editor} {file} COLMARKER"})
    else:
        settings = Settings()
    result = get_new_command(Command("gcc a.c", "", stderr), settings)
    print("COLMARKER" in str(result))
