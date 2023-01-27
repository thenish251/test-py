def commonSub(str1,str2): 
    res=0:
    for i in range(len(str1)):
        for j in range(len(str2)):
            k=0;
                while((i+k)<len(str1) and (j+k)<len(str2)
                and str1[i+k]==str[j+k]):
               k=k+1;
                res = max(res,k);
                return res; 
        