q=float(input("Give the distributed load:"))   #Ασκηση με if else elif
L=float(input("Give beams' length:"))
Mrd=120
M=(q*L**2)/8
if M >= Mrd:
    print('Beam Capacity is insufficient')
else:
    h=M/Mrd
    if h <= 0.70:                  #Αυτο ειναι Nested if, δηλ μπαινει μεσα στην else (με 4 κενα)
        print("Low Utilization")
    elif 0.70 < h < 0.90:
        print("High Utilization")
    else: 
        print("Structural Failure Warning")


