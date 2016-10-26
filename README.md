# Attacks and Call Traces

***This is a public domain, only for reproducing and trace tool usage, who is interesting in ROP attacks***

***Please put your own algorithm code in a safe place***

##Call Traces
Look into the folder Call Traces.

##Paper1 Reproduce
for dsn 16, check README_ATTACK and discussions (***very important!***)

###Metasploit for proftpd:

Run the proftpd 
 ![picture alt](https://github.com/yaoGroupAnomaly/reproduceAttacks/blob/master/image/startProftpd.png "Get the Shell from metasploit")


The scressnhot for metasploit
 ![picture alt](https://github.com/yaoGroupAnomaly/reproduceAttacks/blob/master/image/getTheshell.png "Get the Shell from metasploit")


###ROP and return to LibC
The screenshot for gzip ROP

 ![picture alt](https://github.com/yaoGroupAnomaly/reproduceAttacks/blob/master/image/ropShell.png "Get the Shell from metasploit")


return2Libc:

 ![picture alt](https://github.com/yaoGroupAnomaly/reproduceAttacks/blob/master/image/LibCgetAshell.png "Return toLibc how to find addresses")

 ![picture alt](https://github.com/yaoGroupAnomaly/reproduceAttacks/blob/master/image/returnToLibcCode.png "Map address to code")


##Paper2 Reproduce
for ccs 16, under construction 


## Reference 
if you feel these instructions helpful, citing the papers:

A Sharper Sense of Self: Probabilistic Reasoning of Program Behaviors for Anomaly Detection with Context Sensitivity. In Proc. DSN, 2016.

Unearthing Stealthy Program Attacks Buried in Extremely Long Execution Paths. In Proc. CCS, 2015.

Probabilistic Program Modeling for High-Precision Anomaly Classification. In Proc. CSF, 2015.

are highly aprreciated.


