#include <iostream>
#include <conio.h>
#include<math.h>
#include<graphics.h>
using namespace std;
bool gameover=false,gamewon=false,goup=true,goup2=true,goup3=true,goup4=true;
void user(int x,int y)    //for printing user object(Game character)
{
	setcolor(WHITE);
	circle(x,y,15);
	setfillstyle(SOLID_FILL,YELLOW);
	floodfill(x+1,y-1,WHITE);
}

void enemy(int &x,int &y,char d)    //for printing enemy object(Game character)
{
	setcolor(WHITE);
	circle(x,y,15);
	setfillstyle(SOLID_FILL,RED);
	floodfill(x+1,y-1,WHITE);
	
	if(d=='e'){
		if(goup)
		{
			y+=5;
			if(y>470)
				goup=false;
		}
		else
		{
			y-=5;
			if(y<50)
				goup=true;
		}
	}
	else if(d=='m'){
		if(goup)
		{
			y+=10;
			if(y>470)
				goup=false;
		}
		else
		{
			y-=10;
			if(y<50)
				goup=true;
		}
	}
	else{
		if(goup)
		{
			y+=15;
			if(y>470)
				goup=false;
		}
		else
		{
			y-=15;
			if(y<50)
				goup=true;
		}
	}	
}

void enemy2(int &x,int &y,char d)    //for printing enemy object(Game character)
{
	setcolor(WHITE);
	circle(x,y,15);
	setfillstyle(SOLID_FILL,RED);
	floodfill(x+1,y-1,WHITE);
	if(d=='e'){

		if(goup2)
		{
			y+=10;
			if(y>470)
				goup2=false;
		}
		else
		{
			y-=5;
			if(y<50)
				goup2=true;
		}
	}
	else if(d=='m'){
		if(goup2)
		{
			y+=15;
			if(y>470)
				goup2=false;
		}
		else
		{
			y-=10;
			if(y<50)
				goup2=true;
		}
	}
	else{
		if(goup2)
		{
			y+=20;
			if(y>470)
				goup2=false;
		}
		else
		{
			y-=15;
			if(y<50)
				goup2=true;
		}
	}
}

void enemy3(int &x,int &y,char d)    //for printing enemy object(Game character)
{
	setcolor(WHITE);
	circle(x,y,15);
	setfillstyle(SOLID_FILL,RED);
	floodfill(x+1,y-1,WHITE);
	if(d=='e'){
		if(goup3)
		{
			x+=8;
			if(x>563)
				goup3=false;
		}
		else
		{
			x-=4;
			if(x<270)
				goup3=true;
		}
	}
	else if(d=='m'){
		if(goup3)
		{
			x+=12;
			if(x>563)
				goup3=false;
		}
		else
		{
			x-=8;
			if(x<270)
				goup3=true;
		}
	}
	else{
		if(goup3)
		{
			x+=16;
			if(x>563)
				goup3=false;
		}
		else
		{
			x-=12;
			if(x<270)
				goup3=true;
		}
	}
}

void enemy4(int &x,int &y,char d)    //for printing enemy object(Game character)
{
	setcolor(WHITE);
	circle(x,y,15);
	setfillstyle(SOLID_FILL,RED);
	floodfill(x+1,y-1,WHITE);
	if(d=='e'){
		if(goup4)
		{
			x+=5;
			if(x>563)
				goup4=false;
		}
		else
		{
			x-=3;
			if(x<270)
				goup4=true;
		}
	}
	else if(d=='m'){
		if(goup4)
		{
			x+=12;
			if(x>563)
				goup4=false;
		}
		else
		{
			x-=7;
			if(x<270)
				goup4=true;
		}
	}
	else{
		if(goup4)
		{
			x+=20;
			if(x>563)
				goup4=false;
		}
		else
		{
			x-=15;
			if(x<270)
				goup4=true;
		}
	}
}


