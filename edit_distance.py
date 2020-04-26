
# coding: utf-8

# In[22]:


import numpy as np
def edit_distance(a,b):
    m=len(a)
    n=len(b)
    D=dict()
    
    
    for i in range(m+1):
        D[i,0]=i
    for j in range(n+1):
        D[0,j]=j
            
    for j in np.arange(1,n+1,1):
        for i in np.arange(1,m+1,1):
            insertion=D[i,j-1]+1
            deletion=D[i-1,j]+1
            match=D[i-1,j-1]
            mismatch=D[i-1,j-1]+1
            #print(insertion, deletion,match,mismatch)
            if a[i-1]==b[j-1]:
                #print(i,j)
                D[i,j]= min(insertion, deletion, match)
            else:
                #print(i,j)
                D[i,j]= min(insertion, deletion, mismatch)
                #print(D[i,j])
    return D[m,n]
if __name__ == "__main__":
    print(int(edit_distance(input(), input())))
        
    
    


# In[10]:





# In[13]:





# In[ ]:




