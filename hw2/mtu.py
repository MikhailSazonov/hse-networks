import subprocess
import sys
import os
import socket

def discover_mtu(host):
	size_down = 0
	size_up = 10000
	while size_up > size_down + 1:
		middle = (size_up + size_down) // 2

		code = os.system("ping -c 1 -M do -s " + str(middle) + " " + host + ' > /dev/null 2> /dev/null')

		if code:
			size_up = middle
		else:
			size_down = middle
	
	code = os.system("ping -c 1 -M do -s " + str(size_up) + " " + host + ' > /dev/null 2> /dev/null')
	if code:
		return size_down + 28
	else:
		return size_up + 28



# Формально проверяем корректность аргумента, хотя при запуске из докера при отсутствии хоста скрипт фоллбэкнется на google.com

if len(sys.argv) == 1:
	print('No host in args.')
	exit(0)

if len(sys.argv) > 2:
	print('Too many args.')
	exit(0)

try:
	socket.gethostbyname(sys.argv[1])
except:
	print('Unknown host.')
	exit(0)

code = os.system("ping -c 1 -M do -s 1 " + sys.argv[1] + ' > /dev/null 2> /dev/null')

if code:
	print('ICMP is banned, exit...')
	exit(0)


print('Discovering MTU for the ' + sys.argv[1] + '.')
print('MTU:', discover_mtu(sys.argv[1]))
