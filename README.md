# venmo-finance-dl

* Uses [finance-dl open source tool](https://github.com/jbms/finance-dl) to pull Venmo transactions/balances data into CSVs
* Sets passwords in keyring rather than cleartext

## Install

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```
venv/bin/finance-dl --config-module finance_dl_config --config venmo
```