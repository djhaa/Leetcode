### [5746. 到目标元素的最小距离](https://leetcode-cn.com/problems/minimum-distance-to-the-target-element/)
> 从`start`位置开始分别向左右两边遍历，直到找到第一个等于`target`元素的值  
> **注意：可能存在一边不存在`target`元素的情况，需注意判断**
- [cpp version](./A.cpp)
- [python3 version](./A.py)

### [5747. 将字符串拆分为递减的连续值](https://leetcode-cn.com/problems/splitting-a-string-into-descending-consecutive-values/)
> 回溯问题，分别枚举第一个字符值的长度，然后判断后续是否存在子字符串对应的数值小于前一个并且与其相差1即可
- [python3 version](./B.py)

### [5749. 邻位交换的最小次数](https://leetcode-cn.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/)
> 本题是[Leetcode 31. 下一个排列](https://leetcode-cn.com/problems/next-permutation/)的进阶版本，可以通过执行`K`次下一个排列函数求得当前序列`K`次后的序列，然后模拟计算交换次数即可
- [python3 version](./C.py)

### [5748. 包含每个查询的最小区间](https://leetcode-cn.com/problems/minimum-interval-to-include-each-query/)
> 此题类似于`BiWeekly Contest 51`第四题，先将数组`intervals`和`queries`按从小到大排序(`queries`记得绑定原始下标)，遍历`queries`，将前端点符合要求的数组添加到有序集合中，再遍历有序集合，对于有序集合中后端点不符合要求的数据从有序集合中剔除，若集合不为空，则集合开头数据即使答案。
- [cpp version](./D.cpp)