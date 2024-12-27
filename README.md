# Time Lock on Bitcoin
A time lock mechanism for Bitcoin that allows you to lock funds on the Bitcoin blockchain for a specified period. This project provides a smart way to control the release of funds by making them unavailable until a certain block height or timestamp is reached.

## Features
Time Lock: Lock Bitcoin transactions until a certain block height or a specific time.

Secure: Uses Bitcoin’s OP_CHECKLOCKTIMEVERIFY (CLTV) to implement the time lock feature.

Simple to Use: Provides an easy-to-use library for creating and verifying time-locked Bitcoin transactions.

Flexible: Supports both block height and timestamp-based locks.

## How It Works
Bitcoin's OP_CHECKLOCKTIMEVERIFY (CLTV) is a script opcode that allows you to specify the earliest time (or block height) at which a transaction can be included in a block. If the conditions are not met, the transaction is invalid and cannot be included in the blockchain.

This project provides tools to create time-locked transactions using CLTV and also helps to verify whether a transaction can be spent based on the current block height or timestamp.

## Usage
### 1. Creating a Time-Locked Transaction
You can create a time-locked Bitcoin transaction using either a specific block height or a timestamp.

Example: Lock Until Block Height
```
import { Transaction, Input, Output } from 'bitcoinjs-lib';

// Example to lock Bitcoin until a certain block height
const lockBlockHeight = 680000;  // Replace with the desired block height

// Create a new transaction
const tx = new Transaction();

// Add an input (the UTXO you want to spend)
tx.addInput('your-previous-txid', 0);

// Add an output (where the funds will go)
tx.addOutput('recipient-address', 0.1);

// Add the time lock condition (lock until block height)
tx.ins[0].bip32Derivation = [{ pubkey: Buffer.from('your-public-key'), masterFingerprint: Buffer.from('fingerprint') }];
tx.addLocktime(lockBlockHeight);

const txHex = tx.toHex();
console.log(`Transaction Hex: ${txHex}`);

```
Example: Lock Until Specific Time
```
import { Transaction } from 'bitcoinjs-lib';

// Example to lock Bitcoin until a specific timestamp
const lockTime = Math.floor(new Date('2024-12-31T00:00:00Z').getTime() / 1000);  // Unix timestamp

// Create a new transaction
const tx = new Transaction();

// Add an input (the UTXO you want to spend)
tx.addInput('your-previous-txid', 0);

// Add an output (where the funds will go)
tx.addOutput('recipient-address', 0.1);

// Add the time lock condition (lock until timestamp)
tx.locktime = lockTime;

const txHex = tx.toHex();
console.log(`Transaction Hex: ${txHex}`);
```

### 2. Verifying a Time-Locked Transaction
To check if a time-locked transaction can be spent, you can verify the current block height or timestamp.
```
import axios from 'axios';

const checkIfCanSpend = async (lockHeight: number, lockTime: number) => {
  // Fetch the current block height and timestamp
  const blockData = await axios.get('https://blockchain.info/q/getblockcount');
  const currentBlockHeight = blockData.data;
  const currentTimestamp = Math.floor(Date.now() / 1000);

  if (currentBlockHeight >= lockHeight) {
    console.log("Transaction can be spent (block height reached).");
  } else if (currentTimestamp >= lockTime) {
    console.log("Transaction can be spent (timestamp reached).");
  } else {
    console.log("Transaction is still locked.");
  }
};

checkIfCanSpend(680000, Math.floor(new Date('2024-12-31T00:00:00Z').getTime() / 1000));
```

## Contributing
Contributions are welcome! If you have suggestions, bug fixes, or new features, feel free to fork the repo and create a pull request.

### Connect With Me:

[![Mail Badge](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:nikolic.miloje0507@gmail.com)
[![Telegram Badge](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/mylord1_1)
[![Skype Badge](https://img.shields.io/badge/Skype-00AFF0?style=for-the-badge&logo=skype&logoColor=white)](https://join.skype.com/ubWuVGchDEnU)
[![Discord Badge](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/users/509337382810550280)
