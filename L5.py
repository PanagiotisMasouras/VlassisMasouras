q=float(input("Give the distributed Load : "))   #χρηση τησ while true και της break
Mrd=120
Vrd=70
L=2
while True:
    M=(q*L**2)/8
    V=(q*L)/2  
    if M<Mrd and V<Vrd:
        hm=M/Mrd
        hv=V/Vrd
        print("L=",L,"----M=",M,"----V=",V)
        print("Beam OK")
        print("hm=",hm,"----hv=",hv)
        L=L+0.5
    else:
        print("----BEAM FAILURE----")
        if M>=Mrd and V>=Vrd:
            print("Combined Failure with critical values :")
            print("L=",L,"----M=",M,"----V=",V)
        elif M>=Mrd:
            print("Bending Failure with critical values :")
            print("L=",L,"----M=",M,"----V=",V)
        elif V>=Vrd:
            print("Shear Failure with critical values :")
            print("L=",L,"----M=",M,"----V=",V)
        break  