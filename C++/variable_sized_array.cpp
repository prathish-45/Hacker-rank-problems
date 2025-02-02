#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, q;
    cin >> n >> q;
    
    // Read the arrays
    vector<vector<int>> arrays(n);
    for (int i = 0; i < n; i++) {
        int k;
        cin >> k;
        arrays[i].resize(k);
        for (int j = 0; j < k; j++) {
            cin >> arrays[i][j];
        }
    }
    
    // Process the queries
    for (int i = 0; i < q; i++) {
        int a, b;
        cin >> a >> b;
        cout << arrays[a][b] << endl;
    }
    
    return 0;
}