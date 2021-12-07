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
                                        
