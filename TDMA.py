def TDMA(CAE,CAW,CAP,S,M,Flag,U_inf,T):
	import numpy as np
	A=np.zeros(M)
	B=np.zeros(M)
	A[0]=CAE[0]/CAP[0]
	B[0]=S[0]/CAP[0]
	#S[1]=S[1]+CAW[1]*T[0]
	#S[M-2]=S[M-2]+CAE[M-2]*T[M-1]
	#A[1]=CAE[1]/CAP[1]
	#B[1]=S[1]/CAP[1]

	for i in range(1,M-1):
		A[i]=CAE[i]/(CAP[i]-CAW[i]*A[i-1])
		B[i]=(S[i]+CAW[i]*B[i-1])/(CAP[i]-CAW[i]*A[i-1])

	#T[M-2]=B[M-2]
	for i in range(M-2,0,-1):
		T[i]=A[i]*T[i+1]+B[i]

	return T