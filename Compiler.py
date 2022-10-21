def isint(s):#Return if s is a int or float
    if s[0]==".":
        s=s[1:]
    elif '.' in s:
        i=s.index('.')
        if i==len(s)-1:
            return(s[:-1].isdigit())
        else:
            return(s[:i].isdigit() and s[i+1:].isdigit())
    return s.isdigit()
def ctype(s):#Return if the number is float int or none
    if s[0] in sultypes:
        return(s[0])
    elif "." in s:
        return("f")
    elif s.isdigit():
        return("i")
    else:
        return("")
def smtIn(tar,hay):#smart index, check for instance of target in hay, so long as no alphanumeric characters follow immediately
    i=0
    while True:
        v=tar in hay
        if v:
            i=hay.index(tar)
            if hay[i:]==tar:
                return(True)
            elif hay[i+len(tar)] in alfnum:
                hay=hay[i+len(tar):]
            else:
                return(True)
        else:
            return(False)
def fwrite(x):#File write, including indentation
    f.write("\n".join("\t"*scp*(xi!="")+xi for xi in x.split("\n")))
def oparse(txt):#Parse the parameters for a print or input command
    obs=txt.split(",")
    st=""
    par=""
    for ob in obs:
        if ob[0]=='"':
            st+=ob[1:-1]
        else:
            tp,val=fullparse(ob)
            st+="%"+ctypes[tp]
            par+=","+val
    return('"'+st+'"'+par)
def cparse(txt,sc=""):#Using order of operations, build skeleton of parse tree
    obs=[]
    b=""
    q=0
    tc=""
    for i in range(len(txt)):
        if txt[i]=="(":
            if q==0:
                if b!="":
                    if b[-1] in sultypes:
                        tc=b[-1]
                        b=b[:-1]
                    else:
                        tc=""
                    obs.append(b)
                b=""
            q+=1
        elif txt[i]==")":
            q-=1
            if q==0:
                obs.append(cparse(b,sc=tc))
                b=""
        else:
            b+=txt[i]
    if b!="":
        obs.append(b)
    nobs=[]
    for tx in obs:
        if type(tx)==str:
            b=tx[0]
            tp="M"
            for i in range(len(tx)):
                ob=b
                if tp=="var":
                    if tx[i] in alfnum:
                        b+=tx[i]
                    else:
                        nobs.append(b)
                        b=tx[i]
                        tp="op"
                elif tp=="num":
                    if isint(b+tx[i]):
                        b+=tx[i]
                    else:
                        nobs.append(b)
                        b=tx[i]
                        tp="op"
                elif tp=="op":
                    if (b+tx[i]) in opc:
                        b+=tx[i]
                    else:
                        nobs.append(["op",b])
                        b=tx[i]
                        tp="M"
                if tp=="M":
                    if tx[i]!=" ":
                        if tx[i] in sultypes:
                            tp="var"
                        elif tx[i] in num:
                            tp="num"
                        else:
                            tp="op"
            if tp=="op":
                nobs.append(["op",b])
            else:
                nobs.append(b)
        else:
            nobs.append(tx)
    obs=nobs
    for i,ob in enumerate(obs):
        if type(ob)!=list:
            obs[i]=[ctype(ob),ob]
    oops=[]
    obs.reverse()
    v=0
    for i,ob in enumerate(obs):
        if (ob[1] in ["!","~"]):
            v+=1
            op=oops.pop(i-v)
            oops.append(["Ev",ob[1],op])
        else:
            oops.append(ob)
    obs=oops
    obs.reverse()
    s=0
    oops=[]
    for i,ob in enumerate(obs):
        if s>0:
            s-=1
        else:
            if i<len(obs)-1:
                if ob[1] in ["+","-"] and obs[i+1][0]=="op" and len(ob)==2:
                    oops.append(["Ev",ob[1],obs[i+1]])
                    s=1
                else:
                    oops.append(ob)
            else:
                oops.append(ob)
    obs=oops
    s=0
    oops=[]
    v=0
    for i,ob in enumerate(obs):
        if s>0:
            s-=1
        else:
            if ob[1] in ["*","/","%"]:
                v+=1
                op=oops.pop(i-v)
                nop=obs[i+1]
                oops.append(["Ev",ob[1],op,nop])
                s=1
            else:
                oops.append(ob)
    obs=oops
    s=0
    oops=[]
    v=0
    for i,ob in enumerate(obs):
        if s>0:
            s-=1
        else:
            if ob[1] in ["+","-"]:
                v+=1
                op=oops.pop(i-v)
                nop=obs[i+1]
                oops.append(["Ev",ob[1],op,nop])
                s=1
            else:
                oops.append(ob)
    obs=oops
    s=0
    oops=[]
    v=0
    for i,ob in enumerate(obs):
        if s>0:
            s-=1
        else:
            if ob[1] in ["<<",">>"]:
                v+=1
                op=oops.pop(i-v)
                nop=obs[i+1]
                oops.append(["i",ob[1],op,nop])
                s=1
            else:
                oops.append(ob)
    obs=oops
    s=0
    oops=[]
    v=0
    for i,ob in enumerate(obs):
        if s>0:
            s-=1
        else:
            if ob[1] in ["<","<=",">",">="]:
                v+=1
                op=oops.pop(i-v)
                nop=obs[i+1]
                oops.append(["b",ob[1],op,nop])
                s=1
            else:
                oops.append(ob)
    obs=oops
    s=0
    oops=[]
    v=0
    for i,ob in enumerate(obs):
        if s>0:
            s-=1
        else:
            if ob[1] in ["==","!="]:
                v+=1
                op=oops.pop(i-v)
                nop=obs[i+1]
                oops.append(["b",ob[1],op,nop])
                s=1
            else:
                oops.append(ob)
    obs=oops
    s=0
    oops=[]
    v=0
    for i,ob in enumerate(obs):
        if s>0:
            s-=1
        else:
            if ob[1] in ["&"]:
                v+=1
                op=oops.pop(i-v)
                nop=obs[i+1]
                oops.append(["i",ob[1],op,nop])
                s=1
            else:
                oops.append(ob)
    obs=oops
    s=0
    oops=[]
    v=0
    for i,ob in enumerate(obs):
        if s>0:
            s-=1
        else:
            if ob[1] in ["^"]:
                v+=1
                op=oops.pop(i-v)
                nop=obs[i+1]
                oops.append(["i",ob[1],op,nop])
                s=1
            else:
                oops.append(ob)
    obs=oops
    s=0
    oops=[]
    v=0
    for i,ob in enumerate(obs):
        if s>0:
            s-=1
        else:
            if ob[1] in ["|"]:
                v+=1
                op=oops.pop(i-v)
                nop=obs[i+1]
                oops.append(["i",ob[1],op,nop])
                s=1
            else:
                oops.append(ob)
    obs=oops
    s=0
    oops=[]
    v=0
    for i,ob in enumerate(obs):
        if s>0:
            s-=1
        else:
            if ob[1] in ["&&"]:
                v+=1
                op=oops.pop(i-v)
                nop=obs[i+1]
                oops.append(["b",ob[1],op,nop])
                s=1
            else:
                oops.append(ob)
    obs=oops
    s=0
    oops=[]
    v=0
    for i,ob in enumerate(obs):
        if s>0:
            s-=1
        else:
            if ob[1] in ["||"]:
                v+=1
                op=oops.pop(i-v)
                nop=obs[i+1]
                oops.append(["b",ob[1],op,nop])
                s=1
            else:
                oops.append(ob)
    obs=oops
    if sc!="":
        return([sc,sc+"-cast",obs[0]])
    return(obs[0])
