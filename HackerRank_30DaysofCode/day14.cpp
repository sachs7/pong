#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Difference {
    private:
    vector<int> elements;
  
  	public:
  	int maximumDifference;
  	
  		// Add your code here
    Difference(vector<int> e) {
        elements = e;
    }

    void computeDifference() {
        auto min_value = min_element(elements.begin(), elements.end());
        auto max_value = max_element(elements.begin(), elements.end());

        maximumDifference = (*max_value) - (*min_value);
    }
    
    }; // End of Difference class

int main() {
    int N;
    cin >> N;
    
    vector<int> a;
    
    for (int i = 0; i < N; i++) {
        int e;
        cin >> e;
        
        a.push_back(e);
    }
    
    Difference d(a);
    
    d.computeDifference();
    
    cout << d.maximumDifference;
    
    return 0;
}
