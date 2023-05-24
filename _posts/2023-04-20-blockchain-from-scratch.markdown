---
layout: post
title: "Creating a blockchain from scratch" 
date: 2023-04-20 08:46:26 +0800
categories: jekyll update
---

We will create a simple blockchain in Python3.

Blockchains have __ main parts:

Block
Chain
Miners
Consensus

Consensus - Mechanism that the miners use to determine which miner
gets to write data on the blockchain

Chain - Network where all blocks of data is stored by miners.

Block - Collection of data that is stored in one period of time. Each
block keeps track of its previous block. This property 

To create a blockhain, these parts must be created and integrated to create
a functioning blockchain.

## Demo chain

Let's call the blockchain that we will create `Demo Chain`. 

Demo chain can:

- Store data given by users into its chain
- Allow miners to connect and write on chain
- Reward miners 
- Make miners agree on which data is valid.

## Implementation

1. Start

Create a directory named `demo-chain`. Inside `demo-chain`, create a file
named `blockchain.py`.

```sh
$ mkdir demo-chain
$ touch demo-chain/blockchain.py
```

Open `blockchain.py` in a text editor.

2.  Creating objects

Let's start by creating objects of the blockchain.

- The `block` object

Each block stores the data that we want to store on the chain.
The block will be handled by all the miners in the chain.
The problem is how the block's data will remain intact.
The solution is to keep a hash of the blocks's data in the 
		

```python3
class Block:
	def __init__(self):
		pass
	
```




