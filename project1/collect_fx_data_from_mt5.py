
# Task 1: Initializing Connection with MetaTrader 5

# Import the MetaTrader5 package
import MetaTrader5 as mt5

# Step 1: Display MetaTrader5 Package Information
print("Task 1: Initializing Connection with MetaTrader 5")
print("--------------------------------------------------")
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# Step 2: Initialize the Connection
print("\nStep 2: Initialize the Connection")
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# Task 2: Connecting to Trading Accounts

# Step 3: Display MetaTrader 5 Version
print("\nTask 2: Connecting to Trading Accounts")
print("--------------------------------------------------")
print("Step 3: Display MetaTrader 5 Version")
print(mt5.version())

# Step 4: Connect to a Trading Account (No Password)
print("\nStep 4: Connect to a Trading Account (No Password)")
account = 17221085
authorized = mt5.login(account)
if authorized:
    print("Connected to account #{}".format(account))
else:
    print("Failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))

# Step 5: Connect to Another Trading Account (With Password)
print("\nStep 5: Connect to Another Trading Account (With Password)")
account = 25115284
authorized = mt5.login(account, password="gqrtz0lbdm")
if authorized:
    # Step 6: Display Trading Account Information
    print("Step 6: Display Trading Account Information 'as is'")
    print(mt5.account_info())

    # Step 7: Display Trading Account Information as a List
    print("\nStep 7: Display Trading Account Information as a List")
    account_info_dict = mt5.account_info()._asdict()
    for prop in account_info_dict:
        print("  {}={}".format(prop, account_info_dict[prop]))
else:
    print("Failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))

# Step 8: Shut Down the Connection
print("\nStep 8: Shut Down the Connection")
mt5.shutdown()

# Task 3: Collecting Historical Data

# Import necessary libraries
from datetime import datetime
import MetaTrader5 as mt5
import pandas as pd
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1500)
import pytz

# Step 9: Initialize the Connection to MetaTrader 5
print("\nTask 3: Collecting Historical Data")
print("--------------------------------------------------")
print("Step 9: Initialize the Connection to MetaTrader 5")

if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# Step 10: Set Time Zone to UTC
print("\nStep 10: Set Time Zone to UTC")
timezone = pytz.timezone("Etc/UTC")

# Step 11: Define Time Interval
print("\nStep 11: Define Time Interval")
utc_from = datetime(2020, 1, 10, tzinfo=timezone)
utc_to = datetime(2020, 1, 11, hour=13, tzinfo=timezone)

# Step 12: Get Historical Data
print("\nStep 12: Get Historical Data")
rates = mt5.copy_rates_range("USDJPY", mt5.TIMEFRAME_M5, utc_from, utc_to)

# Step 13: Shut Down the Connection
print("\nStep 13: Shut Down the Connection")
mt5.shutdown()

# Task 4: Displaying Historical Data

# Step 14: Display the First 10 Elements of the Data
print("\nTask 4: Displaying Historical Data")
print("--------------------------------------------------")
print("Step 14: Display the First 10 Elements of the Data")
counter = 0
for rate in rates:
    counter += 1
    if counter <= 10:
        print(rate)

# Step 15: Create a DataFrame
print("\nStep 15: Create a DataFrame")
rates_frame = pd.DataFrame(rates)

# Step 16: Convert Time to Datetime Format
print("\nStep 16: Convert Time to Datetime Format")
rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')

# Step 17: Display the DataFrame
print("\nStep 17: Display the DataFrame")
print(rates_frame.head(10))
