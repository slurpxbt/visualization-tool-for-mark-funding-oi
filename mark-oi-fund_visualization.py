# whole market data visualization

# imports

import numpy as np
import datetime 
import matplotlib.pyplot as plt
# --------------------------------------------------

# ------------ data file paths
btc_data_path = "D:/files/Finance/trading/skripte/unfinished projects/visualization tool for oi-mark-funding/data storage/avgMark_cumOI_oiWfunding_storage.txt"
eth_data_path = "D:/files/Finance/trading/skripte/unfinished projects/visualization tool for oi-mark-funding/data storage/avgMark_cumOI_oiWfunding_storage_eth.txt"
# ---------------------------


# -----------------------BTC-----------------------------
with open(btc_data_path, "r") as btc_data:
    
    btc_lines = btc_data.read().split("\n")
    btc_lines.remove(btc_lines[-1])         # removes last line which is [""]
    btc_array_data = []

    for i in btc_lines:
        # btc_array_data = [mark_price, OI, funding, time]

        single_elements = i.split(";")  # array ["mark_price", "OI", "funding", "time"]
        temp = [round(float(single_elements[0]), 1), float(single_elements[1]), float(single_elements[2]), single_elements[3]]
        btc_array_data.append(temp)

    btc_data.close()



# -----------------------ETH-----------------------------
with open(eth_data_path, "r") as eth_data:

    eth_lines = eth_data.read().split("\n")
    eth_lines.remove(eth_lines[-1])         # removes last line which is [""]
    eth_array_data = []

    for i in eth_lines:
        # eth_array_data = [mark_price, OI, funding, time]

        single_elements = i.split(";")  # array ["mark_price", "OI", "funding", "time"]
        temp = [round(float(single_elements[0]), 1), float(single_elements[1]), float(single_elements[2]), single_elements[3]]
        eth_array_data.append(temp)
    eth_data.close()


# ---- BTC calcs -----
btc_net_oi_changes = []
btc_pct_oi_changes = []
btc_price_pct_changes = []

for i in range(len(btc_array_data)):

    net_oi_change = round(btc_array_data[i][1] - btc_array_data[i-1][1], 3)
    pct_oi_change = round((btc_array_data[i][1] / btc_array_data[i-1][1] - 1) * 100, 3)
    price_pct_change = round((btc_array_data[i][0] / btc_array_data[i-1][0] - 1) * 100, 3)

    btc_net_oi_changes.append(net_oi_change)
    btc_pct_oi_changes.append(pct_oi_change)
    btc_price_pct_changes.append(price_pct_change)



btc_net_oi_changes[0] = btc_net_oi_changes[1]           
btc_pct_oi_changes[0] = btc_pct_oi_changes[1]           
btc_price_pct_changes[0] = btc_price_pct_changes[1]     


# ---- ETH calcs ----

eth_net_oi_changes = []
eth_pct_oi_changes = []
eth_price_pct_changes = []

for i in range(len(eth_array_data)):

    net_oi_change = round(eth_array_data[i][1] - eth_array_data[i-1][1], 3)
    pct_oi_change = round((eth_array_data[i][1] / eth_array_data[i-1][1] - 1) * 100, 3)
    price_pct_change = round((eth_array_data[i][0] / eth_array_data[i-1][0] - 1) * 100, 3)

    eth_net_oi_changes.append(net_oi_change)
    eth_pct_oi_changes.append(pct_oi_change)
    eth_price_pct_changes.append(price_pct_change)



eth_net_oi_changes[0] = eth_net_oi_changes[1]           
eth_pct_oi_changes[0] = eth_pct_oi_changes[1]          
eth_price_pct_changes[0] = eth_price_pct_changes[1]     


# ------------- whole market positions

# Open interest of whole btc and eth market combine = WholeMkt_OI
# funding of the whole market btc and eth combined = wholeMkt_OIw_funding   => how leveraged is market
# percentage and net OI changes of whole market

wholeMkt_OIw_funding = []
wholeMkT_OI = []

for i in range(len(btc_array_data)):

    oi = round(btc_array_data[i][1] + eth_array_data[i][1], 3)
    OIw_fund = round((btc_array_data[i][1]*btc_array_data[i][2] + eth_array_data[i][1]*eth_array_data[i][2]) / oi, 3)
    
    wholeMkt_OIw_funding.append(OIw_fund)
    wholeMkT_OI.append(oi)



whole_Mkt_net_oi_changes = []
whole_Mkt_pct_oi_changes = []

for i in range(len(eth_array_data)):

    net_oi_change = round(wholeMkT_OI[i] - wholeMkT_OI[i-1], 3)
    pct_oi_change = round((wholeMkT_OI[i] / wholeMkT_OI[i-1] - 1) * 100, 3)

    whole_Mkt_net_oi_changes.append(net_oi_change)
    whole_Mkt_pct_oi_changes.append(pct_oi_change)



whole_Mkt_net_oi_changes[0] = whole_Mkt_net_oi_changes[1]   # foor loops uses last value from array so 1st value is completely wrong that's why I replace it with most logic one
whole_Mkt_pct_oi_changes[0] = whole_Mkt_pct_oi_changes[1]   # foor loops uses last value from array so 1st value is completely wrong that's why I replace it with most logic one




# ---------------------print outs -------------------------------------

