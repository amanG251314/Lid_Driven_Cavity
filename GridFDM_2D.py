def GridFDM_2D(M_x,M_y,L,H):
	import numpy as np
	delx=L/(M_x-1)
	dely=H/(M_y-1)

	x_p=np.zeros(M_x)
	k=0
	for i in range(M_x):
		x_p[i]=delx*k
		k=k+1
	

	y_p=np.zeros(M_y)
	k=0
	for i in range(M_y):
		y_p[i]=dely*k
		k=k+1
	
	x_p,y_p=np.meshgrid(x_p,y_p)
	#rint(delx)
	return delx,dely,x_p,y_p