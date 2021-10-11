//Airline reservation system

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>

//declaring some global variables
int day1,month1,year1,day,month,year;
int monthdays[12]={31,28,31,30,31,30,31,31,30,31,30,31};
int start,des;
char s[100]="bruh";
char d[100]="bruh1"; 

//function to create a time delay before clearing the screen
void delay(int sec){
    int ms=1000*sec;
    clock_t st = clock();
    while (clock()<st+ms)
        ;
}

//function to take time of booking from the system
void dateandtime(){
    struct tm *ptr;
    time_t t;
    t=time(NULL);
    ptr=localtime(&t);
    printf("%s",asctime(ptr));
}

int countLeapYears(int d, int m, int y){
    int years=y;
    if(m<=2)
        years--;
    return (years/4)-(years/100)+(years/400);
}

//function to calculate the difference between two dates
int diffDates(int d1, int m1, int y1, int d2, int m2, int y2){
    int n1=y1*365+d1;
    for(int i=0;i<(m1-1);i++)
        n1+=monthdays[i];
    n1+=countLeapYears(d1,m1,y1);

    int n2=y2*365+d2;
    for(int i=0;i<(m2-1);i++)
        n2+=monthdays[i];
    n2+=countLeapYears(d2,m2,y2);

    return (n2-n1);
}

//function to enter details and print the ticket
void ticket(int r,int c){
    char name[100];
    char dob[20];
    char deets[1];
    printf("\nENTER DETAILS: \n");
    gets(deets);
    printf("\nEnter name: \n");
    gets(name);
    printf("\nEnter date of birth in format dd/mm/yyyy: \n");
    gets(dob);
    printf("Processing...");
    delay(3);
    system("cls");
    printf("---------------------------------------------------\n");
    printf("             WELCOME TO C AIRLINES\n");
    printf("---------------------------------------------------\n");
    printf("Flight no.: MH370\n");
    printf("Departure from: %s\n",s);
    printf("Destination: %s\n",d);
    printf("Date and time of booking: ");
    dateandtime();
    printf("\n");
    printf("Date of flight: ");
    printf("%d/%d/%d\n",day,month,year);
    printf("Departure time: 00:00 GMT\n");
    printf("--------------------------------------------------\n");
    printf("PASSENGER DETAILS: \n");
    printf("Name: ");
    puts(name);
    printf("\n");
    printf("Date of Birth: ");
    puts(dob);
    printf("\n");
    printf("SEAT DETAILS: \n");
    printf("Row: %d\n",r);
    printf("Column: %d\n",c);
    printf("--------------------------------------------------\n");
    printf("               HAVE A SAFE FLIGHT!");
}

bool difference(){
    //taking date of booking from the system
    time_t t;
    t=time(NULL);
    struct tm tm=*localtime(&t);
    day1=tm.tm_mday;
    month1=tm.tm_mon+1;
    year1=tm.tm_year+1900; 
    int m=month-month1;
    int y=(year-year1);

    int diff=diffDates(day1,month1,year1,day,month,year);
    if(diff>60 || diff<1)
        return false;
    else
        return true;
}

//function to choose seats
void booking(int seats[31][6]){
    printf("\nEnter the date of depature you desire in the format DD/MM/YYYY: \n");
        scanf("%d/%d/%d",&day,&month,&year);
    
    if(difference()==false){
        printf("\nYou can only book within 60 days of today. You cannot book on the same day.");
        booking(seats);  
    }
    else{
        printf("\nThe available seats are given by 0 and the occupied seats are given by 1\n");
        for(int i=0;i<31;i++){
            for(int j=0;j<6;j++){
                printf("%d\t",seats[i][j]);
            }
            printf("\n");
        }

        int r,c,n;
        printf("\nEnter the number of seats you want: \n");
        scanf("%d",&n);

        while(n>0){
            printf("\nEnter the row number and column number of the seat you want: \n");
            scanf("%d %d",&r,&c);
            if(seats[r][c]==1){
                printf("\nSorry, this seat is occupied. Please try again.\n");
                delay(3);
                system("cls");
                booking(seats);
            }
            else{
                seats[r][c]=1;
                printf("\nSeat booked!\n");
                ticket(r,c);
                n--;
            }
        }
    }
    
}

