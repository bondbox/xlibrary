# coding:utf-8

import unittest

from xkits_lib.path import Workspace


class TestWorkspace(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.workspace = Workspace()

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_chdir(self):
        self.assertRaises(AssertionError, self.workspace.popd)
        self.workspace.pushd("xkits_lib")
        self.workspace.cwd = "unittest"
        self.workspace.popd()
        self.workspace.popd()
        self.assertRaises(AssertionError, self.workspace.popd)


if __name__ == "__main__":
    unittest.main()
