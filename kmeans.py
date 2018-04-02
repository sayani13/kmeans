import math

l=[]
num=int(input('enter number of transactions'))
for i in range(0,num):
    item=[]
    point=input('enter the point'+str(i)+'in x ,y format in singe quotes')
    try:
        point.index(',')
    except:
        print('incorrect input format')
        break
    item=point.split(",")
    item=list(map(float,item))
    l.append(item)
print l

cluster1=[]
clusters=int(input('enter number of clusters'))
for i in range(0,clusters):
    point=int(input('assumed mean '+str(i)+' is'))
    cluster1.append(point)
    flag=0
    cluster2=[]
    while cluster1!=cluster2:
        if flag==0:
            flag=1
        else:
            cluster1=cluster2

        distance_list=[]
        for i in range(0,clusters):
                lis=[]
                for j in range(0,num):
                    point1=cluster1[i]
                    point2=l[j]
                    distx  = point1[0]-point2[0]
                    disty =point1[1]-point2[1]
                    distance = math.sqrt((distx*distx)+(disty*disty))
                    lis.append(distance)
                distance_list.append(lis)

        cluster_items=[]
        cluster_=[]
        for j in range(0,clusters):
            cluster_.append(cluster_items)
        for i in range(0,num):
            minimum=0
            for j in range(0,clusters):
                if distance_list[j][i]<distance_list[minimum][i]:
                    minimum=j
                cluster_[minimum]+=[i]
                print('the point',str(l[i])+'belongs to cluster',+str(minimum))

        cluster2=[]
        for i in range(0,len(cluster_)):
            centroid=[0,0]
            for j in range(0,len(cluster_[i])):
                val=l1[cluster_[i][j]]
                centroid[0]+=val[0]/len(cluster_[i])
                centroid[1]+=val[1]/len(cluster_[i])
            cluster2.append(centroid)












