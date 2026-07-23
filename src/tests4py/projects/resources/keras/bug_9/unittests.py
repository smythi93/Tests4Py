import unittest


def _t4p_process_list_block(mode, names):
    import os
    import sys
    import types
    import json
    import importlib.util
    for name in ['keras', 'keras.backend', 'keras.backend.numpy_backend',
                 'docs', 'docs.structure']:
        m = types.ModuleType(name)
        if name in ('keras', 'docs'):
            m.__path__ = []
        sys.modules[name] = m
    ds = sys.modules['docs.structure']
    for a in ['EXCLUDE', 'PAGES', 'ROOT', 'template_np_implementation',
              'template_hidden_np_implementation']:
        setattr(ds, a, None)
    sys.modules['keras.backend'].numpy_backend = sys.modules['keras.backend.numpy_backend']
    path = os.path.join(os.getcwd(), 'docs', 'autogen.py')
    spec = importlib.util.spec_from_file_location('docs.autogen', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['docs.autogen'] = module
    spec.loader.exec_module(module)
    block_body = "\n".join("    %s: description of %s follows" % (n, n) for n in names)
    section_end = len(block_body)
    if mode == 'last':
        docstring = block_body + "\n    trailing text without blank line"
    else:
        docstring = block_body + "\n\n    trailing text after blank line"
    result = module.process_list_block(docstring, 0, section_end, 4, '@@MARKER@@')
    return json.dumps(list(result))


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('["@@MARKER@@\\n    trailing text without blank line", "kvgthjzn: description of kvgthjzn follows\\nmlso: description of mlso follows\\npkgunbyp: description of pkgunbyp follows"]', _t4p_process_list_block('last', ['kvgthjzn', 'mlso', 'pkgunbyp']))

    def test_diversity_2(self):
        self.assertEqual('["@@MARKER@@\\n    trailing text without blank line", "dxgerdhu: description of dxgerdhu follows\\njgpfv: description of jgpfv follows\\ndaifguao: description of daifguao follows\\nagwglx: description of agwglx follows"]', _t4p_process_list_block('last', ['dxgerdhu', 'jgpfv', 'daifguao', 'agwglx']))

    def test_diversity_3(self):
        self.assertEqual('["@@MARKER@@\\n    trailing text without blank line", "aqxrw: description of aqxrw follows\\ncnk: description of cnk follows\\nuiymiar: description of uiymiar follows\\ndbpw: description of dbpw follows\\npvg: description of pvg follows"]', _t4p_process_list_block('last', ['aqxrw', 'cnk', 'uiymiar', 'dbpw', 'pvg']))

    def test_diversity_4(self):
        self.assertEqual('["@@MARKER@@\\n    trailing text without blank line", "ddwqqhzo: description of ddwqqhzo follows\\nhktp: description of hktp follows\\nzvumpswf: description of zvumpswf follows\\ngwh: description of gwh follows\\niimfpc: description of iimfpc follows"]', _t4p_process_list_block('last', ['ddwqqhzo', 'hktp', 'zvumpswf', 'gwh', 'iimfpc']))

    def test_diversity_5(self):
        self.assertEqual('["@@MARKER@@\\n    trailing text without blank line", "lqvt: description of lqvt follows\\nlmhg: description of lmhg follows\\nkjnmvwu: description of kjnmvwu follows\\nlflpnez: description of lflpnez follows\\nymgawxjl: description of ymgawxjl follows"]', _t4p_process_list_block('last', ['lqvt', 'lmhg', 'kjnmvwu', 'lflpnez', 'ymgawxjl']))

    def test_diversity_6(self):
        self.assertEqual('["@@MARKER@@\\n    trailing text without blank line", "ckviy: description of ckviy follows\\nndvyqgkn: description of ndvyqgkn follows\\nrpuae: description of rpuae follows\\napzs: description of apzs follows"]', _t4p_process_list_block('last', ['ckviy', 'ndvyqgkn', 'rpuae', 'apzs']))

    def test_diversity_7(self):
        self.assertEqual('["@@MARKER@@\\n    trailing text without blank line", "spwt: description of spwt follows\\naqapirj: description of aqapirj follows\\nvqsxsgud: description of vqsxsgud follows\\ngmxs: description of gmxs follows"]', _t4p_process_list_block('last', ['spwt', 'aqapirj', 'vqsxsgud', 'gmxs']))

    def test_diversity_8(self):
        self.assertEqual('["@@MARKER@@\\n    trailing text without blank line", "kymmxfhr: description of kymmxfhr follows\\nvqfdkmv: description of vqfdkmv follows\\nowzzdwa: description of owzzdwa follows"]', _t4p_process_list_block('last', ['kymmxfhr', 'vqfdkmv', 'owzzdwa']))

    def test_diversity_9(self):
        self.assertEqual('["@@MARKER@@\\n    trailing text without blank line", "bfvz: description of bfvz follows\\nvwl: description of vwl follows\\nbdehfcp: description of bdehfcp follows"]', _t4p_process_list_block('last', ['bfvz', 'vwl', 'bdehfcp']))

    def test_diversity_10(self):
        self.assertEqual('["@@MARKER@@\\n    trailing text without blank line", "prot: description of prot follows\\ntwd: description of twd follows\\nzqla: description of zqla follows\\nhjpjg: description of hjpjg follows\\nvopwri: description of vopwri follows"]', _t4p_process_list_block('last', ['prot', 'twd', 'zqla', 'hjpjg', 'vopwri']))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('["@@MARKER@@s\\n\\n    trailing text after blank line", "yjcpsmnd: description of yjcpsmnd follows\\npjt: description of pjt follows\\nwqvkkkmp: description of wqvkkkmp follows\\nqwnqz: description of qwnqz follows\\nosle: description of osle follow"]', _t4p_process_list_block('sep', ['yjcpsmnd', 'pjt', 'wqvkkkmp', 'qwnqz', 'osle']))

    def test_diversity_2(self):
        self.assertEqual('["@@MARKER@@s\\n\\n    trailing text after blank line", "oqsvdhye: description of oqsvdhye follows\\ngpb: description of gpb follows\\ncjdy: description of cjdy follows\\nywwuiluv: description of ywwuiluv follows\\nqxzshz: description of qxzshz follow"]', _t4p_process_list_block('sep', ['oqsvdhye', 'gpb', 'cjdy', 'ywwuiluv', 'qxzshz']))

    def test_diversity_3(self):
        self.assertEqual('["@@MARKER@@s\\n\\n    trailing text after blank line", "vwudhcue: description of vwudhcue follows\\nyxfzw: description of yxfzw follows\\ncxu: description of cxu follow"]', _t4p_process_list_block('sep', ['vwudhcue', 'yxfzw', 'cxu']))

    def test_diversity_4(self):
        self.assertEqual('["@@MARKER@@s\\n\\n    trailing text after blank line", "praaocb: description of praaocb follows\\nfpguq: description of fpguq follows\\namvq: description of amvq follows\\nexlrman: description of exlrman follows\\nvistg: description of vistg follow"]', _t4p_process_list_block('sep', ['praaocb', 'fpguq', 'amvq', 'exlrman', 'vistg']))

    def test_diversity_5(self):
        self.assertEqual('["@@MARKER@@s\\n\\n    trailing text after blank line", "aqln: description of aqln follows\\nfixjons: description of fixjons follows\\nczrxpc: description of czrxpc follows\\nxir: description of xir follow"]', _t4p_process_list_block('sep', ['aqln', 'fixjons', 'czrxpc', 'xir']))

    def test_diversity_6(self):
        self.assertEqual('["@@MARKER@@s\\n\\n    trailing text after blank line", "qmegus: description of qmegus follows\\nvnqe: description of vnqe follow"]', _t4p_process_list_block('sep', ['qmegus', 'vnqe']))

    def test_diversity_7(self):
        self.assertEqual('["@@MARKER@@s\\n\\n    trailing text after blank line", "woxam: description of woxam follows\\nylzwwk: description of ylzwwk follows\\ndjhtrmk: description of djhtrmk follows\\nycx: description of ycx follows\\nprbmi: description of prbmi follow"]', _t4p_process_list_block('sep', ['woxam', 'ylzwwk', 'djhtrmk', 'ycx', 'prbmi']))

    def test_diversity_8(self):
        self.assertEqual('["@@MARKER@@s\\n\\n    trailing text after blank line", "ard: description of ard follows\\nvdtyo: description of vdtyo follows\\nfaj: description of faj follow"]', _t4p_process_list_block('sep', ['ard', 'vdtyo', 'faj']))

    def test_diversity_9(self):
        self.assertEqual('["@@MARKER@@s\\n\\n    trailing text after blank line", "kbvytha: description of kbvytha follows\\nosjxnd: description of osjxnd follows\\nijvzxwck: description of ijvzxwck follows\\nnhg: description of nhg follows\\nsgxpn: description of sgxpn follow"]', _t4p_process_list_block('sep', ['kbvytha', 'osjxnd', 'ijvzxwck', 'nhg', 'sgxpn']))

    def test_diversity_10(self):
        self.assertEqual('["@@MARKER@@s\\n\\n    trailing text after blank line", "ndwpbe: description of ndwpbe follows\\nochw: description of ochw follows\\ngdyryw: description of gdyryw follow"]', _t4p_process_list_block('sep', ['ndwpbe', 'ochw', 'gdyryw']))