def tparse(tree):#Add the types to the parse tree
    if tree[0]=="Ev":
        #print(tree)
        par=tree[2:]
        pvar=[tparse(val) for val in par]
        vpar=[oval.index(val[0]) for val in pvar]
        ntyp=oval[min(vpar)]
        return([ntyp]+[tree[1]]+pvar)
    else:
        par=tree[2:]
        pvar=[tparse(val) for val in par]
        return(tree[:2]+pvar)
def dparse(tree):#Unparse the tree back to c code so it may be executed. Parenthesis heavy.
    if len(tree)==2:
        return([tree[0],"("+tree[1]+")"])
    else:
        if tree[1] in ["<<",">>","<",">","<=",">=","==","!=","||","&&"]:
            typ=tree[0]
            par=tree[2:]
            pvar=[dparse(val) for val in par]
            return([typ,"("+str(pvar[0][1])+tree[1]+str(pvar[1][1])+")"])
        elif tree[1] in ["!","~","+","-"] and len(tree)==3:
            typ=tree[0]
            par=tree[2:]
            pvar=[dparse(val) for val in par]
            return([typ,"("+str(tree[1])+str(pvar[0][1])+")"])
        elif tree[1] in ["*","/","%","+","-"] and len(tree)==4:
            if tree[0] in "fiub":
                typ=tree[0]
                par=tree[2:]
                pvar=[dparse(val) for val in par]
                return([typ,"("+str(pvar[0][1])+tree[1]+str(pvar[1][1])+")"])
            else:
                raise NotImplementedError("Multiplication, Addition, Subtraction, Division and Modulus between string and other types is under devlopment")
        elif tree[1][1:] == "-cast":
            typ=tree[0]
            par=tree[2:]
            pvar=[dparse(val) for val in par]
            return([typ,"(("+dtypes[typ]+")"+str(pvar[0][1])+")"])
