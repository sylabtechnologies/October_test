// Nov-26-Y18: implement rational numbers
// 1. make mostly inline functions
// 2. set getters as numerator(), denominator(), toString(), toInt(), toDouble()
// 3. implement arithmetic etc as non-member functions for conversions
// 4. use Euclid algorithm for GCD (improve w/ binary GCD?)
// therefore keep denominator minimal & positive
// 5. use synthesized copy constructor, destructor, assigment operator

#pragma once
#include <iostream>
#include <string>
#include <math.h>
using std::string;

class Rational
{
private:
	int _num;
	int _denom;

public:
	Rational(int n, int d = 1) : _num(n), _denom(d) { if _denom != 1 normalize(); }
	Rational() : _num(0), _denom(1) {}
	const int numerator() const { return _num; }
	const int denominator() const { return _denom; }

	// implement conversions
	const string toString() const { return "(" + std::to_string(_num) + "/" + std::to_string(_denom) + ")"; }
	const int toInt() const {	return _num/_denom; }
	const double toDouble() const { return double(_num)/_denom; }

	const Rational operator-() const		// implement unary minus
	{
		return Rational(-_num, _denom);
	}

private:
	int GCD(int, int b);
	void normalize()
	{
		if (_denom == 0) throw std::out_of_range("null denominator!");
		if (_denom < 0) { _denom = -_denom; _num = -_num; }
		int n = GCD(_num, _denom);
		if (n > 1) { _num /= n; _denom /= n; }
	}
};

Rational operator+(const Rational&, const Rational&);
Rational operator-(const Rational&, const Rational&);
Rational operator*(const Rational&, const Rational&);
Rational operator/(const Rational&, const Rational&);
bool operator==(const Rational&, const Rational&);
bool operator!=(const Rational&, const Rational&);
bool operator>(const Rational&, const Rational&);
bool operator<(const Rational&, const Rational&);
std::istream& operator>>(std::istream&, Rational&);
std::ostream& operator<<(std::ostream&, const Rational&);
