# SmartConract_AlgodApp
## Introduction

Web3 technology is inherently about the user controlled internet. It is being achieved by a growing stack of decentralized technologies, such as blockchains, smart contracts, oracles, crypto wallets, storage networks, and more.

## Objective of the Project

This project tries to enable clients to be able to solve the challenges ensuring that certificates are available to all trainees in a secure way, and (if possible) that certificate holders can benefit from smart contract actions now and in the future. At present, certificates are distributed as simple PDF files, without the ability to verify their authenticity nor can trainer undertake smart actions with the trainees/their contracts.

## Install Sandbox

Algorand provides a docker instance for setting up a node, which can be used to get started developing quickly. To install and use this instance, follow these instructions.
git clone https://github.com/algorand/sandbox.git
cd sandbox
./sandbox up testnet

## Setup
In order to access the algorand network, the easiest way to get started is by creating an account at https://developer.purestake.io/login. The API keys referenced in this project (found in files indexer.py and algod.py) should be replaced with your own.
