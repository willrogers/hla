#!/usr/bin/env python

"""
NSLS2 V1 Unit Test
-------------------
"""

# cause timeout by nosetest
#from cothread.catools import caget
#print caget('SR:C00-Glb:G00{POS:00}RB-S', timeout=10)

import sys, os, time

if sys.version_info[:2] == (2, 6):
    import unittest2 as unittest
elif sys.version_info[:2] == (2,7):
    import unittest

import numpy as np
import random

import logging
logging.basicConfig(filename="utest.log",
    format='%(asctime)s - %(name)s [%(levelname)s]: %(message)s',
    level=logging.DEBUG)


logging.info("initializing NSLS2V1")
import aphla as ap
ap.initNSLS2V1()
# cause timeout when run by nosetest
#ap.initNSLS2V1SRTwiss()

logging.info("NSLS2V1 initialized")

refpvrb = [
    'V:1-SR:C15-BI:G2{BPM:1691}SA:X',
    'V:1-SR:C15-BI:G2{BPM:1691}SA:Y',
    'V:1-SR:C15-BI:G2{BPM:1711}SA:X',
    'V:1-SR:C15-BI:G2{BPM:1711}SA:Y',
    'V:1-SR:C15-BI:G4{BPM:1734}SA:X',
    'V:1-SR:C15-BI:G4{BPM:1734}SA:Y',
    'V:1-SR:C15-BI:G4{BPM:1745}SA:X',
    'V:1-SR:C15-BI:G4{BPM:1745}SA:Y',
    'V:1-SR:C15-BI:G6{BPM:1769}SA:X',
    'V:1-SR:C15-BI:G6{BPM:1769}SA:Y',
    'V:1-SR:C15-BI:G6{BPM:1784}SA:X',
    'V:1-SR:C15-BI:G6{BPM:1784}SA:Y',
    ]
ref_v0 = np.array(ap.caget(refpvrb), 'd')


def markForStablePv():
    global ref_v0, refpvrb
    ref_v0 = np.array(ap.caget(refpvrb), 'd')
    
def waitForStablePv(**kwargs):
    """
    wait for the orbit to be stable.

    This is in hlalib.py, but here does not need the dependance on getOrbit().
    """
    diffstd = kwargs.get('diffstd', 1e-7)
    minwait = kwargs.get('minwait', 2)
    maxwait = kwargs.get('maxwait', 30)
    step    = kwargs.get('step', 2)
    diffstd_list = kwargs.get('diffstd_list', False)
    verbose = kwargs.get('verbose', 0)

    t0 = time.time()
    time.sleep(minwait)
    global ref_v0
    dv = np.array(caget(refpvrb)) - ref_v0
    dvstd = [dv.std()]  # record the history
    timeout = False

    while dv.std() < diffstd:
        time.sleep(step)
        dt = time.time() - t0
        if dt  > maxwait:
            timeout = True
            break
        dv = np.array(caget(refpvrb)) - ref_v0
        dvstd.append(dv.std())

    if diffstd_list:
        return timeout, dvstd

"""
Element
~~~~~~~
"""

