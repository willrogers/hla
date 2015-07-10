"""
Not really unit tests, but tests to show whether data has
correctly been loaded into the aphla database.
"""
import dls_packages
from cothread.catools import caget
import unittest
import sys
sys.path.append('..')
import aphla as ap


class TestAP(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        ap.machines.load('SRI0913')
        ap.machines.use('SR')

    def test_elements_loaded(self):
        elements = ap.getElements('*')
        # 2325 in THERING plus DCCT
        self.assertEqual(len(elements), 2326)

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

    def test_sext_k_value(self):
        sexts = ap.getElements('S1D')
        for s in sexts:
            self.assertAlmostEqual(s.k2, 6.9)

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
        self.assertAlmostEqual(current, ca_current)

    def test_orbit(self):
        orbit = ap.getOrbit(spos=True)
        self.assertTrue(orbit.shape == (172, 3))

    def test_SRI0913(self):
        # SRI0913 loaded by default.
        q1b = ap.getElements('Q1B')
        for q in q1b:
            self.assertAlmostEqual(q.k1, -1.2286, 3)
        s1d = ap.getElements('S1D')
        for s in s1d:
            self.assertAlmostEqual(s.k2, 6.9, 3)

    def test_SRLETHz(self):
        # SRI0913 loaded by default.
        ap.machines.load('SRLETHz')
        ap.machines.use('SR')
        q1b = ap.getElements('Q1B')
        for q in q1b:
            self.assertAlmostEqual(q.k1, -0.0499, 3)
        s1d = ap.getElements('S1D')
        for s in s1d:
            self.assertAlmostEqual(s.k2, 6.2004, 3)
        # Back to default.
        ap.machines.load('SRI0913')
        ap.machines.use('SR')

if __name__ == '__main__':
    unittest.main()
