import wnutils.xml as wx
import matplotlib.pyplot as plt
import math

xml1 = wx.Xml('out_Ia_rho_9_ONEMG.xml')
xml2 = wx.Xml('out_Ia_weak_rho_9_ONEMG.xml')
xml3 = wx.Xml('out_Ia_rho_9.xml')
xml4 = wx.Xml('out_Ia_weak_rho_9.xml')

props1 = xml1.get_properties_as_floats(['time', 't9', 'radius', 'rho', 'muekT', 'velocity', 'pressure', 'Ye', 'entropy per nucleon'])
props2 = xml2.get_properties_as_floats(['time', 't9', 'radius', 'rho', 'muekT', 'velocity', 'pressure', 'Ye', 'entropy per nucleon'])
props3 = xml3.get_properties_as_floats(['time', 't9', 'radius', 'rho', 'muekT', 'velocity', 'pressure', 'Ye', 'entropy per nucleon'])
props4 = xml4.get_properties_as_floats(['time', 't9', 'radius', 'rho', 'muekT', 'velocity', 'pressure', 'Ye', 'entropy per nucleon'])

cst1 = props1['t9']*pow(10,9)
const1 = pow(cst1,4)
Lum1 = 4*math.pi*(props1['radius']**2)*(5.670*pow(10,-5))*const1
teff1 = cst1

cst2 = props2['t9']*pow(10,9)
const2 = pow(cst2,4)
Lum2 = 4*math.pi*(props2['radius']**2)*(5.670*pow(10,-5))*const2
teff2 = cst2

cst3 = props3['t9']*pow(10,9)
const3 = pow(cst3,4)
Lum3 = 4*math.pi*(props3['radius']**2)*(5.670*pow(10,-5))*const3
teff3 = cst3

cst4 = props4['t9']*pow(10,9)
const4 = pow(cst4,4)
Lum4 = 4*math.pi*(props4['radius']**2)*(5.670*pow(10,-5))*const4
teff4 = cst4


plt.plot(teff1/pow(10,9),Lum1/pow(10,51), Label = r'O/Ne/Mg WD without electron capture')
plt.plot(teff2/pow(10,9),Lum2/pow(10,51), Label = r'O/Ne/Mg WD with electron capture')
plt.plot(teff3/pow(10,9),Lum3/pow(10,51), Label = r'C/O WD without electron capture')
plt.plot(teff4/pow(10,9),Lum4/pow(10,51), Label = r'C/O WD with electron capture')

plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$T_9$')
plt.ylabel('Log L (ergs s$^{-1}$)')
plt.axis([15,1.e-8,1.e-15,20])
plt.title(r'$\rho_0 = 10^9$')
plt.suptitle('HR Diagram: Evolution After Type Ia Supernova')

plt.legend()
plt.show()
