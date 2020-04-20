import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

import wnutils.xml as wx


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

plt.rc('text', usetex=True)
plt.rc('font', family = 'serif')
plt.rcParams['font.size']=15





plt.plot(props1['time'], props1['t9'], Label = r'$\rho_0$ = $5 \times 10^8$ g/cc')
plt.plot(props2['time'], props2['t9'], Label = r'$\rho_0$ = $10^9$ g/cc')
plt.plot(props3['time'], props3['t9'], Label = r'$\rho_0$ = $3 \times 10^9$ g/cc')
plt.plot(props4['time'], props4['t9'], Label = r'$\rho_0$ = $5 \times 10^8$ g/cc')
plt.plot(props5['time'], props5['t9'], Label = r'$\rho_0$ = $9 \times 10^8$ g/cc')

plt.xlabel('Time (s)')
plt.ylabel(r'$T_9$ (K)')
plt.xlim([0, 25])
plt.legend()
plt.suptitle('$T_9$ vs Time')
plt.title('With Electron Capture')



plt.figure(2)
plt.plot(props1['time'],props1['rho']/pow(10,9), Label = r'$\rho_0$ = $5 \times 10^8$ g/cc')
plt.plot(props2['time'],props2['rho']/pow(10,9), Label = r'$\rho_0$ = $10^9$ g/cc')
plt.plot(props3['time'],props3['rho']/pow(10,9), Label = r'$\rho_0$ = $3 \times 10^9$ g/cc')
plt.plot(props4['time'],props4['rho']/pow(10,9), Label = r'$\rho_0$ = $5 \times 10^9$ g/cc')
plt.plot(props5['time'],props5['rho']/pow(10,9), Label = r'$\rho_0$ = $9 \times 10^9$ g/cc')


plt.xlabel('Time (s)')
plt.ylabel(r'$\rho$ ($10^{9}$ g/cc)')
plt.xlim([0,20])
plt.legend()
plt.suptitle('Density vs Time')
plt.title('With Electron Capture')





plt.figure(3)
plt.plot(props1['time'],props1['muekT'], Label = r'$\rho_0$ = $5 \times 10^8$ g/cc')
plt.plot(props2['time'],props2['muekT'], Label = r'$\rho_0$ = $10^9$ g/cc')
plt.plot(props3['time'],props3['muekT'], Label = r'$\rho_0$ = $3 \times 10^9$ g/cc')
plt.plot(props4['time'],props4['muekT'], Label = r'$\rho_0$ = $5 \times 10^9$ g/cc')
plt.plot(props5['time'],props5['muekT'], Label = r'$\rho_0$ = $9 \times 10^9$ g/cc')


plt.xlabel('Time (s)')
plt.ylabel(r'$\mu_e/kT$ in MeV')
plt.xlim([-2,50])
plt.ylim([-8,100])
plt.legend()
plt.suptitle('Chemical Potential vs Time')
plt.title('With Electron Capture')







plt.figure(4)
plt.plot(props1['time'],props1['muekT'], Label = r'$\rho_0$ = $5 \times 10^8$ g/cc')
plt.plot(props2['time'],props2['muekT'], Label = r'$\rho_0$ = $10^9$ g/cc')
plt.plot(props3['time'],props3['muekT'], Label = r'$\rho_0$ = $3 \times 10^9$ g/cc')
plt.plot(props4['time'],props4['muekT'], Label = r'$\rho_0$ = $5 \times 10^9$ g/cc')
plt.plot(props5['time'],props5['muekT'], Label = r'$\rho_0$ = $9 \times 10^9$ g/cc')


plt.xlabel('Time (s)')
plt.ylabel(r'$\mu_e/kT$ in MeV')
plt.xlim([0,20])
plt.ylim([-5, 100])
plt.legend()
plt.suptitle('Chemical Potential vs Time')
plt.title('With Electron Capture')






