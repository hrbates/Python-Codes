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

const1 = pow((props1['t9']*pow(10,9)),4)
Lum1 = 4*math.pi*(props1['radius']**2)*(5.670*pow(10,-5))*const1/10**51 

const2 = pow((props2['t9']*pow(10,9)),4)
Lum2 = 4*math.pi*(props2['radius']**2)*(5.670*pow(10,-5))*const2/10**51

const3 = pow((props3['t9']*pow(10,9)),4)
Lum3 = 4*math.pi*(props3['radius']**2)*(5.670*pow(10,-5))*const3/10**51

const4 = pow((props4['t9']*pow(10,9)),4)
Lum4 = 4*math.pi*(props4['radius']**2)*(5.670*pow(10,-5))*const4/10**51



plt.plot(props1['time'], Lum1, Label = r'O/Ne/Mg WD without electron capture')
plt.plot(props2['time'], Lum2, Label = r'O/Ne/Mg WD with electron capture')
plt.plot(props3['time'], Lum3, Label = r'C/O WD without electron capture')
plt.plot(props4['time'], Lum4, Label = r'C/O WD with electron capture')

plt.xlabel('Time (s)')
plt.ylabel('Log Luminosity ($10^{51}$ ergs s$^{-1}$)')
plt.yscale('log')
plt.xlim([-1000,1.e5])
plt.suptitle('Combined Light Curve: ~1 Day')
plt.title(r'$\rho_0 = 10^9$')
plt.legend()

plt.show()


