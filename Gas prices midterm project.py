#read the file, I want the year and the price of gas together, iits going to be the total amount of gas over the year divided by 52 weeks
#Becaause this is a weekly text file, it mentions incomplete years, which are 1993 and 2013

#First, lets read the file
def read_file():
    gas_price = open('Gas Prices.txt', 'r')
    x = gas_price.readlines()
    list1 = []
    list2 = []
    for things in x:
        things = things.split(':')
        list1.append(things)
        list2.append(things)
    #This for loop makes the first list only have the year and the gas price
    i = 0
    for line in list1:
        a = line[0]
        b = line[1]
        a = a[6:]
        list1[i] = [a,b]
        i +=1
    i = 0
    for line in list2:
        a = line[0]
        b = line[1]
        c = a[0:2] +'-' + a[6:]
        list2[i] = [c,b]
        i += 1
#This is finding the average price per year with years in the text file that have 52 gas prices, a das price a week
    aveyear = []
    avemonth = []
    max_min_year = []
    i = 0
    g = 0
    sum1 = 0
    sum2 = 0
    c, d = list1[0]
    e, f = list2[0]
    max1 = float(d)
    min1 = float(d)
    for line in list1:
        a,b = line
        if a == c:
            sum1 += float(b)
            i += 1
            if max1 < float(b):
                max1 = float(b)
            if min1 > float(b):
                min1 = float(b)

        else:
            max_min_year.append((min1,max1))
            min1 = float(b)
            max1 = float(b)
            if i == 52:
                aveyear.append((a, round(sum1/i , 3)))
            i = 1
            c = a
            sum1 = float(b)
    for line in list2:
        a, b = line
        if a == e:
            sum2 += float(b)
            g += 1
        else:
            avemonth.append((a,round(sum2 / 4 , 3)))
            g = 1
            e = a
            sum2 = float(f)
    print('Ave year' , aveyear)
    print('Ave month' , avemonth)
    print('Max and min each year' , max_min_year)
        

    
   
read_file()
    
    
    

