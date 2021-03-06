#include "stdafx.h"
#include <iostream>
#include "Rational.h"
using namespace std;

int main()
{
	Rational r1, r2, r3;

	cout << "Test two fractions: ";
	cin >> r1 >> r2;
	cout << endl;

	// test +, -, *, /
	r3 = r1 + r2;
	cout << r1 << "+" << r2 << " = " << r3 << endl;

	r3 = r1 - r2;
	cout << r1 << "-" << r2 << " = " << r3 << endl;

	r3 = r1 * r2;
	cout << r1 << "*" << r2 << " = " << r3 << endl;

	r3 = r1 / r2;
	cout << r1 << "/" << r2 << " = " << r3 << endl;

	bool compareOK = r1 == r2;
	cout << r1 << "==" << r2 << " = " << ((compareOK) ? "true" : "false");
	cout << endl;

    return 0;
}

