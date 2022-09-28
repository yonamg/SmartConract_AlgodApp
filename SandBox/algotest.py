from algosdk import account, mnemonic

def generate_algorand_keypair():

    private_key,address=account.generate_account()

    print("my Addresse:{}".format(address))

    print("My Private Key:{}".format(private_key))

    print("my Passphrase:{}".format(mnemonic.from_private_key(private_key)))


generate_algorand_keypair()

