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


print('---BuTools: PH package test file---')
print('Enable the verbose messages with the BuToolsVerbose flag')
butools.verbose = True
print('Enable input parameter checking with the BuToolsCheckInput flag')
butools.checkInput = True
np.set_printoptions(precision=5,linewidth=1024)
print('========================================')
print('Testing BuTools function MomentsFromME')
print('Input:')
print('------')
a = ml.matrix([[0.2,0.3,0.5]])
print('a = ')
print(a)
A = ml.matrix([[-1, 0, 0],[0, -3, 2],[0, -2, -3]])
print('A = ')
print(A)
print('Test:')
print('-----')
print('moms = MomentsFromME(a, A):')
moms = MomentsFromME(a, A)
print('moms = ')
print(moms)
assert CheckMoments(moms)==True, "The function returned invalid moments!"
print('moms = MomentsFromME(a, A, 9):')
moms = MomentsFromME(a, A, 9)
print('moms = ')
print(moms)
assert CheckMoments(moms)==True, "The function returned invalid moments!"
print('========================================')
print('Testing BuTools function MomentsFromPH')
print('Input:')
print('------')
a = ml.matrix([[0.1,0.9,0]])
print('a = ')
print(a)
A = ml.matrix([[-6.2, 2, 0],[2, -9, 1],[1, 0, -3]])
print('A = ')
print(A)
print('Test:')
print('-----')
print('moms = MomentsFromPH(a, A, 5):')
moms = MomentsFromPH(a, A, 5)
print('moms = ')
print(moms)
assert CheckMoments(moms)==True, "The function returned invalid moments!"
print('========================================')
print('Testing BuTools function CdfFromME')
print('Input:')
print('------')
a = ml.matrix([[0.2,0.3,0.5]])
print('a = ')
print(a)
A = ml.matrix([[-1, 0, 0],[0, -3, 2],[0, -2, -3]])
print('A = ')
print(A)
x = np.arange(0.0,5.01,0.01)
print('Test:')
print('-----')
print('cdf = CdfFromME(a, A, x):')
cdf = CdfFromME(a, A, x)
plt.plot(x, cdf)
assert np.all(np.diff(cdf)>=0), "The cdf is not increasing monotonously!"
assert np.abs(np.sum(1-cdf)*0.01-MomentsFromME(a, A, 1)[0])<0.01, "The mean computed from the cdf does not match the theoretical result!"
print('========================================')
print('Testing BuTools function CdfFromPH')
print('Input:')
print('------')
a = ml.matrix([[0.1,0.9,0]])
print('a = ')
print(a)
A = ml.matrix([[-6.2, 2, 0],[2, -9, 1],[1, 0, -3]])
print('A = ')
print(A)
x = np.arange(0.0,3.002,0.002)
print('Test:')
print('-----')
print('cdf = CdfFromPH(a, A, x):')
cdf = CdfFromPH(a, A, x)
plt.plot(x, cdf)
assert np.all(np.diff(cdf)>=0), "The cdf is not increasing monotonously!"
assert np.abs(np.sum(1-cdf)*0.002-MomentsFromME(a, A, 1)[0])<0.002, "The mean computed from the cdf does not match the theoretical result!"
print('========================================')
print('Testing BuTools function PdfFromME')
print('Input:')
print('------')
a = ml.matrix([[0.2,0.3,0.5]])
print('a = ')
print(a)
A = ml.matrix([[-1, 0, 0],[0, -3, 2],[0, -2, -3]])
print('A = ')
print(A)
x = np.arange(0.0,5.01,0.01)
print('Test:')
print('-----')
print('pdf = PdfFromME(a, A, x):')
pdf = PdfFromME(a, A, x)
plt.plot(x, pdf)
assert np.all(pdf>=0), "The pdf is negative!"
assert np.abs(x.dot(pdf)*0.01-MomentsFromME(a, A, 1)[0])<0.01, "The mean computed from the pdf does not match the theoretical result!"
print('========================================')
print('Testing BuTools function PdfFromPH')
print('Input:')
print('------')
a = ml.matrix([[0.1,0.9,0]])
print('a = ')
print(a)
A = ml.matrix([[-6.2, 2, 0],[2, -9, 1],[1, 0, -3]])
print('A = ')
print(A)
x = np.arange(0.0,3.002,0.002)
print('Test:')
print('-----')
print('pdf = PdfFromPH(a, A, x):')
pdf = PdfFromPH(a, A, x)
plt.plot(x, pdf)
assert np.all(pdf>=0), "The pdf is negative!"
assert np.abs(x.dot(pdf)*0.002-MomentsFromPH(a, A, 1)[0])<0.002, "The mean computed from the pdf does not match the theoretical result!"
print('========================================')
print('Testing BuTools function IntervalPdfFromPH')
print('Input:')
print('------')
a = ml.matrix([[0.1,0.9,0]])
print('a = ')
print(a)
A = ml.matrix([[-6.2, 2, 0],[2, -9, 1],[1, 0, -3]])
print('A = ')
print(A)
x = np.arange(0.0,3.002,0.002)
print('Test:')
print('-----')
print('x, y = IntervalPdfFromPH(a, A, x):')
x, y = IntervalPdfFromPH(a, A, x)
plt.plot(x, y)
assert np.all(y>=0), "The interval pdf is negative!"
assert np.abs(x.dot(y)*0.002-MomentsFromPH(a, A, 1)[0])<0.002, "The mean computed from the interval pdf does not match the theoretical"
print('========================================')
print('Testing BuTools function RandomPH')
print('Test:')
print('-----')
print('a, A = RandomPH(3, 8, 4):')
a, A = RandomPH(3, 8, 4)
print('a = ')
print(a)
print('A = ')
print(A)
assert CheckPHRepresentation(a, A), "RandomPH failed to return a valid PH representation!"
assert np.max(np.abs(MomentsFromPH(a, A, 1)[0]-8))<10**-14, "RandomPH failed to match the given mean value!"
print('========================================')
print('Testing BuTools function CheckMERepresentation')
print('Input:')
print('------')
a = ml.matrix([[-0.2,0.2]])
print('a = ')
print(a)
A = ml.matrix([[1, -1],[1, -2]])
print('A = ')
print(A)
print('Test:')
print('-----')
print('flag = CheckMERepresentation(a, A):')
flag = CheckMERepresentation(a, A)
print('flag = ')
print(flag)
assert flag==False, "CheckMERepresentation did not detect that the initial vector is invalid!"
print('Input:')
print('------')
a = ml.matrix([[-0.2,0.4,0.8]])
print('a = ')
print(a)
A = ml.matrix([[-2, 0, 3],[0, -1, 1],[0, -1, -1]])
print('A = ')
print(A)
print('Test:')
print('-----')
print('flag = CheckMERepresentation(a, A):')
flag = CheckMERepresentation(a, A)
print('flag = ')
print(flag)
assert flag==False, "CheckMERepresentation did not detect that the dominant eigenvalue is invalid!"
print('Input:')
print('------')
a = ml.matrix([[0.2,0.3,0.5]])
print('a = ')
print(a)
A = ml.matrix([[-1, 0, 0],[0, -3, 2],[0, -2, -3]])
print('A = ')
print(A)
print('Test:')
print('-----')
print('flag = CheckMERepresentation(a, A):')
flag = CheckMERepresentation(a, A)
print('flag = ')
print(flag)
assert flag==True, "CheckMERepresentation did not recognize that the given ME representation is valid!"
print('========================================')
print('Testing BuTools function CheckPHRepresentation')
print('Input:')
print('------')
a = ml.matrix([[0.2]])
print('a = ')
print(a)
A = ml.matrix([[-1, 1],[1, -2]])
print('A = ')
print(A)
print('Test:')
print('-----')
print('flag = CheckPHRepresentation(a, A):')
flag = CheckPHRepresentation(a, A)
print('flag = ')
print(flag)
assert flag==False, "CheckPHRepresentation did not recognize the wrong input dimensions!"
print('Input:')
print('------')
a = ml.matrix([[0.2,0.7]])
print('a = ')
print(a)
A = ml.matrix([[-1, 1],[1, -2]])
print('A = ')
print(A)
print('Test:')
print('-----')
print('flag = CheckPHRepresentation(a, A):')
flag = CheckPHRepresentation(a, A)
print('flag = ')
print(flag)
assert flag==True, "CheckPHRepresentation did not recognize that the given PH representation is valid!"
print('========================================')
print('Testing BuTools function CheckMEPositiveDensity')
print('Input:')
print('------')
a = ml.matrix([[0.2,0.3,0.5]])
print('a = ')
print(a)
A = ml.matrix([[-1, 0, 0],[0, -3, 2],[0, -2, -3]])
print('A = ')
print(A)
print('Test:')
print('-----')
print('flag = CheckMEPositiveDensity(a, A):')
flag = CheckMEPositiveDensity(a, A)
print('flag = ')
print(flag)
assert flag==True, "CheckMEPositiveDensity did not recognize that the given ME distribution has positive density!"
print('Input:')
print('------')
a = ml.matrix([[0.2,0.3,0.5]])
print('a = ')
print(a)
A = ml.matrix([[-1, 0, 0],[0, -3, 2.9],[0, -2.9, -3]])
print('A = ')
print(A)
print('Test:')
print('-----')
print('flag = CheckMEPositiveDensity(a, A):')
flag = CheckMEPositiveDensity(a, A)
print('flag = ')
print(flag)
assert flag==False, "CheckMEPositiveDensity did not recognize that the given ME distribution does not have positive density!"
print('========================================')
print('Testing BuTools function APHFrom3Moments')
print('Input:')
print('------')
moms = [10.0, 125.0, 8400.0]
print('moms = ')
print(moms)
print('Test:')
print('-----')
print('a, A = APHFrom3Moments(moms):')
a, A = APHFrom3Moments(moms)
print('a = ')
print(a)
print('A = ')
print(A)
phmoms = MomentsFromPH(a, A, 3)
print('phmoms = ')
print(phmoms)
assert la.norm((np.array(phmoms)-np.array(moms))/np.array(moms))<10**-12, "APHFrom3Moments failed to match the given moments!"
print('Input:')
print('------')
moms = [10.0, 525.0, 31400.0]
print('moms = ')
print(moms)
print('Test:')
print('-----')
print('a, A = APHFrom3Moments(moms):')
a, A = APHFrom3Moments(moms)
print('a = ')
print(a)
print('A = ')
print(A)
phmoms = MomentsFromPH(a, A, 3)
print('phmoms = ')
print(phmoms)
assert la.norm((np.array(phmoms)-np.array(moms))/np.array(moms))<10**-12, "APHFrom3Moments failed to match the given moments!"
print('========================================')
print('Testing BuTools function PH2From3Moments')
print('Input:')
print('------')
moms = [10.0, 160.0, 3500.0]
print('moms = ')
print(moms)
print('Test:')
print('-----')
print('a, A = PH2From3Moments(moms):')
a, A = PH2From3Moments(moms)
print('a = ')
print(a)
print('A = ')
print(A)
phmoms = MomentsFromPH(a, A, 3)
print('phmoms = ')
print(phmoms)
assert la.norm((np.array(phmoms)-np.array(moms))/np.array(moms))<10**-12, "PH2From3Moments failed to match the given moments!"
print('Input:')
print('------')
moms = [10.0, 260.0, 13500.0]
print('moms = ')
print(moms)
print('Test:')
print('-----')
print('a, A = PH2From3Moments(moms):')
a, A = PH2From3Moments(moms)
print('a = ')
print(a)
print('A = ')
print(A)
phmoms = MomentsFromPH(a, A, 3)
print('phmoms = ')
print(phmoms)
assert la.norm((np.array(phmoms)-np.array(moms))/np.array(moms))<10**-12, "PH2From3Moments failed to match the given moments!"
print('========================================')
print('Testing BuTools function PH3From5Moments')
print('Input:')
print('------')
a = ml.matrix([[0.1,0.9,0]])
A = ml.matrix([[-6.2, 2, 0],[2, -9, 1],[1, 0, -3]])
moms = MomentsFromPH(a, A)
print('moms = ')
print(moms)
print('Test:')
print('-----')
print('a, A = PH3From5Moments(moms):')
a, A = PH3From5Moments(moms)
print('a = ')
print(a)
print('A = ')
print(A)
phmoms = MomentsFromME(a, A, 5)
print('phmoms = ')
print(phmoms)
assert la.norm((np.array(phmoms)-np.array(moms))/np.array(moms))<10**-12, "PH3From5Moments failed to match the given moments!"
print('Input:')
print('------')
a = ml.matrix([[0.2,0.3,0.5]])
A = ml.matrix([[-1, 0, 0],[0, -3, 0.5],[0, -0.5, -3]])
moms = MomentsFromME(a, A)
print('moms = ')
print(moms)
print('Test:')
print('-----')
print('a, A = PH3From5Moments(moms):')
a, A = PH3From5Moments(moms)
print('a = ')
print(a)
print('A = ')
print(A)
phmoms = MomentsFromME(a, A, 5)
print('phmoms = ')
print(phmoms)
assert la.norm((np.array(phmoms)-np.array(moms))/np.array(moms))<10**-12, "PH3From5Moments failed to match the given moments!"
print('========================================')
print('Testing BuTools function MEFromMoments')
print('Input:')
print('------')
a = ml.matrix([[0.1,0.9,0]])
A = ml.matrix([[-6.2, 2, 0],[2, -9, 1],[1, 0, -3]])
moms = MomentsFromPH(a, A, 5)
print('moms = ')
print(moms)
print('Test:')
print('-----')
print('a, A = MEFromMoments(moms):')
a, A = MEFromMoments(moms)
print('a = ')
print(a)
print('A = ')
print(A)
memoms = MomentsFromME(a, A, 5)
print('memoms = ')
print(memoms)
assert la.norm((np.array(memoms)-np.array(moms))/np.array(moms))<10**-12, "MEFromMoments failed to match the given moments!"
print('========================================')
print('Testing BuTools function APH2ndMomentLowerBound')
print('Input:')
print('------')
mean = 1.9
print('mean = ')
print(mean)
n = 4
print('n = ')
print(n)
print('Test:')
print('-----')
print('mom2 = APH2ndMomentLowerBound(mean, n):')
mom2 = APH2ndMomentLowerBound(mean, n)
print('mom2 = ')
print(mom2)
print('cv2 = mom2/mean**2-1:')
cv2 = mom2/mean**2-1
print('1/cv2:')
print(1/cv2)
assert np.abs(cv2-1/n)<10**-14, "APH2ndMomentLowerBound did not give the expected result!"
print('========================================')
print('Testing BuTools function APH3rdMomentLowerBound')
print('Input:')
print('------')
mean = 1.9
print('mean = ')
print(mean)
mom2 = 5
print('mom2 = ')
print(mom2)
n = 3
print('n = ')
print(n)
print('Test:')
print('-----')
print('mom3lower = APH3rdMomentLowerBound(mean, mom2, n):')
mom3lower = APH3rdMomentLowerBound(mean, mom2, n)
print('mom3lower = ')
print(mom3lower)
print('mom3upper = APH3rdMomentUpperBound(mean, mom2, n):')
mom3upper = APH3rdMomentUpperBound(mean, mom2, n)
print('mom3upper = ')
print(mom3upper)
assert mom3upper>mom3lower, "Lower bound is larger than the upper bound!"
print('Input:')
print('------')
mean = 1.9
print('mean = ')
print(mean)
mom2 = 5
print('mom2 = ')
print(mom2)
n = 4
print('n = ')
print(n)
print('Test:')
print('-----')
print('mom3lower = APH3rdMomentLowerBound(mean, mom2, n):')
mom3lower = APH3rdMomentLowerBound(mean, mom2, n)
print('mom3lower = ')
print(mom3lower)
print('mom3upper = APH3rdMomentUpperBound(mean, mom2, n):')
mom3upper = APH3rdMomentUpperBound(mean, mom2, n)
print('mom3upper = ')
print(mom3upper)
assert mom3upper>mom3lower, "Lower bound is larger than the upper bound!"
assert mom3upper==np.inf, "Upper bound must be infinity with 4 phases!"
print('========================================')
print('Testing BuTools function APH3rdMomentUpperBound')
print('Input:')
print('------')
mean = 1.9
print('mean = ')
print(mean)
mom2 = 5
print('mom2 = ')
print(mom2)
n = 3
print('n = ')
print(n)
print('Test:')
print('-----')
print('mom3lower = APH3rdMomentLowerBound(mean, mom2, n):')
mom3lower = APH3rdMomentLowerBound(mean, mom2, n)
print('mom3lower = ')
print(mom3lower)
print('mom3upper = APH3rdMomentUpperBound(mean, mom2, n):')
mom3upper = APH3rdMomentUpperBound(mean, mom2, n)
print('mom3upper = ')
print(mom3upper)
assert mom3upper>mom3lower, "Lower bound is larger than the upper bound!"
print('Input:')
print('------')
mean = 1.9
print('mean = ')
print(mean)
mom2 = 5
print('mom2 = ')
print(mom2)
n = 4
print('n = ')
print(n)
print('Test:')
print('-----')
print('mom3lower = APH3rdMomentLowerBound(mean, mom2, n):')
mom3lower = APH3rdMomentLowerBound(mean, mom2, n)
print('mom3lower = ')
print(mom3lower)
print('mom3upper = APH3rdMomentUpperBound(mean, mom2, n):')
mom3upper = APH3rdMomentUpperBound(mean, mom2, n)
print('mom3upper = ')
print(mom3upper)
assert mom3upper>mom3lower, "Lower bound is larger than the upper bound!"
assert mom3upper==np.inf, "Upper bound must be infinity with 4 phases!"
print('========================================')
print('Testing BuTools function CanonicalFromPH2')
print('Input:')
print('------')
a = ml.matrix([[0.12,0.88]])
print('a = ')
print(a)
A = ml.matrix([[-1.28, 0],[3.94, -3.94]])
print('A = ')
print(A)
print('Test:')
print('-----')
print('b, B = CanonicalFromPH2(a, A):')
b, B = CanonicalFromPH2(a, A)
print('b = ')
print(b)
print('B = ')
print(B)
Cm = SimilarityMatrix(A, B)
err1 = la.norm(A*Cm-Cm*B)
err2 = la.norm(a*Cm-b)
print("Transformation errors:")
print(np.max(err1, err2))
assert err1<10**-12 and err2<10**-12, "Transformation to canonical PH(2) failed!"
print('========================================')
print('Testing BuTools function CanonicalFromPH3')
print('Input:')
print('------')
a = ml.matrix([[0.1,0.9,0]])
print('a = ')
print(a)
A = ml.matrix([[-6.2, 2, 0],[2, -9, 1],[1, 0, -3]])
print('A = ')
print(A)
print('Test:')
print('-----')
print('b, B = CanonicalFromPH3(a, A):')
b, B = CanonicalFromPH3(a, A)
print('b = ')
print(b)
print('B = ')
print(B)
Cm = SimilarityMatrix(A, B)
err1 = la.norm(A*Cm-Cm*B)
err2 = la.norm(a*Cm-b)
print("Transformation errors:")
print(np.max(err1, err2))
assert err1<10**-12 and err2<10**-12, "Transformation to canonical PH(3) failed!"
print('========================================')
print('Testing BuTools function AcyclicPHFromME')
print('Input:')
print('------')
a = ml.matrix([[-0.4,1.4,0.]])
print('a = ')
print(a)
A = ml.matrix([[-4., 1., 1.],[0., -2., 1.],[1., 0., -8.]])
print('A = ')
print(A)
print('Test:')
print('-----')
print('b, B = AcyclicPHFromME(a, A):')
b, B = AcyclicPHFromME(a, A)
print('b = ')
print(b)
print('B = ')
print(B)
print('ma = MomentsFromME(a, A, 5):')
ma = MomentsFromME(a, A, 5)
print('ma = ')
print(ma)
print('mb = MomentsFromME(b, B, 5):')
mb = MomentsFromME(b, B, 5)
print('mb = ')
print(mb)
assert la.norm((np.array(ma)-np.array(mb))/np.array(ma))<10**-7, "Transformation to acyclic representation failed!"
print('========================================')
print('Testing BuTools function MonocyclicPHFromME')
print('Input:')
print('------')
a = ml.matrix([[0.2,0.3,0.5]])
print('a = ')
print(a)
A = ml.matrix([[-1., 0., 0.],[0., -3., 2.],[0., -2., -3.]])
print('A = ')
print(A)
print('Test:')
print('-----')
print('b, B = MonocyclicPHFromME(a, A):')
b, B = MonocyclicPHFromME(a, A)
print('b = ')
print(b)
print('B = ')
print(B)
print('ma = MomentsFromME(a, A, 5):')
ma = MomentsFromME(a, A, 5)
print('ma = ')
print(ma)
print('mb = MomentsFromME(b, B, 5):')
mb = MomentsFromME(b, B, 5)
print('mb = ')
print(mb)
assert la.norm((np.array(ma)-np.array(mb))/np.array(ma))<10**-7, "Transformation to monocyclic representation failed!"
print('========================================')
print('Testing BuTools function PHFromME')
print('Input:')
print('------')
a = ml.matrix([[-0.4,1.4]])
print('a = ')
print(a)
A = ml.matrix([[-3.8, 2],[2, -9]])
print('A = ')
print(A)
print('flag = CheckMERepresentation(a, A):')
flag = CheckMERepresentation(a, A)
print('flag = ')
print(flag)
print('flag = CheckPHRepresentation(a, A):')
flag = CheckPHRepresentation(a, A)
print('flag = ')
print(flag)
print('Test:')
print('-----')
print('b, B = PHFromME(a, A):')
b, B = PHFromME(a, A)
print('b = ')
print(b)
print('B = ')
print(B)
print('flag = CheckPHRepresentation(b, B):')
flag = CheckPHRepresentation(b, B)
print('flag = ')
print(flag)
Cm = SimilarityMatrix(A, B)
err1 = la.norm(A*Cm-Cm*B)
err2 = la.norm(a*Cm-b)
print("Transformation error:")
print(np.max(err1, err2))
assert flag and err1<10**-12 and err2<10**-12, "Transformation to PH failed!"
print('Input:')
print('------')
a = ml.matrix([[-0.5,1.5]])
print('a = ')
print(a)
A = ml.matrix([[-3.8, 2],[2, -9]])
print('A = ')
print(A)
print('flag = CheckMERepresentation(a, A):')
flag = CheckMERepresentation(a, A)
print('flag = ')
print(flag)
print('flag = CheckPHRepresentation(a, A):')
flag = CheckPHRepresentation(a, A)
print('flag = ')
print(flag)
print('Test:')
print('-----')
print('b, B = PHFromME(a, A):')
b, B = PHFromME(a, A)
print('b = ')
print(b)
print('B = ')
print(B)
print('flag = CheckPHRepresentation(b, B):')
flag = CheckPHRepresentation(b, B)
print('flag = ')
print(flag)
Cm = SimilarityMatrix(A, B)
err1 = la.norm(A*Cm-Cm*B)
err2 = la.norm(a*Cm-b)
print("Transformation error:")
print(np.max(err1, err2))
assert flag and err1<10**-12 and err2<10**-12, "Transformation to PH failed!"
print('========================================')
print('Testing BuTools function MEOrder')
print('Input:')
print('------')
a = ml.matrix([[1.0/6,1.0/6,1.0/6,1.0/6,1.0/6,1.0/6]])
print('a = ')
print(a)
A = ml.matrix([[-1., 0., 0., 0., 0., 0.],[0.5, -2., 1., 0., 0., 0.],[1., 0., -3., 1., 0., 0.],[1., 0., 1., -4., 1., 0.],[4., 0., 0., 0., -5., 0.],[5., 0., 0., 0., 0., -6.]])
print('A = ')
print(A)
print('Test:')
print('-----')
print('co = MEOrder(a, A, "cont"):')
co = MEOrder(a, A, "cont")
print('co = ')
print(co)
print('oo = MEOrder(a, A, "obs"):')
oo = MEOrder(a, A, "obs")
print('oo = ')
print(oo)
print('coo = MEOrder(a, A, "obscont"):')
coo = MEOrder(a, A, "obscont")
print('coo = ')
print(coo)
print('mo = MEOrder(a, A, "moment"):')
mo = MEOrder(a, A, "moment")
print('mo = ')
print(mo)
assert co==2, "Wrong controllability order returned!"
assert oo==6, "Wrong observability order returned!"
assert coo==2, "The minimum of the controllability and observability order is wrong!"
assert mo==2, "Wrong moment order returned!"
print('Input:')
print('------')
a = ml.matrix([[2.0/3,1.0/3]])
print('a = ')
print(a)
A = ml.matrix([[-1., 1.],[0., -3.]])
print('A = ')
print(A)
print('Test:')
print('-----')
print('co = MEOrder(a, A, "cont"):')
co = MEOrder(a, A, "cont")
print('co = ')
print(co)
print('oo = MEOrder(a, A, "obs"):')
oo = MEOrder(a, A, "obs")
print('oo = ')
print(oo)
print('coo = MEOrder(a, A, "obscont"):')
coo = MEOrder(a, A, "obscont")
print('coo = ')
print(coo)
print('mo = MEOrder(a, A, "moment"):')
mo = MEOrder(a, A, "moment")
print('mo = ')
print(mo)
assert co==2, "Wrong controllability order returned!"
assert oo==1, "Wrong observability order returned!"
assert coo==1, "The minimum of the controllability and observability order is wrong!"
assert mo==1, "Wrong moment order returned!"
print('Input:')
print('------')
b = ml.matrix([[0.2,0.3,0.5]])
B = ml.matrix([[-1., 0., 0.],[0., -3., 1.],[0., -1., -3.]])
print('a, A = MonocyclicPHFromME(b, B):')
a, A = MonocyclicPHFromME(b, B)
print('a = ')
print(a)
print('A = ')
print(A)
print('Test:')
print('-----')
print('co = MEOrder(a, A, "cont"):')
co = MEOrder(a, A, "cont")
print('co = ')
print(co)
print('oo = MEOrder(a, A, "obs"):')
oo = MEOrder(a, A, "obs")
print('oo = ')
print(oo)
print('coo = MEOrder(a, A, "obscont"):')
coo = MEOrder(a, A, "obscont")
print('coo = ')
print(coo)
print('mo = MEOrder(a, A, "moment"):')
mo = MEOrder(a, A, "moment")
print('mo = ')
print(mo)
assert co==9, "Wrong controllability order returned!"
assert oo==3, "Wrong observability order returned!"
assert coo==3, "The minimum of the controllability and observability order is wrong!"
assert mo==3, "Wrong moment order returned!"
print('========================================')
print('Testing BuTools function MEOrderFromMoments')
print('Input:')
print('------')
a = ml.matrix([[0.1,0.9,0]])
print('a = ')
print(a)
A = ml.matrix([[-6.2, 2., 0.],[2., -9., 1.],[1., 0., -3.]])
print('A = ')
print(A)
print('Test:')
print('-----')
print('moms = MomentsFromME(a, A):')
moms = MomentsFromME(a, A)
print('moms = ')
print(moms)
print('mo = MEOrderFromMoments(moms):')
mo = MEOrderFromMoments(moms)
print('mo = ')
print(mo)
assert mo==3, "Wrong moment order returned!"
print('Input:')
print('------')
b = ml.matrix([[0.2,0.3,0.5]])
print('b = ')
print(b)
B = ml.matrix([[-1., 0., 0.],[0., -3., 2.],[0., -2., -3.]])
print('B = ')
print(B)
print('a, A = MonocyclicPHFromME(b, B):')
a, A = MonocyclicPHFromME(b, B)
print('moms = MomentsFromME(a, A):')
moms = MomentsFromME(a, A)
print('moms = ')
print(moms)
print('Test:')
print('-----')
print('mo = MEOrderFromMoments(moms):')
mo = MEOrderFromMoments(moms)
print('mo = ')
print(mo)
assert mo==3, "Wrong moment order returned!"
print('========================================')
print('Testing BuTools function MinimalRepFromME')
print('Input:')
print('------')
a = ml.matrix([[1.0/6,1.0/6,1.0/6,1.0/6,1.0/6,1.0/6]])
print('a = ')
print(a)
A = ml.matrix([[-1., 0., 0., 0., 0., 0.],[0.5, -2., 1., 0., 0., 0.],[1., 0., -3., 1., 0., 0.],[1., 0., 1., -4., 1., 0.],[4., 0., 0., 0., -5., 0.],[5., 0., 0., 0., 0., -6.]])
print('A = ')
print(A)
print('Test:')
print('-----')
print('b, B = MinimalRepFromME(a, A, "cont"):')
b, B = MinimalRepFromME(a, A, "cont")
print('b = ')
print(b)
print('B = ')
print(B)
assert Length(b)==2, "Non-minimal representation returned based on controllability!"
print('b, B = MinimalRepFromME(a, A, "obs"):')
b, B = MinimalRepFromME(a, A, "obs")
print('b = ')
print(b)
print('B = ')
print(B)
assert Length(b)==6, "Non-minimal representation returned based on observability!"
print('b, B = MinimalRepFromME(a, A, "obscont"):')
b, B = MinimalRepFromME(a, A, "obscont")
print('b = ')
print(b)
print('B = ')
print(B)
assert Length(b)==2, "Non-minimal representation returned based on observability and controllability!"
print('b, B = MinimalRepFromME(a, A, "moment"):')
b, B = MinimalRepFromME(a, A, "moment")
print('b = ')
print(b)
print('B = ')
print(B)
assert Length(b)==2, "Non-minimal representation returned based on the moments!"
print('Input:')
print('------')
a = ml.matrix([[2.0/3,1.0/3]])
print('a = ')
print(a)
A = ml.matrix([[-1., 1.],[0., -3.]])
print('A = ')
print(A)
print('Test:')
print('-----')
print('b, B = MinimalRepFromME(a, A, "cont"):')
b, B = MinimalRepFromME(a, A, "cont")
print('b = ')
print(b)
print('B = ')
print(B)
assert Length(b)==2, "Non-minimal representation returned based on controllability!"
print('b, B = MinimalRepFromME(a, A, "obs"):')
b, B = MinimalRepFromME(a, A, "obs")
print('b = ')
print(b)
print('B = ')
print(B)
assert Length(b)==1, "Non-minimal representation returned based on observability!"
print('b, B = MinimalRepFromME(a, A, "obscont"):')
b, B = MinimalRepFromME(a, A, "obscont")
print('b = ')
print(b)
print('B = ')
print(B)
assert Length(b)==1, "Non-minimal representation returned based on observability and controllability!"
print('b, B = MinimalRepFromME(a, A, "moment"):')
b, B = MinimalRepFromME(a, A, "moment")
print('b = ')
print(b)
print('B = ')
print(B)
assert Length(b)==1, "Non-minimal representation returned based on the moments!"
print('Input:')
print('------')
b = ml.matrix([[0.2,0.3,0.5]])
B = ml.matrix([[-1., 0., 0.],[0., -3., 1.],[0., -1., -3.]])
print('a, A = MonocyclicPHFromME(b, B):')
a, A = MonocyclicPHFromME(b, B)
print('a = ')
print(a)
print('A = ')
print(A)
print('Test:')
print('-----')
print('b, B = MinimalRepFromME(a, A, "cont"):')
b, B = MinimalRepFromME(a, A, "cont")
print('b = ')
print(b)
print('B = ')
print(B)
assert Length(b)==Length(a), "Non-minimal representation returned based on controllability!"
print('b, B = MinimalRepFromME(a, A, "obs"):')
b, B = MinimalRepFromME(a, A, "obs")
print('b = ')
print(b)
print('B = ')
print(B)
Cm = SimilarityMatrix(B, A)
err1 = la.norm(B*Cm-Cm*A)
err2 = la.norm(b*Cm-a)
print("Transformation error:")
print(np.max(err1, err2))
assert Length(b)==3 and err1+err2<10**-12, "Non-minimal representation returned based on observability!"
print('b, B = MinimalRepFromME(a, A, "obscont"):')
b, B = MinimalRepFromME(a, A, "obscont")
print('b = ')
print(b)
print('B = ')
print(B)
Cm = SimilarityMatrix(B, A)
err1 = la.norm(B*Cm-Cm*A)
err2 = la.norm(b*Cm-a)
print("Transformation error:")
print(np.max(err1, err2))
assert Length(b)==3 and err1+err2<10**-12, "Non-minimal representation returned based on observability and controllability!"
print('b, B = MinimalRepFromME(a, A, "moment"):')
b, B = MinimalRepFromME(a, A, "moment")
print('b = ')
print(b)
print('B = ')
print(B)
Cm = SimilarityMatrix(B, A)
err1 = la.norm(B*Cm-Cm*A)
err2 = la.norm(b*Cm-a)
print("Transformation error:")
print(np.max(err1, err2))
assert Length(b)==3 and err1+err2<10**-12, "Non-minimal representation returned based on the moments!"
print('========================================')
print('Testing BuTools function SamplesFromPH')
print('Input:')
print('------')
a = ml.matrix([[0.1,0.9,0]])
print('a = ')
print(a)
A = ml.matrix([[-6.2, 2, 0],[2, -9, 1],[1, 0, -3]])
print('A = ')
print(A)
print('Test:')
print('-----')
print('x = SamplesFromPH(a, A, 1000):')
x = SamplesFromPH(a, A, 1000)
print('mt = MarginalMomentsFromTrace(x, 3):')
mt = MarginalMomentsFromTrace(x, 3)
print('mt = ')
print(mt)
print('mp = MomentsFromPH(a, A, 3):')
mp = MomentsFromPH(a, A, 3)
print('mp = ')
print(mp)
