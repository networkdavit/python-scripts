#first run pip install dnspython or pip3 install dnspython

import re
import dns.resolver

def validate_email_syntax(email):
    email_regex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    return bool(email_regex.match(email))

def validate_domain(domain):
    try:
        dns.resolver.resolve(domain, 'A')
        return True
    except dns.resolver.NoAnswer:
        return False
    except dns.resolver.NXDOMAIN:
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def validate_mx_record(domain):
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        return len(mx_records) > 0
    except dns.resolver.NoAnswer:
        return False
    except dns.resolver.NXDOMAIN:
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def validate_email(email):
    if not validate_email_syntax(email):
        return False, "Invalid email syntax"

    domain = email.split('@')[1]

    if not validate_domain(domain):
        return False, "Domain does not exist"

    if not validate_mx_record(domain):
        return False, "No MX record found for domain"

    return True, "Email is valid"

email = "example@example.com"
is_valid, message = validate_email(email)
print(f"Is the email '{email}' valid? {is_valid} - {message}")
