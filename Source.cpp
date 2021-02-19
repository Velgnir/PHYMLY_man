#include <iostream>
using namespace std;
int main() 
{
	int x, y, z;
	float v;
	cin >> x >> y >> z;
	v = sqrt(x * x + y * y + z * z);
	cout << "Result: " << v;
	return v;
}