import numpy as np
# 50
dt = np.dtype([("position", "i", (2,)), ("rgb", "i", (3,))])

data = np.array([
    ([1,1],[66, 135, 245]),
    ([6,2],[141, 66, 245]),
    ([100,3],[66, 245, 99])
],dtype=dt)

#51 
#computing with euclidean distance which is sqrt(abs(x2-x1)**2+abs(y2-y1)**2)
vec=np.random.rand(100,2)
differences = vec[1:] -vec[:-1]
res=np.sqrt(np.sum(differences**2,axis=1))
print(res)

# 53
float_array=np.array([1.0, 2.5, 3.75, -4.25], dtype=np.float32)
int_array=float_array.astype(np.int32)
print(int_array)

with open("file.txt","r") as file:
    data = file.read().replace("\n",'').replace(" ","").split(",")
print(data)

#equvivalent of the enumarate for nump is np.ndenumerate
arr=np.array([[10,20,30],[40,50,60]])
for index in np.ndenumerate(arr):
    print(index)

rand_arr=np.random.rand(5,5)
print(rand_arr)

another_arr=np.sort(rand_arr[:,len(rand_arr[0])-1],axis=0)
another_arr

nulls=np.isnan(rand_arr)
# nulls


a=int(input())
sample_arr=np.array([2,3,8,9,10,6])
diff=min(abs(sample_arr-a))
if diff+a in sample_arr:
    print(diff+a)
elif diff-a in sample_arr:
    print(diff-a)
elif a-diff in sample_arr:
    print(a-diff)

rand_1 = np.random.rand(3,1)
rand_2 = np.random.rand(1,3)
print(rand_1+rand_2)

class array:
    def __init__(self,name):
        self.name=name
# arr=array("Integers")

# Consider a given vector, how to add 1 to each element indexed by a second vector (be careful with repeated indices)?
vec=np.array([1,2,3,4,5])
vec+1

f=np.array([9,3,10,90,50,70,80])
i=np.array([6,3,2,4,5,0,1])
x=f[i]
print(x)

arr=np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])
print(np.sum(arr,axis=0)[2:])

d=np.array([1,2,3,4,5,6,7,8,9,10,11,12,14,13,15,16])
s=np.array([
    (0,8),
    (5,9),
    (1,6),
    (0,6)
])
for i in s:
    print(np.mean(d[i[0]:i[1]+1]))


vec=np.array([1,2,3,4,5])
n=int(list(vec.shape)[0])-1
a=np.zeros(3)
step=1
while n!=0:
    vec=np.insert(vec,step,a)
    step+=4
    n-=1
vec


arr1=np.random.rand(5,5,3)
arr2=np.random.rand(5,5)
arr1*arr2


num_arr = np.array([[1,3,1], [3,1,3], [2,9,2], [9,2,9]])
 
num_arr = np.roll(num_arr,2,axis=0)
print(num_arr)


triangles=np.array([15,18,19,2,56,7,8,9,5,6,6,1,2,3,56])
print(np.unique(triangles))


c=np.bincount(np.array([5,9,8,6,3]))
indices = np.argwhere(c==1)
ind = indices.reshape(len(indices))
print(ind)

z=np.array([1,2,3,4,5,6,7,8,910,10,52,25])
matrix = np.zeros([len(z)//3 + (0 if len(z)%3==0 else 1),3])
for i in np.ndenumerate(z):
    ind=list(list(i)[0])[0]
    val=int(list(i)[1])
    matrix[ind//3][ind%3]=val
# matrix

p = np.array([
    [3,9],
    [1,10]
])
for i in p:
    print(abs(i[1]-i[0]))

Z = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
start = 0
while start<=len(Z)-4:
    print(list((Z[start],Z[start+1],Z[start+2],Z[start+3])))
    start+=1


a=[1,2,3,4,5,6,1,2,1]
map={}
mx_freq=0
ans=None
for i in a:
    ls=map.get(i,0)+1
    if mx_freq<ls:
        ans=(i,ls)
        mx_freq=ls
        map[i]=ls
print(f"the most frequent value in the array is {list(ans)[0]} repeated {list(ans)[1]} times in the array")


rand_arr=np.random.rand(10,10)
arrays = []
ans=None
for i in range(7):
    for j in range(7):
        if rand_arr[i:i+3,i:i+3] in arrays:
            ans=rand_arr[i:i+3,i:i+3]
        np.append(arrays,rand_arr[i:i+3,i:i+3])
print(ans)
n=int(input())
arr=[89,23,15,69,43,57,952,548,3]
print(sorted(arr)[-n:])

x=[1,2,3,4,5]
cartesian=["x","y","z"]
for i in x:
    for j in cartesian:
        print(i,j)
a=[1,2,3,4,5]
b=a.copy()

z=[1,2,3,4,5,6]
for i in range(len(z)):
    z[i]=z[i]**3    

nums = [25,98,1,2,10,30,3,8]
binary_representation = []
for i in nums:
    binary_representation.append(int(str(bin(i))[2:]))
# binary_representation

a=np.array([
    [1,2,3],
    [5,9,10],
    [1,2,3]
])
print(np.unique(a))
