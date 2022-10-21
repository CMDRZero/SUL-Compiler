def isint(s):
  if s[0]==".":
    s=s[1:]
  elif '.' in s:
    i=s.index('.')
    if i==len(s)-1:
      return(s[:-1].isdigit())
    else:
      return(s[:i].isdigit() and s[i+1:].isdigit())
  return s.isdigit()
def ctype(s):
  if s[0] in sultypes:
    return(s[0])
  elif "." in s:
    return("f")
  elif s.isdigit():
    return("i")
  else:
    return("")

def smtIn(tar,hay):
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
def fwrite(x):
  f.write("\n".join("\t"*scp*(xi!="")+xi for xi in x.split("\n")))
def oparse(txt):
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
def cparse(txt,sc=""):
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
def tparse(tree):
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
def dparse(tree):
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
def fullparse(txt):
  return(dparse(tparse(cparse(txt))))
def makesyntaxtree(tree):
  if len(tree)==2:
    return("["+dtypes[tree[0]]+" "+tree[1]+"]")
  else:
    return("["+dtypes[tree[0]]+" ["+tree[1]+" "+" ".join([makesyntaxtree(branch) for branch in tree[2:]])+"]]")

opc=["+","-","!","~","*","&","/","%","<<",">>","<",">","<=",">=","==","!=","^","|","&&","||"]
alfnum="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
sultypes="iufpbsc"
num="0123456789"
alf="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
oval="sfiub"
dtypes={"i":"int","u":"unsigned int","f":"float","b":"int","c":"char","Ev":"Eval"}#to implement: string, ptr
ctypes={"i":"d","u":"i","f":"f","c":"c"}

#a=cparse("(!1<<1)*b(~3)>0")
#ta=tparse(a)
#syn=makesyntaxtree(ta)
#print(a)
#print(ta)
#print(dparse(ta))
#print(cparse("(1+2)*(3+4)"))
#error

with open("code.sul","r") as f:
  txt=f.read()
#print(txt)
scp=0
with open("code.c","w") as f:
  fwrite("#include <stdio.h>\n#include <string.h>\n\nint main(void) {\n")
  scp+=1
  for line in txt.split("\n"):
    if "::" in line:
      rep,val=line.split("::")
      txt=txt.replace(rep,val)
      txt=txt.replace(line.replace(rep,val)+"\n","")
      #print(rep,val)
  lines=txt.split("\n")
  L=len(lines)
  fwrite("unsigned long LCT["+str(L)+"];\nmemset(LCT,0,"+str(L)+"*sizeof(unsigned long));\n")
  vars=[]
  for line in lines:
    co=""
    sus=0
    q=False
    t=0
    for i in range(len(line)):
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
        if not(co=="" and t and line[i] not in alfnum):
          co+=line[i]
          if t and line[i] not in alfnum:
            vars.append((co[0],co[:-1]))
            sus=1
            t=0
      if line[i]=='"':
        q=not q
  uvars=[]
  for c,var in vars:
    if (c,var) not in uvars:
      uvars.append((c,var))
  vars=uvars
  for c,var in vars:
    fwrite(dtypes[c]+" "+var+"; ")
  fwrite("\n")
  for c,var in vars:
    fwrite("int CT"+var+" = -1; ")
  fwrite("\n")
  fwrite("for(unsigned long RTCT=1; RTCT<10000; RTCT++){\n")
  scp+=1
  LN=-1
  for line in lines:
    LN+=1
    reqs=[]
    rests=[]
    q=0
    r=0
    b=""
    for i in range(len(line)):
      if line[i] in "@?":
        r=1
        t=line[i]
      elif r:
        if line[i]=="[":
          q=1
          b=""
        elif line[i]=="]":
          q=0
          rests.append((t,b))
        elif q==0:
          r=0
      if q and line[i] not in "[]":
        b+=line[i]
    ro=0
    vin=[]
    vaw=[]
    for t,cond in rests:
      if t=="@":
        for c,var in vars:
          if smtIn(var,cond):
            #vin.append(var)
            vaw.append(var)
        sub=0
        for i in range(len(cond)):
          if cond[i-sub]in"0123456789" and cond[i-1-sub]!="!" and cond[i-1-sub]not in"0123456789":
            ro=1
          elif cond[i-sub]in"0123456789" and cond[i-1-sub]=="!" and cond[i-1-sub]not in"0123456789":
            cond=cond[:i-1-sub]+cond[i-sub:]
            sub+=1
        reqs.append(cond)
      elif t=="?":
        for c,var in vars:
          if smtIn(var,cond):
            vaw.append(var)
        for i in range(len(cond)):
          if cond[i]in"0123456789" and cond[i-1]!="!":
            ro=1
          elif cond[i]in"0123456789" and cond[i-1]=="!":
            cond=cond[:i-1]+cond[i:]
    if ro:
      reqs.append("RTCT==1")
    if line[-1]=="#":
      reqs.append("LCT["+str(LN-1)+"]>LCT["+str(LN)+"] && LCT["+str(LN-1)+"]<RTCT")
    for var in vaw:
      reqs.append("CT"+str(var)+">LCT["+str(LN)+"] && CT"+str(var)+"<RTCT")
    fwrite("if("+" && ".join(reqs)+"){\n")
    scp+=1
    if ";" in line:
      slines=line.split(";")
    else:
      slines=[line]
    for sline in slines:
      if sline[0:2]=="<>":
        v=""
        i=2
        while sline[i] in alfnum:
          v+=sline[i]
          i+=1
        fwrite("CT"+v+"=RTCT;\n")
      elif sline[0:5]=='print':
        i=6
        v2=""
        while sline[i] !=')':
          v2+=sline[i]
          i+=1
        fwrite('printf('+oparse(v2)+');\n')
      elif "<<" in sline:
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
        if v1[0:7]=='input("':
          i=sline.index(v1)+7
          v2=""
          while sline[i] !='"':
            v2+=sline[i]
            i+=1
          fwrite('printf("'+v2+'");scanf("%'+ctypes[v0[0]]+'",&'+v0+');\n')
        elif v1[0:5]=='input':
          i=sline.index(v1)+6
          v2=""
          while sline[i] !=')':
            v2+=sline[i]
            i+=1
            fwrite('printf("%'+ctypes[v2[0]]+'",&'+v0+');scanf("%'+ctypes[v0[0]]+'",&'+v0+');\n')
        else:
          fwrite(v0+"="+v1+";\n")
        fwrite("CT"+v0+"=RTCT;\n")
#Assignment Operand
      elif ":" in sline:
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
        if v1[0:7]=='input("':
          i=sline.index(v1)+7
          v2=""
          while sline[i] !='"':
            v2+=sline[i]
            i+=1
          fwrite('printf("'+v2+'");scanf("%'+ctypes[v0[0]]+'",&'+v0+');\n')
        elif v1[0:5]=='input':
          i=sline.index(v1)+6
          v2=""
          while sline[i] !=')':
            v2+=sline[i]
            i+=1
            fwrite('printf("%'+ctypes[v2[0]]+'",&'+v0+');scanf("%'+ctypes[v0[0]]+'",&'+v0+');\n')
        else:
          fwrite(v0+"="+v1+";\n")
    fwrite("LCT["+str(LN)+"]=RTCT;\n")
    scp-=1
    fwrite("}\n")
    
  #print(vars)
  scp-=1
  fwrite("}\n")
  scp-=1
  fwrite("}\n")
  
