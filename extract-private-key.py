from web3 import Web3
import json

keystore_path = 'node1/data/keystore/UTC--2025-03-26T05-16-11.459661867Z--36be6f5d277f83242e22f716ab23e57e23797f5f'
password = "node1"

with open(keystore_path, 'r') as file:
    keystore_data = json.load(file)

web3 = Web3()

try:
    account = web3.eth.account.from_key(web3.eth.account.decrypt(keystore_data, password))
    print("Private Key:", account._private_key.hex())
except ValueError as e:
    print(f"Error decrypting keystore: {e}")