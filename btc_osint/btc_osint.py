import blockcypher
import sys

def fetch_wallet_transactions(wallet_address):
    transactions = blockcypher.get_address_full(wallet_address)
    return transactions

def analyze_transactions(transactions, wallet_address):
    incoming = []
    outgoing = []

    for tx in transactions['txs']:
        inputs = tx['inputs']
        outputs = tx['outputs']

        for inp in inputs:
            if 'addresses' in inp and wallet_address in inp['addresses']:
                outgoing.append(tx)

        for out in outputs:
            if 'addresses' in out and wallet_address in out['addresses']:
                incoming.append(tx)

    return incoming, outgoing

def detect_fraud(incoming, outgoing):

    fraud_indicators = []

    for tx in incoming:
        if tx['total'] > 1e8:  
            fraud_indicators.append(f"Large incoming transaction: {tx['hash']}")

    for tx in outgoing:
        if tx['total'] > 1e8:  
            fraud_indicators.append(f"Large outgoing transaction: {tx['hash']}")

    return fraud_indicators

def summarize_transactions(transactions, tx_type):
    print(f"\nSummary of {tx_type} transactions:")
    for tx in transactions:
        print(f"Transaction Hash: {tx['hash']}")
        print(f"Total Amount: {tx['total'] / 1e8} BTC")
        print(f"Confirmations: {tx['confirmations']}")
        print(f"Received Time: {tx['received']}")
        print(f"Inputs:")
        for inp in tx['inputs']:
            print(f"  - Address: {inp.get('addresses', ['N/A'])[0]}")
            print(f"  - Output Value: {inp.get('output_value', 'N/A') / 1e8} BTC")
        print(f"Outputs:")
        for out in tx['outputs']:
            print(f"  - Address: {out.get('addresses', ['N/A'])[0]}")
            print(f"  - Value: {out.get('value', 'N/A') / 1e8} BTC")
        print("\n")


wallet_address =  sys.argv[1]
transactions = fetch_wallet_transactions(wallet_address)
incoming, outgoing = analyze_transactions(transactions, wallet_address)
fraud_indicators = detect_fraud(incoming, outgoing)
summarize_transactions(incoming, 'Incoming')
summarize_transactions(outgoing, 'Outgoing')
print("Fraud Indicators:")
for indicator in fraud_indicators:
    print(indicator)
