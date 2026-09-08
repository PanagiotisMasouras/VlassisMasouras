q=float(input("Give Distributed Load : "))     #Ασκηση με and και or
l=float(input("Give Beams' Length : "))
Mrd=120
Vrd=70
M=(q*l**2)/8
V=(q*l)/2
if M>=Mrd or V>=Vrd:
    print("Beam NOT-OK")
else:
    hm=M/Mrd
    hv=V/Vrd
    print("Beam OK")
    print(hm)
    print(hv)
