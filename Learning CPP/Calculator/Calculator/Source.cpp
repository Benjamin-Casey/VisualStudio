#include <iostream>


int chooseOperator()
{
	std::cout << "1. Addition. 2. Subtraction. 3. Multiplication. 4. Division.";
	std::cout << "Choose an operator:" << std::endl;
	int x;
	std::cin >> x;
	return x;
}

int numInput()
{
	int x;
	std::cout << "Enter value: ";
	std::cin >> x;
	return x;
}

int calculateValue(int x, int op, int y)
{
	if (op == 1)	//Addition
		return x + y;
	if (op == 2)	//Subtraction
		return y - x;
	if (op == 3)	//Multiplaication
		return x * y;
	if (op == 4)	//Division
		return y / x;
}

int main()
{
	std::cout << "Your number is: " << calculateValue(numInput(), chooseOperator(), numInput());
	int x;
	std::cin >> x;
	return 0;
}