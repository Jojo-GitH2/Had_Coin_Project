from flask import Flask, jsonify
from blockchain import Blockchain

# Part 2 - Mining our Blockchain
# Create a Web App
app = Flask(__name__)

# Create a Blockchain

blockchain = Blockchain()


# Mining a new block
@app.route("/mine_block", methods=["GET"])
def mine_block():
    previous_block = blockchain.get_previous_block()  # Get the previous block
    previous_proof = previous_block["proof"]  # Get the proof of the previous block
    proof = blockchain.proof_of_work(
        previous_proof
    )  # Find the proof of work for the new block
    previous_hash = blockchain.hash(
        previous_block
    )  # Get the hash of the previous block
    block = blockchain.create_block(proof, previous_hash)  # Create the new block
    response = {
        "message": "Congratulations, you just mined a block!",
        "index": block["index"],
        "timestamp": block["timestamp"],
        "proof": block["proof"],
        "previous_hash": block["previous_hash"],
    }
    return jsonify(response), 200


# Get the full blockchain
@app.route("/get_chain", methods=["GET"])
def get_chain():
    response = {"chain": blockchain.chain, "length": len(blockchain.chain)}
    return jsonify(response), 200


# Check if the blockchain is valid
@app.route("/is_valid", methods=["GET"])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    # print(blockchain.chain)
    if is_valid:
        response = {"message": "The blockchain is valid."}
    else:
        response = {"message": "The blockchain is not valid."}

    return jsonify(response), 200


# Running the app

app.config["DEBUG"] = True
app.run(host="0.0.0.0", port=5000)
