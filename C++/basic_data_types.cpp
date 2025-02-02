#include <iostream>
#include <cstdio>
#include<iomanip>
using namespace std;

int main() {
    // Complete the code.
    int n;
    long l;
    char c;
    float f;
    double d;
    cin >> n >> l >> c >> f >> d;
    cout << n << endl;
    cout << l << endl;
    cout << c << endl;
    // Use fixed and setprecision to ensure correct formatting for float and double
    cout << fixed << setprecision(3) << f << endl;
    cout << fixed << setprecision(9) << d << endl;
    return 0;
}