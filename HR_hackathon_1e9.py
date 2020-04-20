import wnutils.xml as wx
import matplotlib.pyplot as plt
import math

xml1 = wx.Xml('out_Ia_rho_9.xml')
xml2 = wx.Xml('out_Ia_weak_rho_9.xml')

props1 = xml1.get_properties_as_floats(['time', 't9', 'radius'])
props2 = xml2.get_properties_as_floats(['time', 't9', 'radius'])


cst1 = props1['t9']*pow(10,9)
const1 = pow(cst1,4)
Lum1 = 4*math.pi*(props1['radius']**2)*(5.670*pow(10,-5))*const1
teff1 = cst1

cst2 = props2['t9']*pow(10,9)
const2 = pow(cst2,4)
Lum2 = 4*math.pi*(props2['radius']**2)*(5.670*pow(10,-5))*const2
teff2 = cst2



plt.plot(teff1/pow(10,9),Lum1/pow(10,51), Label = 'without electron capture')
plt.plot(teff2/pow(10,9),Lum2/pow(10,51), Label = 'with electron capture')

plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$T_9$')
plt.ylabel('Log L (ergs s$^{-1}$)')
plt.axis([15,1.e-8,1.e-15,20])
plt.title(r'$\rho_0 = 9 \times 10^9$ g/cc')
plt.suptitle('HR Diagram: Evolution After Type Ia Supernova')

plt.legend()
plt.show()
