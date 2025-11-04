# coding:utf-8

from dataclasses import dataclass
import sys
from typing import Callable
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional
from typing import Set
from typing import Tuple
from typing import Union
from unittest import TestCase
from unittest import main

from xkits_lib.annot import each_annot


@dataclass
class FakeSuper():
    index: int


@dataclass
class FakeChild(FakeSuper):
    alias: str


class TestType(TestCase):

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

    def test_each(self):
        if sys.version_info >= (3, 8):  # Python >= 3.8
            self.assertEqual(each_annot(Callable[[str, int], bool]), (Callable[[str, int], bool],))  # noqa:E501
            self.assertEqual(each_annot(Optional[Union[int, str]]), (int, str, type(None)))  # noqa:E501
            self.assertEqual(each_annot(Union[int, Optional[str]]), (int, str, type(None)))  # noqa:E501
            self.assertEqual(each_annot(Union[int, Dict[str, int]]), (int, Dict[str, int]))  # noqa:E501
            self.assertEqual(each_annot(Union[int, Union[str, int]]), (int, str))  # noqa:E501
            self.assertEqual(each_annot(Union[int, List[int]]), (int, List[int]))  # noqa:E501
            self.assertEqual(each_annot(Union[int, None]), (int, type(None)))
            self.assertEqual(each_annot(Tuple[str, ...]), (Tuple[str, ...],))
            self.assertEqual(each_annot(Dict[str, int]), (Dict[str, int],))
            self.assertEqual(each_annot(Optional[int]), (int, type(None)))
            self.assertEqual(each_annot(List[bool]), (List[bool],))
            self.assertEqual(each_annot(Literal[1]), (Literal[1],))
            self.assertEqual(each_annot(Set[float]), (Set[float],))
            self.assertEqual(each_annot(bytearray), (bytearray,))
            self.assertEqual(each_annot(FakeChild), (FakeChild,))
            self.assertEqual(each_annot(Callable), (Callable,))
            self.assertEqual(each_annot(Union[int]), (int,))
            self.assertEqual(each_annot(bytes), (bytes,))
            self.assertEqual(each_annot(float), (float,))
            self.assertEqual(each_annot(tuple), (tuple,))
            self.assertEqual(each_annot(bool), (bool,))
            self.assertEqual(each_annot(dict), (dict,))
            self.assertEqual(each_annot(list), (list,))
            self.assertEqual(each_annot(int), (int,))
            self.assertEqual(each_annot(set), (set,))
            self.assertEqual(each_annot(str), (str,))
            # check error
            self.assertRaises(TypeError, each_annot, Literal)

        if sys.version_info >= (3, 9):  # Python >= 3.9
            # TypeError: 'type' object is not subscriptable in Python < 3.9
            self.assertEqual(each_annot(eval("tuple[str, ...]")), (eval("tuple[str, ...]"),))  # noqa:E501
            self.assertEqual(each_annot(eval("dict[str, int]")), (eval("dict[str, int]"),))  # noqa:E501
            self.assertEqual(each_annot(eval("list[bool]")), (eval("list[bool]"),))  # noqa:E501
            self.assertEqual(each_annot(eval("set[float]")), (eval("set[float]"),))  # noqa:E501

        if sys.version_info >= (3, 10):  # Python >= 3.10
            self.assertEqual(each_annot(eval("Optional[str | int]")), (int, str, type(None)))  # noqa:E501
            self.assertEqual(each_annot(eval("Optional[str] | int")), (str, type(None), int))  # noqa:E501
            self.assertEqual(each_annot(eval("Union[str, int | str]")), (str, int))  # noqa:E501
            self.assertEqual(each_annot(eval("str | Union[int, str]")), (str, int))  # noqa:E501
            self.assertEqual(each_annot(eval("str | None")), (str, type(None)))
            self.assertEqual(each_annot(eval("str | int")), (str, int))


if __name__ == "__main__":
    main()
