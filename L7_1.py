L_values = [2, 4, 6, 8, 10]
q = 20
Mrd = 120
M_values=[]
for x in L_values:
    M=(q*x**2)/8
    M_values.append(M)
    if M>=Mrd:
        print(x, M, "Beam Failure")
    else:
        print(x,M,"Beam OK")

