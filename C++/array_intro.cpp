#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    int list[n];
    for(int i = 0; i < n; i++) {
        cin >> list[i];
    }
    
    // Reverse the array
    reverse(list, list + n);
    
    // Print the reversed array
    for(int i = 0; i < n; i++) {
        cout << list[i] << " ";
    }
    cout << endl;
    
    return 0;
}