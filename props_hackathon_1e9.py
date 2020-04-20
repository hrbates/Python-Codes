import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

import wnutils.xml as wx

xml1 = wx.Xml('out_Ia_rho_9.xml')
xml2 = wx.Xml('out_Ia_weak_rho_9.xml')

props1 = xml1.get_properties_as_floats(['time', 't9', 'radius', 'rho', 'muekT', 'velocity', 'pressure', 'Ye', 'entropy per nucleon'])
props2 = xml2.get_properties_as_floats(['time', 't9', 'radius', 'rho', 'muekT', 'velocity', 'pressure', 'Ye', 'entropy per nucleon'])

plt.rc('text', usetex=True)
plt.rc('font', family = 'serif')
plt.rcParams['font.size']=15





plt.plot(props1['time'], props1['t9'], Label = r'without electron capture')
plt.plot(props2['time'], props2['t9'], Label = r'with electron capture')

plt.xlabel('Time (s)')
plt.ylabel(r'$T_9$ (K)')
plt.xlim([0,13])
plt.legend()
plt.suptitle('$T_9$ vs Time')
plt.title(r'$\rho_0 = 10^9$')



plt.figure(2)
plt.plot(props1['time'],props1['rho']/pow(10,9), Label = r'without electron capture')
plt.plot(props2['time'],props2['rho']/pow(10,9), Label = r'with electron capture')

plt.xlabel('Time (s)')
plt.ylabel(r'$\rho$ ($10^{9}$ g/cc)')
plt.xlim([0,10])
plt.legend()
plt.suptitle('Density vs Time')
plt.title(r'$\rho_0 = 10^9$')





plt.figure(3)
plt.plot(props1['time'],props1['muekT'], Label = r'without electron capture')
plt.plot(props2['time'],props2['muekT'], Label = r'with electron capture')

plt.xlabel('Time (s)')
plt.ylabel(r'$\mu_e/kT$ in MeV')
plt.xlim([-2,160])
plt.ylim([-12,50])
plt.legend()
plt.suptitle('Chemical Potential vs Time')
plt.title(r'$\rho_0 = 10^9$')







plt.figure(4)
plt.plot(props1['time'],props1['muekT'], Label = r'without electron capture')
plt.plot(props2['time'],props2['muekT'], Label = r'with electron capture')

plt.xlabel('Time (s)')
plt.ylabel(r'$\mu_e/kT$ in MeV')
plt.xlim([0,20])
plt.ylim([-5, 50])
plt.legend()
plt.suptitle('Chemical Potential vs Time')
plt.title(r'$\rho_0 = 10^9$')







plt.figure(5)
plt.plot(props1['time'],props1['velocity']/pow(10,8), Label = r'without electron capture')
plt.plot(props2['time'],props2['velocity']/pow(10,8), Label = r'with electron capture')

plt.xlabel(r'Time (s)')
plt.ylabel(r'Velocity $(10^8 cm/s)$')
plt.xlim([0, 25])
plt.legend()
plt.suptitle('Velocity vs Time')
plt.title(r'$\rho_0 = 10^9$')







plt.figure(6)
plt.plot(props1['time'],props1['pressure']/pow(10,26),Label = r'without electron capture' )
plt.plot(props2['time'],props2['pressure']/pow(10,26),Label = r'with electron capture' )

plt.xlabel('Time (s)')
plt.ylabel('Pressure $(10^{26}$ dynes cm$^{-2})$')
plt.xlim([0,20])
plt.legend()
plt.suptitle('Pressure vs Time')
plt.title(r'$\rho_0 = 10^9$')






plt.figure(7)
plt.plot(props1['time'],props1['entropy per nucleon'],Label = r'without electron capture' )
plt.plot(props2['time'],props2['entropy per nucleon'],Label = r'with electron capture' )

plt.xlabel('Time (s)')
plt.ylabel('Entropy per Nucleon $(k)$')
plt.suptitle('Entropy per Nucleon vs Time')
plt.title(r'$\rho_0 = 10^9$')
plt.legend()



plt.figure(8)
plt.plot(props1['time'], props1['Ye'], Label = r'without electron capture')
plt.plot(props2['time'], props2['Ye'], Label = r'with electron capture')

plt.xlabel('Time (s)')
plt.ylabel(r'$Y_e$')
plt.ylim([0.464,0.5005])
plt.xlim([-1000000, 100000000])
plt.legend()
plt.suptitle('$Y_e$ vs Time')
plt.title(r'$\rho_0 = 10^9$')








plt.show()