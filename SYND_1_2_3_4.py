q=float(input("Give the distributed load : "))  #Συνδυαστικη ασκηση L1234
Mrd=120
Vrd=70
for l in range(2,11,2):
    M=(q*l**2)/8
    V=(q*l)/2
    if M>=Mrd or V>=Vrd:
        print("Beam Failure")
    else:
        hm=M/Mrd
        hv=V/Vrd
        print("----L=",l,"----M=",M,"----V=",V)
        print("Beam-OK")
        print("hm=",hm,"----hv=",hv)