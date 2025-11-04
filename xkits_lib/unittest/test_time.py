# coding:utf-8

from datetime import datetime
from datetime import timezone
from datetime import tzinfo
from unittest import TestCase
from unittest import main

from xkits_lib.time import Timestamp


class TestTimestamp(TestCase):

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

    def test_now(self):
        self.assertIsInstance(timestamp := Timestamp().dump(), str)
        self.assertIsInstance(ts := Timestamp.load(timestamp), Timestamp)
        self.assertIsInstance(ts.delta, float)
        self.assertIsNotNone(ts.value.tzinfo)
        self.assertEqual(str(ts), timestamp)

    def test_ts(self):
        self.assertIsInstance(now := datetime.now(), datetime)
        self.assertIsInstance(timestamp := Timestamp(now).dump(), str)
        self.assertIsInstance(ts := Timestamp.load(timestamp), Timestamp)
        self.assertEqual(ts.value.replace(microsecond=0), now.astimezone().replace(microsecond=0))  # noqa:E501
        self.assertIsInstance(ts.delta, float)
        self.assertIsNotNone(ts.value.tzinfo)
        self.assertEqual(str(ts), timestamp)

    def test_tz(self):
        self.assertIsInstance(tz := timezone.utc, tzinfo)
        self.assertIsInstance(now := datetime.now(tz), datetime)
        self.assertIsInstance(timestamp := Timestamp(now).dump(), str)
        self.assertIsInstance(ts := Timestamp.load(timestamp), Timestamp)
        self.assertIs(ts.value.tzinfo, timezone.utc)
        self.assertIsInstance(ts.delta, float)
        self.assertEqual(str(ts), timestamp)
        self.assertEqual(ts.value.replace(microsecond=0), now.replace(microsecond=0))  # noqa:E501


if __name__ == "__main__":
    main()
