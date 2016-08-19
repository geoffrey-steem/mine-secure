# steem-index
Computes the h-index equivelent for an account

Requires Python 3:

1) Either start steemd locally with --rpc-endpoint
and connect to it with cli wallet: `cli_wallet -r 127.0.0.1:8093`
or connect cli wallet to a public steemd client, e.g., `cli_wallet -s ws://steemit.com:8090 -r 127.0.0.1:8090 -s 127.0.0.1:8093` (See [this guide for help](https://steemit.com/steem/@steem-id/tutorial-how-to-use-cliwallet-without-downloading-complete-blockchain-on-windows-x64))
2) import your key into the wallet if it isn't there already: `new >>> set_password stuff`
`new >>> unlock stuff`
`new >>> import_key 5stuff`
3) In a fresh terminal window, `git clone http://github.com/geoffrey-steem/mine-secure.git`
4) `cd mine-secure`
5) `pip install -r requirements.py`
6) `python3 mine-secure.py [cli_wallet_ip] [cli_wallet_server_port]`
7) Follow the prompts, and WRITE DOWN your new owner key!
8) Backup your new `wallet.json`

Steem library created by [@Xeroc](http://steemit.com/@xeroc)
