while True:
    n1 = raw_input("Please enter lower edge frequency (in GHz): ")
    if(n1=='q'):
        break;
        exit();
    furr=(300)/float(n1)
    n2 = raw_input("Dimension ")
    furra=float(n2)/furr
    print 'Dimenasion in terms of wavelength is ' +str(furra)
    print ''
print ''
