import unittest
import luigi
from luigi import Event, Task, build

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):

        class DummyException_pwloposm(Exception):
            pass

        def _run(self):
            if self.fail:
                raise DummyException_pwloposm()
        T = type('ET_pwloposm', (Task,), {'fail': luigi.BoolParameter(), 'run': _run})
        successes = []
        failures = []

        def _s(task):
            successes.append(task)

        def _f(task, exc):
            failures.append(task)
        T.event_handler(Event.SUCCESS)(_s)
        T.event_handler(Event.FAILURE)(_f)
        t = T(True)
        build([t], local_scheduler=True)
        self.assertEqual(len(successes) + len(failures), 1)

    def test_diversity_2(self):

        class DummyException_gpafgkxyk(Exception):
            pass

        def _run(self):
            if self.fail:
                raise DummyException_gpafgkxyk()
        T = type('ET_gpafgkxyk', (Task,), {'fail': luigi.BoolParameter(), 'run': _run})
        successes = []
        failures = []

        def _s(task):
            successes.append(task)

        def _f(task, exc):
            failures.append(task)
        T.event_handler(Event.SUCCESS)(_s)
        T.event_handler(Event.FAILURE)(_f)
        t = T(True)
        build([t], local_scheduler=True)
        self.assertEqual(len(successes) + len(failures), 1)

    def test_diversity_3(self):

        class DummyException_rykhuvg(Exception):
            pass

        def _run(self):
            if self.fail:
                raise DummyException_rykhuvg()
        T = type('ET_rykhuvg', (Task,), {'fail': luigi.BoolParameter(), 'run': _run})
        successes = []
        failures = []

        def _s(task):
            successes.append(task)

        def _f(task, exc):
            failures.append(task)
        T.event_handler(Event.SUCCESS)(_s)
        T.event_handler(Event.FAILURE)(_f)
        t = T(True)
        build([t], local_scheduler=True)
        self.assertEqual(len(successes) + len(failures), 1)

    def test_diversity_4(self):

        class DummyException_vbjk(Exception):
            pass

        def _run(self):
            if self.fail:
                raise DummyException_vbjk()
        T = type('ET_vbjk', (Task,), {'fail': luigi.BoolParameter(), 'run': _run})
        successes = []
        failures = []

        def _s(task):
            successes.append(task)

        def _f(task, exc):
            failures.append(task)
        T.event_handler(Event.SUCCESS)(_s)
        T.event_handler(Event.FAILURE)(_f)
        t = T(True)
        build([t], local_scheduler=True)
        self.assertEqual(len(successes) + len(failures), 1)

    def test_diversity_5(self):

        class DummyException_ocetl(Exception):
            pass

        def _run(self):
            if self.fail:
                raise DummyException_ocetl()
        T = type('ET_ocetl', (Task,), {'fail': luigi.BoolParameter(), 'run': _run})
        successes = []
        failures = []

        def _s(task):
            successes.append(task)

        def _f(task, exc):
            failures.append(task)
        T.event_handler(Event.SUCCESS)(_s)
        T.event_handler(Event.FAILURE)(_f)
        t = T(True)
        build([t], local_scheduler=True)
        self.assertEqual(len(successes) + len(failures), 1)

    def test_diversity_6(self):

        class DummyException_wdvy(Exception):
            pass

        def _run(self):
            if self.fail:
                raise DummyException_wdvy()
        T = type('ET_wdvy', (Task,), {'fail': luigi.BoolParameter(), 'run': _run})
        successes = []
        failures = []

        def _s(task):
            successes.append(task)

        def _f(task, exc):
            failures.append(task)
        T.event_handler(Event.SUCCESS)(_s)
        T.event_handler(Event.FAILURE)(_f)
        t = T(True)
        build([t], local_scheduler=True)
        self.assertEqual(len(successes) + len(failures), 1)

    def test_diversity_7(self):

        class DummyException_ytxh(Exception):
            pass

        def _run(self):
            if self.fail:
                raise DummyException_ytxh()
        T = type('ET_ytxh', (Task,), {'fail': luigi.BoolParameter(), 'run': _run})
        successes = []
        failures = []

        def _s(task):
            successes.append(task)

        def _f(task, exc):
            failures.append(task)
        T.event_handler(Event.SUCCESS)(_s)
        T.event_handler(Event.FAILURE)(_f)
        t = T(True)
        build([t], local_scheduler=True)
        self.assertEqual(len(successes) + len(failures), 1)

    def test_diversity_8(self):

        class DummyException_uvwoakp(Exception):
            pass

        def _run(self):
            if self.fail:
                raise DummyException_uvwoakp()
        T = type('ET_uvwoakp', (Task,), {'fail': luigi.BoolParameter(), 'run': _run})
        successes = []
        failures = []

        def _s(task):
            successes.append(task)

        def _f(task, exc):
            failures.append(task)
        T.event_handler(Event.SUCCESS)(_s)
        T.event_handler(Event.FAILURE)(_f)
        t = T(True)
        build([t], local_scheduler=True)
        self.assertEqual(len(successes) + len(failures), 1)

    def test_diversity_9(self):

        class DummyException_tqayvc(Exception):
            pass

        def _run(self):
            if self.fail:
                raise DummyException_tqayvc()
        T = type('ET_tqayvc', (Task,), {'fail': luigi.BoolParameter(), 'run': _run})
        successes = []
        failures = []

        def _s(task):
            successes.append(task)

        def _f(task, exc):
            failures.append(task)
        T.event_handler(Event.SUCCESS)(_s)
        T.event_handler(Event.FAILURE)(_f)
        t = T(True)
        build([t], local_scheduler=True)
        self.assertEqual(len(successes) + len(failures), 1)

    def test_diversity_10(self):

        class DummyException_cccz(Exception):
            pass

        def _run(self):
            if self.fail:
                raise DummyException_cccz()
        T = type('ET_cccz', (Task,), {'fail': luigi.BoolParameter(), 'run': _run})
        successes = []
        failures = []

        def _s(task):
            successes.append(task)

        def _f(task, exc):
            failures.append(task)
        T.event_handler(Event.SUCCESS)(_s)
        T.event_handler(Event.FAILURE)(_f)
        t = T(True)
        build([t], local_scheduler=True)
        self.assertEqual(len(successes) + len(failures), 1)

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):

        class DummyException_vprbrged(Exception):
            pass

        def _run(self):
            if self.fail:
                raise DummyException_vprbrged()
        T = type('ET_vprbrged', (Task,), {'fail': luigi.BoolParameter(), 'run': _run})
        successes = []
        failures = []

        def _s(task):
            successes.append(task)

        def _f(task, exc):
            failures.append(task)
        T.event_handler(Event.SUCCESS)(_s)
        T.event_handler(Event.FAILURE)(_f)
        t = T(False)
        build([t], local_scheduler=True)
        self.assertEqual(len(successes) + len(failures), 1)

    def test_diversity_2(self):

        class DummyException_dknalwmf(Exception):
            pass

        def _run(self):
            if self.fail:
                raise DummyException_dknalwmf()
        T = type('ET_dknalwmf', (Task,), {'fail': luigi.BoolParameter(), 'run': _run})
        successes = []
        failures = []

        def _s(task):
            successes.append(task)

        def _f(task, exc):
            failures.append(task)
        T.event_handler(Event.SUCCESS)(_s)
        T.event_handler(Event.FAILURE)(_f)
        t = T(False)
        build([t], local_scheduler=True)
        self.assertEqual(len(successes) + len(failures), 1)

    def test_diversity_3(self):

        class DummyException_zutamrhje(Exception):
            pass

        def _run(self):
            if self.fail:
                raise DummyException_zutamrhje()
        T = type('ET_zutamrhje', (Task,), {'fail': luigi.BoolParameter(), 'run': _run})
        successes = []
        failures = []

        def _s(task):
            successes.append(task)

        def _f(task, exc):
            failures.append(task)
        T.event_handler(Event.SUCCESS)(_s)
        T.event_handler(Event.FAILURE)(_f)
        t = T(False)
        build([t], local_scheduler=True)
        self.assertEqual(len(successes) + len(failures), 1)

    def test_diversity_4(self):

        class DummyException_nyixueoh(Exception):
            pass

        def _run(self):
            if self.fail:
                raise DummyException_nyixueoh()
        T = type('ET_nyixueoh', (Task,), {'fail': luigi.BoolParameter(), 'run': _run})
        successes = []
        failures = []

        def _s(task):
            successes.append(task)

        def _f(task, exc):
            failures.append(task)
        T.event_handler(Event.SUCCESS)(_s)
        T.event_handler(Event.FAILURE)(_f)
        t = T(False)
        build([t], local_scheduler=True)
        self.assertEqual(len(successes) + len(failures), 1)

    def test_diversity_5(self):

        class DummyException_vqou(Exception):
            pass

        def _run(self):
            if self.fail:
                raise DummyException_vqou()
        T = type('ET_vqou', (Task,), {'fail': luigi.BoolParameter(), 'run': _run})
        successes = []
        failures = []

        def _s(task):
            successes.append(task)

        def _f(task, exc):
            failures.append(task)
        T.event_handler(Event.SUCCESS)(_s)
        T.event_handler(Event.FAILURE)(_f)
        t = T(False)
        build([t], local_scheduler=True)
        self.assertEqual(len(successes) + len(failures), 1)

    def test_diversity_6(self):

        class DummyException_jwlmou(Exception):
            pass

        def _run(self):
            if self.fail:
                raise DummyException_jwlmou()
        T = type('ET_jwlmou', (Task,), {'fail': luigi.BoolParameter(), 'run': _run})
        successes = []
        failures = []

        def _s(task):
            successes.append(task)

        def _f(task, exc):
            failures.append(task)
        T.event_handler(Event.SUCCESS)(_s)
        T.event_handler(Event.FAILURE)(_f)
        t = T(False)
        build([t], local_scheduler=True)
        self.assertEqual(len(successes) + len(failures), 1)

    def test_diversity_7(self):

        class DummyException_tjly(Exception):
            pass

        def _run(self):
            if self.fail:
                raise DummyException_tjly()
        T = type('ET_tjly', (Task,), {'fail': luigi.BoolParameter(), 'run': _run})
        successes = []
        failures = []

        def _s(task):
            successes.append(task)

        def _f(task, exc):
            failures.append(task)
        T.event_handler(Event.SUCCESS)(_s)
        T.event_handler(Event.FAILURE)(_f)
        t = T(False)
        build([t], local_scheduler=True)
        self.assertEqual(len(successes) + len(failures), 1)

    def test_diversity_8(self):

        class DummyException_gkdiuvxp(Exception):
            pass

        def _run(self):
            if self.fail:
                raise DummyException_gkdiuvxp()
        T = type('ET_gkdiuvxp', (Task,), {'fail': luigi.BoolParameter(), 'run': _run})
        successes = []
        failures = []

        def _s(task):
            successes.append(task)

        def _f(task, exc):
            failures.append(task)
        T.event_handler(Event.SUCCESS)(_s)
        T.event_handler(Event.FAILURE)(_f)
        t = T(False)
        build([t], local_scheduler=True)
        self.assertEqual(len(successes) + len(failures), 1)

    def test_diversity_9(self):

        class DummyException_unfonvgsv(Exception):
            pass

        def _run(self):
            if self.fail:
                raise DummyException_unfonvgsv()
        T = type('ET_unfonvgsv', (Task,), {'fail': luigi.BoolParameter(), 'run': _run})
        successes = []
        failures = []

        def _s(task):
            successes.append(task)

        def _f(task, exc):
            failures.append(task)
        T.event_handler(Event.SUCCESS)(_s)
        T.event_handler(Event.FAILURE)(_f)
        t = T(False)
        build([t], local_scheduler=True)
        self.assertEqual(len(successes) + len(failures), 1)

    def test_diversity_10(self):

        class DummyException_unmemxxuv(Exception):
            pass

        def _run(self):
            if self.fail:
                raise DummyException_unmemxxuv()
        T = type('ET_unmemxxuv', (Task,), {'fail': luigi.BoolParameter(), 'run': _run})
        successes = []
        failures = []

        def _s(task):
            successes.append(task)

        def _f(task, exc):
            failures.append(task)
        T.event_handler(Event.SUCCESS)(_s)
        T.event_handler(Event.FAILURE)(_f)
        t = T(False)
        build([t], local_scheduler=True)
        self.assertEqual(len(successes) + len(failures), 1)