class Test0Element(unittest.TestCase):
    def setUp(self):
        pass 
        
    def tearDown(self):
        pass

    @unittest.skip("no tune element")
    def test_tune(self):
        logging.info("test_tune")
        self.assertEqual(len(ap.getElements('tune')), 1)
        tune = ap.getElements('tune')[0]
        pvx = tune.pv(field='x')[0]
        pvy = tune.pv(field='y')[0]

        nux, nuy = tune.x, tune.y
        #val = tune.value
        #self.assertTrue(len(val), 2)
        #self.assertAlmostEqual(nux, val[0])
        #self.assertAlmostEqual(nuy, val[1])
        self.assertTrue(nux > 30.0)
        self.assertTrue(nuy > 15.0)

    def test_dcct(self):
        dccts = ap.getElements('dcct')
        self.assertEqual(len(dccts), 1)
        dcct = dccts[0]
        # current
        #pv = u'SR:C00-BI:G00{DCCT:00}CUR-RB'
        pv = 'V:1-SR-BI{DCCT}CUR-I'
        vsrtag = 'aphla.sys.V1SR'
        self.assertEqual(dcct.name,    'dcct')
        #self.assertEqual(dcct.devname, 'DCCT')
        self.assertEqual(dcct.family,  'DCCT')
        self.assertEqual(len(dcct.pv()), 1)
        #self.assertEqual(dcct.pv(tag='aphla.eget'), [pv])
        self.assertEqual(dcct.pv(tag=vsrtag), [pv])
        #self.assertEqual(dcct.pv(tags=['aphla.eget', vsrtag]), [pv])

        self.assertIn('value', dcct.fields())
        self.assertGreater(dcct.value, 1.0)
        self.assertLess(dcct.value, 600.0)

        self.assertGreater(dcct.value, 1.0)
        self.assertGreater(ap.eget('DCCT', 'value'), 1.0)
        self.assertEqual(len(ap.eget('DCCT', ['value'])), 1)
        self.assertGreater(ap.eget('DCCT', ['value'])[0], 1.0)

    def test_bpm(self):
        bpms = ap.getElements('BPM')
        self.assertEqual(len(bpms), 180)

        bpm = bpms[0]
        #self.assertEqual(bpm.pv(field='xref'), [pvxbba, pvxgold])
        self.assertGreater(bpm.index, 1)
        self.assertFalse(bpm.virtual)
        self.assertEqual(bpm.virtual, 0)
        #self.assertEqual(len(bpm.value), 2)

        self.assertIn('x', bpm.fields())
        self.assertIn('y', bpm.fields())
        self.assertEqual(len(bpm.get(['x', 'y'])), 2)
        self.assertEqual(len(ap.eget('BPM', 'x')), len(bpms))
        self.assertEqual(len(ap.eget('BPM', ['x', 'y'])), len(bpms))

        self.assertGreater(ap.getDistance(bpms[0].name, bpms[1].name), 0.0)

    def test_vbpm(self):
        vbpms = ap.getElements('HLA:VBPM', include_virtual=True)
        self.assertIsNotNone(vbpms)
        vbpm = vbpms[0]
        self.assertIn('x', vbpm.fields())
        self.assertIn('y', vbpm.fields())

        bpms = ap.getElements('BPM')
        nbpm = len(bpms)
        self.assertEqual(len(vbpm.x), nbpm)
        self.assertEqual(len(vbpm.y), nbpm)
        self.assertEqual(len(vbpm.sb), nbpm)
        #print vbpm.x, np.std(vbpm.x)
        #print vbpm.y, np.std(vbpm.y)
        self.assertGreater(np.std(vbpm.x), 0.0)
        self.assertGreaterEqual(np.std(vbpm.y), 0.0)

    @unittest.skip("ORM data PV changed")
    def test_corr_orbit(self):
        bpm = ap.getElements('P*C1[0-3]*')
        trim = ap.getGroupMembers(['*', '[HV]COR'], op='intersection')
        v0 = ap.getOrbit('P*', spos=True)
        ap.correctOrbit([e.name for e in bpm], [e.name for e in trim])
        time.sleep(4)
        v1 = ap.getOrbit('P*', spos=True)
        import matplotlib.pylab as plt
        plt.clf()
        ax = plt.subplot(211) 
        fig = plt.plot(v0[:,-1], v0[:,0], 'r-x', label='X') 
        fig = plt.plot(v0[:,-1], v0[:,1], 'g-o', label='Y')
        ax = plt.subplot(212)
        fig = plt.plot(v1[:,-1], v1[:,0], 'r-x', label='X')
        fig = plt.plot(v1[:,-1], v1[:,1], 'g-o', label='Y')
        plt.savefig("test_nsls2_orbit_correct.png")


    def test_hcor(self):
        # hcor
        hcor = ap.element.CaElement(
            name = 'cxl1g2c01a', index = 125, cell = 'C01',
            devname = 'cl1g2c01a', family = 'HCOR', girder = 'G2', length = 0.2,
            sb = 30.4673, se = 30.6673, symmetry = 'A')

        self.assertTrue(hcor.name == 'cxl1g2c01a')
        self.assertTrue(hcor.cell == 'C01')
        self.assertTrue(hcor.girder == 'G2')
        self.assertTrue(hcor.devname == 'cl1g2c01a')
        self.assertTrue(hcor.family == 'HCOR')
        self.assertTrue(hcor.symmetry == 'A')


        self.assertAlmostEqual(hcor.length, 0.2)
        self.assertAlmostEqual(hcor.sb, 30.4673)
        self.assertAlmostEqual(hcor.se, 30.6673)

        pvrb = 'SR:C01-MG:G02A{HCor:L1}Fld-I'
        pvsp = 'SR:C01-MG:G02A{HCor:L1}Fld-SP'
        hcor.updatePvRecord(pvrb, {'handle': 'READ', 'field': 'x'})
        hcor.updatePvRecord(pvsp, {'handle': 'SET', 'field': 'x'}) 

        self.assertIn('x', hcor.fields())
        self.assertEqual(hcor.pv(field='x', handle='read'), [pvrb])
        self.assertEqual(hcor.pv(field='x', handle='set'), [pvsp])

        self.assertEqual(hcor.pv(field='y'), [])
        self.assertEqual(hcor.pv(field='y', handle='read'), [])
        self.assertEqual(hcor.pv(field='y', handle='set'), [])
        
        #v = ap.eget(hcor.name, ['x', 'y'])
        #self.assertGreaterEqual(abs(v[0]), 0.0)
        #self.assertIsNone(v[1])


"""
Channel Finder
"""

class TestChanFinderCsvData(unittest.TestCase):
    """
    """
    def setUp(self):
        #self.cfs_csv = 'us_nsls2v1_cfs.csv'
        self.cfs_db = 'us_nsls2v1.db'
        self.cfs_url = os.environ.get('HLA_CFS_URL', None)
        pass

    def test_conf(self):
        self.assertTrue(os.path.exists(ap.conf.filename(self.cfs_db)))

    def test_db_tags(self):
        cfa = ap.chanfinder.ChannelFinderAgent()
        self.assertTrue(os.path.exists(ap.conf.filename(self.cfs_db)))
        cfa.importSqliteDb(ap.conf.filename(self.cfs_db))

        tags = cfa.tags(ap.machines.HLA_TAG_SYS_PREFIX + '.V1*')
        for t in ['V1SR', 'V1LTB', 'V1LTD1', 'V1LTD2']:
            self.assertIn(ap.machines.HLA_TAG_SYS_PREFIX + '.' + t, tags)

    def test_url_tags(self):
        #http://web01.nsls2.bnl.gov/ChannelFinder
        if self.cfs_url is None: return
        self.assertIsNotNone(self.cfs_url)
        cfa = ap.chanfinder.ChannelFinderAgent()
        cfa.downloadCfs(self.cfs_url, tagName=ap.machines.HLA_TAG_PREFIX + '.*')

        tags = cfa.tags(ap.machines.HLA_TAG_SYS_PREFIX + '.V1*')
        for t in ['V1SR', 'V1LTB', 'V1LTD1', 'V1LTD2']:
            self.assertIn(ap.machines.HLA_TAG_SYS_PREFIX + '.' + t, tags)



"""
Lattice
-------------
"""

