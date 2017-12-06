import sys
val = input().split()
val = list(map(int,val))
n_e = val[0]
m_m = val[1]
m_a = val[2]
count = 0
m_o = []
e_w = []
for i in range(n_e) :
    val = input().split()
    val = list(map(int,val))
    m_o.append(val[0])
    e_w.append(val[1])
    
mn = n_e*m_a - sum(m_o)
if(mn<0) :
    print(count)
    sys.exit()
i = mn
while(i!=0) :
    val = min(e_w)
    inx = e_w.index(min(e_w))
    if(m_o[inx]<m_m) :
        if((m_m-m_o[inx])>i) :
            count = count + val*i
            i = i-i
        else :
            count = count + val*(m_m-m_o[inx])
            i = i-(m_m-m_o[inx])
    e_w[inx] = m_m+1

print(count)
