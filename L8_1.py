#λιστα της μορφης (q,L,Mrd,Vrd)
beams = [
    (18, 4, 100, 60),
    (20, 5, 120, 70),
    (15, 6, 130, 65),
    (22, 3, 90, 55)
]
sb=[] #safe beams#
fb=[] #failed beams#
for i in range(0,4,1):
    q=beams[i][0]
    L=beams[i][1]
    Mrd=beams[i][2]
    Vrd=beams[i][3]
    M=q*L**2/8
    V=q*L/2
    hm = M / Mrd
    hv = V / Vrd
    print("L =", L, "M =", M, "V =", V)
    print("hm =", hm, "hv =", hv)
    if M < Mrd and V < Vrd:
        print("Beam OK")
        sb.append((L,M,V))
    else:
        if M >= Mrd and V >= Vrd:
            print("Combined Failure")
        elif M >= Mrd:
            print("Bending Failure")
        elif V >= Vrd:
            print("Shear Failure")
        fb.append((L,M,V))
    print("----------------------")
print("safe beams->",sb)
print("failed beams->",fb)

critical_values=[]
for i in range(0,4,1):
    q=beams[i][0]
    L=beams[i][1]
    Mrd=beams[i][2]
    Vrd=beams[i][3]
    while True:
        M=q*L**2/8
        V=q*L/2
        if M<=Mrd and V<=Vrd:
          print("Safe beam")
          q=q+1
        else:
            critical_values.append((q,L,M,V))
            break
print("Critical values ->", critical_values)