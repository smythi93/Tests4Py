import unittest
import luigi
import luigi.worker
import luigi.scheduler
import luigi.execution_summary

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):

        def _run(t):
            t.run_count += 1
            if t.run_count == 1:
                raise ValueError()

        def _complete(t):
            return t.run_count > 0
        Foo = type('Foo_wgudunap', (luigi.Task,), {'run_count': 0, 'run': _run, 'complete': _complete})
        sch = luigi.scheduler.Scheduler(prune_on_get_work=False)
        w = luigi.worker.Worker(scheduler=sch)
        w.add(Foo())
        w.run()
        w.add(Foo())
        w.run()
        s = luigi.execution_summary.summary(w)
        self.assertNotIn(':(', s)

    def test_diversity_2(self):

        def _run(t):
            t.run_count += 1
            if t.run_count == 1:
                raise ValueError()

        def _complete(t):
            return t.run_count > 0
        Foo = type('Foo_iskz', (luigi.Task,), {'run_count': 0, 'run': _run, 'complete': _complete})
        sch = luigi.scheduler.Scheduler(prune_on_get_work=False)
        w = luigi.worker.Worker(scheduler=sch)
        w.add(Foo())
        w.run()
        w.add(Foo())
        w.run()
        s = luigi.execution_summary.summary(w)
        self.assertNotIn(':(', s)

    def test_diversity_3(self):

        def _run(t):
            t.run_count += 1
            if t.run_count == 1:
                raise ValueError()

        def _complete(t):
            return t.run_count > 0
        Foo = type('Foo_tnlluqfn', (luigi.Task,), {'run_count': 0, 'run': _run, 'complete': _complete})
        sch = luigi.scheduler.Scheduler(prune_on_get_work=False)
        w = luigi.worker.Worker(scheduler=sch)
        w.add(Foo())
        w.run()
        w.add(Foo())
        w.run()
        s = luigi.execution_summary.summary(w)
        self.assertNotIn(':(', s)

    def test_diversity_4(self):

        def _run(t):
            t.run_count += 1
            if t.run_count == 1:
                raise ValueError()

        def _complete(t):
            return t.run_count > 0
        Foo = type('Foo_shei', (luigi.Task,), {'run_count': 0, 'run': _run, 'complete': _complete})
        sch = luigi.scheduler.Scheduler(prune_on_get_work=False)
        w = luigi.worker.Worker(scheduler=sch)
        w.add(Foo())
        w.run()
        w.add(Foo())
        w.run()
        s = luigi.execution_summary.summary(w)
        self.assertNotIn(':(', s)

    def test_diversity_5(self):

        def _run(t):
            t.run_count += 1
            if t.run_count == 1:
                raise ValueError()

        def _complete(t):
            return t.run_count > 0
        Foo = type('Foo_kfeafwic', (luigi.Task,), {'run_count': 0, 'run': _run, 'complete': _complete})
        sch = luigi.scheduler.Scheduler(prune_on_get_work=False)
        w = luigi.worker.Worker(scheduler=sch)
        w.add(Foo())
        w.run()
        w.add(Foo())
        w.run()
        s = luigi.execution_summary.summary(w)
        self.assertNotIn(':(', s)

    def test_diversity_6(self):

        def _run(t):
            t.run_count += 1
            if t.run_count == 1:
                raise ValueError()

        def _complete(t):
            return t.run_count > 0
        Foo = type('Foo_cjjhqbu', (luigi.Task,), {'run_count': 0, 'run': _run, 'complete': _complete})
        sch = luigi.scheduler.Scheduler(prune_on_get_work=False)
        w = luigi.worker.Worker(scheduler=sch)
        w.add(Foo())
        w.run()
        w.add(Foo())
        w.run()
        s = luigi.execution_summary.summary(w)
        self.assertNotIn(':(', s)

    def test_diversity_7(self):

        def _run(t):
            t.run_count += 1
            if t.run_count == 1:
                raise ValueError()

        def _complete(t):
            return t.run_count > 0
        Foo = type('Foo_nrkinhz', (luigi.Task,), {'run_count': 0, 'run': _run, 'complete': _complete})
        sch = luigi.scheduler.Scheduler(prune_on_get_work=False)
        w = luigi.worker.Worker(scheduler=sch)
        w.add(Foo())
        w.run()
        w.add(Foo())
        w.run()
        s = luigi.execution_summary.summary(w)
        self.assertNotIn(':(', s)

    def test_diversity_8(self):

        def _run(t):
            t.run_count += 1
            if t.run_count == 1:
                raise ValueError()

        def _complete(t):
            return t.run_count > 0
        Foo = type('Foo_cjgiina', (luigi.Task,), {'run_count': 0, 'run': _run, 'complete': _complete})
        sch = luigi.scheduler.Scheduler(prune_on_get_work=False)
        w = luigi.worker.Worker(scheduler=sch)
        w.add(Foo())
        w.run()
        w.add(Foo())
        w.run()
        s = luigi.execution_summary.summary(w)
        self.assertNotIn(':(', s)

    def test_diversity_9(self):

        def _run(t):
            t.run_count += 1
            if t.run_count == 1:
                raise ValueError()

        def _complete(t):
            return t.run_count > 0
        Foo = type('Foo_iphs', (luigi.Task,), {'run_count': 0, 'run': _run, 'complete': _complete})
        sch = luigi.scheduler.Scheduler(prune_on_get_work=False)
        w = luigi.worker.Worker(scheduler=sch)
        w.add(Foo())
        w.run()
        w.add(Foo())
        w.run()
        s = luigi.execution_summary.summary(w)
        self.assertNotIn(':(', s)

    def test_diversity_10(self):

        def _run(t):
            t.run_count += 1
            if t.run_count == 1:
                raise ValueError()

        def _complete(t):
            return t.run_count > 0
        Foo = type('Foo_ccymzm', (luigi.Task,), {'run_count': 0, 'run': _run, 'complete': _complete})
        sch = luigi.scheduler.Scheduler(prune_on_get_work=False)
        w = luigi.worker.Worker(scheduler=sch)
        w.add(Foo())
        w.run()
        w.add(Foo())
        w.run()
        s = luigi.execution_summary.summary(w)
        self.assertNotIn(':(', s)

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):

        def _run(t):
            t.run_count += 1

        def _complete(t):
            return t.run_count > 0
        Foo = type('Foo_hhnt', (luigi.Task,), {'run_count': 0, 'run': _run, 'complete': _complete})
        sch = luigi.scheduler.Scheduler(prune_on_get_work=False)
        w = luigi.worker.Worker(scheduler=sch)
        w.add(Foo())
        w.run()
        w.add(Foo())
        w.run()
        s = luigi.execution_summary.summary(w)
        self.assertNotIn(':(', s)

    def test_diversity_2(self):

        def _run(t):
            t.run_count += 1

        def _complete(t):
            return t.run_count > 0
        Foo = type('Foo_zmfshjzci', (luigi.Task,), {'run_count': 0, 'run': _run, 'complete': _complete})
        sch = luigi.scheduler.Scheduler(prune_on_get_work=False)
        w = luigi.worker.Worker(scheduler=sch)
        w.add(Foo())
        w.run()
        w.add(Foo())
        w.run()
        s = luigi.execution_summary.summary(w)
        self.assertNotIn(':(', s)

    def test_diversity_3(self):

        def _run(t):
            t.run_count += 1

        def _complete(t):
            return t.run_count > 0
        Foo = type('Foo_tkvwcbfut', (luigi.Task,), {'run_count': 0, 'run': _run, 'complete': _complete})
        sch = luigi.scheduler.Scheduler(prune_on_get_work=False)
        w = luigi.worker.Worker(scheduler=sch)
        w.add(Foo())
        w.run()
        w.add(Foo())
        w.run()
        s = luigi.execution_summary.summary(w)
        self.assertNotIn(':(', s)

    def test_diversity_4(self):

        def _run(t):
            t.run_count += 1

        def _complete(t):
            return t.run_count > 0
        Foo = type('Foo_zroe', (luigi.Task,), {'run_count': 0, 'run': _run, 'complete': _complete})
        sch = luigi.scheduler.Scheduler(prune_on_get_work=False)
        w = luigi.worker.Worker(scheduler=sch)
        w.add(Foo())
        w.run()
        w.add(Foo())
        w.run()
        s = luigi.execution_summary.summary(w)
        self.assertNotIn(':(', s)

    def test_diversity_5(self):

        def _run(t):
            t.run_count += 1

        def _complete(t):
            return t.run_count > 0
        Foo = type('Foo_esvxttax', (luigi.Task,), {'run_count': 0, 'run': _run, 'complete': _complete})
        sch = luigi.scheduler.Scheduler(prune_on_get_work=False)
        w = luigi.worker.Worker(scheduler=sch)
        w.add(Foo())
        w.run()
        w.add(Foo())
        w.run()
        s = luigi.execution_summary.summary(w)
        self.assertNotIn(':(', s)

    def test_diversity_6(self):

        def _run(t):
            t.run_count += 1

        def _complete(t):
            return t.run_count > 0
        Foo = type('Foo_sodzrwtz', (luigi.Task,), {'run_count': 0, 'run': _run, 'complete': _complete})
        sch = luigi.scheduler.Scheduler(prune_on_get_work=False)
        w = luigi.worker.Worker(scheduler=sch)
        w.add(Foo())
        w.run()
        w.add(Foo())
        w.run()
        s = luigi.execution_summary.summary(w)
        self.assertNotIn(':(', s)

    def test_diversity_7(self):

        def _run(t):
            t.run_count += 1

        def _complete(t):
            return t.run_count > 0
        Foo = type('Foo_dojk', (luigi.Task,), {'run_count': 0, 'run': _run, 'complete': _complete})
        sch = luigi.scheduler.Scheduler(prune_on_get_work=False)
        w = luigi.worker.Worker(scheduler=sch)
        w.add(Foo())
        w.run()
        w.add(Foo())
        w.run()
        s = luigi.execution_summary.summary(w)
        self.assertNotIn(':(', s)

    def test_diversity_8(self):

        def _run(t):
            t.run_count += 1

        def _complete(t):
            return t.run_count > 0
        Foo = type('Foo_ajszohh', (luigi.Task,), {'run_count': 0, 'run': _run, 'complete': _complete})
        sch = luigi.scheduler.Scheduler(prune_on_get_work=False)
        w = luigi.worker.Worker(scheduler=sch)
        w.add(Foo())
        w.run()
        w.add(Foo())
        w.run()
        s = luigi.execution_summary.summary(w)
        self.assertNotIn(':(', s)

    def test_diversity_9(self):

        def _run(t):
            t.run_count += 1

        def _complete(t):
            return t.run_count > 0
        Foo = type('Foo_cvzp', (luigi.Task,), {'run_count': 0, 'run': _run, 'complete': _complete})
        sch = luigi.scheduler.Scheduler(prune_on_get_work=False)
        w = luigi.worker.Worker(scheduler=sch)
        w.add(Foo())
        w.run()
        w.add(Foo())
        w.run()
        s = luigi.execution_summary.summary(w)
        self.assertNotIn(':(', s)

    def test_diversity_10(self):

        def _run(t):
            t.run_count += 1

        def _complete(t):
            return t.run_count > 0
        Foo = type('Foo_ehnvv', (luigi.Task,), {'run_count': 0, 'run': _run, 'complete': _complete})
        sch = luigi.scheduler.Scheduler(prune_on_get_work=False)
        w = luigi.worker.Worker(scheduler=sch)
        w.add(Foo())
        w.run()
        w.add(Foo())
        w.run()
        s = luigi.execution_summary.summary(w)
        self.assertNotIn(':(', s)