class Test0Lattice(unittest.TestCase):
    """
    Lattice testing
    """
    def setUp(self):
        logging.info("TestLattice")
        # this is the internal default lattice
        self.lat = ap.machines.getLattice('V1SR')
        self.assertTrue(self.lat)
        self.logger = logging.getLogger('tests.TestLattice')

    def test_neighbors(self):
        bpm = self.lat.getElementList('BPM')
        self.assertTrue(bpm)
        self.assertGreaterEqual(len(bpm), 180)

        el = self.lat.getNeighbors(bpm[2].name, 'BPM', 2)
        self.assertEqual(len(el), 5)
        for i in range(5):
            self.assertEqual(el[i].name, bpm[i].name,
                             "%d: %s != %s" % (i, el[i].name, bpm[i].name))

    def test_virtualelements(self):
        velem = ap.machines.HLA_VFAMILY
        elem = self.lat.getElementList(velem)
        self.assertTrue(elem)
        #elem = self.lat.getElementList(velem, 
        self.assertTrue(self.lat.hasGroup(ap.machines.HLA_VFAMILY))

    def test_getelements(self):
        elems = self.lat.getElementList('BPM')
        self.assertGreater(len(elems), 0)
        

    def test_locations(self):
        elem1 = self.lat.getElementList('*')
        for i in range(len(elem1)):
            if elem1[i].virtual: continue
            if i == 0: continue
            self.assertGreaterEqual(elem1[i].sb, elem1[i-1].sb,
                                    msg="{0}({4},sb={1})<{2}(sb={3})".format(
                    elem1[i].name, elem1[i].sb, elem1[i-1].name, elem1[i-1].sb,
                    i))
            self.assertGreaterEqual(elem1[i].se, elem1[i-1].sb,
                                    "{0}({4},se={1})<{2}(sb={3})".format(
                    elem1[i].name, elem1[i].se, elem1[i-1].name, elem1[i-1].sb, 
                    i))

        elem1 = self.lat.getElementList('BPM')
        for i in range(len(elem1)):
            if i == 0: continue
            self.assertGreaterEqual(elem1[i].sb, elem1[i-1].sb,
                                    "%f (%s) %f (%s)" % (
                    elem1[i].sb, elem1[i].name,
                    elem1[i-1].sb, elem1[i-1].name))
            
        elem1 = self.lat.getElementList('QUAD')
        for i in range(len(elem1)):
            if i == 0: continue
            self.assertGreaterEqual(elem1[i].sb, elem1[i-1].sb,
                                    "%f (%s) %f (%s)" % (
                    elem1[i].sb, elem1[i].name,
                    elem1[i-1].sb, elem1[i-1].name))
        
            

    def test_groups(self):
        grp = 'HLATEST'
        self.assertFalse(self.lat.hasGroup(grp))
        self.lat.addGroup(grp)
        self.assertTrue(self.lat.hasGroup(grp))

        #with self.assertRaises(ValueError) as ve:
        #    self.lat.addGroupMember(grp, 'A')
        #self.assertEqual(ve.exception, ValueError)

        self.lat.removeGroup(grp)
        self.assertFalse(self.lat.hasGroup(grp))

        
class Test1LatticeSr(unittest.TestCase):
    def setUp(self):
        logging.info("TestLatticeSr")
        self.lat = ap.machines.getLattice('V1SR')
        self.logger = logging.getLogger('tests.TestLatticeSr')
        pass

    def test_tunes(self):
        tune, = self.lat.getElementList('tune')
        self.assertTrue(abs(tune.x) > 0)
        self.assertTrue(abs(tune.y) > 0)
        
    def test_current(self):
        self.assertTrue(self.lat.hasElement('dcct'))
        
        cur1a = self.lat['dcct']
        cur1b, = self.lat.getElementList('dcct')
        self.assertTrue(cur1a.sb <= 0.0)
        self.assertTrue(cur1a.value > 0.0)
        self.assertTrue(cur1b.value > 0.0)

    def test_lines(self):
        elem1 = self.lat.getElementList('DIPOLE')
        s0, s1 = elem1[0].sb, elem1[0].se
        i = self.lat._find_element_s((s0+s1)/2.0)
        self.assertTrue(i >= 0)
        i = self.lat.getLine(srange=(0, 25))
        self.assertTrue(len(i) > 1)

    def test_getelements_sr(self):
        elems = self.lat.getElementList(['pl1g2c01a', 'pl2g2c01a'])
        self.assertTrue(len(elems) == 2)
        
        # only cell 1,3,5,7,9 and PL1, PL2
        elems = self.lat.getElementList('pl*g2c0*')
        self.assertTrue(len(elems) == 10)

    def test_groupmembers(self):
        bpm1 = self.lat.getElementList('BPM')
        g2a = self.lat.getElementList('G2')
        
        b1 = self.lat.getGroupMembers(['BPM', 'C20'], op='intersection')
        self.assertTrue(len(b1) == 6)
        
        b1 = self.lat.getGroupMembers(['BPM', 'G2'], op='union')
        self.assertTrue(len(b1) > len(bpm1))
        self.assertTrue(len(b1) > len(g2a))
        self.assertTrue(len(b1) < len(bpm1) + len(g2a))
        
        cx1 = self.lat.getElementList('HCOR')
        c1 = self.lat.getGroupMembers(['HCOR', 'QUAD'],
                                            op = 'intersection')
        self.assertFalse(c1)

        elem1 = self.lat.getGroupMembers(
            ['BPMX', 'TRIMX', 'QUAD', 'TRIMY'], op='union')
        self.assertTrue(len(elem1) > 120)
        for i in range(len(elem1)):
            if i == 0: continue
            self.assertTrue(elem1[i].sb >= elem1[i-1].sb)

        el1 = self.lat.getGroupMembers(['BPM', 'C0[2-3]', 'G2'],
                                            op='intersection')
        self.assertTrue(len(el1) == 4)

    def test_field(self):
        bpm = self.lat.getElementList('BPM')
        self.assertTrue(len(bpm) > 0)
        for e in bpm: 
            self.assertTrue(abs(e.x) >= 0)
            self.assertTrue(abs(e.y) >= 0)

        hcor = self.lat.getElementList('HCOR')
        self.assertTrue(len(bpm) > 0)
        for e in hcor: 
            k = e.x
            e.x = 1e-8
            self.assertTrue(abs(e.x) >= 0)
            e.x = k
            try:
                k = e.y
            except:
                pass
            else:
                self.assertTrue(False,
                                "AttributeError exception expected")


