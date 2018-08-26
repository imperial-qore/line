import sys
sys.path.append("/home/gabor/github/butools/Python")
import math
import numpy as np
import numpy.matlib as ml
import matplotlib.pyplot as plt
import butools
from butools.utils import *
from butools.ph import *
from butools.dph import *
from butools.map import *
from butools.moments import *
from butools.reptrans import*
from butools.mc import *
from butools.dmap import *
from butools.trace import *
from butools.mam import *
from butools.queues import *
from butools.fitting import *
from contextlib import redirect_stdout
import os


print('---BuTools: DPH package test file---')
print('Enable the verbose messages with the BuToolsVerbose flag')
butools.verbose = True
print('Enable input parameter checking with the BuToolsCheckInput flag')
butools.checkInput = True
np.set_printoptions(precision=5,linewidth=1024)
outFile = open('/home/gabor/github/butools/test/docex/DPH_python.docex','w')
with redirect_stdout(outFile):
    print('=== MomentsFromMG ===')
    print('>>> a = ml.matrix([[-0.6,0.3,1.3]])')
    a = ml.matrix([[-0.6,0.3,1.3]])
    print('>>> A = ml.matrix([[0.25, 0.2, -0.15],[0.3, 0.1, 0.25],[0, 0.2, 0.47]])')
    A = ml.matrix([[0.25, 0.2, -0.15],[0.3, 0.1, 0.25],[0, 0.2, 0.47]])
    print('>>> moms = MomentsFromMG(a, A)')
    moms = MomentsFromMG(a, A)
    print('>>> print(moms)')
    print(moms)
    print('>>> moms = MomentsFromMG(a, A, 3)')
    moms = MomentsFromMG(a, A, 3)
    print('>>> print(moms)')
    print(moms)
    print('=== MomentsFromDPH ===')
    print('>>> a = ml.matrix([[0.76,0,0.24]])')
    a = ml.matrix([[0.76,0,0.24]])
    print('>>> A = ml.matrix([[0.34, 0.66, 0],[0.79, 0.05, 0.07],[0.26, 0.73, 0.01]])')
    A = ml.matrix([[0.34, 0.66, 0],[0.79, 0.05, 0.07],[0.26, 0.73, 0.01]])
    print('>>> moms = MomentsFromDPH(a, A, 5)')
    moms = MomentsFromDPH(a, A, 5)
    print('>>> print(moms)')
    print(moms)
    print('=== PmfFromMG ===')
    print('>>> a = ml.matrix([[-0.6,0.3,1.3]])')
    a = ml.matrix([[-0.6,0.3,1.3]])
    print('>>> A = ml.matrix([[0.25, 0.2, -0.15],[0.3, 0.1, 0.25],[0, 0.2, 0.47]])')
    A = ml.matrix([[0.25, 0.2, -0.15],[0.3, 0.1, 0.25],[0, 0.2, 0.47]])
    print('>>> x = np.arange(0.0,101.0,1.0)')
    x = np.arange(0.0,101.0,1.0)
    print('>>> pmf = PmfFromMG(a, A, x)')
    pmf = PmfFromMG(a, A, x)
    print('>>> plt.plot(x, pmf)')
    print('=== PmfFromDPH ===')
    print('>>> a = ml.matrix([[0.76,0,0.24]])')
    a = ml.matrix([[0.76,0,0.24]])
    print('>>> A = ml.matrix([[0.34, 0.66, 0],[0.79, 0.05, 0.07],[0.26, 0.73, 0.01]])')
    A = ml.matrix([[0.34, 0.66, 0],[0.79, 0.05, 0.07],[0.26, 0.73, 0.01]])
    print('>>> x = np.arange(0.0,1001.0,1.0)')
    x = np.arange(0.0,1001.0,1.0)
    print('>>> pmf = PmfFromDPH(a, A, x)')
    pmf = PmfFromDPH(a, A, x)
    print('>>> plt.plot(x, pmf)')
    print('=== CdfFromMG ===')
    print('>>> a = ml.matrix([[-0.6,0.3,1.3]])')
    a = ml.matrix([[-0.6,0.3,1.3]])
    print('>>> A = ml.matrix([[0.25, 0.2, -0.15],[0.3, 0.1, 0.25],[0, 0.2, 0.47]])')
    A = ml.matrix([[0.25, 0.2, -0.15],[0.3, 0.1, 0.25],[0, 0.2, 0.47]])
    print('>>> x = np.arange(0.0,101.0,1.0)')
    x = np.arange(0.0,101.0,1.0)
    print('>>> cdf = CdfFromMG(a, A, x)')
    cdf = CdfFromMG(a, A, x)
    print('>>> plt.plot(x, cdf)')
    print('=== CdfFromDPH ===')
    print('>>> a = ml.matrix([[0.76,0,0.24]])')
    a = ml.matrix([[0.76,0,0.24]])
    print('>>> A = ml.matrix([[0.34, 0.66, 0],[0.79, 0.05, 0.07],[0.26, 0.73, 0.01]])')
    A = ml.matrix([[0.34, 0.66, 0],[0.79, 0.05, 0.07],[0.26, 0.73, 0.01]])
    print('>>> x = np.arange(0.0,1001.0,1.0)')
    x = np.arange(0.0,1001.0,1.0)
    print('>>> cdf = CdfFromDPH(a, A, x)')
    cdf = CdfFromDPH(a, A, x)
    print('>>> plt.plot(x, cdf)')
    print('=== RandomDPH ===')
    print('>>> a, A = RandomDPH(3, 10, 5)')
    a, A = RandomDPH(3, 10, 5)
    print('>>> print(a)')
    print(a)
    print('>>> print(A)')
    print(A)
    print('=== CheckMGRepresentation ===')
    print('>>> a = ml.matrix([[-0.6,0.3,1.3]])')
    a = ml.matrix([[-0.6,0.3,1.3]])
    print('>>> A = ml.matrix([[0.25, 0.2, -0.15],[0.3, 0.1, 0.25],[0, 0.2, 0.47]])')
    A = ml.matrix([[0.25, 0.2, -0.15],[0.3, 0.1, 0.25],[0, 0.2, 0.47]])
    print('>>> flag = CheckMGRepresentation(a, A)')
    flag = CheckMGRepresentation(a, A)
    print('>>> print(flag)')
    print(flag)
    print('>>> a = ml.matrix([[-0.6,0.3,1.3]])')
    a = ml.matrix([[-0.6,0.3,1.3]])
    print('>>> A = ml.matrix([[0.35, 0.2, -0.25],[0.3, 0.1, 0.25],[0, 0.2, 0.47]])')
    A = ml.matrix([[0.35, 0.2, -0.25],[0.3, 0.1, 0.25],[0, 0.2, 0.47]])
    print('>>> flag = CheckMGRepresentation(a, A)')
    flag = CheckMGRepresentation(a, A)
    print('>>> print(flag)')
    print(flag)
    print('=== CheckDPHRepresentation ===')
    print('>>> a = ml.matrix([[0.48,0.08,0.26,0.18]])')
    a = ml.matrix([[0.48,0.08,0.26,0.18]])
    print('>>> A = ml.matrix([[0, 0.08, 0.08, 0.8],[0.55, 0, 0.24, 0.19],[0.06, 0.03, 0, 0.001],[0.23, 0.005, 0.2, 0.53]])')
    A = ml.matrix([[0, 0.08, 0.08, 0.8],[0.55, 0, 0.24, 0.19],[0.06, 0.03, 0, 0.001],[0.23, 0.005, 0.2, 0.53]])
    print('>>> flag = CheckDPHRepresentation(a, A)')
    flag = CheckDPHRepresentation(a, A)
    print('>>> print(flag)')
    print(flag)
    print('>>> a = ml.matrix([[0.48,0.08]])')
    a = ml.matrix([[0.48,0.08]])
    print('>>> A = ml.matrix([[0, 0.08],[0.55, 0.5]])')
    A = ml.matrix([[0, 0.08],[0.55, 0.5]])
    print('>>> flag = CheckDPHRepresentation(a, A)')
    flag = CheckDPHRepresentation(a, A)
    print('>>> print(flag)')
    print(flag)
    print('=== MGFromMoments ===')
    print('>>> moms = [4.08, 20.41, 130.45, 1054.41, 10463.73]')
    moms = [4.08, 20.41, 130.45, 1054.41, 10463.73]
    print('>>> a, A = MGFromMoments(moms)')
    a, A = MGFromMoments(moms)
    print('>>> print(a)')
    print(a)
    print('>>> print(A)')
    print(A)
    print('>>> memoms = MomentsFromMG(a, A, 5)')
    memoms = MomentsFromMG(a, A, 5)
    print('>>> print(memoms)')
    print(memoms)
    print('=== DPHFromMG ===')
    print('>>> a = ml.matrix([[-0.6,0.3,1.3]])')
    a = ml.matrix([[-0.6,0.3,1.3]])
    print('>>> A = ml.matrix([[0.1, 0.2, 0],[0.3, 0.1, 0.25],[-0.3, 0.2, 0.77]])')
    A = ml.matrix([[0.1, 0.2, 0],[0.3, 0.1, 0.25],[-0.3, 0.2, 0.77]])
    print('>>> flag = CheckMGRepresentation(a, A)')
    flag = CheckMGRepresentation(a, A)
    print('>>> print(flag)')
    print(flag)
    print('>>> flag = CheckDPHRepresentation(a, A)')
    flag = CheckDPHRepresentation(a, A)
    print('>>> print(flag)')
    print(flag)
    print('>>> b, B = DPHFromMG(a, A)')
    b, B = DPHFromMG(a, A)
    print('>>> print(b)')
    print(b)
    print('>>> print(B)')
    print(B)
    print('>>> flag = CheckDPHRepresentation(b, B)')
    flag = CheckDPHRepresentation(b, B)
    print('>>> print(flag)')
    print(flag)
    print('>>> Cm = SimilarityMatrix(A, B)')
    Cm = SimilarityMatrix(A, B)
    print('>>> err1 = la.norm(A*Cm-Cm*B)')
    err1 = la.norm(A*Cm-Cm*B)
    print('>>> err2 = la.norm(a*Cm-b)')
    err2 = la.norm(a*Cm-b)
    print('>>> print(np.max(err1, err2))')
    print(np.max(err1, err2))
    print('=== CanonicalFromDPH2 ===')
    print('>>> a = ml.matrix([[0,1.0]])')
    a = ml.matrix([[0,1.0]])
    print('>>> A = ml.matrix([[0.23, 0.22],[0.41, 0.48]])')
    A = ml.matrix([[0.23, 0.22],[0.41, 0.48]])
    print('>>> b, B = CanonicalFromDPH2(a, A)')
    b, B = CanonicalFromDPH2(a, A)
    print('>>> print(b)')
    print(b)
    print('>>> print(B)')
    print(B)
    print('>>> ev = la.eigvals(A)')
    ev = la.eigvals(A)
    print('>>> print(ev)')
    print(ev)
    print('>>> flag = CheckDPHRepresentation(b, B)')
    flag = CheckDPHRepresentation(b, B)
    print('>>> print(flag)')
    print(flag)
    print('>>> Cm = SimilarityMatrix(A, B)')
    Cm = SimilarityMatrix(A, B)
    print('>>> err1 = la.norm(A*Cm-Cm*B)')
    err1 = la.norm(A*Cm-Cm*B)
    print('>>> err2 = la.norm(a*Cm-b)')
    err2 = la.norm(a*Cm-b)
    print('>>> a = ml.matrix([[1.0,0]])')
    a = ml.matrix([[1.0,0]])
    print('>>> A = ml.matrix([[0, 0.61],[0.56, 0.44]])')
    A = ml.matrix([[0, 0.61],[0.56, 0.44]])
    print('>>> b, B = CanonicalFromDPH2(a, A)')
    b, B = CanonicalFromDPH2(a, A)
    print('>>> print(b)')
    print(b)
    print('>>> print(B)')
    print(B)
    print('>>> ev = la.eigvals(A)')
    ev = la.eigvals(A)
    print('>>> print(ev)')
    print(ev)
    print('>>> flag = CheckDPHRepresentation(b, B)')
    flag = CheckDPHRepresentation(b, B)
    print('>>> print(flag)')
    print(flag)
    print('>>> Cm = SimilarityMatrix(A, B)')
    Cm = SimilarityMatrix(A, B)
    print('>>> err1 = la.norm(A*Cm-Cm*B)')
    err1 = la.norm(A*Cm-Cm*B)
    print('>>> err2 = la.norm(a*Cm-b)')
    err2 = la.norm(a*Cm-b)
    print('>>> print(np.max(err1, err2))')
    print(np.max(err1, err2))
    print('=== CanonicalFromDPH3 ===')
    print('>>> a = ml.matrix([[0.46,0.22,0.32]])')
    a = ml.matrix([[0.46,0.22,0.32]])
    print('>>> A = ml.matrix([[0.67, 0.01, 0.12],[0.06, 0.45, 0.15],[0.18, 0.43, 0.32]])')
    A = ml.matrix([[0.67, 0.01, 0.12],[0.06, 0.45, 0.15],[0.18, 0.43, 0.32]])
    print('>>> b, B = CanonicalFromDPH3(a, A)')
    b, B = CanonicalFromDPH3(a, A)
    print('>>> print(b)')
    print(b)
    print('>>> print(B)')
    print(B)
    print('>>> ev = la.eigvals(A)')
    ev = la.eigvals(A)
    print('>>> print(ev)')
    print(ev)
    print('>>> flag = CheckDPHRepresentation(b, B)')
    flag = CheckDPHRepresentation(b, B)
    print('>>> print(flag)')
    print(flag)
    print('>>> Cm = SimilarityMatrix(A, B)')
    Cm = SimilarityMatrix(A, B)
    print('>>> err1 = la.norm(A*Cm-Cm*B)')
    err1 = la.norm(A*Cm-Cm*B)
    print('>>> err2 = la.norm(a*Cm-b)')
    err2 = la.norm(a*Cm-b)
    print('>>> print(np.max(err1, err2))')
    print(np.max(err1, err2))
    print('>>> a = ml.matrix([[0.76,0.12,0.12]])')
    a = ml.matrix([[0.76,0.12,0.12]])
    print('>>> A = ml.matrix([[0.31, 0., 0.],[0.98, 0., 0.02],[0.88, 0.04, 0.08]])')
    A = ml.matrix([[0.31, 0., 0.],[0.98, 0., 0.02],[0.88, 0.04, 0.08]])
    print('>>> b, B = CanonicalFromDPH3(a, A)')
    b, B = CanonicalFromDPH3(a, A)
    print('>>> print(b)')
    print(b)
    print('>>> print(B)')
    print(B)
    print('>>> ev = la.eigvals(A)')
    ev = la.eigvals(A)
    print('>>> print(ev)')
    print(ev)
    print('>>> flag = CheckDPHRepresentation(b, B)')
    flag = CheckDPHRepresentation(b, B)
    print('>>> print(flag)')
    print(flag)
    print('>>> Cm = SimilarityMatrix(A, B)')
    Cm = SimilarityMatrix(A, B)
    print('>>> err1 = la.norm(A*Cm-Cm*B)')
    err1 = la.norm(A*Cm-Cm*B)
    print('>>> err2 = la.norm(a*Cm-b)')
    err2 = la.norm(a*Cm-b)
    print('>>> print(np.max(err1, err2))')
    print(np.max(err1, err2))
    print('>>> a = ml.matrix([[0.67,0.07,0.26]])')
    a = ml.matrix([[0.67,0.07,0.26]])
    print('>>> A = ml.matrix([[0.31, 0., 0.],[0.98, 0., 0.02],[0.88, 0.04, 0.08]])')
    A = ml.matrix([[0.31, 0., 0.],[0.98, 0., 0.02],[0.88, 0.04, 0.08]])
    print('>>> b, B = CanonicalFromDPH3(a, A)')
    b, B = CanonicalFromDPH3(a, A)
    print('>>> print(b)')
    print(b)
    print('>>> print(B)')
    print(B)
    print('>>> ev = la.eigvals(A)')
    ev = la.eigvals(A)
    print('>>> print(ev)')
    print(ev)
    print('>>> flag = CheckDPHRepresentation(b, B)')
    flag = CheckDPHRepresentation(b, B)
    print('>>> print(flag)')
    print(flag)
    print('>>> Cm = SimilarityMatrix(A, B)')
    Cm = SimilarityMatrix(A, B)
    print('>>> err1 = la.norm(A*Cm-Cm*B)')
    err1 = la.norm(A*Cm-Cm*B)
    print('>>> err2 = la.norm(a*Cm-b)')
    err2 = la.norm(a*Cm-b)
    print('>>> print(np.max(err1, err2))')
    print(np.max(err1, err2))
    print('>>> a = ml.matrix([[0.78,0.04,0.18]])')
    a = ml.matrix([[0.78,0.04,0.18]])
    print('>>> A = ml.matrix([[0.06, 0.25, 0.31],[0.45, 0.18, 0.33],[0.98, 0, 0.01]])')
    A = ml.matrix([[0.06, 0.25, 0.31],[0.45, 0.18, 0.33],[0.98, 0, 0.01]])
    print('>>> b, B = CanonicalFromDPH3(a, A)')
    b, B = CanonicalFromDPH3(a, A)
    print('>>> print(b)')
    print(b)
    print('>>> print(B)')
    print(B)
    print('>>> ev = la.eigvals(A)')
    ev = la.eigvals(A)
    print('>>> print(ev)')
    print(ev)
    print('>>> flag = CheckDPHRepresentation(b, B)')
    flag = CheckDPHRepresentation(b, B)
    print('>>> print(flag)')
    print(flag)
    print('>>> Cm = SimilarityMatrix(A, B)')
    Cm = SimilarityMatrix(A, B)
    print('>>> err1 = la.norm(A*Cm-Cm*B)')
    err1 = la.norm(A*Cm-Cm*B)
    print('>>> err2 = la.norm(a*Cm-b)')
    err2 = la.norm(a*Cm-b)
    print('>>> print(np.max(err1, err2))')
    print(np.max(err1, err2))
    print('=== AcyclicDPHFromMG ===')
    print('>>> a = ml.matrix([[0,0,1.0]])')
    a = ml.matrix([[0,0,1.0]])
    print('>>> A = ml.matrix([[0.22, 0, 0],[0.3, 0.1, 0.55],[0.26, 0, 0.73]])')
    A = ml.matrix([[0.22, 0, 0],[0.3, 0.1, 0.55],[0.26, 0, 0.73]])
    print('>>> b, B = AcyclicDPHFromMG(a, A)')
    b, B = AcyclicDPHFromMG(a, A)
    print('>>> print(b)')
    print(b)
    print('>>> print(B)')
    print(B)
    print('>>> ma = MomentsFromMG(a, A, 5)')
    ma = MomentsFromMG(a, A, 5)
    print('>>> print(ma)')
    print(ma)
    print('>>> mb = MomentsFromMG(b, B, 5)')
    mb = MomentsFromMG(b, B, 5)
    print('>>> print(mb)')
    print(mb)
    print('>>> flag = CheckDPHRepresentation(b, B)')
    flag = CheckDPHRepresentation(b, B)
    print('>>> print(flag)')
    print(flag)
    print('>>> Cm = SimilarityMatrix(A, B)')
    Cm = SimilarityMatrix(A, B)
    print('>>> err1 = la.norm(A*Cm-Cm*B)')
    err1 = la.norm(A*Cm-Cm*B)
    print('>>> err2 = la.norm(a*Cm-b)')
    err2 = la.norm(a*Cm-b)
    print('>>> print(np.max(err1, err2))')
    print(np.max(err1, err2))
    print('=== DPH2From3Moments ===')
    print('>>> a = ml.matrix([[0.9,0.1]])')
    a = ml.matrix([[0.9,0.1]])
    print('>>> A = ml.matrix([[0.2, 0.61],[0.58, 0.41]])')
    A = ml.matrix([[0.2, 0.61],[0.58, 0.41]])
    print('>>> moms = MomentsFromDPH(a, A)')
    moms = MomentsFromDPH(a, A)
    print('>>> print(moms)')
    print(moms)
    print('>>> b, B = DPH2From3Moments(moms)')
    b, B = DPH2From3Moments(moms)
    print('>>> print(b)')
    print(b)
    print('>>> print(B)')
    print(B)
    print('>>> phmoms = MomentsFromDPH(b, B, 3)')
    phmoms = MomentsFromDPH(b, B, 3)
    print('>>> print(phmoms)')
    print(phmoms)
    print('=== DPH3From5Moments ===')
    print('>>> a = ml.matrix([[0.7,0.1,0.2]])')
    a = ml.matrix([[0.7,0.1,0.2]])
    print('>>> A = ml.matrix([[0.2, 0.51, 0.1],[0.58, 0.41, 0],[0.1, 0.4, 0.3]])')
    A = ml.matrix([[0.2, 0.51, 0.1],[0.58, 0.41, 0],[0.1, 0.4, 0.3]])
    print('>>> moms = MomentsFromDPH(a, A)')
    moms = MomentsFromDPH(a, A)
    print('>>> print(moms)')
    print(moms)
    print('>>> b, B = DPH3From5Moments(moms)')
    b, B = DPH3From5Moments(moms)
    print('>>> print(b)')
    print(b)
    print('>>> print(B)')
    print(B)
    print('>>> phmoms = MomentsFromMG(b, B, 5)')
    phmoms = MomentsFromMG(b, B, 5)
    print('>>> print(phmoms)')
    print(phmoms)
    print('=== SamplesFromDPH ===')
    print('>>> a = ml.matrix([[0.76,0,0.24]])')
    a = ml.matrix([[0.76,0,0.24]])
    print('>>> A = ml.matrix([[0.34, 0.66, 0],[0.79, 0.05, 0.07],[0.26, 0.73, 0.01]])')
    A = ml.matrix([[0.34, 0.66, 0],[0.79, 0.05, 0.07],[0.26, 0.73, 0.01]])
    print('>>> x = SamplesFromDPH(a, A, 1000)')
    x = SamplesFromDPH(a, A, 1000)
    print('>>> mt = MarginalMomentsFromTrace(x, 3)')
    mt = MarginalMomentsFromTrace(x, 3)
    print('>>> print(mt)')
    print(mt)
    print('>>> mp = MomentsFromDPH(a, A, 3)')
    mp = MomentsFromDPH(a, A, 3)
    print('>>> print(mp)')
    print(mp)
