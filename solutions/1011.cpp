#include <vector>
#include <iostream>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    bool valid(vector<int>& weights, int days, int boat) {
        int load = 0;
        for (int w : weights) {
            if (load + w > boat) {
                days--;
                if (days <= 0) {
                    return false;
                }
                load = 0;
            }
            load += w;
        }
        return true;
    }

    int shipWithinDays(vector<int>& weights, int days) {
        int ll = *max_element(weights.begin(), weights.end());
        int rr = accumulate(weights.begin(), weights.end(), 0);
        while (ll < rr) {
            int mid = ll + (rr-ll) / 2;
            if (valid(weights, days, mid)) {
                rr = mid;
            } else {
                ll = mid+1;
            }
        }
        return ll;
    }
};

int main(int argc, char *argv[]) {
    auto s = new Solution();
    vector<int> weights{1,2,3,4,5,6,7,8,9,10};
    int days = 5;
    cout << s->shipWithinDays(weights, days) << endl;
    return 0;
}