class TestLatticeLtd1(unittest.TestCase):
    def setUp(self):
        logging.info("TestLatticeLtd1")
        self.lat  = ap.machines._lat
        self.assertTrue(self.lat)
        self.logger = logging.getLogger('tests.TestLatticeLtd1')
        
    def tearDown(self):
        ap.machines._lat = self.lat

    def test_image(self):
        #lat = ap.machines._lat
        ap.machines.use('V1LTD1')
        vf = ap.getElements('vf1bd1')[0]
        self.assertIn('image', vf.fields())

        d = np.reshape(vf.image, (vf.image_ny, vf.image_nx))
        import matplotlib.pylab as plt
        plt.imshow(d)
        plt.savefig("test.png")

    def _gaussian(self, height, center_x, center_y, width_x, width_y):
        """Returns a gaussian function with the given parameters"""
        width_x = float(width_x)
        width_y = float(width_y)
        return lambda x,y: height*np.exp(
            -(((center_x-x)/width_x)**2+((center_y-y)/width_y)**2)/2)

    @unittest.skip("for lower version of Python/modules")
    def test_fit_gaussian_image(self):
        import matplotlib.pylab as plt
        from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
        from mpl_toolkits.axes_grid1.inset_locator import mark_inset
        d1 = ap.catools.caget('LTB-BI:BD1{VF1}Img1:ArrayData')

        self.assertEqual(len(d1), 1220*1620)

        d2 = np.reshape(d1, (1220, 1620))
        params = ap.fitGaussianImage(d2)
        fit = self._gaussian(*params)

        plt.clf()
        extent=(500, 1620, 400, 1220)
        #plt.contour(fit(*np.indices(d2.shape)), cmap=plt.cm.copper)
        plt.imshow(d2, interpolation="nearest", cmap=plt.cm.bwr)
        ax = plt.gca()
        ax.set_xlim(750, 850)
        ax.set_ylim(550, 650)
        (height, y, x, width_y, width_x) = params
        #axins = zoomed_inset_axes(ax, 6, loc=1)
        #axins.contour(fit(*np.indices(d2.shape)), cmap=plt.cm.cool)
        #axins.set_xlim(759, 859)
        #axins.set_ylim(559, 660)
        #mark_inset(ax, axins, loc1=2, loc2=4, fc='none', ec='0.5')

        plt.text(0.95, 0.05, """
        x : %.1f
        y : %.1f
        width_x : %.1f
        width_y : %.1f""" %(x, y, width_x, width_y),
             fontsize=16, horizontalalignment='right',
             verticalalignment='bottom', transform=ax.transAxes)

        plt.savefig("test2.png")

    def test_virtualelements(self):
        pass


class TestLatticeLtb(unittest.TestCase):
    def setUp(self):
        logging.info("TestLatticeLtb")
        self.lat  = ap.machines.getLattice('V1LTB')
        self.assertTrue(self.lat)
        self.logger = logging.getLogger('tests.TestLatticeLtb')

    def readInvalidFieldY(self, e):
        k = e.y
        
    def test_field(self):
        bpmlst = self.lat.getElementList('BPM')
        self.assertGreater(len(bpmlst), 0)
        
        elem = bpmlst[0]
        self.assertGreaterEqual(abs(elem.x), 0)
        self.assertGreaterEqual(abs(elem.y), 0)

        hcorlst = self.lat.getElementList('HCOR')
        self.assertGreater(len(hcorlst), 0)
        for e in hcorlst: 
            self.logger.warn("Skipping 'x' of %s" % e.name)
            #self.assertGreaterEqual(abs(e.x), 0.0)
            #k = e.x
            #e.x = k + 1e-10
            #self.assertGreaterEqual(abs(e.x), 0.0)
            pass

    def test_virtualelements(self):
        pass

class TestNSLS2V1(unittest.TestCase):
    def setUp(self):
        pass

    def test_elements(self):
        el = ap.getElements(['AA'])
        self.assertEqual(len(el), 1)
        self.assertIsNone(el[0])

"""
Twiss
~~~~~
"""

