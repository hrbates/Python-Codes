import wnutils.xml as wx
import matplotlib.pyplot as plt
import math

xml1 = wx.Xml('out_Ia_weak_rho_5e8.xml')
xml2 = wx.Xml('out_Ia_weak_rho_9.xml')
xml3 = wx.Xml('out_Ia_weak_rho_3e9.xml')
xml4 = wx.Xml('out_Ia_weak_rho_5e9.xml')
xml5 = wx.Xml('out_Ia_weak_rho_9e9.xml')

props1 = xml1.get_properties_as_floats(['time', 't9', 'radius', 'rho', 'muekT', 'velocity', 'pressure', 'Ye', 'entropy per nucleon'])
props2 = xml2.get_properties_as_floats(['time', 't9', 'radius', 'rho', 'muekT', 'velocity', 'pressure', 'Ye', 'entropy per nucleon'])
props3 = xml3.get_properties_as_floats(['time', 't9', 'radius', 'rho', 'muekT', 'velocity', 'pressure', 'Ye', 'entropy per nucleon'])
props4 = xml4.get_properties_as_floats(['time', 't9', 'radius', 'rho', 'muekT', 'velocity', 'pressure', 'Ye', 'entropy per nucleon'])
props5 = xml5.get_properties_as_floats(['time', 't9', 'radius', 'rho', 'muekT', 'velocity', 'pressure', 'Ye', 'entropy per nucleon'])

const1 = pow((props1['t9']*pow(10,9)),4)
Lum1 = 4*math.pi*(props1['radius']**2)*(5.670*pow(10,-5))*const1/10**51 

const2 = pow((props2['t9']*pow(10,9)),4)
Lum2 = 4*math.pi*(props2['radius']**2)*(5.670*pow(10,-5))*const2/10**51

const3 = pow((props3['t9']*pow(10,9)),4)
Lum3 = 4*math.pi*(props3['radius']**2)*(5.670*pow(10,-5))*const3/10**51

const4 = pow((props4['t9']*pow(10,9)),4)
Lum4 = 4*math.pi*(props4['radius']**2)*(5.670*pow(10,-5))*const4/10**51

const5 = pow((props5['t9']*pow(10,9)),4)
Lum5 = 4*math.pi*(props5['radius']**2)*(5.670*pow(10,-5))*const5/10**51



plt.plot(props1['time'], Lum1, Label = r'$\rho_0$ = $5 \times 10^8$ g/cc')
plt.plot(props2['time'], Lum2, Label = r'$\rho_0$ = $10^9$ g/cc')
plt.plot(props3['time'], Lum3, Label = r'$\rho_0$ = $3 \times 10^9$ g/cc')
plt.plot(props4['time'], Lum4, Label = r'$\rho_0$ = $5 \times 10^9$ g/cc')
plt.plot(props5['time'], Lum5, Label = r'$\rho_0$ = $9 \times 10^9$ g/cc')



plt.xlabel('Time (s)')
plt.ylabel('Log Luminosity ($10^{51}$ ergs s$^{-1}$)')
plt.yscale('log')
plt.xlim([-100,10000])
plt.title(r'With Electron Capture')
plt.suptitle('Combined Light Curve: Several Hours')

plt.legend()

plt.show()