//main function
void main(){
    int l=0, u=1;
    int seats[31][6];  
    //airplane has 30 rows and 5 columns of seats
    system("cls");
    printf("Welcome to C Airlines!");
    printf("\nCities we fly to:\n");
    printf("1. MUMBAI (CHHATRAPATI SHAVAJI MAHARAJ INTERNATIONAL AIRPORT)\n");
    printf("2. BERLIN (BERLIN BRANDENBURG AIRPORT)\n");
    printf("3. KAULA LAMPUR (KUALA LAMPUR INTERNATIONAL AIRPORT)\n");
    printf("4. BEIJING (BEIJING CAPITAL INTERNATIONAL AIRPORT)\n");
    printf("5. STOCKHOLM (STOCKHOLM ARLANDA AIRPORT)\n");
    printf("6. LONDON (HEATHROW INTERNATIONAL AIRPORT)\n");
    printf("7. NEW YORK (JOHN F KENNEDY INTERNATIONAL AIRPORT)\n");
    printf("8. CHICAGO (O'HARE INTERNATIONAL AIRPORT)\n");
    printf("9. LOS ANGELES (LOS ANGELES INTERNATIONAL AIRPORT)\n");
    printf("10. TOKYO (NARITA INTERNATIONAL AIRPORT)\n");

    printf("\nEnter the number preceding the start city:\n");
    scanf("%d",&start);
    printf("\nEnter the number preceding the destination:\n");
    scanf("%d",&des);

    if(start==des){
        printf("\nDestination cannot be the same as starting point. Please enter both again.\n");
        delay(3);
        main();
    }
    else{
        switch(start){
            case 1:
                strcpy(s,"CHHATRAPATI SHAVAJI MAHARAJ INTERNATIONAL AIRPORT (BOM)");
                break;
            case 2:
                strcpy(s,"BERLIN BRANDENBURG AIRPORT (BER)");
                break;
            case 3:
                strcpy(s,"KUALA LAMPUR INTERNATIONAL AIRPORT (KUL)");
                break;
            case 4:
                strcpy(s,"BEIJING CAPITAL INTERNATIONAL AIRPORT (PEK)");
                break;
            case 5:
                strcpy(s,"STOCKHOLM ARLANDA AIRPORT (ARN)");
                break;
            case 6:
                strcpy(s,"HEATHROW INTERNATIONAL AIRPORT (LHR)");
                break;
            case 7:
                strcpy(s,"JOHN F KENNEDY INTERNATIONAL AIRPORT (JFK)");
                break;
            case 8:
                strcpy(s,"O'HARE INTERNATIONAL AIRPORT (ORD)");
                break;
            case 9:
                strcpy(s,"LOS ANGELES INTERNATIONAL AIRPORT (LAX)");
                break;
            case 10:
                strcpy(s,"NARITA INTERNATIONAL AIRPORT (NRT)");
                break;
            default:
                printf("\nEnter a valid number (1-10).\n");
                main();
                break;
        }

        switch(des){
            case 1:
                strcpy(d,"CHHATRAPATI SHAVAJI MAHARAJ INTERNATIONAL AIRPORT (BOM)");
                break;
            case 2:
                strcpy(d,"BERLIN BRANDENBURG AIRPORT (BER)");
                break;
            case 3:
                strcpy(d,"KUALA LAMPUR INTERNATIONAL AIRPORT (KUL)");
                break;
            case 4:
                strcpy(d,"BEIJING CAPITAL INTERNATIONAL AIRPORT (PEK)");
                break;
            case 5:
                strcpy(d,"STOCKHOLM ARLANDA AIRPORT (ARN)");
                break;
            case 6:
                strcpy(d,"HEATHROW INTERNATIONAL AIRPORT (LHR)");
                break;
            case 7:
                strcpy(d,"JOHN F KENNEDY INTERNATIONAL AIRPORT (JFK)");
                break;
            case 8:
                strcpy(d,"O'HARE INTERNATIONAL AIRPORT (ORD)");
                break;
            case 9:
                strcpy(d,"LOS ANGELES INTERNATIONAL AIRPORT (LAX)");
                break;
            case 10:
                strcpy(d,"NARITA INTERNATIONAL AIRPORT (NRT)");
                break;
            default:
                printf("\nEnter a valid number (1-10).\n");
                main();
                break;
        }
        
        printf("Processing...");
        delay(3);
        system("cls");

        //randomly assigning seats 'vacant' and 'occupied' status
        for(int i=1;i<31;i++){
            for(int j=1;j<6;j++){
                int num = (rand()%(u-l+1))+l;
                seats[i][j]=num;
            }
        }
        for(int i=0;i<1;i++){
            for(int j=1;j<6;j++)
                seats[i][j]=(j);
        }
        for(int i=1;i<31;i++){
            for(int j=0;j<1;j++)
                seats[i][j]=(i);
        }

        seats[0][0]=0;
        booking(seats);
    }
}