import subprocess
import platform
import ipaddress
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def generate_ips(subnet):
    network = ipaddress.ip_network(subnet, strict=False)
    return [str(ip) for ip in network.hosts()]

def ping_ip(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        result = subprocess.run(["ping", param, "1", ip],
                                capture_output=True,
                                text=True)
        output = result.stdout.lower()
        if "unreachable" in output or "timed out" in output or "could not find host" in output:
            return None
        return ip  # return only if alive
    except Exception as e:
        return None

if __name__ == "__main__":
    subnet = "192.168.0.0/24"
    ip_list = generate_ips(subnet)

    print(f"[🚀] Starting ThreadPool scan for {len(ip_list)} IPs...\n")
    start = time.time()

    live_hosts = []

    with ThreadPoolExecutor(max_workers=150) as executor:
        future_to_ip = {executor.submit(ping_ip, ip): ip for ip in ip_list}
        
        for future in as_completed(future_to_ip):
            ip = future_to_ip[future]
            result = future.result()
            if result:
                live_hosts.append(result)
                print(f"[+] {result} is alive")

    end = time.time()
    print(f"\n[✔️] Scan complete in {end - start:.2f} seconds.")
    print(f"[+] Total live hosts found: {len(live_hosts)}")
    for host in live_hosts:
        print(f"   [+] {host}")