#for i in range(len(btc_array_data)):
    #print(btc_net_oi_changes[i], " btc net oi", i)
    #print(btc_pct_oi_changes[i], " btc pct oi", i)
    #print(eth_net_oi_changes[i], " eth net oi", i)
    #print(eth_pct_oi_changes[i], " eth pct oi", i)
    #print(wholeMkT_OI[i], " whole oi", i)
    #print(wholeMkt_OIw_funding[i], " whole mkt funding", i)
    #print(whole_Mkt_net_oi_changes[i], " whole net oi", i)
    #print(whole_Mkt_pct_oi_changes[i], " whole pct oi", i)




# ---------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------- PLOTING ---------------------------------------------------------------------------------------

# BTC --------------------------------


fig = plt.figure()

btc_price_graph = fig.add_subplot(6, 1, 1)
btc_oi_graph = fig.add_subplot(6, 1, 2)
btc_total_oi_chg_graph = fig.add_subplot(6, 1, 3)
btc_pct_oi_cgh_graph = fig.add_subplot(6, 1, 4)
btc_pct_price_chg_graph = fig.add_subplot(6, 1, 5)
btc_funding_graph = fig.add_subplot(6, 1, 6)

btc_price_data = [i[0] for i in btc_array_data]
btc_price_graph.plot(btc_price_data)
btc_price_graph.set_ylabel("price")

btc_oi_data = [i[1] for i in btc_array_data]
btc_oi_graph.plot(btc_oi_data)
btc_oi_graph.set_ylabel("net oi")

btc_total_oi_chg_data = [i for i in btc_net_oi_changes]
btc_total_oi_chg_graph.plot(btc_total_oi_chg_data)
btc_total_oi_chg_graph.set_ylabel("net oi change")

btc_pct_oi_cgh_data = [i for i in btc_pct_oi_changes]
btc_pct_oi_cgh_graph.plot(btc_pct_oi_cgh_data)
btc_pct_oi_cgh_graph.set_ylabel("pct oi change")

btc_pct_price_chg_data = [i for i in btc_price_pct_changes]
btc_pct_price_chg_graph.plot(btc_pct_price_chg_data)
btc_pct_price_chg_graph.set_ylabel("pct price change")


btc_funding_data = [i[2] for i in btc_array_data]
btc_funding_graph.plot(btc_funding_data)
btc_funding_graph.set_ylabel("funding")

plt.show()

# ------------------------------------

# ETH --------------------------------



fig = plt.figure()

eth_price_graph = fig.add_subplot(6, 1, 1)
eth_oi_graph = fig.add_subplot(6, 1, 2)
eth_total_oi_chg_graph = fig.add_subplot(6, 1, 3)
eth_pct_oi_cgh_graph = fig.add_subplot(6, 1, 4)
eth_pct_price_chg_graph = fig.add_subplot(6, 1, 5)
eth_funding_graph = fig.add_subplot(6, 1, 6)

eth_price_data = [i[0] for i in eth_array_data]
eth_price_graph.plot(eth_price_data)
eth_price_graph.set_ylabel("price")

eth_oi_data = [i[1] for i in eth_array_data]
eth_oi_graph.plot(eth_oi_data)
eth_oi_graph.set_ylabel("net oi")

eth_total_oi_chg_data = [i for i in eth_net_oi_changes]
eth_total_oi_chg_graph.plot(eth_total_oi_chg_data)
eth_total_oi_chg_graph.set_ylabel("net oi change")

eth_pct_oi_cgh_data = [i for i in eth_pct_oi_changes]
eth_pct_oi_cgh_graph.plot(eth_pct_oi_cgh_data)
eth_pct_oi_cgh_graph.set_ylabel("pct oi change")

eth_pct_price_chg_data = [i for i in eth_price_pct_changes]
eth_pct_price_chg_graph.plot(eth_pct_price_chg_data)
eth_pct_price_chg_graph.set_ylabel("pct price change")


eth_funding_data = [i[2] for i in eth_array_data]
eth_funding_graph.plot(eth_funding_data)
eth_funding_graph.set_ylabel("funding")

plt.show()

# WHOLE MARKET DATA ------------------

fig = plt.figure()

Wmkt_oi_graph = fig.add_subplot(4, 1, 1)
Wmkt_funding_graph = fig.add_subplot(4, 1, 2)
Wmkt_net_oi_chg_graph = fig.add_subplot(4, 1, 3)
Wmkt_pct_oi_chg_graph = fig.add_subplot(4, 1, 4)


Wmkt_oi_data = [i for i in wholeMkT_OI]
Wmkt_oi_graph.plot(Wmkt_oi_data)
Wmkt_oi_graph.set_ylabel("whole market OI")

Wmkt_funding_data = [i for i in wholeMkt_OIw_funding]
Wmkt_funding_graph.plot(Wmkt_funding_data)
Wmkt_funding_graph.set_ylabel("Whole market funding")

Wmkt_net_oi_chg_data = [i for i in whole_Mkt_net_oi_changes]
Wmkt_net_oi_chg_graph.plot(Wmkt_net_oi_chg_data)
Wmkt_net_oi_chg_graph.set_ylabel("Net OI changes")

Wmkt_pct_oi_chg_data = [i for i in whole_Mkt_pct_oi_changes]
Wmkt_pct_oi_chg_graph.plot(Wmkt_pct_oi_chg_data)
Wmkt_pct_oi_chg_graph.set_ylabel("Pct OI changes")

plt.show()
# ----------------------------------------------------------------------------------------------------------------------------------------
