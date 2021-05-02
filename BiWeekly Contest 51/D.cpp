class Solution {
public:
    struct node {
        int id, pre, index;
    };

    static bool cmp(vector<int>& u, vector<int>& v){
        return u[1] > v[1];
    }

    static bool cmp1(node u, node v){
        return u.pre > v.pre;
    }

    vector<int> closestRoom(vector<vector<int>>& rooms, vector<vector<int>>& queries) {
        int n = rooms.size(), m = queries.size();
        vector<node> nums;
        sort(rooms.begin(), rooms.end(), cmp);
        for(int i = 0; i < m; i++){
            int id = queries[i][0], pre = queries[i][1];
            nums.push_back((node){id, pre, i});
        }
        sort(nums.begin(), nums.end(), cmp1);
        set<int> coll;
        vector<int> res(m);
        int l = 0;
        for(int i = 0; i < m; i++){
            int pre = nums[i].pre, id = nums[i].id, index = nums[i].index;
            while(l < n && rooms[l][1] >= pre){
                coll.insert(rooms[l][0]);
                l++;
            }
            if(coll.empty()){
                res[index] = -1;
            }else{
                // lower_bound 返回首个大于等于查找元素的迭代器
                auto it = coll.lower_bound(id);
                if(it == coll.end()){
                    res[index] = *(--it);
                }else if(it == coll.begin()){
                    res[index] = *it;
                }else{
                    int x = *it, y = *(--it);
                    if(abs(x - id) < abs(y - id)) res[index] = x;
                    else res[index] = y;
                }
            }
        }
        return res;
    }
};