from time import time
cvf=0
Portal=2
import os
import binascii
import math

Deep=4
Spin2=300

lenf=0
name=""
szx=""
wer=""
namez = input("c: compress or e: extract? ")


#@Author Jurijus pacalovas
class compression:
       
        def cryptograpy_compression4(self):
                
                self.name = "Written: Jurijus pacalovas Date: 29/09/2021 18:06"
                
                if namez=="c" or namez=="e":
                    if namez=="c":
                        i=1
                    if namez=="e":
                        i=2
                    
                    #import mpmath as m
                    #m.mp.dps = 100000
                    #PI=4 * m.atan(1)

                    spin=0
                    c=0
                    A=0
                    Spin=0
                    sda4=""
                    sda5=""
                    sda6=""
                    e4a=""
                    e4b=""
                    ei8=""
                        
                    name = input("What is name of file? ")
                    namem=""
                    namema="?"
        
                    nameas=name
                    nac=len(nameas)

                    if i==2:
                        if nameas[nac-4:nac]!=".bin":
                             print("Program close because this is file is not .bin")
                             raise SystemExit
                        
                        nameas=name[:nac-4]
                        nac=len(nameas)
                    
                    if i==1:
                        
                        nameas=name+".bin"
                    
                    nac=len(nameas)
                    
                    Circle_times3=0
                    cvf=2
                    cvf1=0
                    s=""
                    
                    e2=0
                    e3=1
                    e4=""
                    ei4=0
                    ei5=7
                    
                    e4=""
                    
                    c=2
                    sw=2
                    elw=0
                 
                    sda3=""
                    sda2=""

                    sda5=""
                    sda6=""
                    sda7=""
                    sda8=""
                    sda9=""
                    sda11=""
                    sda12=""
                    
                    sda14=""
                    sdaB=""
                    D=0

                    block=1
                    block2=0
                    block3=0
                    
                    count=0
                    
                    x=0
                    x1=0
                    x2=0
                    n=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
      
                        s=str(data)

                        lenf1=len(data)
                        lenf7=len(data)
                        
                        END_working=0
                        Circle_times2=0
                        ii=0
                        sda20=""
                        
                        while END_working<10:
                       
                            Circle_times3=Circle_times3+1

                            with open(nameas, "ab") as f2:
                                if Circle_times3==1:

                                 
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    sda=sda+sda2

                                    if Circle_times3==1:
                                        sda2=sda
                            
                                    n = int(sda2, 2)
                                
                                    qqwslenf=len(sda2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                  
                                    lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1

                                    sda2=sda

                                    lenf3=len(sda2)
                                lenf2=len(sda2)
                                #print(lenf2)
                                if i==1:
                                    if lenf7>=(2**32)-1:
                                        raise SystemExit
                                        
                                    if lenf7<=0:
                                        raise SystemExit 
                                #########################################################################################################################################################
                                
                                block2=0
                                if i==2:

                                    lenf5=len(sda2)

                                    block2=0
                                    ei4=0
                                    ei5=1

                                    
                                    sda3=sda2
                                    
                                    block3=0
                                    Colaider3=""
                                   
                                    lenf5=len(sda3)
                                    
                                    
                                    #Extract
                                    
                                    
                                    s=""

                                    sda3=sda2
                                    lenf6=len(sda3)
                                    
                                    sda4=""
                                    sda5=""
                                    sda6=""
                                    sda7=""
                                    sda8=""
                                    sda9=""
                                    sda17=""
                                    Bytes_row4=""
                                    sda19=""
                                    
                                    ei=0
                                   

                                    if Circle_times2==0:
                                           
                                           g=1
                                           
                                    if sda2[0:8]=="01111111": 
                                    
                                    	
                                    	 sda17=sda2[8:]
                                    	 n = int(sda17, 2)
                                    	 qqwslenf=len(sda17)
                                    	 qqwslenf=(qqwslenf//8)*2
                                    	 qqwslenf=str(qqwslenf)
                                    	 qqwslenf="%0"+qqwslenf+"x"
                                    	 jl=binascii.unhexlify(qqwslenf % n)
                                    	 sssssw=len(jl)
                                    	 szxzzza=""
                                    	 szxzs=""
                                    	 f2.write(jl)
                                    	 x2 = time()
                                    	 x3=x2-x
                                    	 return print(x3)
                                        
                                    	   
                                    	
                                    	
                                    
                                    

                                    if g==1:

                                        if sda2[lenf5-8:lenf5]=="10000000":

                                            sda2=sda2[1:lenf5-8]

                                        elif sda2[lenf5-7:lenf5]=="1000000":

                                            sda2=sda2[1:lenf5-7]

                                        elif sda2[lenf5-6:lenf5]=="100000":

                                            sda2=sda2[1:lenf5-6]

                                        elif sda2[lenf5-5:lenf5]=="10000":

                                            sda2=sda2[1:lenf5-5]


                                        elif sda2[lenf5-4:lenf5]=="1000":

                                            sda2=sda2[1:lenf5-4]

                                        elif sda2[lenf5-3:lenf5]=="100":

                                            sda2=sda2[1:lenf5-3]

                                        elif sda2[lenf5-2:lenf5]=="10":

                                            sda2=sda2[1:lenf5-2]

                                        elif sda2[lenf5-1:lenf5]=="1":

                                            sda2=sda2[1:lenf5-1]
                                        else:
                                        	 raise SystemExit
                                        	

                                    

                                    sda3=sda2

                                    lenf6=len(sda3)
                        
                                    count_times4=0

                                    FF=len(sda3)
                                    
                                    sda17=""
                                    sda19=""
                                    
                                    sda3=sda2
                                    Spin=0
                                    lenf6=len(sda3)
                                    ei4=0
                                    ei5=20
                                    block3=0
                                    Colaider3=""
                                    block2=0
                                    block3=0

                                    szx=""

                                    sda6=""

                                    #Compression

                                    sda9=""

                                    sda10=""
                                    sda11=""
                                    sda12=""
                                    sda13=""
                                    sda17=""

                                    ei=0
 
                                    lenf6F=lenf6

                                    ei=0

                                    Spin=0
                                    
                                   
                                   
                                   
                                  
                                    ei=0
                                    T14=0
                                    
                                    while sda11!="00000000":
                                    	sda11=sda2[ei:ei+8]
                                    	T14=T14+1
                                    	ei=ei+8
                                    	
                                    T12=sda2[0:(T14*8)-8]
                                    sda2=sda2[0:T14*8]
                                    
                                    sda10=sda2
                                   
                                   
                                    T6 = int(sda10, 2)
                                    if T6==0:
                                    	 raise SystemExit
                                    
                                    T7=1
                                    T1=1
                                    T8=0
                                  
                                    
                                    
                                    T3=1
                                    T4=0
                                    T5=0
                                    
                                    T15=0
                                    
                                    while T15!=T12:
	                                    T2=T1%2
	                                    T3=T1
	                                    
	                                    if T2==0:
	                                        T3=T3//2
	                                        T1=T3
	                                        T4=T4+1
	                                        
	                                       
	                                    
	                                    	
	                                    else:
	                                    	T3=(T3*3)+1
	                                    	T1=T3
	                                    	T4=T4+1

	                                    	
	                                    if T3==1 and T4>=2:
	                                    	T4=T4
	                                    	T8=T4
	                                    	T5=T3
	                                    	T7=T7+1
	                                    	T1=T7
	                                    	T4=0	
	                                    if T6==T8:
	                                    	T15=T15+1
	                                    	

                                    sda17=bin(T7)[2:]   
                                    if sda17[0:1]=="0":
                                    	 raise SystemExit
                                    sda17=sda17[1:]
                                
                                    
                                   
                                   
                                   
                                  
                                    
                                    	

                                    lenf=len(sda17)
                                            
                                    szx=""
                                    xc=8-lenf%8
                                    z=0
                                    if xc!=0:
                                        if xc!=8:
                                                while z<xc:
                                                        szx="0"+szx
                                                        z=z+1

                                    lenf=len(sda17)
                                    B3=""

                                                                                      

                                   
                                    sda17=szx+sda17
                                         
                                    sda2=sda17
                                    Circle_times2=Circle_times2+1
                                    
                                    
                                    if   Circle_times2==1:
                                         #print(sda17)
                                       
                                         n = int(sda17, 2)
                                         qqwslenf=len(sda17)
                                         qqwslenf=(qqwslenf//8)*2
                                         qqwslenf=str(qqwslenf)
                                         qqwslenf="%0"+qqwslenf+"x"
                                         jl=binascii.unhexlify(qqwslenf % n)
                                         sssssw=len(jl)

                                         szxzzza=""
                                         szxzs=""
                                            
                                         f2.write(jl)
                                         x2 = time()
                                         x3=x2-x
                                         return print(x3)
                                        
                                if i==1:

                                    sda17=""
                                    sda19=""
                                    
                                    sda3=sda2
                                    Spin=0
                                    lenf6=len(sda3)
                                    ei4=0
                                    ei5=20
                                    block3=0
                                    Colaider3=""
                                    block2=0
                                    block3=0

                                    szx=""

                                    sda6=""

                                    #Compression

                                    sda9=""

                                    sda10=""
                                    sda11=""
                                    sda12=""
                                    sda13=""

                                    ei=0
 
                                    lenf6F=lenf6

                                    ei=0
                                    Spin=0
                                  
                                    T3=1
                                    T4=0
                                    T5=0
                                  
                                   
                                    
                                    sda10="1"+sda3
                                   
                                    T1 = int(sda10, 2)
                                    T10=T1
                                    
                                    while T5!=1:
	                                    T2=T1%2
	                                    T3=T1
	                                    
	                                    if T2==0:
	                                        T3=T3//2
	                                        T1=T3
	                                        T4=T4+1
	                                        
	                                       
	                                    
	                                    	
	                                    else:
	                                    	T3=(T3*3)+1
	                                    	T1=T3
	                                    	T4=T4+1
	                                    	
	                                    	
	                                    	
	                                    
	                                    	
	                                    if T3==1 and T4>=2:
	                                    	T4=T4
	                                    	T5=T3
	                                    	
	                                    	
	                                    
	                                  
	                               
                                    T7=1
                                    T1=1
                                    T8=0
                                    T6=T4
                                    T9=T4
                                    
                                    T3=1
                                    T4=0
                                    T5=0
                                    
                                    while T7!=T10:
	                                    T2=T1%2
	                                    T3=T1
	                                    
	                                    if T2==0:
	                                        T3=T3//2
	                                        T1=T3
	                                        T4=T4+1
	                                        
	                                       
	                                    
	                                    	
	                                    else:
	                                    	T3=(T3*3)+1
	                                    	T1=T3
	                                    	T4=T4+1

	                                    	
	                                    if T3==1 and T4>=2:
	                                    	T4=T4
	                                    	T8=T4
	                                    	T5=T3
	                                    	T7=T7+1
	                                    	T1=T7
	                                    	T4=0	
	                                    if T6==T8:
	                                    	T12=T12+1

                                    
                                
                                    
                                     
                                                
                                          
                                    sda6=sda4
                                    sda4=""
                                      
                                    #####################################################################################################################################################
                                                  
                                    block2=0
                                    
                                    Spinh=0              
                                    block2=0
                              
                                    e4=""
                                    e4a=""
                                    e4b=""
                                    block2=0
                                    sda5=""
                                     
                                    sda2=sda17
                                   

                                    if i==1:
                                        wer=""
                                        wer=sda6
                                        sda4=""
                                        szx=""
                                        
                                        Circle_times2=Circle_times2+1

                                        lenf9=len(sda17)
                                        #print(Circle_times2)
                                        
                                        
                                        if  Circle_times2==1:
                                            #print(lenf6-1)

                                            if T7==T10:
                                            	sda17=bin(T9)[2:]
                                            	sda18=bin(T12)[:2]
                                            	lenf=len(sda18)
                                            	szx=""
                                            	xc=8-lenf%8
                                            	z=0
                                            	if xc!=0:
                                            	        if xc!=8:
                                            	            while z<xc:
                                            	            	szx="0"+szx
                                            	            	z=z+1
                                            	sda19=szx+sda18+"00000000"
                                            	sda17=sda19+sda17
                                            	sda17="1"+sda17+"1"
                                            
       
                                           
                                            	
                                            
                                            lenf=len(sda17)
                                            
                                            szx=""
                                            xc=8-lenf%8
                                            z=0
                                            if xc!=0:
                                                if xc!=8:
                                                    while z<xc:
                                                        szx="0"+szx
                                                        z=z+1

                                            lenf=len(sda17)
                                            B3=""

                                                                                      

                                            sda17=sda17+szx
                                            L=len(sda17)
                                            if L>lenf6F:
                                                     
                                            	sda17="01111111"+sda3

                                            n = int(sda17, 2)
                                            qqwslenf=len(sda17)
                                            qqwslenf=(qqwslenf//8)*2
                                            qqwslenf=str(qqwslenf)
                                            qqwslenf="%0"+qqwslenf+"x"
                                            jl=binascii.unhexlify(qqwslenf % n)
                                            sssssw=len(jl)

                                            szxzzza=""
                                            szxzs=""
                                            sda2=sda6
                                              
                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            xs=float(x3)

                                            Speed=0

                                            if x3!=0:

                                                   Speed=(lenf7//xs)#B/s
                                                   print(Speed)
                                                   print("B/s")

                                            if x3==0:
                                                   print("FAST")

                                            return print(x3)
                                            
d=compression()

xw=d.cryptograpy_compression4()
print(xw)
