"""
Not really unit tests, but tests to show whether data has
correctly been loaded into the aphla database.
"""
from pkg_resources import require
require('cothread')
require('h5py')
require('mock')
import cothread
import unittest
import mock
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
        self.assertEqual(len(elements), self.nelements)

    def test_quads_loaded(self):
        q = ap.getElements('QUAD')
        self.assertEqual(q[0].pv(handle='readback'), ['SR01A-PC-Q1D-01:I'])
        self.assertEqual(q[0].pv(handle='setpoint'), ['SR01A-PC-Q1D-01:SETI'])
        self.assertEqual(q[-1].pv(handle='readback'), ['SR24A-PC-Q1D-10:I'])
        self.assertEqual(q[-1].pv(handle='setpoint'), ['SR24A-PC-Q1D-10:SETI'])
        self.assertEqual(len(q), 248)

    def test_bend_loaded(self):
        b = ap.getElements('BEND')
        self.assertEqual(len(b), self.nbend)

    def test_sexts_loaded(self):
        s = ap.getElements('SEXT')
        self.assertEqual(s[0].pv(handle='readback', field='b2'), ['SR01A-PC-S1D-01:I'])
        self.assertEqual(s[0].pv(handle='setpoint', field='b2'), ['SR01A-PC-S1D-01:SETI'])
        self.assertEqual(s[-1].pv(handle='readback', field='b2'), ['SR24A-PC-S1D-07:I'])
        self.assertEqual(s[-1].pv(handle='setpoint', field='b2'), ['SR24A-PC-S1D-07:SETI'])
        self.assertEqual(len(s), self.nsexts)

    def test_squads_loaded(self):
        sq = ap.getElements('SQUAD')
        self.assertEqual(sq[0].pv(handle='readback', field='a1'), ['SR01A-PC-SQUAD-01:I'])
        self.assertEqual(sq[0].pv(handle='setpoint', field='a1'), ['SR01A-PC-SQUAD-01:SETI'])
        self.assertEqual(sq[-1].pv(handle='readback', field='a1'), ['SR24A-PC-SQUAD-04:I'])
        self.assertEqual(sq[-1].pv(handle='setpoint', field='a1'), ['SR24A-PC-SQUAD-04:SETI'])
        self.assertEqual(len(sq), self.nsquads)

    def test_correctors_loaded(self):
        for plane in ('H', 'V'):
            device = '{}STR'.format(plane)
            c = ap.getElements(device)
            self.assertEqual(c[0].pv(handle='readback'), ['SR01A-PC-{}-01:I'.format(device)])
            self.assertEqual(c[0].pv(handle='setpoint'), ['SR01A-PC-{}-01:SETI'.format(device)])
            self.assertEqual(c[-1].pv(handle='readback'), ['SR24A-PC-{}-07:I'.format(device)])
            self.assertEqual(c[-1].pv(handle='setpoint'), ['SR24A-PC-{}-07:SETI'.format(device)])
            self.assertEqual(len(c), self.ncorrectors)

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
        tmp = cothread.catools.caget
        mock_caget = mock.MagicMock()
        cothread.catools.caget = mock_caget
        mock_caget.assertCalledWith('SR-DI-DCCT-01:SIGNAL')
        cothread.catools.caget = tmp

    def test_orbit(self):
        orbit = ap.getOrbit(spos=True)
        self.assertTrue(orbit.shape == (173, 3))

    def check_quad_params(self, q1bk):
        q1b = ap.getElements('Q1B')
        for q in q1b:
            self.assertAlmostEqual(q.k1, q1bk, 3)

    def check_sext_params(self, s1dk2):
        s1d = ap.getElements('S1D')
        for s in s1d:
            self.assertAlmostEqual(s.k2, s1dk2, 3)

    def test_ring_length(self):
        length = sum(e.length for e in ap.getElements('*'))
        self.assertAlmostEqual(length, self.ring_length)


