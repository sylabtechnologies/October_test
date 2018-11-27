// overload stream ops for linear vector

#pragma once

#include <iostream>
#include <vector>
#include <iterator>
#include <limits>

template<typename T> std::ostream& operator<< (std::ostream& os, std::vector<T>& myvec)
{
	if (!myvec.empty())
	{
		os << "[ ";
		copy(myvec.begin(), myvec.end(), std::ostream_iterator<T>{os, ", "});
		os << "\b\b ]";	// cute
	}

	return os;
}

template<typename T> std::istream& operator>> (std::istream& iis, std::vector<T>& myvec)
{
	long long vecSize; size_t sztSize;

	iis >> vecSize;
	if (vecSize < 0 || vecSize > std::numeric_limits<std::size_t>::max())
		throw std::out_of_range("Vector I/O out of range");

	sztSize = static_cast<size_t>(vecSize);
	if (sztSize > myvec.max_size())
		throw std::out_of_range("Vector I/O max_size exceeded");

	myvec.clear(); myvec.resize(sztSize);
	for (size_t i = 0; i < sztSize; i++)
	{
		T temp;
		iis >> temp; if (!iis.good()) throw std::out_of_range("Vector I/O failure");
		myvec[i] = temp;
	}

	return iis;
}

