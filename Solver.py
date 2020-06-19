def Solver(M_x,M_y,L,H,U_inf,neu):
  from GridFDM_2D import GridFDM_2D
  from coefficientSourceTerm import coefficientSourceTerm
  import numpy as np
  from ADI import ADI
  delx,dely,x_p,y_p=GridFDM_2D(M_x,M_y,L,H)
  #print(dely)
  CAW_psi,CAE_psi,CAN_psi,CAS_psi,CAP_psi,ita=coefficientSourceTerm(delx,dely,M_x,M_y)
  alpha=0.1
  def CAE_ohm(u,neu):
      return 1-(u*(delx/(2*neu)))
  def CAW_ohm(u,neu):
      return 1+(u*(delx/(2*neu)))
  def CAN_ohm(v,neu,ita):
      return (ita**2) *(1-v*(delx/(2*neu)))  
  def CAS_ohm(v,neu,ita):
      return (ita**2) *(1+v*(delx/(2*neu)))
	# initial guess
  psi=np.zeros((M_y,M_x)) 
  ohm=np.zeros((M_y,M_x))
  for i in range(M_y):
    ohm[i,:]=-((2*U_inf)/dely)*(i/M_y)*0
  u=np.zeros((M_y,M_x))
  u[M_y-1,:]=U_inf
  v=np.zeros((M_y,M_x))
  whil=0
  while 1==1:
    whil=whil+1
    print(whil)
		# u velocity
    u_old=np.array(u)
    for j in range(1,M_y-1):
      u[j,:]=(psi[j+1,:]-psi[j-1,:])/(2*dely)
       
    # v velocity
    v_old=np.array(v)
    for i in range(1,M_x-1):
      v[:,i]=-(psi[:,i+1]-psi[:,i-1])/(2*delx)
    
    
    # psi (ADI Scheme)
    psi_old=np.array(psi)
    S_psi=(delx**2)*ohm
    psi=ADI(psi,M_x,M_y,L,H,CAE_psi,CAW_psi,CAN_psi,CAS_psi,CAP_psi,S_psi,U_inf,4)
    psi=alpha*psi+(1-alpha)*psi_old

    # ohm(ADI Scheme)
    ohm_old=np.array(ohm)
    CAE_ohm1=CAE_ohm(u,neu)
    #print(CAE_ohm1)
    CAW_ohm1=CAW_ohm(u,neu)
    CAN_ohm1=CAN_ohm(v,neu,ita)
    CAS_ohm1=CAS_ohm(v,neu,ita)
    CAP_ohm1=CAE_ohm1+CAW_ohm1+CAN_ohm1+CAS_ohm1 

    ##coefficient at boundaries
    CAP_ohm1[:,0]=1
    CAW_ohm1[:,0]=0
    CAE_ohm1[:,0]=0
    CAN_ohm1[:,0]=0
    CAS_ohm1[:,0]=0

    CAP_ohm1[0,:]=1
    CAW_ohm1[0,:]=0
    CAE_ohm1[0,:]=0
    CAN_ohm1[0,:]=0
    CAS_ohm1[0,:]=0

    CAP_ohm1[:,M_x-1]=1
    CAW_ohm1[:,M_x-1]=0
    CAE_ohm1[:,M_x-1]=0
    CAN_ohm1[:,M_x-1]=0
    CAS_ohm1[:,M_x-1]=0

    CAP_ohm1[M_y-1,:]=1
    CAW_ohm1[M_y-1,:]=0
    CAE_ohm1[M_y-1,:]=0
    CAN_ohm1[M_y-1,:]=0
    CAS_ohm1[M_y-1,:]=0

    S_ohm=np.zeros((M_y,M_x))
    for j in range(1,M_y-1):
      ohm[j,M_x-1]=-(2/(delx**2))*psi[j,M_x-2]
      ohm[j,0]=-(2/delx**2)*psi[j,1]
    for i in range(1,M_x-1):
      ohm[0,i]=-(2/dely**2)*psi[1,i]
      ohm[M_y-1,i]=-(2*psi[M_y-2,i]+2*U_inf*dely)/(dely**2)
    #print(ohm)
    ohm=ADI(ohm,M_x,M_y,L,H,CAE_ohm1,CAW_ohm1,CAN_ohm1,CAS_ohm1,CAP_ohm1,S_ohm,U_inf,5)
    ohm=alpha*ohm+(1-alpha)*ohm_old
    # Convergence criteria
    #a=np.amax(abs(ohm-ohm_old))
    #print(a)
    if np.amax(abs(ohm-ohm_old))<10**(-10):
      break
  
  return psi,ohm,u,v,x_p,y_p