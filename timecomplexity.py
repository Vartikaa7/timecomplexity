import time,random
def bubble(a,n):
    for i in range(n):
        for j in range(n-i-1):
            if a[j]<a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
def selection(a,n):
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if a[j]>a[min_idx]:
                min_idx=j
        a[i],a[min_idx]=a[min_idx],a[i]
def insertion(a,n):
    for i in range(1,n):
        key=a[i]
        j=i-1
        while j>=0 and key>a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
def partition(a,l,h):
    pivot=a[h]
    i=l-1
    for j in range(l,h):
        if a[j]<=pivot:
            i+=1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[h]=a[h],a[i+1]
    return (i+1) 
def quick(a,l,h):
    if l<h:
        pi=partition(a,l,h)
        quick(a,l,pi-1)
        quick(a,pi+1,h)
def merge(arr):
    if len(arr)>1:
        mid=len(arr)//2
        sa1=arr[ :mid]
        sa2=arr[mid: ]
        merge(sa1)
        merge(sa2)
        i=j=k=0
        while i<len(sa1) and j<len(sa2):
            if sa1[i]<sa2[j]:
                arr[k]=sa1[i]
                i+=1
            else:
                arr[k]=sa2[j]
                j+=1
            k+=1
        while i<len(sa1):
            arr[k]=sa1[i]
            i+=1
            k+=1
        while j<len(sa2):
            arr[k]=sa2[j]
            k+=1
            j+=1
def timecomp(n,d,j):
    a=[0]*n
    for i in range(n):
        b=random.randint(1,n)
        a[i]=b
    a1=a.copy()
    start=time.time()
    bubble(a1,n)
    end=time.time()
    e=end-start
    d["bubble"][j]=e
    a2=a.copy()
    start=time.time()
    selection(a2,n)
    end=time.time()
    e=end-start
    d["selection"][j]=e
    a3=a.copy()
    start=time.time()
    insertion(a3,n)
    end=time.time()
    e=end-start
    d["insertion"][j]=e
    a4=a.copy()
    start=time.time()
    quick(a4,0,n-1)
    end=time.time()
    e=end-start
    d["quick"][j]=e
    a5=a.copy()
    start=time.time()
    merge(a5)
    end=time.time()
    e=end-start
    d["merge"][j]=e
d={"bubble":[0,0,0,0,0],"selection":[0,0,0,0,0],"insertion":[0,0,0,0,0],"quick":[0,0,0,0,0],"merge":[0,0,0,0,0]}
for j in range(5):
    n=int(input())
    timecomp(n,d,j)
    print(d)
