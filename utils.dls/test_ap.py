"""
Not really unit tests, but tests to show whether data has
correctly been loaded into the aphla database.
"""
from pkg_resources import require
require('cothread')
from cothread.catools import caget
import unittest
import sys
sys.path.append('..')
import aphla as ap


class CommonTests(object):
    """
    Any tests that apply to all ring modes.
    This class doesn't inherit from unittest.TestCase since
    I don't want tests to be run directly.
    """

    def test_elements_loaded(self):
        elements = ap.getElements('*')
        # 2405 in THERING plus DCCT
        self.assertEqual(len(elements), 2406)

    def test_quads_loaded(self):
        q = ap.getElements('QUAD')
        self.assertEqual(q[0].pv(handle='readback'), ['SR01A-PC-Q1D-01:I'])
        self.assertEqual(q[0].pv(handle='setpoint'), ['SR01A-PC-Q1D-01:SETI'])
        self.assertEqual(q[-1].pv(handle='readback'), ['SR24A-PC-Q1D-10:I'])
        self.assertEqual(q[-1].pv(handle='setpoint'), ['SR24A-PC-Q1D-10:SETI'])
        self.assertEqual(len(q), 248)

    def test_bend_loaded(self):
        b = ap.getElements('BEND')
        self.assertEqual(len(b), 48)

    def test_sexts_loaded(self):
        q = ap.getElements('SEXT')
        self.assertEqual(q[0].pv(handle='readback'), ['SR01A-PC-S1D-01:I'])
        self.assertEqual(q[0].pv(handle='setpoint'), ['SR01A-PC-S1D-01:SETI'])
        self.assertEqual(q[-1].pv(handle='readback'), ['SR24A-PC-S1D-07:I'])
        self.assertEqual(q[-1].pv(handle='setpoint'), ['SR24A-PC-S1D-07:SETI'])
        self.assertEqual(len(q), 168)

    def test_correctors_loaded(self):
        for plane in ('H', 'V'):
            device = '{}STR'.format(plane)
            c = ap.getElements(device)
            self.assertEqual(c[0].pv(handle='readback'), ['SR01A-PC-{}-01:I'.format(device)])
            self.assertEqual(c[0].pv(handle='setpoint'), ['SR01A-PC-{}-01:SETI'.format(device)])
            self.assertEqual(c[-1].pv(handle='readback'), ['SR24A-PC-{}-07:I'.format(device)])
            self.assertEqual(c[-1].pv(handle='setpoint'), ['SR24A-PC-{}-07:SETI'.format(device)])
            self.assertEqual(len(c), 172)

    def test_quad_k_value(self):
        q = ap.getElements('QUAD')
        self.assertTrue(hasattr(q[0], 'k1'))

    def test_rf_cavity_loaded(self):
        r = ap.getElements('RF')
        self.assertEqual(len(r), 1)
        cav = r[0]
        self.assertEqual(cav.pv(field='f', handle='readback'),
                         ['LI-RF-MOSC-01:FREQ'])
        self.assertEqual(cav.pv(field='f', handle='setpoint'),
                         ['LI-RF-MOSC-01:FREQ_SET'])

    def test_current(self):
        # Just fetched using channel access.
        current = ap.getCurrent('DCCT')
        ca_current = caget('SR-DI-DCCT-01:SIGNAL')
        self.assertAlmostEqual(current, ca_current, 3)

    def test_orbit(self):
        orbit = ap.getOrbit(spos=True)
        self.assertTrue(orbit.shape == (173, 3))

    def test_quad_params(self, q1bk):
        q1b = ap.getElements('Q1B')
        for q in q1b:
            self.assertAlmostEqual(q.k1, q1bk, 3)

    def test_sext_params(self, s1dk2):
        s1d = ap.getElements('S1D')
        for s in s1d:
            self.assertAlmostEqual(s.k2, s1dk2, 3)

    def test_ring_length(self):
        length = sum(e.length for e in ap.getElements('*'))
        self.assertAlmostEqual(length, 561.6)

class TestSRLETHz(CommonTests, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ap.machines.load('SRLETHz')
        ap.machines.use('SR')

    def test_quad_params(self):
        CommonTests.test_quad_params(self, -0.0499)

    def test_sext_params(self):
        CommonTests.test_sext_params(self, 6.2004)


class TestSRI0913(CommonTests, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ap.machines.load('SRI0913')
        ap.machines.use('SR')

    def test_quad_params(self):
        CommonTests.test_quad_params(self, -1.2286)

    def test_sext_params(self):
        CommonTests.test_sext_params(self, 6.9)


class TestSRI21(CommonTests, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ap.machines.load('SRI21')
        ap.machines.use('SR')

    def test_quad_params(self):
        CommonTests.test_quad_params(self, -1.2149)

    def test_sext_params(self):
        CommonTests.test_sext_params(self, 6.9)


if __name__ == '__main__':
    unittest.main()
