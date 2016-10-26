import subprocess
import glob


def process_file(folder,fname):
	address_map = dict()
	found_count = 0
	not_found_count = 0
	
	f = open(folder+"/"+fname)
	
	print folder+"/"+fname
	#out = open(folder+"/context-test-result", "w")
	for line in f:
		#print line
		#if line.find("--- SIGCHLD") != -1:
		#	continue 
		#if line.find("resumed>") != -1:
		#	continue
		#if line.find("--- SIGALRM") != -1:
		#	continue
		
		if line.find("[") != -1 and line.find("]") != -1:
			address = line[line.find("[")+1:line.find("]")]
			address = address.strip()
			#if (len(address.strip()) > 7): 
			#	continue
			#print address
	
			if address_map.has_key(address):
				func = address_map[address]
			else:
				res = subprocess.check_output(["addr2line", "-f", "-e", folder+"/program", address])
			
				func = res.split("\n")[0]
				address_map[address] = func
			#print func

			# if CAN NOT find function, find ?? in result
			if func.find("??") != -1:
				not_found_count = not_found_count+1
				#print line
				#print address
				#print res
			else:
				found_count = found_count + 1

			#print call_func
	f.close()
	print "found count:",  found_count
	print "not found count:", not_found_count
	print "not found percent:", float(not_found_count)/(found_count+not_found_count)
	

def main():

	process_file("backdoor-attack-context-strace","1.trace")
	process_file("backdoor-attack-context-strace","2.trace")
	process_file("backdoor-attack-context-strace","3.trace")
	process_file("backdoor-attack-context-strace","4.trace")
	process_file("backdoor-attack-context-strace","5.trace")
	process_file("backdoor-attack-context-strace","6.trace")
	process_file("backdoor-attack-context-strace","7.trace")
	
	process_file("Telnet-IAC-Buffer-Overflow-context","0.trace")
	
	process_file("gzip_v5_rop_context","context-sens.trace")

	process_file("gzip_v5_rop_chain_context","context-sens.trace")


	

main()
