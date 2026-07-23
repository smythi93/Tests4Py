import unittest
import sys
import luigi


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        class MyTask_none_apqwpgkyx(luigi.Task):
        
            def complete(self):
                return True
        _saved = sys.argv
        sys.argv = ['harness', '--no-lock', '--local-scheduler']
        try:
            luigi.run(main_task_cls=MyTask_none_apqwpgkyx)
        finally:
            sys.argv = _saved
        self.assertTrue(True)

    def test_diversity_2(self):
        class MyTask_none_dkequ(luigi.Task):
        
            def complete(self):
                return True
        _saved = sys.argv
        sys.argv = ['harness', '--no-lock', '--local-scheduler']
        try:
            luigi.run(main_task_cls=MyTask_none_dkequ)
        finally:
            sys.argv = _saved
        self.assertTrue(True)

    def test_diversity_3(self):
        class MyTask_none_wrdo(luigi.Task):
        
            def complete(self):
                return True
        _saved = sys.argv
        sys.argv = ['harness', '--no-lock', '--local-scheduler']
        try:
            luigi.run(main_task_cls=MyTask_none_wrdo)
        finally:
            sys.argv = _saved
        self.assertTrue(True)

    def test_diversity_4(self):
        class MyTask_none_kxqewf(luigi.Task):
        
            def complete(self):
                return True
        _saved = sys.argv
        sys.argv = ['harness', '--no-lock', '--local-scheduler']
        try:
            luigi.run(main_task_cls=MyTask_none_kxqewf)
        finally:
            sys.argv = _saved
        self.assertTrue(True)

    def test_diversity_5(self):
        class MyTask_none_obswuuamb(luigi.Task):
        
            def complete(self):
                return True
        _saved = sys.argv
        sys.argv = ['harness', '--no-lock', '--local-scheduler']
        try:
            luigi.run(main_task_cls=MyTask_none_obswuuamb)
        finally:
            sys.argv = _saved
        self.assertTrue(True)

    def test_diversity_6(self):
        class MyTask_none_esgsibki(luigi.Task):
        
            def complete(self):
                return True
        _saved = sys.argv
        sys.argv = ['harness', '--no-lock', '--local-scheduler']
        try:
            luigi.run(main_task_cls=MyTask_none_esgsibki)
        finally:
            sys.argv = _saved
        self.assertTrue(True)

    def test_diversity_7(self):
        class MyTask_none_vumoob(luigi.Task):
        
            def complete(self):
                return True
        _saved = sys.argv
        sys.argv = ['harness', '--no-lock', '--local-scheduler']
        try:
            luigi.run(main_task_cls=MyTask_none_vumoob)
        finally:
            sys.argv = _saved
        self.assertTrue(True)

    def test_diversity_8(self):
        class MyTask_none_tzisnobv(luigi.Task):
        
            def complete(self):
                return True
        _saved = sys.argv
        sys.argv = ['harness', '--no-lock', '--local-scheduler']
        try:
            luigi.run(main_task_cls=MyTask_none_tzisnobv)
        finally:
            sys.argv = _saved
        self.assertTrue(True)

    def test_diversity_9(self):
        class MyTask_none_jizcb(luigi.Task):
        
            def complete(self):
                return True
        _saved = sys.argv
        sys.argv = ['harness', '--no-lock', '--local-scheduler']
        try:
            luigi.run(main_task_cls=MyTask_none_jizcb)
        finally:
            sys.argv = _saved
        self.assertTrue(True)

    def test_diversity_10(self):
        class MyTask_none_quzn(luigi.Task):
        
            def complete(self):
                return True
        _saved = sys.argv
        sys.argv = ['harness', '--no-lock', '--local-scheduler']
        try:
            luigi.run(main_task_cls=MyTask_none_quzn)
        finally:
            sys.argv = _saved
        self.assertTrue(True)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        class MyTask_explicit_rsmn(luigi.Task):
        
            def complete(self):
                return True
        luigi.run(cmdline_args=['--no-lock', '--local-scheduler'], main_task_cls=MyTask_explicit_rsmn)
        self.assertTrue(True)

    def test_diversity_2(self):
        class MyTask_explicit_barbhpk(luigi.Task):
        
            def complete(self):
                return True
        luigi.run(cmdline_args=['--no-lock', '--local-scheduler'], main_task_cls=MyTask_explicit_barbhpk)
        self.assertTrue(True)

    def test_diversity_3(self):
        class MyTask_explicit_lgkmqzc(luigi.Task):
        
            def complete(self):
                return True
        luigi.run(cmdline_args=['--no-lock', '--local-scheduler'], main_task_cls=MyTask_explicit_lgkmqzc)
        self.assertTrue(True)

    def test_diversity_4(self):
        class MyTask_explicit_ejpflqq(luigi.Task):
        
            def complete(self):
                return True
        luigi.run(cmdline_args=['--no-lock', '--local-scheduler'], main_task_cls=MyTask_explicit_ejpflqq)
        self.assertTrue(True)

    def test_diversity_5(self):
        class MyTask_explicit_wsrgxkpvz(luigi.Task):
        
            def complete(self):
                return True
        luigi.run(cmdline_args=['--no-lock', '--local-scheduler'], main_task_cls=MyTask_explicit_wsrgxkpvz)
        self.assertTrue(True)

    def test_diversity_6(self):
        class MyTask_explicit_efws(luigi.Task):
        
            def complete(self):
                return True
        luigi.run(cmdline_args=['--no-lock', '--local-scheduler'], main_task_cls=MyTask_explicit_efws)
        self.assertTrue(True)

    def test_diversity_7(self):
        class MyTask_explicit_ochy(luigi.Task):
        
            def complete(self):
                return True
        luigi.run(cmdline_args=['--no-lock', '--local-scheduler'], main_task_cls=MyTask_explicit_ochy)
        self.assertTrue(True)

    def test_diversity_8(self):
        class MyTask_explicit_tzzelrjpe(luigi.Task):
        
            def complete(self):
                return True
        luigi.run(cmdline_args=['--no-lock', '--local-scheduler'], main_task_cls=MyTask_explicit_tzzelrjpe)
        self.assertTrue(True)

    def test_diversity_9(self):
        class MyTask_explicit_yigv(luigi.Task):
        
            def complete(self):
                return True
        luigi.run(cmdline_args=['--no-lock', '--local-scheduler'], main_task_cls=MyTask_explicit_yigv)
        self.assertTrue(True)

    def test_diversity_10(self):
        class MyTask_explicit_xngrs(luigi.Task):
        
            def complete(self):
                return True
        luigi.run(cmdline_args=['--no-lock', '--local-scheduler'], main_task_cls=MyTask_explicit_xngrs)
        self.assertTrue(True)
