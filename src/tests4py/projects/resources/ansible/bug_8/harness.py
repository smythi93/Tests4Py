import sys

from ansible.plugins.shell.powershell import ShellModule

if __name__ == "__main__":
    pwsh = ShellModule()
    print(pwsh.join_path(*sys.argv[1:]))
