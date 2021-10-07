#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	int main;
	
	Menu :
	cout << "==================================================================================" << endl;
	cout << "				Menu Calculator								   " << endl;
	cout << "==================================================================================" << endl;
	cout << "1. Standard Manipulation (+-*/)" << endl;
	cout << "2. Exponential Calculation" << endl;
	cout << "3. Logarithmic Calculation" << endl;
	cout << "4. Exit" << endl;
	cout << "==================================================================================" << endl;
	cout << "Enter your choice (1-4): ";
	cin >> main;
	
	switch (main)
	
	{
		case 1 :
			{
				double left, right;
				double result;
				char oper;
				cout << "Please enter: a (+-*/) b, and hit return" << endl;
				while (cin >> left >> oper >> right) 
				{ 
				switch (oper) 
				{ 
				case '+' : result = left + right; 
				break; 
				case '-' : result = left - right; 
				break; 
				case '*' : result = left * right; 
				break; 
				case '/' : result = left / right; 
				break; 
				default  : cout << "Bad operator" << oper << "’"; 
				break;
				} 
			cout << "="<< result << endl; system ("PAUSE"); goto Menu;
			} 
			}
		case 2 :
			{
				double left, right;
				
				cout << "Exponential Calculation (a^b)" << endl;
				cout << "Enter the number (a)" << endl;
				cin >> left;
				cout << "Enter the rank notation (b)" << endl;
				cin >> right; 
				cout <<  " Result = " << pow (left, (right)) << endl ; system ("PAUSE");
			    goto Menu;
			}
		case 3 :
				double x;
				char main;
			{
			
				
				cout << " a. Normal Logarithm" << endl; 
				cout << " b. Base 10 log logarithm" << endl;
				cout << " choose a or b = ";
				cin >> main;
				switch (main)
				{
					case 'a' :
						{
							cout << " find value log x, if x is know = ";
							cin >> x;
							cout << " Log" << x << " = " << log (x) << endl; system ("PAUSE");
							goto Menu;
						}
				}
			}
			
			{
				case 'b' :
					{
						cout << " find value x, if x is known = ";
						cin >> x;
						cout <<  " Log " << x << " = " << log10(x) << endl; system ("PAUSE");
						goto Menu;
					}
					
			}
		
		
		case 4 :
			{
				cout << "\nThank You for Your Business, have a nice day"; 
				goto end; 
				break;
			}
		default :
			{
				cout << "Wrong Syntax\a" << endl;
			}
		back : cout << " Again? (y/n)" << endl;
		char jawab;
		cin >> jawab;
		switch (jawab)
		{
			case 'y' :
				{
				goto Menu; 
				break;
				}
			case 'n' :
				{
					cout << "Thank you for your business, have a nice day"; 
					goto end; 
					break;
				}
				default:
					{
						cout << "Wrong Syntax\a\n";
					}
			
		}
		}
		
			end : return 0;
			
}
