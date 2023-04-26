The bug in cookiecutter 3 does occur whenever a selection of choices is provided in the `cookiecutter.json`, i.e., a
key has a list as the value. The output of `cookiecutter` shows the possible choices two times as 1, .., n and 
(1, .., n). 