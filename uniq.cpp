// uniq.cpp : implement uniq

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>

using namespace std;

void message(const char* msg) { cout << msg << endl; }
void exit_msg(const char* msg) { message(msg); exit(EXIT_FAILURE); }

int main(int argc, char *argv[])
{
	if (argc != 2) exit_msg("Usage: uniq filename.ext");

	ifstream testfile(argv[1]);
	if (!testfile) exit_msg("Cannot open input file");

	string nextLine, prevLine;
	bool firstTime = true;

	while (getline(testfile, nextLine))
	{
		if (firstTime)
		{
			prevLine = nextLine;
			cout << nextLine << endl;

			firstTime = false;
			continue;
		}

		if (nextLine != prevLine)
		{
			cout << nextLine << endl;
			prevLine = nextLine;
		}
	}

    return 0;
}

