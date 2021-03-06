// Rational.cpp : Implement rational number class

#include "stdafx.h"
#include "Rational.h"
using std::string;

int Rational::GCD(int a, int b)
{
	a = abs(a);
	b = abs(b);

	while (b != 0) {
		int temp = b;
		b = a % b;
		a = temp;
	}
	return a;
}

// implement arithmetic
Rational operator+(const Rational &lhs, const Rational& rhs)
{
	int opNum = lhs.numerator()*rhs.denominator() + lhs.denominator()*rhs.numerator();
	int opDenom = lhs.denominator()*rhs.denominator();
	return Rational(opNum, opDenom);
}

Rational operator-(const Rational &lhs, const Rational& rhs)
{
	int opNum = lhs.numerator()*rhs.denominator() - lhs.denominator()*rhs.numerator();
	int opDenom = lhs.denominator()*rhs.denominator();
	return Rational(opNum, opDenom);
}

Rational operator*(const Rational &lhs, const Rational& rhs)
{
	int opNum = lhs.numerator()*rhs.numerator();
	int opDenom = lhs.denominator()*rhs.denominator();
	return Rational(opNum, opDenom);
}

Rational operator/(const Rational &lhs, const Rational& rhs)
{
	int opNum = lhs.numerator()*rhs.denominator();
	int opDenom = lhs.denominator()*rhs.numerator();
	return Rational(opNum, opDenom);
}

// implement utilities
bool operator==(const Rational& op1, const Rational& op2)
{
	return op1.numerator()*op2.denominator() == op1.denominator()*op2.numerator();
}

bool operator!=(const Rational& op1, const Rational& op2)
{
	return !(op1 == op2);
}

bool operator>(const Rational& op1, const Rational& op2)
{
	return op1.numerator()*op2.denominator() > op1.denominator()*op2.numerator();
}

bool operator<(const Rational& op1, const Rational& op2)
{
	return op1.numerator()*op2.denominator() < op1.denominator()*op2.numerator();
}

void findNumDenom(const string& buffer, string& strNum, string& strDenom)
{
	size_t start, middle, finish;

	start = buffer.find('(');
	if (start == std::string::npos) throw std::out_of_range("use (n/m) fraction format!");

	middle = buffer.find('/', start + 1);
	if (middle == std::string::npos) throw std::out_of_range("use (n/m) fraction format!");;

	finish = buffer.find(')', middle + 1);
	if (finish == std::string::npos) throw std::out_of_range("use (n/m) fraction format!");

	strNum   = buffer.substr(start + 1, middle - start - 1);
	strDenom = buffer.substr(middle + 1, finish - middle - 1);
}

std::istream& operator>>(std::istream& iis, Rational& rhs)
{
	std::string buffer, strNum, strDenom;
	iis >> buffer;
	
	try
	{
		findNumDenom(buffer, strNum, strDenom);
		rhs = Rational(std::stoi(strNum), std::stoi(strDenom));
	}
	catch (const std::exception& e)
	{
		if (buffer.length() > 0)
		{
			std::cerr << "> " << buffer;
			std::cerr << " < Rational I/O Error: " << e.what() << std::endl;
			exit(EXIT_FAILURE);
		}

		rhs = Rational();
	}

	return iis;
}

std::ostream& operator<<(std::ostream& os, const Rational& rhs)
{
	if (rhs.denominator() == 1)
		return os << rhs.numerator();
	else
		return os << rhs.toString();
}