class I0913RingTests(unittest.TestCase):

    def setUp(self):
        self.nelements = 2406
        self.ring_length = 561.6
        self.nelements = 2428
        self.nbend = 48
        self.ncorrectors = 172
        self.nsquads = 96
        self.nsexts = 168


class TestSRLETHz(CommonTests, I0913RingTests):

    @classmethod
    def setUpClass(cls):
        ap.machines.load('SRLETHz')
        ap.machines.use('SR')

    def test_quad_params(self):
        CommonTests.check_quad_params(self, -0.0499)

    def test_sext_params(self):
        CommonTests.check_sext_params(self, 6.2004)


class TestSRI0913(CommonTests, I0913RingTests):

    @classmethod
    def setUpClass(cls):
        ap.machines.load('SRI0913')
        ap.machines.use('SR')

    def test_quad_params(self):
        CommonTests.check_quad_params(self, -1.2286)

    def test_sext_params(self):
        CommonTests.check_sext_params(self, 6.9)


class TestSRI21(CommonTests, I0913RingTests):

    @classmethod
    def setUpClass(cls):
        ap.machines.load('SRI21')
        ap.machines.use('SR')

    def setUp(self):
        super(TestSRI21, self).setUp()
        self.nelements = 2428

    def test_quad_params(self):
        CommonTests.check_quad_params(self, -1.2149)

    def test_sext_params(self):
        CommonTests.check_sext_params(self, 6.9)


class TestVMX(CommonTests, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ap.machines.load('VMX')
        ap.machines.use('SR')

    def setUp(self):
        self.nelements = 2476
        self.ring_length = 561.571
        self.nbend = 50
        self.ncorrectors = 173
        self.nsquads = 98
        self.nsexts = 171


class TestUnitConv(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # It shouldn't matter which ring mode we use.
        ap.machines.load('SRI21')
        ap.machines.use('SR')

    def testQuad(self):
        q1d1 = ap.getElements('Q1D')[0]
        ans = q1d1.convertUnit('b1', 100, None, 'phy')
        mml_ans = -0.98431858
        self.assertAlmostEqual(ans, mml_ans, 4)

    def testSext(self):
        """
        The match with MML unit conversion is poor, but investigating shows
        that the results are closer to the MML version than MML is to the
        actual data in master_calibration.csv.
        """
        sexts = ['S1A', 'S1B', 'S1C', 'S1D']
        mml_vals = {0:  -0.16126809,
                   1: 0.17840085,
                   5: 1.53650252,
                   10: 3.23212636,
                   20: 6.61219007,
                   50: 16.57752386,
                   100: 32.10677341}

        # Note calibration for each sext is the same.
        for sext in sexts:
            for current in mml_vals:
                s1 = ap.getElements(sext)[0]
                ans = s1.convertUnit('b2', current, None, 'phy')
                self.assertAlmostEqual(ans, mml_vals[current], 2)

    def testHcor(self):
        hcors = {0: 0.00020387,
                 52: 0.00020361,
                 170: 0.00020339}

        for index, mml_ans in hcors.iteritems():
            v10 = ap.getElements('VSTR')[index]
            ans = v10.convertUnit('b0', 1, None, 'phy')
            self.assertAlmostEqual(ans, mml_ans, 4)

    def testVcor(self):
        vcors = {0: 0.00203543,
                 9: 0.0014426,
                 171: 0.00205298}

        for index, mml_ans in vcors.iteritems():
            v10 = ap.getElements('VSTR')[index]
            ans = v10.convertUnit('b0', 10, None, 'phy')
            self.assertAlmostEqual(ans, mml_ans, 4)

    def testMinibetaQuad(self):
        qm09 = ap.getElements('QM09')
        mml_vals = [0.00595159,
                    -0.01164893,
                    0.00557956,
                    0.00604992]
        for q, val in zip(qm09, mml_vals):
            ans = q.convertUnit('b1', 1, None, 'phy')
            self.assertAlmostEqual(ans, val, 2)


if __name__ == '__main__':
    unittest.main()
