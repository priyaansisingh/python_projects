#to identify a meraki number
#inputs are positive integers only

m=n=0

def meraki_helper(part):
    global m, n
    item=str(part)
    if(len(item)==1):  
        print('Yes, {} is a Meraki number.'. format(item))
        m=m+1
    for i in range(0, len(item)-1, 1):
        if(abs(int(item[i]) - int(item[i+1]))==1):
            if(i==len(item)-2):
                print('Yes, {} is a Meraki number.'. format(item))
                m=m+1
            continue
        else:
            print('No, {} is not a Meraki number.'. format(item))
            n=n+1
            break
            
#num=list(map(int, input().split()))
num=[12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321]
for item in num:
    meraki_helper(item)
print('There are {} Meraki numbers and {} Non-Meraki numbers in the input list.'.format(m, n))