def fullparse(txt):#Call the unparsing of the fully typed parse tree
    return(dparse(tparse(cparse(txt))))
def makesyntaxtree(tree):#For debugging, call this on a tree to get a nested bracket notation tree
    if len(tree)==2:
        return("["+dtypes[tree[0]]+" "+tree[1]+"]")
    else:
        return("["+dtypes[tree[0]]+" ["+tree[1]+" "+" ".join([makesyntaxtree(branch) for branch in tree[2:]])+"]]")
def scopecompile(txt,params,name,out,level=0):#Compile the code at a given scope level, lvl 0 = main(), lvl 1 = func
    global scp
    if level==0:
        name="main"
        out="i"
    fwrite(dtypes[out[0]]+" "+name+"("+params+"){\n")
    scp+=1#These mean add indentation
    for line in txt.split("\n"): #This checks for replacement (::) lines
        if "::" in line:
            rep,val=line.split("::")
            txt=txt.replace(rep,val)
            txt=txt.replace(line.replace(rep,val)+"\n","")#Delete the replacement line afterwards
            #print(rep,val)
    #Find Function defs here, and remove them
    f=0
    sl=[]
    fname=""
    for line in txt.split("\n"): #This checks for func defs (>>) lines
        if f==0:
            if ">>" in line:
                f=1
                f,val=line.split(">>")
                val=val[:-1]
                i=0
                par=""
                fname=""
                while f[i]!="(":
                    fname+=f[i]
                    i+=1
                i+=1
                while f[i] !=')':
                    par+=f[i]
                    i+=1
        else:
            if line!="}":
                sl.append(line)
            else:
                scopecompile("\n".join(sl),par,fname,val,level=1)
                sl=[]
                f=0
    lines=txt.split("\n")
    L=len(lines)
    fwrite("unsigned long LCT["+str(L)+"];\nmemset(LCT,0,"+str(L)+"*sizeof(unsigned long));\n")#Initalize the Call time array
    vars=[]
    for line in lines:#Iterate over every line
        co=""
        sus=0
        q=False
        t=0
        for i in range(len(line)):#Kinda forgot what this does, but it checks if any defines a variable output via : << and <>
            if line[i]==":" and not q:
                vars.append((co[0],co))
                sus=1
            elif line[i:i+2]=="<<" and not q:
                vars.append((co[0],co))
                sus=1
            elif line[i]==";" and not q:
                co=""
                sus=0
            elif line[i:i+2]=="<>":
                t=1
            elif not sus:
                if not(co=="" and t and line[i] not in alfnum):#Idk what this does, it was 12am ok, i was tired
                    co+=line[i]
                    if t and line[i] not in alfnum:
                        vars.append((co[0],co[:-1]))
                        sus=1
                        t=0
            if line[i]=='"':
                q=not q
    gvars=[]
    for p in params:
        gvars.append((p[0],p))#Initialize global variables (just the parameters here)
    uvars=[]#Make a version of all of the variables (vars) and filter out duplicates
    for c,var in vars:
        if (c,var) not in uvars and (c,var) not in gvars:
            uvars.append((c,var))
    vars=uvars
    for c,var in vars:
        fwrite(dtypes[c]+" "+var+"; ")#Initialize each variable
    fwrite("\n")
    vars+=gvars#Append the global variables, so they can be used
    for c,var in vars:
        fwrite("int CT"+var+" = -1; ")#Initialize each varaible's call time
    fwrite("\nint called;\n")#Initialize the execution checker
    fwrite("for(unsigned long RTCT=1; 1; RTCT++){\n")#Main loop
    scp+=1
    fwrite("called=0;\n")#No functions have been called yet
    LN=-1
    for line in lines:#Iterate over everyline
        LN+=1#Do some basic variable setting
        reqs=[]
        rests=[]
        q=0
        r=0
        b=""
        for i in range(len(line)):#Check for suspension (?) and await-if (@) commands
            if line[i] in "@?":
                r=1
                t=line[i]
            elif r:
                if line[i]=="[":
                    q=1
                    b=""
                elif line[i]=="]":
                    q=0
                    rests.append((t,b))#Add each condition and its type to a list of restrictions
                elif q==0:
                    r=0
            if q and line[i] not in "[]":
                b+=line[i]
        ro=0
        vin=[]
        vaw=[]
        for t,cond in rests:
            if t=="@":#Handling of await-if commands
                for c,var in vars:
                    if smtIn(var,cond):#Check over every variable in the file, if its in this command, add it to a list of variables to await
                        vaw.append(var)
                sub=0
                for i in range(len(cond)):#Check for unperma called integers, and note that, else remove the !
                    if cond[i-sub]in"0123456789" and cond[i-1-sub]!="!" and cond[i-1-sub]not in"0123456789":
                        ro=1
                    elif cond[i-sub]in"0123456789" and cond[i-1-sub]=="!" and cond[i-1-sub]not in"0123456789":
                        cond=cond[:i-1-sub]+cond[i-sub:]
                        sub+=1
                reqs.append(cond)
            elif t=="?":#Handling of suspend commands
                for c,var in vars:
                    if smtIn(var,cond):#Check over every variable in the file, if its in this command, add it to a list of variables to await
                        vaw.append(var)
                for i in range(len(cond)):#Check for unperma called integers, and note that, else remove the !
                    if cond[i]in"0123456789" and cond[i-1]!="!":
                        ro=1
                    elif cond[i]in"0123456789" and cond[i-1]=="!":
                        cond=cond[:i-1]+cond[i:]
        if ro:
            reqs.append("RTCT==1")#If theres at least one non perma int, add a only call once req
        if line[-1]=="#":
            reqs.append("LCT["+str(LN-1)+"]>LCT["+str(LN)+"] && LCT["+str(LN-1)+"]<RTCT")#Fancy stuff to construct the restrictions
        for var in vaw:
            reqs.append("CT"+str(var)+">LCT["+str(LN)+"] && CT"+str(var)+"<RTCT")
        fwrite("if("+" && ".join(reqs)+"){\n")#Write the if statement
        fwrite("called=1;\n")#Write termination stopping line
        scp+=1
        if ";" in line:#Turn the code in front into either many lines delimited by ; or just one
            slines=line.split(";")
        else:
            slines=[line]
        for sline in slines:
            if sline[0:2]=="<>":#Check for push (<>) commands
                v=""
                i=2
                while sline[i] in alfnum:
                    v+=sline[i]
                    i+=1
                fwrite("CT"+v+"=RTCT;\n")
            elif sline[0:5]=='print':#Check for print commands
                i=6
                v2=""
                while sline[i] !=')':
                    v2+=sline[i]
                    i+=1
                fwrite('printf('+oparse(v2)+');\n')
            elif "<<" in sline:#Check for broadcast (<<) commands
                v0=""
                i=0
                while sline[i] in alfnum:
                    v0+=sline[i]
                    i+=1
                i=sline.index("<<")+2
                while sline[i] ==" ":
                    i+=1
                v1=""
                while sline[i] not in "@?#":
                    v1+=sline[i]
                    i+=1
                    if i==len(sline):
                        break
                if v1[0:5]=='input':#input commands
                    i=sline.index(v1)+6
                    v2=""
                    while sline[i] !=')':
                        v2+=sline[i]
                        i+=1
                    fwrite('printf('+oparse(v2)+');scanf("%'+ctypes[v0[0]]+'",&'+v0+');\n')
                else:#Else just assign it normally
                    fwrite(v0+"="+v1+";\n")
                fwrite("CT"+v0+"=RTCT;\n")
            elif ":" in sline:#Check for assignment (:) commands
                v0=""
                i=0
                while sline[i] in alfnum:
                    v0+=sline[i]
                    i+=1
                i=sline.index(":")+1
                while sline[i] ==" ":
                    i+=1
                v1=""
                while sline[i] not in "@?#":
                    v1+=sline[i]
                    i+=1
                    if i==len(sline):
                        break
                #fwrite(v0+" = "+v1+";\n")
                if v1[0:5]=='input':#input commands
                    i=sline.index(v1)+6
                    v2=""
                    while sline[i] !=')':
                        v2+=sline[i]
                        i+=1
                    fwrite('printf('+oparse(v2)+');scanf("%'+ctypes[v0[0]]+'",&'+v0+');\n')
                else:
                    fwrite(v0+"="+v1+";\n")
        fwrite("LCT["+str(LN)+"]=RTCT;\n")
        scp-=1
        fwrite("}\n")
    #print(vars)
    fwrite("if(!called){\n")
    scp+=1
    #fwrite('printf("inters: %d\n",(RTCT));\n')
    fwrite("return 0;\n")
    scp-=1
    fwrite("}\n")
    scp-=1
    fwrite("}\n")
    scp-=1
    fwrite("}\n")


#Base variables
opc=["+","-","!","~","*","&","/","%","<<",">>","<",">","<=",">=","==","!=","^","|","&&","||"]
alfnum="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
sultypes="iufpbsc"
num="0123456789"
alf="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
oval="sfiub"
dtypes={"i":"int","u":"unsigned int","f":"float","b":"int","c":"char","Ev":"Eval","v":"void"}#to implement: string, ptr
ctypes={"i":"d","u":"i","f":"f","c":"c"}

with open("code.sul","r") as f:#If you want to use a different file, change this file name
    txt=f.read()
scp=0
with open("code.c","w") as f:#Output file
    fwrite("#include <stdio.h>\n#include <string.h>\n\n")#Write simple c imports and base code
    scopecompile(txt,"void","main","i",level=0)
    
