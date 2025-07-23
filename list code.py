l=[1,2,3,4,5,6,7,8,]
# taking empty list
k=[]
#iteratig list
for i in l:
#giving condition to devide the the list
    if i%2 == 0:
        # After the division we can square the output
        k.append(i*i)
print(k)
