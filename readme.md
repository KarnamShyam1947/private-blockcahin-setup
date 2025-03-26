# Private Ethereum Blockchain Setup

This repository provides the steps to set up a private Ethereum blockchain using Geth. Follow the instructions to create and configure nodes, a bootnode, and the genesis file to start a private Ethereum network.

## Introduction

### Why Set Up a Private Ethereum Chain?

A private Ethereum blockchain is ideal for:

- Testing smart contracts or dApps in a controlled environment.
- Experimenting with Ethereum configurations without interacting with the public network.
- Implementing permissioned blockchain solutions for businesses.
- Learning Ethereum in a safe and isolated network.

This setup will give you complete control over the blockchain, including who can join and who can mine on it.

### Why Geth?

Geth (Go Ethereum) is the most popular client for running an Ethereum node. It is widely supported, reliable, and feature-rich. It allows you to:

- Create private networks for testing and development.
- Run Ethereum nodes and interact with the network.
- Mine and validate transactions on your private chain.

## Tools Required

Before you begin, ensure that you have the following tools installed:

1. **Geth** (version <= 1.13.15)  
   You can download Geth from [here](https://geth.ethereum.org/downloads/).
   
2. **Bootnode**  
   You can download Bootnode from [here](https://github.com/ethereum/go-ethereum/wiki/Bootnode).

## Setup Steps

### 1. Create Folders for Node Data

To organize your Ethereum node data, create directories for each node and the bootnode:

```bash
mkdir -p node1 node2 boot-node
```

### 2. Create New Accounts for Nodes

Generate new Ethereum accounts for your nodes. Make sure to store the account address and password securely for future use.

```bash
geth --datadir ./node1/data account new
geth --datadir ./node2/data account new
```

### 3. Create the Genesis File (`genesis.json`)

The `genesis.json` file is required to define the initial state of the blockchain. You need to add the account info generated in step 2 into this file.

Example of a `genesis.json` file:

```json
{
    "config": {
        "chainId": 98765,
        "homesteadBlock": 0,
        "eip150Block": 0,
        "eip155Block": 0,
        "eip158Block": 0,
        "byzantiumBlock": 0,
        "constantinopleBlock": 0,
        "petersburgBlock": 0,
        "istanbulBlock": 0,
        "muirGlacierBlock": 0,
        "berlinBlock": 0,
        "londonBlock": 0
    },
    "difficulty": "0x20000",
    "gasLimit": "0x8000000",
    "alloc": {
        "0x74aBc0b0790561F810EdfD5b32Ed9748AfaA0e4c": {
            "balance": "10000000000000000000000000"
        }
    }
}
```

### 4. Initialize the Nodes

Initialize each node with the `genesis.json` file. This step sets up the blockchain configuration on each node.

```bash
geth --datadir ./node1/data init genesis.json
geth --datadir ./node2/data init genesis.json
```

### 5. Generate Key for Bootnode

Bootnodes are used to bootstrap the network. You need to generate a key for the bootnode:

```bash
bootnode -genkey boot.key
```

### 6. Start the Bootnode

Start the bootnode with the generated key. The bootnode helps in discovering other nodes on the network.

```bash
bootnode -nodekey boot.key -verbosity 7 -addr "0.0.0.0:30301"
```

### 7. Export Environment Variables

To allow the unlocking of accounts, export the following environment variable:

#### On Linux/macOS:

```bash
export GETH_ALLOW_INSECURE_UNLOCK=true
```

#### On Windows:

On Windows, environment variables are set differently:

1. Open **Command Prompt** or **PowerShell**.
2. Run the following command to set the environment variable temporarily for the current session:

   ```bash
   set GETH_ALLOW_INSECURE_UNLOCK=true
   ```

   This will allow the node to unlock accounts. If you want to set the variable permanently, you can do so through the **Environment Variables** section in **System Properties** (Control Panel > System and Security > System > Advanced System Settings > Environment Variables).

### 8. Start the Nodes

Start the Ethereum nodes and connect them to the bootnode to join the network. Make sure to replace the bootnode enode URL with your own.

```bash
geth \
    --datadir node1 \
    --port 30304 \
    --bootnodes enode://716ab29f4a94f4c096ca79cb0ba2272360240caef81f327e3cb49af9c696b20eb80c4f1c5c24aa1e0cde4e1d888dd6228a761e1773e32e496c975e8e7833f106@127.0.0.1:0?discport=30301 \
    --authrpc.port 8547 \
    --ipcdisable \
    --http \
    --http.addr 0.0.0.0 \
    --http.crossdomain="*" \
    --http.api web3,eth,debug,personal,net \
    --networkid 98765 \
    --unlock 0x74aBc0b0790561F810EdfD5b32Ed9748AfaA0e4c \
    --password pswd.txt \
    --mine \
    --miner.etherbase=0x74aBc0b0790561F810EdfD5b32Ed9748AfaA0e4c
```

### 9. Repeat for Other Nodes

You can repeat the above steps to start additional nodes like `node2`, connecting them to the bootnode for synchronization.

---

## Conclusion

You now have a fully functional private Ethereum network running with multiple nodes. You can interact with the network, deploy smart contracts, and test your dApps in a private, isolated environment.

For further information or issues, feel free to open an issue on this repository.
