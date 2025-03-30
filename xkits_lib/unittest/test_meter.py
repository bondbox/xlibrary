# coding:utf-8

import unittest
from unittest import mock

from xkits_lib import meter


class TestTimeMeter(unittest.TestCase):

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

    @mock.patch.object(meter, "time")
    def test_runtime(self, mock_time):
        mock_time.side_effect = [1.0, 2.0, 3.0, 4.0, 5.0]
        timer = meter.TimeMeter(startup=False)
        self.assertEqual(timer.created_time, 1.0)
        self.assertEqual(timer.started_time, 0.0)
        self.assertEqual(timer.stopped_time, 0.0)
        self.assertEqual(timer.runtime, 0.0)
        timer.startup()
        self.assertEqual(timer.created_time, 1.0)
        self.assertEqual(timer.started_time, 2.0)
        self.assertEqual(timer.stopped_time, 0.0)
        self.assertEqual(timer.runtime, 1.0)
        self.assertEqual(timer.runtime, 2.0)
        self.assertEqual(timer.runtime, 3.0)

    @mock.patch.object(meter, "time")
    def test_restart(self, mock_time):
        mock_time.side_effect = [1.0, 2.0, 3.0]
        timer = meter.TimeMeter(startup=True)
        self.assertEqual(timer.created_time, 1.0)
        self.assertEqual(timer.started_time, 1.0)
        self.assertEqual(timer.stopped_time, 0.0)
        self.assertTrue(timer.started)
        self.assertFalse(timer.stopped)
        timer.restart()
        self.assertEqual(timer.created_time, 1.0)
        self.assertEqual(timer.started_time, 2.0)
        self.assertEqual(timer.stopped_time, 0.0)
        self.assertTrue(timer.started)
        self.assertFalse(timer.stopped)
        timer.restart()
        self.assertEqual(timer.created_time, 1.0)
        self.assertEqual(timer.started_time, 3.0)
        self.assertEqual(timer.stopped_time, 0.0)
        self.assertTrue(timer.started)
        self.assertFalse(timer.stopped)

    @mock.patch.object(meter, "time")
    def test_startup(self, mock_time):
        mock_time.side_effect = [1.0, 2.0]
        timer = meter.TimeMeter(startup=False)
        self.assertEqual(timer.created_time, 1.0)
        self.assertEqual(timer.started_time, 0.0)
        self.assertEqual(timer.stopped_time, 0.0)
        self.assertFalse(timer.started)
        self.assertFalse(timer.stopped)
        timer.startup()
        self.assertEqual(timer.created_time, 1.0)
        self.assertEqual(timer.started_time, 2.0)
        self.assertEqual(timer.stopped_time, 0.0)
        self.assertTrue(timer.started)
        self.assertFalse(timer.stopped)
        timer.startup()
        self.assertEqual(timer.created_time, 1.0)
        self.assertEqual(timer.started_time, 2.0)
        self.assertEqual(timer.stopped_time, 0.0)
        self.assertTrue(timer.started)
        self.assertFalse(timer.stopped)

    @mock.patch.object(meter, "time")
    def test_shutdown(self, mock_time):
        mock_time.side_effect = [1.0, 2.0]
        timer = meter.TimeMeter(startup=True)
        self.assertEqual(timer.created_time, 1.0)
        self.assertEqual(timer.started_time, 1.0)
        self.assertEqual(timer.stopped_time, 0.0)
        self.assertTrue(timer.started)
        self.assertFalse(timer.stopped)
        timer.shutdown()
        self.assertEqual(timer.created_time, 1.0)
        self.assertEqual(timer.started_time, 1.0)
        self.assertEqual(timer.stopped_time, 2.0)
        self.assertFalse(timer.started)
        self.assertTrue(timer.stopped)
        timer.shutdown()
        self.assertEqual(timer.created_time, 1.0)
        self.assertEqual(timer.started_time, 1.0)
        self.assertEqual(timer.stopped_time, 2.0)
        self.assertFalse(timer.started)
        self.assertTrue(timer.stopped)

    @mock.patch.object(meter, "time")
    @mock.patch.object(meter, "sleep")
    def test_alarm(self, mock_sleep, mock_time):
        mock_time.side_effect = [1.0, 2.0, 3.0, 5.0]
        timer = meter.TimeMeter(startup=False)
        self.assertEqual(timer.created_time, 1.0)
        self.assertEqual(timer.started_time, 0.0)
        self.assertEqual(timer.stopped_time, 0.0)
        timer.alarm(3.0)
        self.assertEqual(timer.created_time, 1.0)
        self.assertEqual(timer.started_time, 2.0)
        self.assertEqual(timer.stopped_time, 0.0)
        mock_sleep.assert_called_once_with(2.0)

    @mock.patch.object(meter, "time")
    def test_reset(self, mock_time):
        mock_time.side_effect = [1.0]
        timer = meter.TimeMeter(startup=True)
        self.assertEqual(timer.created_time, 1.0)
        self.assertEqual(timer.started_time, 1.0)
        self.assertEqual(timer.stopped_time, 0.0)
        timer.reset()
        self.assertEqual(timer.created_time, 1.0)
        self.assertEqual(timer.started_time, 0.0)
        self.assertEqual(timer.stopped_time, 0.0)


