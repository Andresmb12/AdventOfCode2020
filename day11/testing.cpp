#include<iostream>

using namespace std;

int main()
{
	int coche[5];
	int len=sizeof(coche)/sizeof(coche[0]);
	cout<<len<<endl;
	for(int i=0; i<len; i++)
	{
		coche[i]=i;
	}
	
	for(auto c: coche) cout<<c;
	
	cout<<endl<<"todo bien";
	return 0;
}
