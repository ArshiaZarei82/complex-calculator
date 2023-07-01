def add(ex,index):
    return (float(ex[index-1]) + float(ex[index+1]))

def sub(ex,index):
    return (float(ex[index-1]) - float(ex[index+1]))

def div(ex,index):
    return (float(ex[index-1]) / float(ex[index+1]))

def mult(ex,index):
    return (float(ex[index-1]) * float(ex[index+1]))

listofnumbers = []
for x in range(0,1000):
    listofnumbers.append(str(x))
listofnumbers.append("00")
listofnumbers.append("000")
listofnumbers.append("0000")

#print(listofnumbers)
def Eval(exper):
    exper = list(exper)


    while True:
        expercopy = exper
        flag = False

        index = 0
        for x in range(len(expercopy)-1):
            if expercopy[x] in listofnumbers and expercopy[x+1] in listofnumbers:
                index = x
                flag = True
            
        if flag == True:
            exper[index:index+2] = [exper[index] + exper[index+1]]
        else:
            break

    if exper[0] =="-":
        exper[0:2] = [exper[0] + exper[1]]

    
    while "*" in exper:
        operindex = exper.index("*")

        result = mult(exper,operindex)
        exper[operindex-1:operindex+2] = [result]
            
    while "/" in exper:
        operindex = exper.index("/")

        result = div(exper,operindex)
        exper[operindex-1:operindex+2] = [result]
            
    while "-" in exper:
        operindex = exper.index("-")

        result = sub(exper,operindex)
        exper[operindex-1:operindex+2] = [result]
            
    while "+" in exper:
        operindex = exper.index("+")

        result = add(exper,operindex)
        exper[operindex-1:operindex+2] = [result]
    return str(exper[0])  

def braket(exper):
    if "(" not in exper:
        return Eval(exper)
    
    else :

        strexper = ""
        for x in exper:
            strexper += x

        begin = end = None

        if "(" in exper:
            begin = strexper.index("(")

            end = strexper.rindex(")")
        exper = list(exper)
        exper[begin:end+1] = [braket(exper[begin+1 : end])]
    return(Eval(exper))





yo = braket("-14+((115*2)-60)/20")
print(yo)