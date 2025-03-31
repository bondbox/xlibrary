# coding:utf-8

import unittest

from xkits_lib.unit import DataUnit


class TestDataUnit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_bytes(self):
        self.assertEqual(DataUnit(123).bytes, 123)
        self.assertEqual(DataUnit(123456).bytes, 123456)
        self.assertEqual(DataUnit(123456789).bytes, 123456789)

    def test_bytes_n(self):
        self.assertEqual(DataUnit(-123).bytes, -123)
        self.assertEqual(DataUnit(-123456).bytes, -123456)
        self.assertEqual(DataUnit(-123456789).bytes, -123456789)

    def test_human(self):
        self.assertEqual(DataUnit(0).human, "0")
        self.assertEqual(DataUnit(999).human, "999")
        self.assertEqual(DataUnit(1000).human, "1.00k")
        self.assertEqual(DataUnit(1000**2).human, "1.00M")
        self.assertEqual(DataUnit(1000**3).human, "1.00G")
        self.assertEqual(DataUnit(1000**4).human, "1.00T")
        self.assertEqual(DataUnit(1000**5).human, "1.00P")
        self.assertEqual(DataUnit(1000**6).human, "1.00E")
        self.assertEqual(DataUnit(1000**7).human, "1.00Z")
        self.assertEqual(DataUnit(1000**8).human, "1.00Y")

    def test_human_n(self):
        self.assertEqual(DataUnit(-1).human, "-1")
        self.assertEqual(DataUnit(-1000).human, "-1.00k")
        self.assertEqual(DataUnit(-1000**2).human, "-1.00M")
        self.assertEqual(DataUnit(-1000**3).human, "-1.00G")
        self.assertEqual(DataUnit(-1000**4).human, "-1.00T")
        self.assertEqual(DataUnit(-1000**5).human, "-1.00P")
        self.assertEqual(DataUnit(-1000**6).human, "-1.00E")
        self.assertEqual(DataUnit(-1000**7).human, "-1.00Z")
        self.assertEqual(DataUnit(-1000**8).human, "-1.00Y")

    def test_ihuman(self):
        self.assertEqual(DataUnit(0).ihuman, "0B")
        self.assertEqual(DataUnit(1023).ihuman, "1023B")
        self.assertEqual(DataUnit(1024).ihuman, "1.00KiB")
        self.assertEqual(DataUnit(1024**2).ihuman, "1.00MiB")
        self.assertEqual(DataUnit(1024**3).ihuman, "1.00GiB")
        self.assertEqual(DataUnit(1024**4).ihuman, "1.00TiB")
        self.assertEqual(DataUnit(1024**5).ihuman, "1.00PiB")
        self.assertEqual(DataUnit(1024**6).ihuman, "1.00EiB")
        self.assertEqual(DataUnit(1024**7).ihuman, "1.00ZiB")
        self.assertEqual(DataUnit(1024**8).ihuman, "1.00YiB")

    def test_ihuman_n(self):
        self.assertEqual(DataUnit(-1).ihuman, "-1B")
        self.assertEqual(DataUnit(-1024).ihuman, "-1.00KiB")
        self.assertEqual(DataUnit(-1024**2).ihuman, "-1.00MiB")
        self.assertEqual(DataUnit(-1024**3).ihuman, "-1.00GiB")
        self.assertEqual(DataUnit(-1024**4).ihuman, "-1.00TiB")
        self.assertEqual(DataUnit(-1024**5).ihuman, "-1.00PiB")
        self.assertEqual(DataUnit(-1024**6).ihuman, "-1.00EiB")
        self.assertEqual(DataUnit(-1024**7).ihuman, "-1.00ZiB")
        self.assertEqual(DataUnit(-1024**8).ihuman, "-1.00YiB")


if __name__ == "__main__":
    unittest.main()
