'''
Site oficial da blockchain:
https://www.blockchain.com/pt/explorer

Algumas informações aplicadas nas variaveis foram retiradas deste Bloco: #703758
https://www.blockchain.com/btc/block/0000000000000000000ce40d3d2412203f38aed7a0281332835df0c5e0c37029

Algoritmo afim de estudo somente.
'''

from hashlib import sha256
from time import time


def apply_sha256(text):
    return sha256(text.encode('ascii')).hexdigest()


def mine(block_number, transactions, previous_hash, zero_amount):
    nounce = 0

    while True:
        text = str(block_number) + transactions + previous_hash + str(nounce)
        hash = apply_sha256(text)

        if hash.startswith('0' * zero_amount):
            return nounce, hash
        nounce += 1


if __name__ == '__main__':
    block_number = 703758
    transactions = '''
                    John->Robert->10
                    Mary->Mark->15
                    Bryan->Julie->24
                    '''
    zero_amount = 4  # Se sua máquina não for para minerar, não coloque um número muito alto. Algoritmo afins de estudo somente.
    previous_hash = '77a888815e48c92f568c55b50f1e17254725a204ac05363157e981b0f8793034'
    begin = time()
    result = mine(block_number, transactions, previous_hash, zero_amount)

    print(result)
    print(f'{time() - begin:.2f}')
