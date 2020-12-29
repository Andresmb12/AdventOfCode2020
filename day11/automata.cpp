#include<iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

typedef vector<string> matrix;

matrix next_gen(matrix& M);
int adjacents_occupied(matrix& m, int row, int col);
int is_occupied(char seat);
int count_seats(matrix& M);
int look_directions(matrix& M, int row, int col);


int main()
{
	string s;
	ifstream file("input.txt");
	matrix data , gen2, temp;
	int ocup_seats;
	
	while (getline(file,s))
	{
		data.push_back( s + '\n');
	}
	
	file.close();
	/*show initial generation
	for(string d:data)
		cout<<d;
	cout<<endl;*/
	
	int aux = 0;
	do
	{
		temp = data;
		gen2 = next_gen(data);
		data = gen2;
		
		/* cout<<endl<<"New generation:"<<endl;
		for (string d:gen2)
			cout<<d; */
		
	}while(temp != data );
	
	ocup_seats = count_seats(gen2);
	cout<<endl<<"There are "<<ocup_seats<<" occupied seats"<<endl;	
	
	return 0;
		
}

int count_seats(matrix& M)
{
	int sum = 0;
	for (string s:M)
		sum += count(s.begin(),s.end(),'#');
	return sum;	
}

int is_occupied(char seat)
{
	return seat == '#';
}

int cell(matrix& M, int row,int col)
{
	if(row < 0 || row >= M.size() || col < 0 || col >= M[0].size() )
		return 0; //null fronter	
}

int adjacents_occupied(matrix& M, int row, int col)
{	
	return is_occupied( cell( M,row-1,col-1 ) ) + is_occupied( cell( M,row-1,col ) ) + is_occupied( cell( M,row-1,col+1 ) ) +
			is_occupied( cell( M,row,col-1 ) ) + is_occupied( cell( M,row,col+1 ) ) + 
			is_occupied( cell( M,row+1,col-1 ) ) + is_occupied( cell( M,row+1,col ) ) + is_occupied( cell( M,row+1,col+1 ) );
}

int check_direction(matrix& M, int row, int col, int horizontal_offset, int vertical_offset)
{
	int nrows = M.size(); int ncols = M[0].size()-1;
	int i = row; int j = col;
	char nextseat = ' ';
	int sol = 0;
	i += vertical_offset; j += horizontal_offset;
	
	while( i >=0 and j <ncols and i<nrows and j >= 0 and nextseat!='#' and nextseat!='L' )
	{
		nextseat=M[i][j];
		i += vertical_offset;
		j += horizontal_offset;	
	}
	
	return nextseat == '#';	
}

int look_directions(matrix& M, int row, int col)
{
	vector<pair<int,int> > directions= { {-1, -1}, {-1,0} ,{-1,1} , {0,1} , {0,-1} , {+1,-1} , {+1,0}, {1,1} };
	int neighbours = 0;
	for (pair<int,int> p: directions)
		neighbours += check_direction(M,row,col,p.first,p.second);
		
	return neighbours;	
}

char newstate(matrix& M,int row, int col)
{
	int adj=adjacents_occupied(M,row,col); //For Part 1
	int part2adj = look_directions(M,row,col); //For Part 2
	char currentseat = M[row][col];
	char newseat=currentseat;	
	if(currentseat =='L' && part2adj==0 )
		newseat = '#';
	if(currentseat =='#' && part2adj >= 5)
		newseat = 'L';
	
	return newseat;
			
}

matrix next_gen(matrix& M)
{
	matrix newgen(M);
	int nrows = M.size();
	int ncols = M[0].size()-1;
	for(int i = 0; i < nrows; i++)
	{
		for(int j = 0; j < ncols; j++)
		{
			newgen[i][j] = newstate(M,i,j);
		}
	}
		
	return newgen;
}
