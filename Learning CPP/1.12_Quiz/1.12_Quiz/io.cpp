#include <iostream>

int readNumber()
{
	int x;
	std::cout << "Enter a number: ";
	std::cin >> x;
	return x;
}

void writeAnswer(int num)	//This function prints number entered in readNumber()
{
	std::cout << "Your number is: " << num;
}