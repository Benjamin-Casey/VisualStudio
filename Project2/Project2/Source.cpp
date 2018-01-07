#include <iostream>
int x;
int y;
int p;
int add(int x, int y)
{
	std::cout << "add";
std::cout << p ;
	return p=x+y;
	

}

int multiply(int x, int y)
{
	return x * y;


}

int sub(int x, int y)
{
	return x - y;


}

int divide(int x, int y)
{
	return x / y;


}

int power(int x, int y)
{
	
	int result = 1;
	for (int i = 0; i < y; ++i)
	{
		result *= x;
	}

	std::cout << result;
	return 0;
}

int main()
{
	int a;
	std::cout << "pick an operator";
	std::cin >>  a ;
	std::cout << "Two number pls";
	std::cin >> x;  
	std::cin >> y;
	switch (a)
	{
	case 1:
			 add(x,y);
			break;
	case 2:
				sub(x, y);
				break;
	case 3:
					multiply(x, y);
					break;
	case 4:
						divide(x, y);
						break;
	case 5:
							power(x, y);
							break;

	}
		

	int o;
		std::cin >> o;

	return 0;
}