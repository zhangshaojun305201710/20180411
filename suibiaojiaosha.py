#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print(i,j,k,'就这么简单')

# 这里是注释不影响代码以#开头，python缩进严格必须缩进 不能以为空的没用， if 是选择 这里表示 如果 i 不等于 k 而且 i != j 而且 j != k 就用print打印
# 例如当i=1往下j=1往下k=1 因为题目三个数里面不能有两个一样的，所以不合条件跳过。i=1 j=1 k=2 print(1,1,2)
# print(1,1,3)  .... k 不能大于5 当k=5 不合条件 跳出去 i=1 j=2 k=1 .....   i=4 j =4 k=4 结束  这个editplus 是代替记事本的好太多。