import unittest

import pysnooper
from python_toolbox import temp_file_tools


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        with temp_file_tools.create_temp_folder(prefix="pysnooper") as folder:
            path = folder / "test_1.log"

            @pysnooper.snoop(str(path))
            def function_1(foo):
                x = 42
                y = 2
                return x / y

            result = function_1("test")
            self.assertEqual(21, result)
            self.assertTrue(path.exists())

    def test_diversity_2(self):
        with temp_file_tools.create_temp_folder(prefix="pysnooper") as folder:
            path = folder / "test_2.log"

            @pysnooper.snoop(str(path))
            def function_2(x):
                if x < 1:
                    return 1
                else:
                    return x * function_2(x - 1)

            result = function_2(4)
            self.assertEqual(24, result)
            self.assertTrue(path.exists())

    def test_diversity_3(self):
        with temp_file_tools.create_temp_folder(prefix="pysnooper") as folder:
            path = folder / "test_3.log"

            @pysnooper.snoop(str(path))
            def function_3(x):
                return x

            result = function_3(4)
            self.assertEqual(4, result)
            self.assertTrue(path.exists())

    def test_diversity_4(self):
        with temp_file_tools.create_temp_folder(prefix="pysnooper") as folder:
            path = folder / "test_4.log"

            @pysnooper.snoop(str(path))
            def function_4(x, y, z):
                if y < z:
                    if x < y:
                        return y
                    elif x < z:
                        return x
                else:
                    if x > y:
                        return y
                    elif x > z:
                        return x
                return z

            result = function_4(2, 3, 1)
            self.assertEqual(2, result)
            self.assertTrue(path.exists())

    def test_diversity_5(self):
        with temp_file_tools.create_temp_folder(prefix="pysnooper") as folder:
            path = folder / "test_5.log"

            @pysnooper.snoop(str(path))
            def function_5(m, n):
                if m <= 0:
                    return n + 1
                elif n <= 0:
                    return function_5(m - 1, 1)
                else:
                    return function_5(m - 1, function_5(m, n - 1))

            result = function_5(3, 2)
            self.assertEqual(29, result)
            self.assertTrue(path.exists())

    def test_diversity_6(self):
        with temp_file_tools.create_temp_folder(prefix="pysnooper") as folder:
            path = folder / "test_6.log"

            @pysnooper.snoop(str(path))
            def function_6(x, y):
                z = 2
                return x**z - z * x * y + y**z

            result = function_6(2, 2)
            self.assertEqual(0, result)
            self.assertTrue(path.exists())

    def test_diversity_7(self):
        with temp_file_tools.create_temp_folder(prefix="pysnooper") as folder:
            path = folder / "test_7.log"

            @pysnooper.snoop(str(path))
            def function_7(x):
                return x * x

            result = function_7(4)
            self.assertEqual(16, result)
            self.assertTrue(path.exists())

    def test_diversity_8(self):
        with temp_file_tools.create_temp_folder(prefix="pysnooper") as folder:
            path = folder / "test_7.log"

            @pysnooper.snoop(str(path))
            def function_8(x):
                i = 0
                while i < len(x):
                    i += 1
                return i

            result = function_8([1, 2, 3, 4])
            self.assertEqual(4, result)
            self.assertTrue(path.exists())

    def test_diversity_9(self):
        with temp_file_tools.create_temp_folder(prefix="pysnooper") as folder:
            path = folder / "test_9.log"

            @pysnooper.snoop(str(path))
            def function_9(x):
                r = 0
                for i in x:
                    r += i
                return r

            result = function_9([1, 2, 3, 4])
            self.assertEqual(10, result)
            self.assertTrue(path.exists())

    def test_diversity_10(self):
        with temp_file_tools.create_temp_folder(prefix="pysnooper") as folder:
            path = folder / "test_10.log"

            @pysnooper.snoop(str(path))
            def function_10(n, k):
                def fac(x):
                    if x <= 0:
                        return 1
                    return x * fac(x - 1)

                return fac(n) / (fac(k) * fac(n - k))

            result = function_10(4, 2)
            self.assertAlmostEqual(6, result, places=10)
            self.assertTrue(path.exists())


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        @pysnooper.snoop()
        def function_1(foo):
            x = 42
            y = 2
            return x / y

        result = function_1("test")
        self.assertEqual(21, result)

    def test_diversity_2(self):
        @pysnooper.snoop()
        def function_2(x):
            if x < 1:
                return 1
            else:
                return x * function_2(x - 1)

        result = function_2(4)
        self.assertEqual(24, result)

    def test_diversity_3(self):
        @pysnooper.snoop()
        def function_3(x):
            return x

        result = function_3(4)
        self.assertEqual(4, result)

    def test_diversity_4(self):
        @pysnooper.snoop()
        def function_4(x, y, z):
            if y < z:
                if x < y:
                    return y
                elif x < z:
                    return x
            else:
                if x > y:
                    return y
                elif x > z:
                    return x
            return z

        result = function_4(2, 3, 1)
        self.assertEqual(2, result)

    def test_diversity_5(self):
        @pysnooper.snoop()
        def function_5(m, n):
            if m <= 0:
                return n + 1
            elif n <= 0:
                return function_5(m - 1, 1)
            else:
                return function_5(m - 1, function_5(m, n - 1))

        result = function_5(3, 2)
        self.assertEqual(29, result)

    def test_diversity_6(self):
        @pysnooper.snoop()
        def function_6(x, y):
            z = 2
            return x**z - z * x * y + y**z

        result = function_6(2, 2)
        self.assertEqual(0, result)

    def test_diversity_7(self):
        @pysnooper.snoop()
        def function_7(x):
            return x * x

        result = function_7(4)
        self.assertEqual(16, result)

    def test_diversity_8(self):
        @pysnooper.snoop()
        def function_8(x):
            i = 0
            while i < len(x):
                i += 1
            return i

        result = function_8([1, 2, 3, 4])
        self.assertEqual(4, result)

    def test_diversity_9(self):
        @pysnooper.snoop()
        def function_9(x):
            r = 0
            for i in x:
                r += i
            return r

        result = function_9([1, 2, 3, 4])
        self.assertEqual(10, result)

    def test_diversity_10(self):
        @pysnooper.snoop()
        def function_10(n, k):
            def fac(x):
                if x <= 0:
                    return 1
                return x * fac(x - 1)

            return fac(n) / (fac(k) * fac(n - k))

        result = function_10(4, 2)
        self.assertAlmostEqual(6, result, places=10)
