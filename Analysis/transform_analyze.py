import pandas as pd
metrics['avg_3yr_roe'] = float(pd.Series(roe[-3:]).mean())
else:
metrics['avg_3yr_roe'] = None


# 3. Debt-to-equity or debt presence
total_debt = bs.get('total_debt')
equity = bs.get('shareholders_equity')
if total_debt is not None and equity:
        try:
    metrics['debt_equity'] = float(total_debt) / float(equity)
        except Exception:
    metrics['debt_equity'] = None
# 4. Dividend payout ratio
metrics['dividend_payout'] = pnl.get('dividend_payout_ratio') if pnl.get('dividend_payout_ratio') is not None else None


# 5. Profit growth (last year or rolling average)
profit = pnl.get('net_profit', [])
    if len(profit) >= 2 and profit[-2]:
        metrics['last_year_profit_growth'] = float((profit[-1] - profit[-2]) / abs(profit[-2]) * 100)
    else:
        metrics['last_year_profit_growth'] = None


    return metrics




def select_pros_cons(metrics, max_select=3):
    pros = []
    cons = []


# Rules derived from project spec
# PROS: values > 10% or favorable thresholds
if metrics.get('debt_equity') is not None and metrics['debt_equity'] < 0.2:
    pros.append('Company is almost debt-free.')
if metrics.get('debt_equity') is not None and metrics['debt_equity'] < 1.0 and metrics['debt_equity'] < 0.8:
    pros.append('Company has reduced debt.')
if metrics.get('avg_3yr_roe') is not None and metrics['avg_3yr_roe'] >= 10:
    pros.append(f"Company has a good return on equity (ROE) track record: 3 Years ROE {metrics['avg_3yr_roe']:.2f}%")
if metrics.get('dividend_payout') is not None and metrics['dividend_payout'] >= 30:
    pros.append(f"Company has been maintaining a healthy dividend payout of {metrics['dividend_payout']:.1f}%")
if metrics.get('last_year_profit_growth') is not None and metrics['last_year_profit_growth'] >= 10:
    pros.append(f"Company has delivered good profit growth of {metrics['last_year_profit_growth']:.1f}%")
if metrics.get('median_sales_growth') is not None and metrics['median_sales_growth'] >= 10:
    pros.append(f"Company's median sales growth is {metrics['median_sales_growth']:.1f}% of last 10 years")


# CONS: values < 10% or unfavorable thresholds
if metrics.get('median_sales_growth') is not None and metrics['median_sales_growth'] < 10:
    cons.append(f"The company has delivered a poor sales growth of {metrics['median_sales_growth']:.1f}% over past period.")
if metrics.get('dividend_payout') is None or (metrics.get('dividend_payout') is not None and metrics['dividend_payout'] < 1):
    cons.append('Company is not paying out dividend.')
if metrics.get('avg_3yr_roe') is not None and metrics['avg_3yr_roe'] < 10:
    cons.append(f"Company has a low return on equity of {metrics['avg_3yr_roe']:.2f}% over last 3 years.")
if metrics.get('last_year_profit_growth') is not None and metrics['last_year_profit_growth'] < 0:
    cons.append(f"Company posted negative profit growth last year: {metrics['last_year_profit_growth']:.1f}%")


# Deduplicate and slice to limits
pros = list(dict.fromkeys(pros))[:max_select]
cons = list(dict.fromkeys(cons))[:max_select]


return pros, cons