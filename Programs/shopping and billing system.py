print("*" * 26 + "WELCOME SHOPPING CENTRE" + "*" * 26)
m = 'Y'
amt=0
while m=='Y':
    print("/" * 80)
    print("\tSECTION:1 STATIONARY\n\tSECTION:2 COSMETIC\n\tSECTION:3 PLASTICS\n\tSECTION:4 FOOD ITEMS\n\tSECTION:5 FURNITURE\n")
    n=int(input("ENTER YOUR CHOICE\t"))
    a1=[80,60,60,60,70,35,35,70,120,200]
    a2=[90,30,60,120,340,230,110,200,390,400]
    a3=[70,70,70,100,180,240,40,400,500,290]
    a4=[40,40,40,150,150,60,60,10,10,30]
    a5=[10000,12000,30000,25000,45000,25000,45000,35000,35000,5000]
    c=1
    if n==1:
        while c==1:
            print("!" * 80)
            print("\t\tWELCOME TO STATIONARY SECTION")
            print("!" * 80)
            print("LIST OF ITEMS\n")
            print("1.coloured marker\t\t\t\t80")
            print("2.english copy\t\t\t\t60")
            print("3.math copy\t\t\t\t60")
            print("4.hindi copy\t\t\t\t60")
            print("5.drawing book\t\t\t\t70")
            print("6.blue gel pen\t\t\t\t35")
            print("7.black gel pen\t\t\t\t35")
            print("8.crayons\t\t\t\t70")
            print("9.sparkle pen\t\t\t\t120")
            print("10.spiral notebook\t\t\t200")
            print("ENTER YOUR CHOICE FROM 1-10")
            a=int(input())
            print("ENTER THE NUM OF ITEMS YOU WANT TO BUY")
            b=int(input())
            amt=amt+(b*a1[a-1])
            print(amt)
            c=0
            print("PRESS 1 TO PLACE MORE ORDER ELSE PRESS 0")
            C=int(input())
    elif n==2:
        while c==1:
            print("!" * 80)
            print("\t\tWELCOME TO COSMETIC SECTION")
            print("!" * 80)
            print("LIST OF ITEMS\n")
            print("1.Hairband set\t\t\t\t90")
            print("2.eye shadow mini pack\t\t\t30")
            print("3.nailpaint with remover\t\t60")
            print("4.makeup kit\t\t\t\t120")
            print("5.facial kit (gold)\t\t\t340")
            print("6.10 piece comb set\t\t\t230")
            print("7.kids pin set\t\t\t\t110")
            print("8.fog perfumes\t\t\t\t200")
            print("9.mini jewellery\t\t\t390")
            print("10.bridal combo \t\t\t400")
            print("ENTER YOUR CHOICE FROM 1-10")
            a=int(input())
            print("ENTER THE NUM OF ITEMS YOU WANT TO BUY")
            b=int(input())
            amt=amt+(b*a2[a-1])
            print(amt)
            C=0
            print("PRESS 1 TO PLACE MORE ORDER ELSE PRESS 0")
            C=int(input())
    elif n==3:
        while c==1:
            print("!" * 80)
            print("\t\tWELCOME TO PLASTIC SECTION")
            print("!" * 80)
            print("LIST OF ITEMS\n")
            print("1.Lunch box \t\t\t70")
            print("2.Three bowl set \t\t70")
            print("3.water bottle \t\t\t70")
            print("4.Tray set(3) \t\t\t100")
            print("5.Cup set \t\t\t180")
            print("6.Stool set \t\t\t200")
            print("7.1L container \t\t\t40")
            print("8.Bathroom objects \t\t400(full set)")
            print("9.Utensils stand \t\t500")
            print("10.Protective cases \t\t290(moblie+remote  each)")
            print("ENTER YOUR CHOICE FROM 1-10")
            a=int(input())
            print("ENTER THE NUM OF ITEMS YOU WANT TO BUY")
            b=int(input())
            amt=amt+(b*a3[a-1])
            print(amt)
            c=0
            print("PRESS 1 TO PLACE MORE ORDER ELSE PRESS 0")
            C=int(input())
    elif n==4:
        while c==1:
            print("!" * 80)
            print("\t\tWELCOME TO FOOD ITEMS SECTION")
            print("!" * 80)
            print("LIST OF ITEMS\n")
            print("1.Burger \t\t\t40")
            print("2.Ice cream \t\t\t40")
            print("3.Chowmien \t\t\t40")
            print("4.Cheese pizza \t\t\t150")
            print("5.Chilli potato \t\t150")
            print("6.Spring roll \t\t\t60")
            print("7.Manchurian \t\t\t60")
            print("8.Samosa \t\t\t10")
            print("9.paties \t\t\t10")
            print("10.Pastry \t\t\t30")
            print("ENTER YOUR CHOICE FROM 1-10")
            a=int(input())
            print("ENTER THE NUM OF ITEMS YOU WANT TO BUY")
            b=int(input())
            amt=amt+(b*a4[a-1])
            print(amt)
            c=0
            print("PRESS 1 TO PLACE MORE ORDER ELSE PRESS 0")
            C=int(input())
    elif n==5:
        while c==1:
            print("!" * 80)
            print("\t\tWELCOME TO FURNITURE SECTION")
            print("!" * 80)
            print("LIST OF ITEMS\n")
            print("1.Double Bed \t\t\t10000")
            print("2.Single bed \t\t\t12000")
            print("3.Sofa set \t\t\t130000")
            print("4.Dining table \t\t\t25000")
            print("5.Computer table \t\t45000")
            print("6.Dressing table \t\t25000")
            print("7.Showcase(glass) \t\t45000")
            print("8.Almirah \t\t\t35000")
            print("9.Corner Table \t\t\t35000")
            print("10.Rolling chair \t\t5000")
            a=int(input())
            print("ENTER THE NUM OF ITEMS YOU WANT TO BUY")
            b=int(input())
            amt=amt+(b*a5[a-1])
            print(amt)
            c=0
            print("PRESS 1 TO PLACE MORE ORDER ELSE PRESS 0")
            C=int(input())
    else:
        print("!" * 30+ "YOU ENTERED WRONG CHOICE" + "!" * 30)
    m=' '
    print("TO GET THE SECTION LIST TYPE'Y' ELSE'N'")
    m=input()
print("#" * 80)
print("#" * 80)
print("*" * 26 + " JAINS SHOPPING CENTRE" + "*" * 26)
if amt>0:
    val=14.5*amt/100
    tamt=amt+val
    print("-"   *  80)
    print("*"  * 60+ "BILL"+  "*"  * 60)
    print("TAX CHARGES 14.5%")
    print("PURCHASE DONE OF:- \tRS.",amt)
    print("TAX TO BE PAID:-\tRS.",val)
    print("\t\t\t----------")
    print("TOTAL AMOUNT:-\t\tRS.",tamt)
    print("\t\t\t----------")
    print("---------THANKS FOR DOING SHOPPING WITH US!-------")
    print("YOUR PLEASURE OUR COMFORT !!!!")
    print("!!!!!!!!!!!!!!!HAVE A NICE DAY!!!!!!!!!!!!!!!!!")
else:
    print("YOU HAVE NOT DONE ANY SHOPPING")
    print("#" * 80)
    print("#" * 80)
                    
    
    
