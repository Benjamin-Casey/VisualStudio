#include <iostream>

int doubleNumber(int x)
{
	return 2 * x;
}

int main()
{
	std::cout << "Enter a number";
	int x;
	std::cin >> x;
	std::cout << doubleNumber(x);

	int y;
	std::cin >> y;

	return 0;
}