class Test0Tunes(unittest.TestCase):
    def setUp(self):
        logging.info("TestTunes")
        #ap.initNSLS2V1SRTwiss()

    @unittest.skip("no tune element")
    def test_tunes(self):
        nu = ap.getTunes()
        self.assertEqual(len(nu), 2)
        self.assertGreater(nu[0], 0.0)
        self.assertGreater(nu[1], 0.0)

    @unittest.skip
    def test_dispersion_meas(self):
        #s, etax, etay = ap.measDispersion('*')
        eta = ap.measDispersion('P*C0[2-4]*')
        s, etax, etay = eta[:,-1], eta[:,0], eta[:,1]

        if False:
            import matplotlib.pylab as plt
            plt.clf()
            plt.plot(s, etax, '-x', label=r'$\eta_x$')
            plt.plot(s, etay, '-o', label=r'$\eta_y$')
            plt.legend(loc='upper right')
            plt.savefig('test_twiss_dispersion_meas.png')

        self.assertGreater(max(abs(etax)), 0.15)
        self.assertGreater(max(abs(etay)), 0.0)
        self.assertGreater(min(abs(s)), 0.0)

    @unittest.skip
    def test_phase_get(self):
        phi = ap.machines.getLattice().getPhase('P*C1[0-1]*')
        s, phix, phiy = phi[:,-1], phi[:,0], phi[:,1]
        if False:
            import matplotlib.pylab as plt
            plt.clf()
            plt.plot(s, phix, '-x', label=r'$\phi_x$')
            plt.plot(s, phiy, '-o', label=r'$\phi_y$')
            plt.legend(loc='upper left')
            plt.savefig('test_twiss_phase_get.png')            
        pass


    @unittest.skip
    def test_beta_get(self):
        beta = ap.machines.getLattice().getBeta('P*C1[5-6]*')
        s, twx, twy = beta[:,-1], beta[:,0], beta[:,1]
        if False:
            import matplotlib.pylab as plt
            twl = ap.machines.getLattice().getBeamlineProfile(s[0], s[-1])
            sprof, vprof = [], []
            for tw in twl:
                sprof.extend(tw[0])
                vprof.extend(tw[1])

            plt.clf()
            plt.plot(sprof, vprof, 'k-')
            plt.plot(s, twx, '-x', label=r'$\beta_x$')
            plt.plot(s, twy, '-o', label=r'$\beta_y$')
            plt.legend(loc='upper right')
            plt.savefig('test_twiss_beta_get.png')            
        self.assertGreater(max(abs(twx)), 20.0)
        self.assertGreater(max(abs(twy)), 20.0)

        pass

    @unittest.skip
    def test_tune_get(self):
        """
        The tunes stored in lattice._twiss is not live, while ap.getTunes is
        live.
        """

        lat = ap.machines.getLattice()
        tunes0a = lat.getTunes()
        self.assertAlmostEqual(tunes0a[0], 33.41, places=2)
        self.assertAlmostEqual(tunes0a[1], 16.31, places=2)

        # adjust quad, live tune should change
        qs = lat.getElementList('QUAD')
        k1 = qs[0].k1
        qs[0].k1 = k1 * 1.02
        time.sleep(6)
        try:
            tunes0b = lat.getTunes()
            tunes1 = ap.getTunes()
        finally:
            qs[0].k1 = k1
        
        self.assertEqual(tunes0a[0], tunes0b[0])
        self.assertEqual(tunes0a[1], tunes0b[1])
        self.assertNotEqual(tunes0b[0], tunes1[0])
        self.assertNotEqual(tunes0b[1], tunes1[1])
        

    @unittest.skip
    def test_chromaticities(self):
        lat = ap.machines.getLattice()
        ch = lat.getChromaticities()
        self.assertEqual(abs(ch[0]), 0)
        self.assertEqual(abs(ch[1]), 0)
        pass

"""
Orbit
~~~~~~
"""

class TestOrbit(unittest.TestCase):
    """
    Tested:

    - orbit dimension
    """

    def setUp(self):
        self.logger = logging.getLogger("tests.TestOrbit")
        self.lat = ap.machines.getLattice('V1SR')
        self.assertTrue(self.lat)

    def tearDown(self):
        self.logger.info("tearDown")
        pass
        
    def test_orbit_read(self):
        self.logger.info("reading orbit")    
        self.assertGreater(len(ap.getElements('BPM')), 0)
        bpm = ap.getElements('BPM')
        for i,e in enumerate(bpm):
            self.assertGreaterEqual(abs(e.x), 0)
            self.assertGreaterEqual(abs(e.y), 0)

        v = ap.getOrbit()
        self.assertGreater(len(v), 0)
        v = ap.getOrbit('*')
        self.assertGreater(len(v), 0)
        v = ap.getOrbit('p[lhm]*')
        self.assertGreater(len(v), 0)

    def test_orbit_bump(self):
        v0 = ap.getOrbit()
        bpm = ap.getElements('BPM')
        hcor = ap.getElements('HCOR')
        hcor1 = ap.getElements('cx*')
        vcor = ap.getElements('VCOR')
        vcor1 = ap.getElements('cy*')
        #for e in hcor:
        #    print e.name, e.pv(field='x')

        self.assertGreater(len(v0), 0)
        self.assertEqual(len(bpm), 180)
        self.assertEqual(len(hcor1), 180)
        self.assertGreaterEqual(len(hcor), 180)
        self.assertEqual(len(vcor1), 180)
        self.assertGreaterEqual(len(vcor), 180)

        # maximum deviation
        mx, my = max(abs(v0[:,0])), max(abs(v0[:,1]))
        ih = np.random.randint(0, len(hcor), 3)
        iv = np.random.randint(0, len(vcor), 4)

        for i in ih: hcor[i].x = hcor[i].x+np.random.rand()*1e-6
        for i in iv: vcor[i].y = vcor[i].y+np.random.rand()*1e-6

        ap.hlalib.waitStableOrbit(v0, minwait=5)

        v1 = ap.getOrbit()
        self.assertGreater(np.std(v1[:,0]), np.std(v0[:,0]))
        self.logger.info("resetting trims")
        ap.hlalib._reset_trims()
        time.sleep(10)

