import subprocess
import glob

# set of syscall@func calls used by this program
legitimate_call_set = set()
call_in_trace_set = set()
address_map = dict()

def get_legitimate_call_set():
	f = open("/home/xmenxk/workspace/syscall-context/nginx/initial-all/complete")
	f.readline()
	call_line = f.readline()
	call_line = call_line[0:call_line.rfind(",")]
	call_set = call_line.split(",")
	for i in range(0, len(call_set)):
		legitimate_call_set.add(call_set[i]) 

def process_file(filename):
	
	f = open(filename)
	#print filename
	out = open(filename.replace("strace-context","strace-translated"), "w")
	for line in f:
		#print line
		if line.find("--- SIGCHLD") != -1:
			continue 
		if line.find("resumed>") != -1:
			continue
		if line.find("--- SIGALRM") != -1:
			continue

		if line.startswith("["):
			address = line[1:line.find("]")]
			if (len(address.strip()) > 7): 
				continue
			#print address
	
			if address_map.has_key(address):
				func = address_map[address]
			else:

				res = subprocess.check_output(["addr2line", "-f", "-e", "../source/my-nginx-strace", address])
			
				func = res.split("\n")[0]
				address_map[address] = func
				#print func

			# if CAN NOT find function
			if func.find("??") != -1:
				print line
				#print address
				#print res
			
			call = line[line.find("]")+2:line.find("(")]
			call_func = call+"@"+func
			if call_func in legitimate_call_set:
				#print call_func
				call_in_trace_set.add(call_func)
				out.write(call_func+"\n")
			else:
				if call_func.startswith("arch_prctl"):
					continue
				if call_func.startswith("ioctl"):
					continue
				if call_func.startswith("pread"):
					continue
				if call_func.startswith("recvfrom"):
					continue

				print call_func
	f.close()
	out.close()

def main():

	get_legitimate_call_set()
	
	for filename in glob.glob("strace-context/*.trace"):
		print filename	
		process_file(filename)
	print len(legitimate_call_set)
	print len(call_in_trace_set)

main()
