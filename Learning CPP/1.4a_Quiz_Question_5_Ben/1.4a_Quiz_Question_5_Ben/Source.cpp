#include <iostream>

int doubleNumber(int x)
{
	return 2 * x;
}

int main()
{
	std::cout << "Enter an integer: ";
	int x;
	std::cin >> x;
	std::cout << "This is double your number: ";
	std::cout << doubleNumber(x);
	int y;
	std::cin >> y;
	return 0;
}