q=float(input("Give an initial Value of q : "))
l=6
Mrd=120
Vrd=70
while True:
    M=(q*l**2)/8
    V=(q*l)/2
    if M<Mrd and V<Vrd:
        hm=M/Mrd
        hv=V/Vrd
        print("+++BEAM OK+++","q=",q,"----M=",M,"----V=",V)
        q=q+1
    else:
        print("+++ATTENTION+++")
        if M>=Mrd and V>=Vrd:
            print("Combined Failure with critical values :")
            print("q=",q,"----M=",M,"----V=",V)
        elif M>=Mrd:
            print("Bending Failure with critical values :")
            print("q=",q,"----M=",M,"----V=",V)
        elif V>=Vrd:
            print("Shear Failure with critical values :")
            print("q=",q,"----M=",M,"----V=",V)
        break