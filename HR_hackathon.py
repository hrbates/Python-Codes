import wnutils.xml as wx
import matplotlib.pyplot as plt
import math

xml1 = wx.Xml('out_Ia_rho_8.xml')
xml2 = wx.Xml('out_Ia_rho_5e8.xml')
xml3 = wx.Xml('out_Ia_rho_9.xml')
xml4 = wx.Xml('out_Ia_rho_3e9.xml')
xml5 = wx.Xml('out_Ia_rho_5e9.xml')
xml6 = wx.Xml('out_Ia_rho_9e9.xml')

props1 = xml1.get_properties_as_floats(['time', 't9', 'radius', 'rho', 'muekT', 'velocity', 'pressure', 'Ye', 'entropy per nucleon'])
props2 = xml2.get_properties_as_floats(['time', 't9', 'radius', 'rho', 'muekT', 'velocity', 'pressure', 'Ye', 'entropy per nucleon'])
props3 = xml3.get_properties_as_floats(['time', 't9', 'radius', 'rho', 'muekT', 'velocity', 'pressure', 'Ye', 'entropy per nucleon'])
props4 = xml4.get_properties_as_floats(['time', 't9', 'radius', 'rho', 'muekT', 'velocity', 'pressure', 'Ye', 'entropy per nucleon'])
props5 = xml5.get_properties_as_floats(['time', 't9', 'radius', 'rho', 'muekT', 'velocity', 'pressure', 'Ye', 'entropy per nucleon'])
props6 = xml6.get_properties_as_floats(['time', 't9', 'radius', 'rho', 'muekT', 'velocity', 'pressure', 'Ye', 'entropy per nucleon'])

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

cst5 = props5['t9']*pow(10,9)
const5 = pow(cst5,4)
Lum5 = 4*math.pi*(props5['radius']**2)*(5.670*pow(10,-5))*const5
teff5 = cst5

cst6 = props6['t9']*pow(10,9)
const6 = pow(cst6,4)
Lum6 = 4*math.pi*(props6['radius']**2)*(5.670*pow(10,-5))*const6
teff6 = cst6



plt.plot(teff1/pow(10,9),Lum1/pow(10,51), Label = r'$\rho_0$ = $10^8$ g/cc')
plt.plot(teff2/pow(10,9),Lum2/pow(10,51), Label = r'$\rho_0 = 5 \times 10^8$ g/cc')
plt.plot(teff3/pow(10,9),Lum3/pow(10,51), Label = r'$\rho_0 = 10^9$ g/cc')
plt.plot(teff4/pow(10,9),Lum4/pow(10,51), Label = r'$\rho_0 = 3 \times 10^9$ g/cc')
plt.plot(teff5/pow(10,9),Lum5/pow(10,51), Label = r'$\rho_0 = 5 \times 10^9$ g/cc')
plt.plot(teff6/pow(10,9),Lum6/pow(10,51), Label = r'$\rho_0 = 9 \times 10^9$ g/cc')

plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$T_9$')
plt.ylabel('Log L (ergs s$^{-1}$)')
plt.axis([15,1.e-7,1.e-14,20])
plt.title('No Electron Capture')
plt.suptitle('HR Diagram: Evolution After Type Ia Supernova')

plt.legend()
plt.show()