bool isBlocked(int x0,int y0)     //for checking that it does not cross the game obstacle
{
	if(x0==760 && y0==460)
	{gamewon=true;return false;}
	int x,y;
	for(int i=0;i<360;i++)
	{
		x=x0+15*cos(i);		//finding x,y points of circle 
		y=y0+15*sin(i);
	if(x<30 || y<30 || x>790 || y>490  )
	return false;
	else if(x>100 && x<110 && y>100 && y<420)
    return false;
	else if(x>710 && x<720 && y>100 && y<420)
	return false;
	else if(x>240 && x<250 && y>30 && y<130)
	{gameover=true;return false;}
	else if(x>580 && x<590 && y>30 && y<130)
	{gameover=true;return false;}
	else if(x>240 && x<250 && y>390 && y<490)
	{gameover=true;return false;}
	else if(x>580 && x<590 && y>390 && y<490)
	{gameover=true;return false;}
	else if(x>180 && x<250 && y>220 && y<230)
	{gameover=true;return false;}
	else if(x>180 && x<250 && y>290 && y<300)
	{gameover=true;return false;}
	else if(x>580 && x<650 && y>220 && y<230)
	{gameover=true;return false;}
	else if(x>580 && x<650 && y>290 && y<300)
	{gameover=true;return false;}
	else if(x>300 && x<530 && y>80 && y<90)
	return false;
	else if(x>300 && x<530 && y>430 && y<440)
	return false;
	else if(x>290 && x<545 && y>170 && y<350)
	{gameover=true;return false;}
	else if(x==280 && y==60){
		gameover=true;return false;
	}
	}
	return true;
}
void map()
{
		int x,y;
		rectangle(20,20,800,500);
		rectangle(30,30,790,490);
		setfillstyle(8,BLUE);
		floodfill(25,25,WHITE);
		line(240,30,240,130);
		line(250,30,250,130);
		line(240,130,250,130);
		floodfill(241,129,WHITE);
		line(240,490,240,390);
		line(250,490,250,390);
		line(240,390,250,390);
		floodfill(241,391,WHITE);
		line(590,30,590,130);
		line(580,30,580,130);
		line(590,130,580,130);
		floodfill(581,31,WHITE);
		line(590,490,590,390);
		line(580,490,580,390);
		line(590,390,580,390);
		floodfill(581,391,WHITE);
		line(580,230,650,230);
		line(580,220,650,220);
		line(580,220,580,230);
		line(650,220,650,230);
		floodfill(581,221,WHITE);
		line(580,300,650,300);
		line(580,290,650,290);
		line(580,300,580,290);
		line(650,300,650,290);
		floodfill(581,291,WHITE);
		line(180,230,250,230);
		line(180,220,250,220);
		line(180,220,180,230);
		line(250,220,250,230);
		floodfill(181,221,WHITE);
		line(180,300,250,300);
		line(180,290,250,290);
		line(180,300,180,290);
		line(250,300,250,290);
		floodfill(181,291,WHITE);
		setcolor(RED);
		for(x=100;x<110;x++)
		{
			line(x,100,x,420);
		}
		for(x=710;x<720;x++)
		{
			line(x,100,x,420);
		}
		for(y=80;y<90;y++)
		{
			line(300,y,530,y);
		}
		for(y=430;y<440;y++)
		{
			line(300,y,530,y);
		}
		setcolor(3);
		setfillstyle(11,3);
		rectangle(290,170,545,350);
		rectangle(300,180,535,340);
		floodfill(291,171,3);
		setcolor(10);
		settextstyle(2, 0, 7); 
		outtextxy(50,520,"Game Controls:");
		setcolor(WHITE); 
		outtextxy(50,550,"W --> Up");
		outtextxy(50,580,"S --> Down");
		outtextxy(50,610,"A --> Left");
		outtextxy(50,640,"D --> Right");
		outtextxy(50,670,"Press 'SPACE' to EXIT");
		setcolor(CYAN);
		outtextxy(820,30,"Rules : ");
		setcolor(LIGHTGRAY);
		outtextxy(820,60,"1) Only RED pipes are allowed to touch.");
		outtextxy(820,90,"2) Border line is immune to electric shock.(Because of Earthing)");
		outtextxy(820,120,"3) This is SUDDEN DEATH Mode(One Life per compile/because you only live once).");
		outtextxy(820,150,"4) Just put the ball in the hole(TARGET).");
		outtextxy(820,180,"5) If You Touch the Red Ball then Game is Over.");
		setfillstyle(5,YELLOW);
		circle(760,460,15);
		floodfill(761,461,LIGHTGRAY);
		outtextxy(670,448,"Target->");
		settextstyle(0, 0, 3); 
		outtextxy(295,505,"GOLFAC :GOLF + PACMAN");
		rectangle(290,500,800,535);
		setfillstyle(5,RED);
		floodfill(291,520,LIGHTGRAY);
		setcolor(CYAN);
		settextstyle(5, 0, 3); 
		outtextxy(1050,670,"Created by DarkPhotons");
	
}