plt.figure(5)
plt.plot(props1['time'],props1['velocity']/pow(10,8), Label = r'$\rho_0$ = $5 \times 10^8$ g/cc')
plt.plot(props2['time'],props2['velocity']/pow(10,8), Label = r'$\rho_0$ = $10^9$ g/cc')
plt.plot(props3['time'],props3['velocity']/pow(10,8), Label = r'$\rho_0$ = $3 \times 10^9$ g/cc')
plt.plot(props4['time'],props4['velocity']/pow(10,8), Label = r'$\rho_0$ = $5 \times 10^9$ g/cc')
plt.plot(props5['time'],props5['velocity']/pow(10,8), Label = r'$\rho_0$ = $9 \times 10^9$ g/cc')


plt.xlabel(r'Time (s)')
plt.ylabel(r'Velocity $(10^8 cm/s)$')
plt.xlim([-2, 50])
plt.legend()
plt.suptitle('Velocity vs Time')
plt.title('With Electron Capture')






plt.figure(6)
plt.plot(props1['time'],props1['pressure']/pow(10,26),Label = r'$\rho_0$ = $5 \times 10^8$ g/cc' )
plt.plot(props2['time'],props2['pressure']/pow(10,26),Label = r'$\rho_0$ = $10^9$ g/cc' )
plt.plot(props3['time'],props3['pressure']/pow(10,26),Label = r'$\rho_0$ = $3 \times 10^9$ g/cc' )
plt.plot(props4['time'],props4['pressure']/pow(10,26),Label = r'$\rho_0$ = $5 \times 10^9$ g/cc' )
plt.plot(props5['time'],props5['pressure']/pow(10,26),Label = r'$\rho_0$ = $9 \times 10^9$ g/cc' )


plt.xlabel('Time (s)')
plt.ylabel('Pressure $(10^{26}$ dynes cm$^{-2})$')
plt.xlim([0,20])
plt.legend()
plt.suptitle('Pressure vs Time')
plt.title('With Electron Capture')






plt.figure(7)
plt.plot(props1['time'],props1['entropy per nucleon'],Label = r'$\rho_0$ = $5 \times 10^8$ g/cc' )
plt.plot(props2['time'],props2['entropy per nucleon'],Label = r'$\rho_0$ = $10^9$ g/cc' )
plt.plot(props3['time'],props3['entropy per nucleon'],Label = r'$\rho_0$ = $3 \times 10^9$ g/cc' )
plt.plot(props4['time'],props4['entropy per nucleon'],Label = r'$\rho_0$ = $5 \times 10^9$ g/cc' )
plt.plot(props5['time'],props5['entropy per nucleon'],Label = r'$\rho_0$ = $9 \times 10^9$ g/cc' )


plt.xlabel('Time (s)')
plt.ylabel('Entropy per Nucleon $(k)$')
plt.suptitle('Entropy per Nucleon vs Time')
plt.title('With Electron Capture')
plt.xlim([-100000, 60000000])
plt.legend()



plt.figure(8)
plt.plot(props1['time'], props1['Ye'], Label = r'$\rho_0$ = $5 \times 10^8$ g/cc')
plt.plot(props2['time'], props2['Ye'], Label = r'$\rho_0$ = $10^9$ g/cc')
plt.plot(props3['time'], props3['Ye'], Label = r'$\rho_0$ = $3 \times 10^9$ g/cc')
plt.plot(props4['time'], props4['Ye'], Label = r'$\rho_0$ = $5 \times 10^9$ g/cc')
plt.plot(props5['time'], props5['Ye'], Label = r'$\rho_0$ = $9 \times 10^9$ g/cc')

plt.xlabel('Time (s)')
plt.ylabel(r'$Y_e$')
plt.ylim([0.437,0.5005])
plt.xlim([-1000, 100000])
plt.legend()
plt.suptitle('$Y_e$ vs Time')
plt.title('With Electron Capture')








plt.show()