class TestOrbitControl(unittest.TestCase): 
    def setUp(self):
        ap.machines.use("V1SR")

    def tearDown(self):
        ap.hlalib._reset_trims()

    @unittest.skip("orm data is not ready")
    def test_correct_orbit(self):
        ap.hlalib._reset_trims()

        # a list of horizontal corrector
        hcor = ap.getElements('HCOR')
        hcor_v0 = [e.x for e in hcor]
        # a list of vertical corrector
        vcor = ap.getElements('VCOR')
        vcor_v0 = [e.y for e in vcor]

        bpm = ap.getElements('BPM')
        bpm_v0 = np.array([(e.x, e.y) for e in bpm], 'd')

        norm0 = (np.linalg.norm(bpm_v0[:,0]), np.linalg.norm(bpm_v0[:,1]))

        ih = np.random.randint(0, len(hcor), 4)
        for i in ih:
            hcor[i].x = np.random.rand() * 1e-5

        iv = np.random.randint(0, len(vcor), 4)
        for i in iv:
            vcor[i].y = np.random.rand() * 1e-5

        #raw_input("Press Enter to correct orbit...")
        time.sleep(4)

        cor = []
        #cor.extend([e.name for e in hcor])
        #cor.extend([e.name for e in vcor])
        cor.extend([hcor[i].name for i in ih])
        cor.extend([vcor[i].name for i in iv])

        bpm_v1 = np.array([(e.x, e.y) for e in bpm], 'd')
        norm1 = (np.linalg.norm(bpm_v1[:,0]), np.linalg.norm(bpm_v1[:,1]))

        self.assertGreater(norm1[0], norm0[0])

        ap.correctOrbit([e.name for e in bpm], cor)
        ap.correctOrbit(bpm, cor)

        #raw_input("Press Enter to recover orbit...")
        bpm_v2 = np.array([(e.x, e.y) for e in bpm], 'd')
        #print "Euclidian norm:", 
        norm2 = (np.linalg.norm(bpm_v2[:,0]), np.linalg.norm(bpm_v2[:,1]))
        self.assertLess(norm2[0], norm1[0])
        self.assertLess(norm2[1], norm1[1])

        for i in ih:
            hcor[i].x = hcor_v0[i]

        for i in iv:
            vcor[i].y = vcor_v0[i]

        time.sleep(4)
        #raw_input("Press Enter ...")
        bpm_v3 = np.array([(e.x, e.y) for e in bpm], 'd')
        #print "Euclidian norm:", 
        norm3 = (np.linalg.norm(bpm_v3[:,0]), np.linalg.norm(bpm_v3[:,1]))
        self.assertLess(norm3[0], norm1[0])
        self.assertLess(norm3[0], norm1[0])

        #for i in range(len(ih)):
        #    x, y = hcor[ih[i]].x, vcor[iv[i]].y
        #    print i, (x - hcor_v0[ih[i]]), (y - vcor_v0[iv[i]])

    @unittest.skip("orm data is not ready")
    def test_local_bump(self):
        hcor = ap.getElements('HCOR')
        hcor_v0 = [e.x for e in hcor]
        vcor = ap.getElements('VCOR')
        vcor_v0 = [e.y for e in vcor]

        bpm = ap.getElements('BPM')
        bpm_v0 = [[e.x, e.y] for e in bpm]

        bpm_v1 = [[e.x, e.y] for e in bpm]

        bpm_v1[0] = [0, 0]
        bpm_v1[1] = [0, 1e-4]
        bpm_v1[2] = [2e-4, 1e-4]
        bpm_v1[3] = [5e-7, 1e-4]
        bpm_v1[4] = [0, 1e-4]
        bpm_v1[5] = [0, 1e-4]
        for i in range(6, len(bpm)):
            bpm_v1[i] = [0, 0]

        ap.setLocalBump(bpm, hcor+vcor, bpm_v1)


"""
BBA
~~~
"""

class TestBba(unittest.TestCase):
    def setUp(self):
        ap.initNSLS2V1()
        ap.hlalib._reset_trims()
        pass

    def test_quad(self):
        qnamelist = ['qh1g2c02a', 'qh1g2c04a', 'qh1g2c06a', 'qh1g2c08a']

        qlst = ap.getElements(qnamelist)
        for i,q in enumerate(qnamelist):
            self.assertGreater(abs(qlst[i].k1), 0.0)

        #qlst[0].value = -0.633004

        for i,qd in enumerate(qlst):
            self.assertGreater(qd.sb, 0.0)
            self.assertEqual(qd.name, qnamelist[i])

            bpm = ap.getClosest(qd.name, 'BPM')
            self.assertTrue(bpm.name)
            self.assertGreater(bpm.sb, 0.0)
            self.assertGreaterEqual(abs(bpm.x), 0.0)
            self.assertGreaterEqual(abs(bpm.y), 0.0)

            hc = ap.getNeighbors(bpm.name, 'HCOR', 1)
            self.assertEqual(len(hc), 3)
            self.assertEqual(hc[1].name, bpm.name)
            self.assertGreaterEqual(abs(hc[0].x), 0.0)
            
        #ap.createLocalBump([], [], [])

"""
ORM
~~~~
"""

