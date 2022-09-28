#import required packages
from algosdk.constants import microalgos_to_algos_ratio
from algosdk.v2client import indexer

def myindexer():
    """Initialize and return an indexer"""

    algod_address = "https://testnet-algorand.api.purestake.io/idx2"

    algod_token = "o3UIhhhoqx6IRyNxrfBZg4EBsRhyOTQC58EM1XRw "

    headers = {
        "X-API-Key": algod_token,
    }

    return indexer.IndexerClient("", algod_address, headers)