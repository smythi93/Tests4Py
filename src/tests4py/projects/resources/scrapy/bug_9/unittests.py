import unittest

# noinspection PyUnresolvedReferences
from scrapy.mail import MailSender


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        captured = {}
        def cb(**kw):
            captured['msg'] = kw['msg']
        ms = MailSender(debug=True)
        ms.send(to='pgerim@coqbjsl.io', subject='subject', body='body', _callback=cb)
        self.assertEqual('pgerim@coqbjsl.io', captured['msg']['To'])

    def test_diversity_2(self):
        captured = {}
        def cb(**kw):
            captured['msg'] = kw['msg']
        ms = MailSender(debug=True)
        ms.send(to='ebdw@bruxxff.io', subject='subject', body='body', _callback=cb)
        self.assertEqual('ebdw@bruxxff.io', captured['msg']['To'])

    def test_diversity_3(self):
        captured = {}
        def cb(**kw):
            captured['msg'] = kw['msg']
        ms = MailSender(debug=True)
        ms.send(to='uxk@vfxwb.io', subject='subject', body='body', _callback=cb)
        self.assertEqual('uxk@vfxwb.io', captured['msg']['To'])

    def test_diversity_4(self):
        captured = {}
        def cb(**kw):
            captured['msg'] = kw['msg']
        ms = MailSender(debug=True)
        ms.send(to='dgtwza@fwixdxn.io', subject='subject', body='body', _callback=cb)
        self.assertEqual('dgtwza@fwixdxn.io', captured['msg']['To'])

    def test_diversity_5(self):
        captured = {}
        def cb(**kw):
            captured['msg'] = kw['msg']
        ms = MailSender(debug=True)
        ms.send(to='xkkqcpe@sbhrwtt.org', subject='subject', body='body', _callback=cb)
        self.assertEqual('xkkqcpe@sbhrwtt.org', captured['msg']['To'])

    def test_diversity_6(self):
        captured = {}
        def cb(**kw):
            captured['msg'] = kw['msg']
        ms = MailSender(debug=True)
        ms.send(to='wkx@pbjr.org', subject='subject', body='body', _callback=cb)
        self.assertEqual('wkx@pbjr.org', captured['msg']['To'])

    def test_diversity_7(self):
        captured = {}
        def cb(**kw):
            captured['msg'] = kw['msg']
        ms = MailSender(debug=True)
        ms.send(to='cwjff@tjpacfh.org', subject='subject', body='body', _callback=cb)
        self.assertEqual('cwjff@tjpacfh.org', captured['msg']['To'])

    def test_diversity_8(self):
        captured = {}
        def cb(**kw):
            captured['msg'] = kw['msg']
        ms = MailSender(debug=True)
        ms.send(to='qcuau@msgtlg.io', subject='subject', body='body', _callback=cb)
        self.assertEqual('qcuau@msgtlg.io', captured['msg']['To'])

    def test_diversity_9(self):
        captured = {}
        def cb(**kw):
            captured['msg'] = kw['msg']
        ms = MailSender(debug=True)
        ms.send(to='jwjrevg@yvg.com', subject='subject', body='body', _callback=cb)
        self.assertEqual('jwjrevg@yvg.com', captured['msg']['To'])

    def test_diversity_10(self):
        captured = {}
        def cb(**kw):
            captured['msg'] = kw['msg']
        ms = MailSender(debug=True)
        ms.send(to='pab@uhau.net', subject='subject', body='body', _callback=cb)
        self.assertEqual('pab@uhau.net', captured['msg']['To'])


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        captured = {}
        def cb(**kw):
            captured['msg'] = kw['msg']
        ms = MailSender(debug=True)
        ms.send(to=['mhzt@sblst.io'], subject='subject', body='body', _callback=cb)
        self.assertEqual('mhzt@sblst.io', captured['msg']['To'])

    def test_diversity_2(self):
        captured = {}
        def cb(**kw):
            captured['msg'] = kw['msg']
        ms = MailSender(debug=True)
        ms.send(to=['xesuwmc@hdu.org'], subject='subject', body='body', _callback=cb)
        self.assertEqual('xesuwmc@hdu.org', captured['msg']['To'])

    def test_diversity_3(self):
        captured = {}
        def cb(**kw):
            captured['msg'] = kw['msg']
        ms = MailSender(debug=True)
        ms.send(to=['ufae@pocopg.org'], subject='subject', body='body', _callback=cb)
        self.assertEqual('ufae@pocopg.org', captured['msg']['To'])

    def test_diversity_4(self):
        captured = {}
        def cb(**kw):
            captured['msg'] = kw['msg']
        ms = MailSender(debug=True)
        ms.send(to=['azxonnxb@oybfdcmb.org'], subject='subject', body='body', _callback=cb)
        self.assertEqual('azxonnxb@oybfdcmb.org', captured['msg']['To'])

    def test_diversity_5(self):
        captured = {}
        def cb(**kw):
            captured['msg'] = kw['msg']
        ms = MailSender(debug=True)
        ms.send(to=['pjwgvsqw@qcb.io'], subject='subject', body='body', _callback=cb)
        self.assertEqual('pjwgvsqw@qcb.io', captured['msg']['To'])

    def test_diversity_6(self):
        captured = {}
        def cb(**kw):
            captured['msg'] = kw['msg']
        ms = MailSender(debug=True)
        ms.send(to=['pcatca@mnauiua.io'], subject='subject', body='body', _callback=cb)
        self.assertEqual('pcatca@mnauiua.io', captured['msg']['To'])

    def test_diversity_7(self):
        captured = {}
        def cb(**kw):
            captured['msg'] = kw['msg']
        ms = MailSender(debug=True)
        ms.send(to=['dkmdxrl@efcd.org'], subject='subject', body='body', _callback=cb)
        self.assertEqual('dkmdxrl@efcd.org', captured['msg']['To'])

    def test_diversity_8(self):
        captured = {}
        def cb(**kw):
            captured['msg'] = kw['msg']
        ms = MailSender(debug=True)
        ms.send(to=['caqfw@ggn.com'], subject='subject', body='body', _callback=cb)
        self.assertEqual('caqfw@ggn.com', captured['msg']['To'])

    def test_diversity_9(self):
        captured = {}
        def cb(**kw):
            captured['msg'] = kw['msg']
        ms = MailSender(debug=True)
        ms.send(to=['lya@nkx.io'], subject='subject', body='body', _callback=cb)
        self.assertEqual('lya@nkx.io', captured['msg']['To'])

    def test_diversity_10(self):
        captured = {}
        def cb(**kw):
            captured['msg'] = kw['msg']
        ms = MailSender(debug=True)
        ms.send(to=['pfbhh@zuxy.net'], subject='subject', body='body', _callback=cb)
        self.assertEqual('pfbhh@zuxy.net', captured['msg']['To'])

