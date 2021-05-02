### [5730. 将所有数字用字符替换](https://leetcode-cn.com/problems/replace-all-digits-with-characters/)
> 根据题目意思直接模拟即可  
- [cpp version](./A.cpp)
- [python3 version](./A.py)

### [5731. 座位预约管理系统](https://leetcode-cn.com/problems/seat-reservation-manager/)
> 根据题意只需要返回最小的可预约座位号即可，采用优先队列实现
- [cpp version](./B.cpp)
- [python3 version](./B.py)

### [5732. 减小和重新排列数组后的最大元素](https://leetcode-cn.com/problems/maximum-element-after-decreasing-and-rearranging/)
> 根据题意数组中的数只能减小无法增大，那么要使得maxinum最大，只能在满足相邻两元素绝对值小于等于`1`的条件下尽可能的避免对数进行减小。因此，排序后从小到大遍历，对于相邻元素的绝对值不满足要求的将较大元素改写为较小元素加`1`
- [cpp version](./C.cpp)
- [python3 version](./C.py)

### [5733. 最近的房间](https://leetcode-cn.com/problems/closest-room/)
> 分别对`rooms`和`queries`按房间面积进行降序排序(对`queries`进行排序时记得绑定原来的数组下标)，遍历`queries`中的查询房间面积，对`rooms`中符合要求的房间`id`添加到集合中，然后二分查找出绝对值最小的房间`id`
- [cpp version](./D.cpp)