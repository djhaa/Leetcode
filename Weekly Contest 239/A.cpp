class Solution {
public:
    int getMinDistance(vector<int>& nums, int target, int start) {
        int res = INT_MAX;
        int l = start, r = start;
        while(l > 0 && nums[l] != target) l--;
        while(r < nums.size()-1 && nums[r] != target) r++;
        if(nums[l] == target) res = min(res, start - l);
        if(nums[r] == target) res = min(res, r - start);
        return res;
    }
};