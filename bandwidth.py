while True:
    n1 = raw_input("Please enter lower edge frequency:")
    if(n1=='q'):
        break;
        exit();
    n2 = raw_input("Please enter upper edge frequency:")
    n3=(float(n2)-float(n1))
    n4=n3/((float(n1))+(n3/2))
    print 'The Bandwidth is ' +str(n4*100.0)+'%'
    print ''
    print ''
