import hashlib


nonce_limit = 1000000

zeros = 4

def mine(block_num, transactions, prev_hash):
    for nonce in range(nonce_limit):
        base_text = str(block_num) + transactions + prev_hash + str(nonce)
        hash_try = hashlib.sha256(base_text.encode()).hexdigest()
        if hash_try.startswith('0' * zeros):
            print(f"Found Hash With Nonce:{nonce}")
            return hash_try
    return - 1
    
block_num = 5
transactions = "687ta8s76dfg627"
prev_hash = "hd6s87fg6fiyaudfsg234re"
combined_text = str(5) + "687ta8s76dfg627" + "hd6s87fg6fiyaudfsg234re" + str(33477)

print(hashlib.sha256(combined_text.encode()).hexdigest())