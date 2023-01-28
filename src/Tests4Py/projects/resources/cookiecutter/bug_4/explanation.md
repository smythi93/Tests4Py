The bug in cookiecutter 4 does occur whenever a `post_gen_project` hook fails. In this case the program should
terminate with an exitcode `!= 1` but it does not trigger an exception.