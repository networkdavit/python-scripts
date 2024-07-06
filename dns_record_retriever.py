import dns.resolver
import sys

def get_dns_records(domain):
    records = {}
    for record_type in ['A', 'AAAA', 'MX', 'NS', 'TXT']:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            records[record_type] = [r.to_text() for r in answers]
        except dns.resolver.NoAnswer:
            records[record_type] = None
        except dns.resolver.NXDOMAIN:
            records[record_type] = 'No such domain'
        except Exception as e:
            records[record_type] = f"Error: {str(e)}"

    return records

domain = sys.argv[1]
dns_records = get_dns_records(domain)
print(dns_records)
