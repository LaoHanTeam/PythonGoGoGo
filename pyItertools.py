import itertools

#排列， 从一个集合中选取N个数依次排列下来 集合【1、2、3、4、5】的p(5,2)的组合为
print list(itertools.permutations([1,2,3,4,5],2))

print "==========================================="

#组合，从一个集合中选取N个数，无序组合
print list(itertools.combinations([1,2,3,4,5],2))
