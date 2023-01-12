import os
import shutil
from pathlib import Path

subjects = {
    'matplotlib': 30,
    'pandas': 169,
    'sanic': 5,
    'scrapy': 40,
    'spacy': 10,
    'thefuck': 32,
    'tornado': 16,
    'tqdm': 9,
    'youtube-dl': 43,
}

def create(to_: Path, from_: Path, s: str):
    assert s in subjects
    src = from_ / s
    dest = to_ / s.replace('-', '')
    if dest.exists():
        return
    os.makedirs(dest)
    shutil.move(src / f'{s}-fail.txt', dest)
    shutil.move(src / f'{s}-pass.txt', dest)
    for i in range(1, subjects[s] + 1):
        bug_dir = dest / f'bug_{i}'
        os.makedirs(bug_dir)
        with (bug_dir / '__init__').open('w') as fp:
            pass
        if (src / f'{i}' / 'bug_patch.txt').exists():
            shutil.move(src / f'{i}' / 'bug_patch.txt', bug_dir)
        if (src / f'{i}' / 'requirements.txt').exists():
            shutil.move(src / f'{i}' / 'requirements.txt', bug_dir)
        if (src / f'{i}' / 'setup.sh').exists():
            shutil.move(src / f'{i}' / 'setup.sh', bug_dir)

    all_content = ",\n".join([f"bug_{i}" for i in range(1, subjects[s] + 1)])

    with (dest / 'init.py').open('w') as fp:
        fp.write(f'from BugsTest.projects.resources.{s.replace("-", "")} '
                 f'import {",".join([f"bug_{i}" for i in range(1, subjects[s] + 1)])}\n'
                 f'__all__ = [\n{all_content}]')


def create_all():
    path = Path.cwd()
    assert path == Path(__file__)
    for s in subjects:
        create(path / 'src' / 'BugsTest' / 'projects' / 'resources', path / 'projects_old', s)


if __name__ == '__main__':
    create_all()
