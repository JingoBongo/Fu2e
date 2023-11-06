from vault_utils import Vault


class Butterfly:
    aboba = 10


volt = Vault('selectTestVault')
volt.put('test', 'string')
volt.put('test', 'updatedstring')

vol2 = Vault('newvolt')

volt.put('test2', Butterfly())
vol2.put('qwerqwerqwergqwegrqwegrqwersdfsdfgdfgvqwerqwerqwergqwegrqwegrqwersdfsdfgdfgvqwerqwerqwergqwegrqwegrqwersdfsdfgdfgvqwerqwerqwergqwegrqwegrqwersdfsdfgdfgvqwerqwerqwergqwegrqwegrqwersdfsdfgdfgv',1)
print(volt.get('test'))
print(volt.get('test2'))
print(vol2.get('qwerqwerqwergqwegrqwegrqwersdfsdfgdfgvqwerqwerqwergqwegrqwegrqwersdfsdfgdfgvqwerqwerqwergqwegrqwegrqwersdfsdfgdfgvqwerqwerqwergqwegrqwegrqwersdfsdfgdfgvqwerqwerqwergqwegrqwegrqwersdfsdfgdfgv'))
