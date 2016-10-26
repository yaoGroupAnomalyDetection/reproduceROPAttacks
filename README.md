# Attacks and Call Traces

***This is a public domain, only for reproducing attacks and trace tool guided. Anyone is interesting in program anomaly detection is welcome to make contributions***

##Call Trace Colection

Please look into the folder CallTraces.

##Reproduce -Type-1
For dsn 16, check README_ATTACK and discussions (***very important!***)

Bckground: Metaexploit, GDB

###Metasploit for proftpd:

Run the proftpd 
 ![picture alt](https://github.com/yaoGroupAnomaly/reproduceAttacks/blob/master/image/startProftpd.png "Get the Shell from metasploit")


The scressnhot for metasploit to get a shell!
 ![picture alt](https://github.com/yaoGroupAnomaly/reproduceAttacks/blob/master/image/getTheshell.png "Get the Shell from metasploit")


###ROP and return to LibC

The screenshot for gzip ROP to get a shell!

 ![picture alt](https://github.com/yaoGroupAnomaly/reproduceAttacks/blob/master/image/ropShell.png "Get the Shell from metasploit")


return2Libc to get a shell!

 ![picture alt](https://github.com/yaoGroupAnomaly/reproduceAttacks/blob/master/image/LibCgetAshell.png "Return toLibc how to find addresses")

 ![picture alt](https://github.com/yaoGroupAnomaly/reproduceAttacks/blob/master/image/returnToLibcCode.png "Map address to code")


##Reproduce --Type 2--
for ccs 16, under construction 


## Reference 
if you feel these instructions helpful, citing the papers:

A Sharper Sense of Self: Probabilistic Reasoning of Program Behaviors for Anomaly Detection with Context Sensitivity. In Proc. DSN, 2016.

Unearthing Stealthy Program Attacks Buried in Extremely Long Execution Paths. In Proc. CCS, 2015.

Probabilistic Program Modeling for High-Precision Anomaly Classification. In Proc. CSF, 2015.

are highly aprreciated.
