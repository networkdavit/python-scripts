import nmap
import matplotlib.pyplot as plt
import sys

def run_nmap_scan(target):
    nm = nmap.PortScanner()
    nm.scan(target, arguments="-sC -sV -p- -A")
    return nm


def categorize_by_severity(scan_data):
    severity = {'low': 0, 'medium': 0, 'high': 0}
    for host in scan_data.all_hosts():
        for proto in scan_data[host].all_protocols():
            ports = scan_data[host][proto].keys()
            for port in ports:
                service = scan_data[host][proto][port]

                if 'http' in service['name'] or 'ftp' in service['name']:
                    severity['high'] += 1
                elif service['state'] == 'open':
                    severity['medium'] += 1
                else:
                    severity['low'] += 1
    return severity


def visualize_severity(severity):
    labels = severity.keys()
    sizes = severity.values()
    colors = ['lightgreen', 'gold', 'lightcoral']
    explode = (0.1, 0, 0) 

    plt.figure(figsize=(7, 7))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')  
    plt.title("Nmap Scan Severity Distribution")
    plt.show()

if __name__ == "__main__":
    target = sys.argv[1] 
    scan_data = run_nmap_scan(target)
    severity = categorize_by_severity(scan_data)
    visualize_severity(severity)
