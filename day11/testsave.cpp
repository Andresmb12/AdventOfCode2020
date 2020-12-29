#include<iostream>
#include <fstream>
#include <vector>
using namespace std;

typedef vector<string> matrix;

int main()
{
	string s;
	ifstream file("test1.txt");
	matrix data;
	
	while (getline(file,s))
	{
		data.push_back( s + '\n');
	}
	
	for(string d:data)
	{
		cout<<d;
	}
	
	
	
	file.close();	
}
