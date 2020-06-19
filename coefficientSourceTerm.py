def coefficientSourceTerm(delx,dely,M_x,M_y):
	import numpy as np
	ita=delx/dely

	CAW_psi=np.ones((M_y,M_x))
	CAE_psi=np.ones((M_y,M_x))
	CAN_psi=np.ones((M_y,M_x))
	CAS_psi=np.ones((M_y,M_x))

	CAN_psi=CAN_psi*(ita**2)
	CAS_psi=CAS_psi*(ita**2)
	CAP_psi=CAW_psi+CAE_psi+CAN_psi+CAS_psi

	CAP_psi[:,0]=1
	CAW_psi[:,0]=0
	CAE_psi[:,0]=0
	CAN_psi[:,0]=0
	CAS_psi[:,0]=0

	CAP_psi[0,:]=1
	CAW_psi[0,:]=0
	CAE_psi[0,:]=0
	CAN_psi[0,:]=0
	CAS_psi[0,:]=0

	CAP_psi[:,M_x-1]=1
	CAW_psi[:,M_x-1]=0
	CAE_psi[:,M_x-1]=0
	CAN_psi[:,M_x-1]=0
	CAS_psi[:,M_x-1]=0

	CAP_psi[M_y-1,:]=1
	CAW_psi[M_y-1,:]=0
	CAE_psi[M_y-1,:]=0
	CAN_psi[M_y-1,:]=0
	CAS_psi[M_y-1,:]=0



	return CAW_psi,CAE_psi,CAN_psi,CAS_psi,CAP_psi,ita