def func(biayaRegisterMember,biayaTiketRegular):
    a = (biayaRegisterMember)
    b = (biayaTiketRegular)
    c = b
    #Cara Jumlah kulmulatif ?
    while b < a + c:
        b += biayaTiketRegular
        c *= 0.9
        print(b)   
        
func(500,15)
