```bash
geth --datadir=node1 init genesis.json
geth --datadir=node2 init genesis.json
geth --datadir=node3 init genesis.json
```


geth \
    --datadir=node1 \
    --networkid 8765 \
    --port 30303 \
    --rpc \
    --rpcport 3030 
    --http \
    --http.port 8545 \
    --http.api eth,web3,personal,net \
    --allow-insecure-unlock \
    --http.corsdomain "*" \
    --mine \
    --miner.threads=1 \
    --unlock "0" \
    --password node1/password.txt

geth --datadir=node1 --networkid 8765 --allow-insecure-unlock --rpc --rpcport 30303 console

To deploy contracts using a specific account in Geth, you will need the **private key** of the account. Here's how to get the private key of the account created on `node1`:

### Step 1: Locate the Account in `node1`

When you create an account with `geth account new --datadir=node1`, it generates a **keystore file** for that account. This file is stored in the `keystore` directory inside your `datadir` (in this case, `node1`).

### Step 2: Find the Keystore File

1. **Navigate to the `node1` directory**:

   ```bash
   cd private-blockchain/node1
   ```

2. **Locate the `keystore` directory**:

   The keystore files are stored in the `keystore` folder within the `datadir` (the `node1` directory).

   ```bash
   ls node1/keystore/
   ```

   You'll see files like:

   ```
   UTC--<timestamp>--<account_address>
   ```

   For example:

   ```
   UTC--2023-03-25T12-34-56.789Z--f82a6f5316bb042f2e2b5b44b26f246d0bcb49f0
   ```

   This file is the **encrypted file** containing your account's private key.

### Step 3: Extract the Private Key

To extract the private key, you will need to decrypt the keystore file using the **password** you set when you created the account. You can do this using `geth` with the following command:

1. **Run the `geth` console**:

   ```bash
   geth --datadir=node1 console
   ```

   This will start a Geth console where you can interact with your Ethereum node.

2. **Unlock the Account**:

   In the Geth console, unlock the account by providing the password. Assuming your account address is `0x<your_account_address>`, run:

   ```javascript
   personal.unlockAccount("0x<your_account_address>", "yourpassword", 15000)
   ```

   - Replace `0x<your_account_address>` with the actual Ethereum address.
   - Replace `yourpassword` with the password you created for the account.

   This will unlock the account for 15 seconds (you can adjust the time as needed).

3. **Export the Private Key**:

   After unlocking the account, you can get the private key by running the following command:

   ```javascript
   eth.accounts[0]
   ```

   This will show the account details, including the private key, in the following format:

   ```
   0x<your_account_address>
   ```

   While the above command does not show the private key directly, you can run the following command to extract the private key if you still need it:

   ```javascript
   personal.exportRawKey("0x<your_account_address>", "yourpassword")
   ```

   This will return the **private key** of your account. It will look like this:

   ```
   0x<your_private_key>
   ```

   **Important**: Keep this private key safe. If someone gains access to it, they can control your account.

### Step 4: Use the Private Key to Deploy Contracts with Hardhat

Once you have the private key, you can use it to deploy contracts using Hardhat. In your Hardhat configuration (`hardhat.config.js`), add the private key to the network configuration as follows:

```javascript
require("@nomiclabs/hardhat-ethers");

module.exports = {
  solidity: "0.8.0",
  networks: {
    private: {
      url: "http://localhost:8545",
      accounts: ["<your_private_key>"]
    }
  }
};
```

Replace `<your_private_key>` with the private key you just retrieved.

---

### Security Note:
- **Never expose your private key** in public or share it in unsecured environments.
- Consider using environment variables to securely store private keys, especially when working in a development environment or deploying to production. For example:

```javascript
accounts: [process.env.PRIVATE_KEY]
```

And set your private key in an `.env` file like this:

```bash
PRIVATE_KEY=your_private_key_here
```

Let me know if you need further assistance!