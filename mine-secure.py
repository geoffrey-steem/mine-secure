# Author: @geoffrey [http://steemit.com/@geoffrey]
# Date: August 19th, 2016

from steemapi.steemwalletrpc import SteemWalletRPC
import sys

if len(sys.argv) == 3:
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    ip = "localhost"
    port = 8093
    
rpc = SteemWalletRPC(ip,port)

try:
    account_names = [acct['name'] for acct in rpc.list_my_accounts()]
    account_keys = rpc.list_keys()

    new_owner_key = rpc.suggest_brain_key()
    new_active_key = account_keys[0]
    new_posting_key = rpc.suggest_brain_key()
    new_memo_key = rpc.suggest_brain_key()

    print('\nThe following accounts will have their keys updated: \n')
    print("\n".join(account_names))
    print('\nYour new OWNER key will be (write this down): ' + new_owner_key['wif_priv_key'])
    print('Your brain key is (write this down): ' + new_owner_key['brain_priv_key'] + '\n')
    ready_prompt = input('Have you written your new owner key down?  Are you ready to reset all of your account keys? y/n: ')
    
    modify_active = input('Your accounts may have different active keys, would you like to reset them all to ' + new_active_key[1] + '? y/n: ')
    modify_active = 'y'
    
    import_prompt = input('\nImport new OWNER key into wallet? [y]/n : ')
    if import_prompt == 'y':
        rpc.import_key(new_owner_key['wif_priv_key'])
        
    if ready_prompt == 'y':
        real_run = 'true'
    else:
        real_run = 'false'
        print('Updated keys will not be broadcast!  This is just a test run.')

    if modify_active == 'y':
        print('\nOwner: ' + new_owner_key['wif_priv_key'] + '\nActive (used for mining): ' + new_active_key[1])
        print('Posting (used to login to steemit.com): ' + new_posting_key['wif_priv_key'] + '\nMemo: ' + new_memo_key['wif_priv_key'])
    else:
        print('\nOwner: ' + new_owner_key['wif_priv_key'] + '\nActive (used for mining): Unmodified')
        print('Posting (used to login to steemit.com): ' + new_posting_key['wif_priv_key'] + '\nMemo: ' + new_memo_key['wif_priv_key'])

    ready_prompt = input('\n Wrote all that down?  Ready for real? y/n:')
    
    if ready_prompt == 'y':
        real_run = 'true'
    else:
        real_run = 'false'
        print('Updated keys will not be broadcast!  This is just a test run.')

      
    if modify_active == 'y':
        for acct in account_names:
            rpc.update_account(acct,"",new_owner_key['pub_key'],new_active_key[0],new_posting_key['pub_key'],new_memo_key['pub_key'],real_run)
    else:
        for acct in account_names:
            rpc.update_account(acct,"",new_owner_key['pub_key'],"",new_posting_key['pub_key'],new_memo_key['pub_key'],real_run)
    
        
    print('Beginning process...')

    print('Completed process!  Your new PRIVATE keys for all listed accounts are: \n')
    print('\nRemember, don\'t store these publically, and don\'t share them with anyone!\nHave a great rest of your day!')
        
except:
    print('Is cli_wallet running with `cli_wallet -r ' +  ip + ':' + str(port) + '`?  And is it unlocked?')