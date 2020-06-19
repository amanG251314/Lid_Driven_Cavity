import matplotlib.pyplot as plt
from Solver import Solver
L=1
H=1
U_inf=1
M_x1=11
M_y1=11
M_x2=31
M_y2=31
M_x3=51
M_y3=51
neu=0.01

psi1,ohm1,u1,v1,x1,y1=Solver(M_x1,M_y1,L,H,U_inf,neu)
psi1,ohm2,u2,v2,x2,y2=Solver(M_x2,M_y2,L,H,U_inf,neu)
psi3,ohm3,u3,v3,x3,y3=Solver(M_x3,M_y3,L,H,U_inf,neu)

def plotu3(u1,u2,u3,u_val,uv_val_p,nx1,nx2,nx3):
	import numpy as np
	plt.scatter(uv_val_p,u_val)
	plt.plot(np.arange(nx1)/(nx1-1),u1.T[int(nx1/2),:])
	plt.plot(np.arange(nx2)/(nx2-1),u2.T[int(nx2/2),:])
	plt.plot(np.arange(nx3)/(nx3-1),u3.T[int(nx3/2),:])
	plt.title('X-velocity (u) at x = L/2 vs y')
	plt.xlabel("y (m)")
	plt.ylabel('X-velocity (u) (m/s)')
	plt.legend(['N={}'.format(nx1),'N={}'.format(nx2),'N={}'.format(nx3),'Validation data from research paper'])

def plotv3(u1,u2,u3,u_val,uv_val_p,nx1,nx2,nx3):
	plt.scatter(uv_val_p,u_val)
	plt.plot(np.arange(nx1)/(nx1-1),u1.T[:,int(nx1/2)])
	plt.plot(np.arange(nx2)/(nx2-1),u2.T[:,int(nx2/2)])
	plt.plot(np.arange(nx3)/(nx3-1),u3.T[:,int(nx3/2)])
	plt.title('Y-velocity (v) at y = H/2 vs x')
	plt.xlabel("x (m)")
	plt.ylabel('Y-velocity (v) (m/s)')
	plt.legend(['N={}'.format(nx1),'N={}'.format(nx2),'N={}'.format(nx3),'Validation data from research paper'])

import numpy as np
## Benchmark data for u and v velocities for Re = 100\n
u_val=np.array([0,-0.0419,-0.0771,-0.1098,-0.1419,-0.1727,-0.1984,-0.2129,-0.2091,-0.1820,\
-0.1312,-0.0602,0.02787,0.1404,0.3105,0.5974,1])
uv_val_p = np.arange(0,1+0.0625,0.0625)
v_val=np.array([0,0.0948,0.1492,0.1743,0.1792,0.1691,0.1457,0.1087,0.0575,\
-0.00774,-0.0840,-0.1630,-0.2278,-0.2537,-0.2186,-0.1233,0])

#Plotting
plt.figure()
plotu3(u1,u2,u3,u_val,uv_val_p,M_x1,M_x2,M_x3)
plt.figure()
plotv3(v1,v2,v3,v_val,uv_val_p,M_y1,M_y2,M_y3)

plt.figure(figsize=(6,6))
cs = plt.contour(x3,y3,u3,70,cmap='rainbow',extend='both',alpha=0.6)
plt.title('Countour plot of X-velocity(u)')
plt.xlabel('x(m)')
plt.ylabel('y(m)')

plt.figure(figsize=(6,6))
cs = plt.contour(x3,y3,v3,70,cmap='rainbow',extend='both',alpha=0.7)
plt.title('Countour plot of Y-velocity(v)')
plt.xlabel('x(m)')
plt.ylabel('y(m)')

plt.figure(figsize=(6,6))
cs = plt.contour(x3,y3,psi3,200,cmap='rainbow',extend='both',alpha=0.5)
plt.clabel(cs,inline=1,fontsize=10)
plt.title('stream-lines')
plt.xlabel('x(m)')
plt.ylabel('y(m)')

plt.figure(figsize=(5,5))
cs = plt.quiver(x3,y3,u3,v3)
plt.title('Velocity plot')
plt.xlabel('x(m)')
plt.ylabel('y(m)')

plt.figure(figsize=(6,6))
plt.contour(x3,y3,psi3,70,cmap='rainbow',extend='both',alpha=0.7)
plt.quiver(x3,y3,u3,v3)
plt.title('Velocity Vector and Streamline Plot')
plt.xlabel('x(m)')
plt.ylabel('y(m)')

plt.figure(figsize=(6,6))
cs = plt.contour(x3,y3,ohm3,800,cmap='rainbow',extend='both',alpha=0.7)
plt.title('Vorticity ')
plt.xlabel('x(m)')
plt.ylabel('y(m)')

plt.show()