class TestDownMeter(unittest.TestCase):

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

    @mock.patch.object(meter, "time")
    def test_downtime(self, mock_time):
        mock_time.side_effect = [1.0, 2.0, 3.0, 4.0, 5.0]
        countdown = meter.DownMeter(lifetime=3)
        self.assertEqual(countdown.created_time, 1.0)
        self.assertEqual(countdown.started_time, 1.0)
        self.assertEqual(countdown.stopped_time, 0.0)
        self.assertEqual(countdown.lifetime, 3.0)
        self.assertEqual(countdown.downtime, 2.0)
        self.assertEqual(countdown.downtime, 1.0)
        self.assertEqual(countdown.downtime, 0.0)
        self.assertEqual(countdown.downtime, -1.0)

    @mock.patch.object(meter, "time")
    def test_downtime_0(self, mock_time):
        mock_time.side_effect = [1.0]
        countdown = meter.DownMeter(lifetime=0)
        self.assertEqual(countdown.created_time, 1.0)
        self.assertEqual(countdown.started_time, 1.0)
        self.assertEqual(countdown.stopped_time, 0.0)
        self.assertEqual(countdown.lifetime, 0.0)
        self.assertEqual(countdown.downtime, 0.0)
        self.assertFalse(countdown.expired)
        self.assertFalse(countdown.expired)
        self.assertFalse(countdown.expired)

    @mock.patch.object(meter, "time")
    def test_expired(self, mock_time):
        mock_time.side_effect = [1.0, 2.0, 3.0, 4.0, 5.0]
        countdown = meter.DownMeter(lifetime=3)
        self.assertEqual(countdown.created_time, 1.0)
        self.assertEqual(countdown.started_time, 1.0)
        self.assertEqual(countdown.stopped_time, 0.0)
        self.assertEqual(countdown.lifetime, 3.0)
        self.assertFalse(countdown.expired)
        self.assertFalse(countdown.expired)
        self.assertFalse(countdown.expired)
        self.assertTrue(countdown.expired)

    @mock.patch.object(meter, "time")
    def test_reset(self, mock_time):
        mock_time.side_effect = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
        countdown = meter.DownMeter(lifetime=1)
        self.assertEqual(countdown.created_time, 1.0)
        self.assertEqual(countdown.started_time, 1.0)
        self.assertEqual(countdown.stopped_time, 0.0)
        self.assertEqual(countdown.lifetime, 1.0)
        self.assertEqual(countdown.downtime, 0.0)
        countdown.reset()
        self.assertEqual(countdown.created_time, 1.0)
        self.assertEqual(countdown.started_time, 3.0)
        self.assertEqual(countdown.stopped_time, 0.0)
        self.assertEqual(countdown.lifetime, 1.0)
        self.assertEqual(countdown.downtime, 0.0)
        countdown.reset()
        self.assertEqual(countdown.created_time, 1.0)
        self.assertEqual(countdown.started_time, 5.0)
        self.assertEqual(countdown.stopped_time, 0.0)
        self.assertEqual(countdown.lifetime, 1.0)
        self.assertEqual(countdown.downtime, 0.0)

    @mock.patch.object(meter, "time")
    def test_renew(self, mock_time):
        mock_time.side_effect = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
        countdown = meter.DownMeter(lifetime=1)
        self.assertEqual(countdown.created_time, 1.0)
        self.assertEqual(countdown.started_time, 1.0)
        self.assertEqual(countdown.stopped_time, 0.0)
        self.assertEqual(countdown.lifetime, 1.0)
        self.assertEqual(countdown.downtime, 0.0)
        countdown.renew(lifetime=2)
        self.assertEqual(countdown.created_time, 1.0)
        self.assertEqual(countdown.started_time, 3.0)
        self.assertEqual(countdown.stopped_time, 0.0)
        self.assertEqual(countdown.lifetime, 2.0)
        self.assertEqual(countdown.downtime, 1.0)
        countdown.renew()
        self.assertEqual(countdown.created_time, 1.0)
        self.assertEqual(countdown.started_time, 5.0)
        self.assertEqual(countdown.stopped_time, 0.0)
        self.assertEqual(countdown.lifetime, 2.0)
        self.assertEqual(countdown.downtime, 1.0)

    @mock.patch.object(meter, "time")
    def test_shutdown(self, mock_time):
        mock_time.side_effect = [1.0, 2.0, 3.0]
        countdown = meter.DownMeter(lifetime=3)
        self.assertEqual(countdown.created_time, 1.0)
        self.assertEqual(countdown.started_time, 1.0)
        self.assertEqual(countdown.stopped_time, 0.0)
        self.assertEqual(countdown.lifetime, 3.0)
        self.assertEqual(countdown.downtime, 2.0)
        self.assertEqual(countdown.downtime, 1.0)
        self.assertRaises(RuntimeError, countdown.shutdown)


