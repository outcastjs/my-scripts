import requests
import socket
import concurrent.futures
import ipaddress

ip_string = input("ip: ")
try:
    ip = ipaddress.ip_address(ip_string)
except ValueError:
    print("bru that aint an ip")
    exit()

response = requests.get(f"https://geo.ipify.org/api/v1?apiKey=at_DHfQruiTMJhCizoxuu6d9oMnuVq0u&ipAddress={ip}")
data = response.json()
print(f"IP Address: {ip}")
if 'location' in data:
    if 'city' in data['location']:
        print(f"city: {data['location']['city']}")
    if 'country' in data['location']:
        print(f"country: {data['location']['country']}")
if 'isp' in data:
    print(f"orgasm: {data['isp']}")

common_ports = [80, 443, 21, 22, 23, 25, 53, 110, 143, 3306, 5432]

def check_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((ip_string, port))
    sock.close()
    if result == 0:
        return port
    else:
        return None

with concurrent.futures.ThreadPoolExecutor() as executor:
    port_results = executor.map(check_port, common_ports)

open_ports = [port for port in port_results if port is not None]
if len(open_ports) == 0:
    print("no open ports found.")
else:
    print(f"open ports on {ip}: {', '.join(map(str, open_ports))}")
