// - make ostream& operator<<!

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <cstdlib>

using namespace std; 

// template it
template<typename T>
ostream& operator<< (ostream& os, vector<T>& myvec)
{
	if (!myvec.empty())
	{
		os << "[ ";
		copy(myvec.begin(), myvec.end(), ostream_iterator<T>{os, ", "});
		os << "\b\b ]";	// cute
	}

	return os;
}

int main()
{
	vector<int> numbers{ 5, 9, -1, 200, 0 };
	cout << numbers << endl;

	// sort in reverse
	sort(numbers.rbegin(), numbers.rend());
	cout << numbers << endl;

	vector<string> test{"Nelson", "Scott", "Manchin", "Morrisey", "Sinema", "McSally"};
	cout << test << endl;
	sort(test.begin(), test.end());
	cout << test << endl;

	return EXIT_SUCCESS;
}