class TestTsCountMeter(unittest.TestCase):

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

    def test_CountMeter_str(self):
        counter = meter.CountMeter()
        self.assertEqual(str(counter), f"CountMeter({id(counter)})")

    def test_StatusCountMeter(self):
        counter = meter.StatusCountMeter()
        self.assertEqual(str(counter), f"StatusCountMeter({id(counter)})")
        self.assertEqual(counter.total, 0)
        self.assertEqual(counter.success, 0)
        self.assertEqual(counter.failure, 0)
        counter.inc()
        self.assertEqual(counter.total, 1)
        self.assertEqual(counter.success, 1)
        self.assertEqual(counter.failure, 0)
        counter.inc(True)
        self.assertEqual(counter.total, 2)
        self.assertEqual(counter.success, 2)
        self.assertEqual(counter.failure, 0)
        counter.inc(False)
        self.assertEqual(counter.total, 3)
        self.assertEqual(counter.success, 2)
        self.assertEqual(counter.failure, 1)
        counter.dec()
        self.assertEqual(counter.total, 4)
        self.assertEqual(counter.success, 2)
        self.assertEqual(counter.failure, 2)

    def test_add(self):
        counter = meter.TsCountMeter()
        self.assertEqual(counter.total, 0)
        self.assertEqual(counter.updated_time, 0.0)
        self.assertLessEqual(counter.created_time, meter.time())
        self.assertRaises(ValueError, counter.inc, 0)
        self.assertEqual(counter.updated_time, 0.0)
        self.assertEqual(counter.total, 0)
        self.assertEqual(counter.inc(1), 1)
        self.assertEqual(counter.total, 1)
        self.assertGreaterEqual(counter.updated_time, counter.created_time)
        self.assertRaises(RuntimeError, counter.dec, 1)
        self.assertEqual(counter.total, 1)
        self.assertEqual(counter.inc(2), 3)
        self.assertEqual(counter.total, 3)

    def test_sub(self):
        counter = meter.TsCountMeter(allow_sub=True)
        self.assertEqual(counter.total, 0)
        self.assertEqual(counter.updated_time, 0.0)
        self.assertLessEqual(counter.created_time, meter.time())
        self.assertRaises(ValueError, counter.dec, 0)
        self.assertEqual(counter.updated_time, 0.0)
        self.assertEqual(counter.total, 0)
        self.assertEqual(counter.inc(10), 10)
        self.assertEqual(counter.total, 10)
        self.assertGreaterEqual(counter.updated_time, counter.created_time)
        self.assertEqual(counter.dec(2), 8)
        self.assertEqual(counter.total, 8)
        self.assertEqual(counter.dec(5), 3)
        self.assertEqual(counter.total, 3)
        self.assertEqual(counter.dec(8), -5)
        self.assertEqual(counter.total, -5)
        self.assertRaises(ValueError, counter.dec, -1)
        self.assertEqual(counter.total, -5)


if __name__ == "__main__":
    unittest.main()
