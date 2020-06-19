def ADI(T1,M_x,M_y,L,H,CAE1,CAW1,CAN1,CAS1,CAP1,S,U_inf,check):
	import numpy as np
	from TDMA import TDMA
	#print(check)

	while 1==1:
		T_old=np.array(T1)
		for j in range(1,M_y-1):
    		# I-Sweep
			I=1
			Tx=T1[j,:]
			#print(T1)
			S_modi1=CAN1[j,:]*T1[j+1,:]+CAS1[j,:]*T1[j-1,:]+S[j,:]
			T1[j,:]=TDMA(CAE1[j,:],CAW1[j,:],CAP1[j,:],S_modi1,M_x,I,U_inf,Tx)

    	
     	
		for i in range(1,M_x-1):
		# J sweep
			J=2
			Ty=T1[:,i]
			S_modi=CAW1[:,i]*T1[:,i-1]+CAE1[:,i]*T1[:,i+1]+S[:,i]            
			T1[:,i]=TDMA(CAN1[:,i],CAS1[:,i],CAP1[:,i],S_modi,M_y,J,U_inf,Ty)

		#print(np.amax(np.absolute(T_old-T1)))
		if np.amax(np.absolute(T_old-T1))<10**(-10):
			break
    
	return T1 