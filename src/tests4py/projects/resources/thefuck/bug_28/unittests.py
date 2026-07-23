import unittest

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        import os, tempfile
        from thefuck.types import Command, Settings
        from thefuck.rules.fix_file import get_new_command
        os.environ['EDITOR'] = 'nano'
        fd, path = tempfile.mkstemp(suffix='.c')
        os.close(fd)
        stderr = path + ':203:18: error'
        settings = Settings({'fixcolcmd': '{editor} {file} COLMARKER'})
        result = get_new_command(Command('gcc a.c', '', stderr), settings)
        self.assertEqual(True, 'COLMARKER' in str(result))

    def test_diversity_2(self):
        import os, tempfile
        from thefuck.types import Command, Settings
        from thefuck.rules.fix_file import get_new_command
        os.environ['EDITOR'] = 'nano'
        fd, path = tempfile.mkstemp(suffix='.c')
        os.close(fd)
        stderr = path + ':191:371: error'
        settings = Settings({'fixcolcmd': '{editor} {file} COLMARKER'})
        result = get_new_command(Command('gcc a.c', '', stderr), settings)
        self.assertEqual(True, 'COLMARKER' in str(result))

    def test_diversity_3(self):
        import os, tempfile
        from thefuck.types import Command, Settings
        from thefuck.rules.fix_file import get_new_command
        os.environ['EDITOR'] = 'nano'
        fd, path = tempfile.mkstemp(suffix='.c')
        os.close(fd)
        stderr = path + ':358:269: error'
        settings = Settings({'fixcolcmd': '{editor} {file} COLMARKER'})
        result = get_new_command(Command('gcc a.c', '', stderr), settings)
        self.assertEqual(True, 'COLMARKER' in str(result))

    def test_diversity_4(self):
        import os, tempfile
        from thefuck.types import Command, Settings
        from thefuck.rules.fix_file import get_new_command
        os.environ['EDITOR'] = 'nano'
        fd, path = tempfile.mkstemp(suffix='.c')
        os.close(fd)
        stderr = path + ':106:120: error'
        settings = Settings({'fixcolcmd': '{editor} {file} COLMARKER'})
        result = get_new_command(Command('gcc a.c', '', stderr), settings)
        self.assertEqual(True, 'COLMARKER' in str(result))

    def test_diversity_5(self):
        import os, tempfile
        from thefuck.types import Command, Settings
        from thefuck.rules.fix_file import get_new_command
        os.environ['EDITOR'] = 'nano'
        fd, path = tempfile.mkstemp(suffix='.c')
        os.close(fd)
        stderr = path + ':321:112: error'
        settings = Settings({'fixcolcmd': '{editor} {file} COLMARKER'})
        result = get_new_command(Command('gcc a.c', '', stderr), settings)
        self.assertEqual(True, 'COLMARKER' in str(result))

    def test_diversity_6(self):
        import os, tempfile
        from thefuck.types import Command, Settings
        from thefuck.rules.fix_file import get_new_command
        os.environ['EDITOR'] = 'nano'
        fd, path = tempfile.mkstemp(suffix='.c')
        os.close(fd)
        stderr = path + ':283:104: error'
        settings = Settings({'fixcolcmd': '{editor} {file} COLMARKER'})
        result = get_new_command(Command('gcc a.c', '', stderr), settings)
        self.assertEqual(True, 'COLMARKER' in str(result))

    def test_diversity_7(self):
        import os, tempfile
        from thefuck.types import Command, Settings
        from thefuck.rules.fix_file import get_new_command
        os.environ['EDITOR'] = 'nano'
        fd, path = tempfile.mkstemp(suffix='.c')
        os.close(fd)
        stderr = path + ':225:102: error'
        settings = Settings({'fixcolcmd': '{editor} {file} COLMARKER'})
        result = get_new_command(Command('gcc a.c', '', stderr), settings)
        self.assertEqual(True, 'COLMARKER' in str(result))

    def test_diversity_8(self):
        import os, tempfile
        from thefuck.types import Command, Settings
        from thefuck.rules.fix_file import get_new_command
        os.environ['EDITOR'] = 'nano'
        fd, path = tempfile.mkstemp(suffix='.c')
        os.close(fd)
        stderr = path + ':232:41: error'
        settings = Settings({'fixcolcmd': '{editor} {file} COLMARKER'})
        result = get_new_command(Command('gcc a.c', '', stderr), settings)
        self.assertEqual(True, 'COLMARKER' in str(result))

    def test_diversity_9(self):
        import os, tempfile
        from thefuck.types import Command, Settings
        from thefuck.rules.fix_file import get_new_command
        os.environ['EDITOR'] = 'nano'
        fd, path = tempfile.mkstemp(suffix='.c')
        os.close(fd)
        stderr = path + ':181:296: error'
        settings = Settings({'fixcolcmd': '{editor} {file} COLMARKER'})
        result = get_new_command(Command('gcc a.c', '', stderr), settings)
        self.assertEqual(True, 'COLMARKER' in str(result))

    def test_diversity_10(self):
        import os, tempfile
        from thefuck.types import Command, Settings
        from thefuck.rules.fix_file import get_new_command
        os.environ['EDITOR'] = 'nano'
        fd, path = tempfile.mkstemp(suffix='.c')
        os.close(fd)
        stderr = path + ':49:354: error'
        settings = Settings({'fixcolcmd': '{editor} {file} COLMARKER'})
        result = get_new_command(Command('gcc a.c', '', stderr), settings)
        self.assertEqual(True, 'COLMARKER' in str(result))

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        import os, tempfile
        from thefuck.types import Command, Settings
        from thefuck.rules.fix_file import get_new_command
        os.environ['EDITOR'] = 'nano'
        fd, path = tempfile.mkstemp(suffix='.c')
        os.close(fd)
        stderr = path + ':85:200: error'
        settings = Settings()
        result = get_new_command(Command('gcc a.c', '', stderr), settings)
        self.assertEqual(False, 'COLMARKER' in str(result))

    def test_diversity_2(self):
        import os, tempfile
        from thefuck.types import Command, Settings
        from thefuck.rules.fix_file import get_new_command
        os.environ['EDITOR'] = 'nano'
        fd, path = tempfile.mkstemp(suffix='.c')
        os.close(fd)
        stderr = path + ':120:340: error'
        settings = Settings()
        result = get_new_command(Command('gcc a.c', '', stderr), settings)
        self.assertEqual(False, 'COLMARKER' in str(result))

    def test_diversity_3(self):
        import os, tempfile
        from thefuck.types import Command, Settings
        from thefuck.rules.fix_file import get_new_command
        os.environ['EDITOR'] = 'nano'
        fd, path = tempfile.mkstemp(suffix='.c')
        os.close(fd)
        stderr = path + ':355:313: error'
        settings = Settings()
        result = get_new_command(Command('gcc a.c', '', stderr), settings)
        self.assertEqual(False, 'COLMARKER' in str(result))

    def test_diversity_4(self):
        import os, tempfile
        from thefuck.types import Command, Settings
        from thefuck.rules.fix_file import get_new_command
        os.environ['EDITOR'] = 'nano'
        fd, path = tempfile.mkstemp(suffix='.c')
        os.close(fd)
        stderr = path + ':192:143: error'
        settings = Settings()
        result = get_new_command(Command('gcc a.c', '', stderr), settings)
        self.assertEqual(False, 'COLMARKER' in str(result))

    def test_diversity_5(self):
        import os, tempfile
        from thefuck.types import Command, Settings
        from thefuck.rules.fix_file import get_new_command
        os.environ['EDITOR'] = 'nano'
        fd, path = tempfile.mkstemp(suffix='.c')
        os.close(fd)
        stderr = path + ':154:12: error'
        settings = Settings()
        result = get_new_command(Command('gcc a.c', '', stderr), settings)
        self.assertEqual(False, 'COLMARKER' in str(result))

    def test_diversity_6(self):
        import os, tempfile
        from thefuck.types import Command, Settings
        from thefuck.rules.fix_file import get_new_command
        os.environ['EDITOR'] = 'nano'
        fd, path = tempfile.mkstemp(suffix='.c')
        os.close(fd)
        stderr = path + ':29:248: error'
        settings = Settings()
        result = get_new_command(Command('gcc a.c', '', stderr), settings)
        self.assertEqual(False, 'COLMARKER' in str(result))

    def test_diversity_7(self):
        import os, tempfile
        from thefuck.types import Command, Settings
        from thefuck.rules.fix_file import get_new_command
        os.environ['EDITOR'] = 'nano'
        fd, path = tempfile.mkstemp(suffix='.c')
        os.close(fd)
        stderr = path + ':325:349: error'
        settings = Settings()
        result = get_new_command(Command('gcc a.c', '', stderr), settings)
        self.assertEqual(False, 'COLMARKER' in str(result))

    def test_diversity_8(self):
        import os, tempfile
        from thefuck.types import Command, Settings
        from thefuck.rules.fix_file import get_new_command
        os.environ['EDITOR'] = 'nano'
        fd, path = tempfile.mkstemp(suffix='.c')
        os.close(fd)
        stderr = path + ':28:84: error'
        settings = Settings()
        result = get_new_command(Command('gcc a.c', '', stderr), settings)
        self.assertEqual(False, 'COLMARKER' in str(result))

    def test_diversity_9(self):
        import os, tempfile
        from thefuck.types import Command, Settings
        from thefuck.rules.fix_file import get_new_command
        os.environ['EDITOR'] = 'nano'
        fd, path = tempfile.mkstemp(suffix='.c')
        os.close(fd)
        stderr = path + ':196:246: error'
        settings = Settings()
        result = get_new_command(Command('gcc a.c', '', stderr), settings)
        self.assertEqual(False, 'COLMARKER' in str(result))

    def test_diversity_10(self):
        import os, tempfile
        from thefuck.types import Command, Settings
        from thefuck.rules.fix_file import get_new_command
        os.environ['EDITOR'] = 'nano'
        fd, path = tempfile.mkstemp(suffix='.c')
        os.close(fd)
        stderr = path + ':274:173: error'
        settings = Settings()
        result = get_new_command(Command('gcc a.c', '', stderr), settings)
        self.assertEqual(False, 'COLMARKER' in str(result))
