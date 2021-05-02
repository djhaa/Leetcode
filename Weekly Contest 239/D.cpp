class Solution {
public:
    using PII = pair<int, int>;
    struct node {
        int id, val;
    };
    
    static bool cmp(vector<int>& u, vector<int>& v){
        if(u[0] == v[0]) return u[1] < v[1];
        return u[0] < v[0];
    }
    
    static bool cmp1(node u, node v){
        return u.val < v.val;
    }
    
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        int n = intervals.size(), m = queries.size();
        vector<node> nums;  
        for(int i = 0 ; i < m; i++){
            int x = queries[i];
            nums.push_back((node){i, x});
        }
        // 从小到大排序
        sort(intervals.begin(), intervals.end(), cmp);
        sort(nums.begin(), nums.end(), cmp1);
        vector<int> res(m);
        set<PII> coll;
        int l = 0;
        for(int i = 0; i < m; i++){
            int id = nums[i].id, val = nums[i].val;
            while(l < n && intervals[l][0] <= val){
                // 区间长度、区间尾端点
                coll.insert({intervals[l][1] - intervals[l][0] + 1, intervals[l][1]});
                l++;
            }
            while(!coll.empty() && coll.begin() -> second < val){
                coll.erase(coll.begin());
            }
            if(coll.empty()){
                res[id] = -1;
            }else{
                res[id] = coll.begin() -> first;
            }
        }
        return res;
    }
};