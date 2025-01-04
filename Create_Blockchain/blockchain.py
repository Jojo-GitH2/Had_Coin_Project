#  Create a blockhain using python
import datetime
import hashlib
import json
from flask import Flask, jsonify

# Part 1 - Building a Blockchain

# Create a class for the blockchain
class Blockchain:
    # Initialize the blockchain with a chain and create the genesis block
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash="0") # Genesis block, proof means the proof of work, previous_hash is the hash of the previous block

    # Create a block with the proof of work and the previous hash
    def create_block(self, proof, previous_hash):
        block = {
            "index": len(self.chain) + 1,
            "timestamp": str(datetime.datetime.now()),
            "proof": proof,
            "previous_hash": previous_hash
        }
        self.chain.append(block)
        return block
    
    # Get the previous block
    def get_previous_block(self):
        return self.chain[-1]
    
    # Find the proof of work by trying different values until the hash has 4 leading zeros
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest() # The operation is arbitrary, can be any operation
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    # Get the hash of a block by encoding it and hashing it. This is used to check the integrity of the blockchain
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    # Check if the blockchain is valid by checking the proof of work and the hash of the previous block
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            # Check that for each block the previous hash is the hash of the previous block
            block = chain[block_index]
            if block["previous_hash"] != self.hash(previous_block):
                return False # The blockchain is invalid
            
            # Check if the proof of work is correct
            previous_proof = previous_block["proof"]
            proof = block["proof"]
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False # The blockchain is invalid
            previous_block = block
            block_index += 1
        return True
    



