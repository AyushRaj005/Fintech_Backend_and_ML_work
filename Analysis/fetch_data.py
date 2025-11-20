import requests
from config import API_BASE, API_KEY, REQUEST_TIMEOUT


def fetch_company(company_id): 
    params = {'id': company_id, 'api_key': API_KEY}
    resp = requests.get(API_BASE, params=params, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    data = resp.json()
    # Basic validation
    if not any(k in data for k in ('balance_sheet','pnl','cash_flow')): raise ValueError('Missing financial statements for {}'.format(company_id))
    return data


if __name__ == '__main__':
    import sys
    cid = sys.argv[1]
    print(fetch_company(cid))