class TestOrmData(unittest.TestCase):
    def setUp(self):
        self.h5filename = "us_nsls2_v1sr_orm.hdf5"
        pass

    def tearDown(self):
        pass

    @unittest.skip("orm data is not ready")
    def test_trim_bpm(self):
        self.assertTrue(ap.conf.has(self.h5filename))
        ormdata = ap.OrmData(ap.conf.filename(self.h5filename))

        trimx = ['fxl2g1c07a', 'cxh1g6c15b']
        for trim in trimx:
            self.assertTrue(ormdata.hasTrim(trim))

        bpmx = ap.getGroupMembers(['BPM', 'C0[2-4]'], op='intersection')
        self.assertEqual(len(bpmx), 18)
        for bpm in bpmx:
            self.assertTrue(ormdata.hasBpm(bpm.name))
        

    @unittest.skip("orm data is not ready")
    def test_measure_orm(self):
        return True
        if hla.NETWORK_DOWN: return True
        hla.reset_trims()
        trimx = ['cxh1g6c15b', 'cyhg2c30a', 'cxl2g6c14b']
        #trimx = ['CXH1G6C15B']
        bpmx = ['ph1g2c30a', 'pl1g2c01a', 'ph1g6c29b', 'ph2g2c30a', 'pm1g4c30a']
        #hla.reset_trims()
        orm = hla.measorm.Orm(bpm = bpmx, trim = trimx)
        orm.measure("orm-test.pkl", verbose=1)
        orm.measure_update(bpm=bpmx, trim=trimx[:2], verbose=1, dkick=5e-5)
        orm.save("orm-test-update.pkl")
        #orm.checkLinearity()
        pass

    @unittest.skip("orm data is not ready")
    def test_measure_orm_sub1(self):
        return True
        if hla.NETWORK_DOWN: return True

        trim = ['cxl1g2c05a', 'cxh2g6c05b', 'cxh1g6c05b', 'fxh2g1c10a',
                'cxm1g4c12a', 'cxh2g6c15b', 'cxl1g2c25a', 'fxh1g1c28a',
                'cyl2g6c30b', 'fyh1g1c16a']
        #trimx = ['CXH1G6C15B']
        bpmx = hla.getGroupMembers(['*', 'BPMX'], op='intersection')
        
        #hla.reset_trims()
        orm = hla.measorm.Orm(bpm = bpmx, trim = trim)
        orm.TSLEEP=15
        orm.measure(output="orm-sub1.pkl", verbose=0)
        #orm.checkLinearity()
        pass

    @unittest.skip("orm data is not ready")
    def test_measure_full_orm(self):
        return True
        if hla.NETWORK_DOWN: return True
        hla.reset_trims()
        bpm = hla.getGroupMembers(['*', 'BPMX'], op='intersection')
        trimx = hla.getGroupMembers(['*', 'TRIMX'], op='intersection')
        trimy = hla.getGroupMembers(['*', 'TRIMY'], op='intersection')
        trim = trimx[:]
        trim.extend(trimy)
        #print bpm, trim
        print "start:", time.time(), " version:", hg_parent_rev()
        orm = hla.measorm.Orm(bpm=bpm, trim=trim)
        orm.TSLEEP = 12
        orm.measure(output=self.full_orm, verbose=0)

    @unittest.skip("orm data is not ready")
    def test_linearity(self):
        return True
        #if hla.NETWORK_DOWN: return True
        orm = hla.measorm.Orm(bpm = [], trim = [])
        #orm.load('orm-test.pkl')
        #orm.load('/home/lyyang/devel/nsls2-hla/machine/nsls2/orm.pkl')
        hla.reset_trims()
        orm.load('./dat/orm-full-0181.pkl')
        #orm.maskCrossTerms()
        bpmpv = [b[2] for i,b in enumerate(orm.bpm)]
        for i,t in enumerate(orm.trim):
            k0 = hla.caget(t[3])
            v0 = np.array(hla.caget(bpmpv))
            caput(t[3], k0 + 1e-6)
            for j in range(10):
                time.sleep(2)
                v1 = np.array(hla.caget(bpmpv))
                print np.std(v1-v0),
                sys.stdout.flush()
            print ""
            caput(t[3], k0)
            if i > 20: break
        #print orm
        #for i,b in enumerate(orm.bpm):
        #    print i, b[0], b[2]
        #orm.checkLinearity(plot=True)
        pass

    @unittest.skip("orm data is not ready")
    def test_update(self):
        """
        same data different mask
        """
        self.assertTrue(ap.conf.has(self.h5filename))
        ormdata_dst = ap.OrmData(ap.conf.filename(self.h5filename))
        ormdata_src = ap.OrmData(ap.conf.filename(self.h5filename))
        
        nrow, ncol = len(ormdata_src.bpm), len(ormdata_src.trim)
        # reset data
        for i in range(nrow):
            for j in range(ncol):
                ormdata_src.m[i,j] = 0.0

        for itrial in range(3):
            idx = []
            for i in range(nrow*ncol//4):
                k = random.randint(0, nrow*ncol-1)
                idx.append(divmod(k, ncol))
                ormdata_src._mask[idx[-1][0]][idx[-1][1]] = 0

        ormdata_dst.update(ormdata_src)
        for i,j in idx:
            self.assertEqual(ormdata_dst.m[i,j], 0.0)

    @unittest.skip("orm data is not ready")
    def test_update_swapped(self):
        """
        same dimension, swapped rows
        """
        self.assertTrue(ap.conf.has(self.h5filename))
        ormdata_dst = ap.OrmData(ap.conf.filename(self.h5filename))
        ormdata_src = ap.OrmData(ap.conf.filename(self.h5filename))
        
        nrow, ncol = len(ormdata_src.bpm), len(ormdata_src.trim)
        # reset data
        for i in range(nrow):
            for j in range(ncol):
                ormdata_src.m[i,j] = 0.0

        # rotate the rows down by 2
        import collections
        rbpm = collections.deque(ormdata_src.bpm)
        rbpm.rotate(2)
        ormdata_src.bpm = [b for b in rbpm]

        for itrial in range(10):
            idx = []
            for i in range(nrow*ncol//4):
                k = random.randint(0, nrow*ncol-1)
                idx.append(divmod(k, ncol))
                ormdata_src._mask[idx[-1][0]][idx[-1][1]] = 0

        ormdata_dst.update(ormdata_src)
        for i,j in idx:
            i0, j0 = (i-2+nrow) % nrow, (j + ncol) % ncol
            self.assertEqual(ormdata_dst.m[i0,j0], 0.0)

    @unittest.skip("no sub matrix")
    def test_update_submatrix(self):
        """
        same dimension, swapped rows
        """
        self.assertTrue(ap.conf.has(self.h5filename))
        ormdata = ap.OrmData(ap.conf.filename(self.h5filename))
        nrow, ncol = len(ormdata.bpm), len(ormdata.trim)

        # prepare for subset
        for itrial1 in range(10):
            idx = []
            bpms, trims = set([]), set([])
            planes = [set([]), set([])]
            for itrial2 in range(nrow*ncol//4):
                k = random.randint(0, nrow*ncol-1)
                i,j = divmod(k, ncol)
                idx.append([i, j])
                bpms.add(ormdata.bpm[i][0])
                planes[0].add(ormdata.bpm[i][1])
                trims.add(ormdata.trim[j][0])
                planes[1].add(ormdata.trim[j][1])

            m = ormdata.getSubMatrix(bpm, trim, planes)

            for i,j in idx:
                self.assertEqual(ormdata_dst.m[i0,j0], 0.0)

        #orm1 = hla.measorm.Orm(bpm = [], trim = [])
        #orm1.load('a.hdf5')
        #orm2 = hla.measorm.Orm(bpm = [], trim = [])
        #orm2.load('b.hdf5')
        #orm = orm1.merge(orm2)
        #orm.checkLinearity()
        #orm.save('c.hdf5')
        
    @unittest.skip("empty")
    def test_shelve(self):
        return True
        #orm = hla.measorm.Orm(bpm = [], trim = [])
        #orm.load('c.hdf5')
        #orm.save('o1.pkl', format='shelve')
        #orm.load('o1.pkl', format='shelve')
        #orm.checkLinearity()

    @unittest.skip("empty")
    def test_orbitreproduce(self):
        return True

        t0 = time.time()
        hla.reset_trims()
        #time.sleep(10)
        t1 = time.time()

        pkl = './dat/orm-full-0181.pkl'
        orm = hla.measorm.Orm([], [])
        if not os.path.exists(pkl): return True
        else: orm.load(pkl)
        print orm
        #print "delay: ", orm.TSLEEP, " seconds"

        dk = 2e-4
        bpm_pvs = [b[2] for i,b in enumerate(orm.bpm)]
        x0 = np.zeros(len(bpm_pvs), 'd')
        #print bpm_pvs[:10]
        trim_k = np.zeros((len(orm.trim), 3), 'd')
        for j,t in enumerate(orm.trim):
            k0 = hla.caget(t[3])
            klst = np.linspace(1000*(k0-dk), 1000*(k0+dk), 20)
            print "%4d/%d" % (j, len(orm.trim)), t, k0
            trim_k[j,1] = k0
            x = np.zeros((len(bpm_pvs), 5), 'd')
            x0 = hla.caget(bpm_pvs)
            x[:,0] = x0
            x[:,2] = x0
            #print bpm_pvs[0], x[0,0], x[0,2]

            t2 = time.time()
            hla.caputwait(t[3], k0-dk, bpm_pvs[0])
            #time.sleep(orm.TSLEEP)
            trim_k[j,0] = k0 - dk
            x[:,1] = hla.caget(bpm_pvs)
            #print time.time() - t2, bpm_pvs[0], x[0,1]
            #time.sleep(orm.TSLEEP)

            hla.caputwait(t[3], k0+dk, bpm_pvs[0])
            #time.sleep(orm.TSLEEP)
            trim_k[j,2] = k0+dk
            
            x[:,3] = hla.caget(bpm_pvs)
            x[:,3] = hla.caget(bpm_pvs)
            #print bpm_pvs[0], x[0,3]

            hla.caputwait(t[3], k0, bpm_pvs[0])
            #time.sleep(3)
            #print x[0,:]

            mask = np.zeros(len(bpm_pvs), 'i')
            x1 = x0[:] - orm.m[:,j] * dk
            x2 = x0[:] + orm.m[:,j] * dk
            for i,b in enumerate(orm.bpm):
                if abs(x2[i] - x1[i]) < 3e-6: continue
                if abs(x2[i] - x[i,3]) < 5e-6 and abs(x1[i]-x[i,1]) < 5e-6:
                    continue
                plt.clf()
                plt.subplot(211)
                plt.plot(trim_k[j,:]*1000.0, np.transpose(1000.*x[i,1:4]), '--o')
                plt.plot(1000*orm._rawkick[j,:], 1000*orm._rawmatrix[:,i,j], 'x')
                plt.plot(klst, 1000.0*x0[i] + orm.m[i,j]*klst, '-')
                plt.grid(True)
                if orm._mask[i,j]: plt.title("%s.%s (masked)" % (t[0], t[1]))
                else: plt.title("%s.%s" % (t[0], t[1]))
                plt.xlabel("angle [mrad]")
                plt.ylabel('orbit [mm]')
                plt.subplot(212)
                plt.plot(1000*orm._rawkick[j,:], 1e6*((orm._rawmatrix[:,i,j] - orm._rawmatrix[0,i,j]) - \
                             orm.m[i,j]*orm._rawkick[j,:]), 'x')
                plt.plot(trim_k[j,:]*1000.0, 1e6*((x[i,1:4] - x[i,0])- trim_k[j,:]*orm.m[i,j]), 'o')
                plt.ylabel("Difference from prediction [um]")
                plt.xlabel("kick [mrad]")
                plt.savefig("orm-check-t%03d-%03d.png" % (j,i))
                if i > 100: break
            break
        print "Time:", time.time() - t1



class TestOrm(unittest.TestCase):
    def setUp(self):
        pass

    def test_measure_orm(self):
        bpms = ap.getElements('BPM')
        trims = ap.getElements('HCOR')
        
        bpmlst = [b.name for b in bpms[:5]]
        trimlst = [t.name for t in trims[:3]]
        ap.measOrbitRm(bpmlst, trimlst, "orm_test.hdf5")



if __name__ == "__main__":
    logging.info("Main")
    unittest.main()
    pass