int main()
{
	char c,d;
	int px=70,py=70,px2=563,py2=60,count=0,inc=5;
	int px1=270,py1=60;
	int px3=270,py3=370;
	int px4=270,py4=150;
	initwindow(1800,725);
	
	setcolor(CYAN);
	settextstyle(2, 0, 15);
	outtextxy(350,200,"GOLFAC :GOLF + PACMAN");
	setcolor(YELLOW);
	outtextxy(350,300,"E --> Easy");
	outtextxy(350,350,"M --> Medium");
	outtextxy(350,400,"H --> Hard");
	setcolor(WHITE);
	d=getch();
	
	switch(d){
		case 'e':
			{
				
				cleardevice();
				do
				{
					map();
					user(px,py);
				 	
				//	enemy2(px2,py2,d);
					enemy3(px3,py3,d);
					enemy4(px4,py4,d);
					setcolor(BLUE);
					inc=inc+5;
					arc(970,320,540-(inc),160-(inc),70);
					arc(970,320,540-(inc),160-(inc),71);
					arc(970,320,200+(inc),300+(inc),75);
					arc(970,320,200+(inc),300+(inc),76);
					arc(970,320,320-(inc),420+(inc),80);
  					setcolor(14);
  					outtextxy(925,300,"MOVE:");
  					char arr[50];
  					sprintf(arr,"%d",count);
    				setcolor(3);
  					outtextxy(955,325,arr);
  					setcolor(WHITE);
					c=getch();
					switch(c)
					{
						case 'w':
							if(isBlocked(px,py-3))
								py-=3;
							count++;
							break;
						case 's':
							if(isBlocked(px,py+3))
							py+=3;count++;break;
						case 'a':
							if(isBlocked(px-3,py))
							px-=3;count++;break;
						case 'd':
							if(isBlocked(px+3,py))
							px+=3;count++;break;
						case ' ':
							break;
					}
					//cout<<py<<py2<<endl;
					if(px>=(px4-20) && px<=(px4+20) && py>=(py4-20) && py<=(py4+20))
						gameover=true;
					else if(px>=(px3-20) && px<=(px3+20) && py>=(py3-20) && py<=(py3+20))
						gameover=true;
					else if(py>=(py2-20) && py<=(py2+20) && px>=(px2-20) && px<=(px2+20))
						gameover=true;
					else if(py>=(py1-20) && py<=(py1+20) && px>=(px1-20) && px<=(px1+20))
						gameover=true;
			
					cleardevice();
					if(gameover)
					{
					settextstyle(2,0,50);
					outtextxy(530,230,"        GAME OVER");
					outtextxy(500,300,"Improve your skill , NOOB!");
					break;
					}
					if(gamewon)
					{
					settextstyle(2,0,50);
					outtextxy(530,230,"        WINNER !");
					outtextxy(300,300,"Bhai Bhai , PRO nikdya tame (RESPECT++) !");
					break;	
					}
				}while(c!=' ');			
			}
			break;
			
			case 'm':
			{
				cleardevice();
				do
				{
					map();
					user(px,py);
					enemy(px1,py1,d);
					//enemy2(px2,py2,d);
					enemy3(px3,py3,d);
					enemy4(px4,py4,d);
					setcolor(BLUE);
					inc=inc+5;
					arc(970,320,540-(inc),160-(inc),70);
					arc(970,320,540-(inc),160-(inc),71);
					arc(970,320,200+(inc),300+(inc),75);
					arc(970,320,200+(inc),300+(inc),76);
					arc(970,320,320-(inc),420+(inc),80);
  					setcolor(14);
  					outtextxy(930,300,"MOVE:");
  					char arr[50];
  					sprintf(arr,"%d",count);
    				setcolor(3);
  					outtextxy(955,325,arr);
  					setcolor(WHITE);
					c=getch();
					switch(c)
					{
						case 'w':
							if(isBlocked(px,py-5))
							py-=5;count++;break;
						case 's':
							if(isBlocked(px,py+5))
							py+=5;count++;break;
						case 'a':
							if(isBlocked(px-5,py))
							px-=5;count++;break;
						case 'd':
							if(isBlocked(px+5,py))
							px+=5;count++;break;
						case ' ':
							break;
					}
					//cout<<py<<py2<<endl;
					if(px>=(px4-20) && px<=(px4+20) && py>=(py4-20) && py<=(py4+20))
						gameover=true;
					else if(px>=(px3-20) && px<=(px3+20) && py>=(py3-20) && py<=(py3+20))
						gameover=true;
					else if(py>=(py2-20) && py<=(py2+20) && px>=(px2-20) && px<=(px2+20))
						gameover=true;
					else if(py>=(py1-20) && py<=(py1+20) && px>=(px1-20) && px<=(px1+20))
						gameover=true;
						
					cleardevice();
					if(gameover)
					{
					settextstyle(2,0,50);
					outtextxy(530,230,"        GAME OVER");
					outtextxy(500,300,"Improve your skill , NOOB!");
					break;
					}
					if(gamewon)
					{
					settextstyle(2,0,50);
					outtextxy(530,230,"        WINNER !");
					outtextxy(300,300,"Bhai Bhai , PRO nikdya tame (RESPECT++) !");
					break;	
					}
				}while(c!=' ');			
			}
			break;
			
			case 'h':
			{
				cleardevice();
				do
				{
					map();
					user(px,py);
					enemy(px1,py1,d);
					enemy2(px2,py2,d);
					enemy3(px3,py3,d);
					enemy4(px4,py4,d);
					setcolor(BLUE);
					inc=inc+5;
					arc(970,320,540-(inc),160-(inc),70);
					arc(970,320,540-(inc),160-(inc),71);
					arc(970,320,200+(inc),300+(inc),75);
					arc(970,320,200+(inc),300+(inc),76);
					arc(970,320,320-(inc),420+(inc),80);
  					setcolor(14);
  					outtextxy(925,300,"MOVE:");
  					char arr[50];
  					sprintf(arr,"%d",count);
    				setcolor(3);
  					outtextxy(955,325,arr);
  					setcolor(WHITE);
					c=getch();
					switch(c)
					{
						case 'w':
							if(isBlocked(px,py-10))
							py-=10;count++;break;
						case 's':
							if(isBlocked(px,py+10))
							py+=10;count++;break;
						case 'a':
							if(isBlocked(px-10,py))
							px-=10;count++;break;
						case 'd':
							if(isBlocked(px+10,py))
							px+=10;count++;break;
						case ' ':
							break;
					}
					//cout<<py<<py2<<endl;
					if(px>=(px4-20) && px<=(px4+20) && py>=(py4-20) && py<=(py4+20))
						gameover=true;
					else if(px>=(px3-20) && px<=(px3+20) && py>=(py3-20) && py<=(py3+20))
						gameover=true;
					else if(py>=(py2-20) && py<=(py2+20) && px>=(px2-20) && px<=(px2+20))
						gameover=true;
					else if(py>=(py1-20) && py<=(py1+20) && px>=(px1-20) && px<=(px1+20))
						gameover=true;
					cleardevice();
					if(gameover)
					{
					settextstyle(2,0,50);
					outtextxy(530,230,"        GAME OVER");
					outtextxy(500,300,"Improve your skill");
					break;
					}
					if(gamewon)
					{
					settextstyle(2,0,50);
					outtextxy(530,230,"        WINNER !");
					break;	
					}
				}while(c!=' ');			
			}
			break;
	}	
	
	getch();
	getch();	
	return 0;
}
