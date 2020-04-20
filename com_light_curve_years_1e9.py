import wnutils.xml as wx
import matplotlib.pyplot as plt
import math

xml1 = wx.Xml('out_Ia_rho_9.xml')
xml2 = wx.Xml('out_Ia_weak_rho_9.xml')

props1 = xml1.get_properties_as_floats(['time', 't9', 'radius', 'rho'])
props2 = xml2.get_properties_as_floats(['time', 't9', 'radius', 'rho'])


const1 = pow((props1['t9']*pow(10,9)),4)
Lum1 = 4*math.pi*(props1['radius']**2)*(5.670*pow(10,-5))*const1/10**51 

const2 = pow((props2['t9']*pow(10,9)),4)
Lum2 = 4*math.pi*(props2['radius']**2)*(5.670*pow(10,-5))*const2/10**51



plt.plot(props1['time'], Lum1, Label = r'without electron capture')
plt.plot(props2['time'], Lum2, Label = r'with electron capture')

plt.xlabel('Time (s)')
plt.ylabel('Log Luminosity ($10^{51}$ ergs s$^{-1}$)')
plt.yscale('log')
plt.xlim([-1000000,1.e8])
plt.title(r'$\rho_0$ = $10^9$ g/cc')
plt.suptitle('Combined Light Curve: Several Years')

plt.legend()

plt.show()