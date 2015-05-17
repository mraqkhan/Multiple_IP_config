import sys, os, string, pexpect

ip_str = raw_input('Please Enter IPs (csv and/or Range(10.3.20.1-10)): ')

subnet_mask = raw_input('Please Enter subnet mask (255.255.255.0): ')

ifname = raw_input('Enter Interface name to assign IPs to: ')

ips = string.split(ip_str, ",")

tmp_ip = []
for ip in ips:
	if "-" in ip:
		range_ip = string.split(ip, "-")
		ips.remove(ip)
		if len(range_ip) > 1:
			if int(range_ip[0][8:]) < int(range_ip[1]) and int(range_ip[1]) < 255:
				for x in range(int(range_ip[0][8:]),int(range_ip[1]) + 1):
					tmp_ip.append(range_ip[0][:7] + "."+str(x))

ips.extend(tmp_ip)

for ip in ips:
	child = pexpect.spawn('netsh interface ipv4 add address '+ifname+' '+ip+' '+subnet_mask)
	print ('netsh interface ipv4 add address '+ifname+' '+ip+' '+subnet_mask+'')
	while True:
		print child.readline()
