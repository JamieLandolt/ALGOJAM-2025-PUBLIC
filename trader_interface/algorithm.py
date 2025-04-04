import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Custom trading Algorithm
class Algorithm():

    ########################################################
    # NO EDITS REQUIRED TO THESE FUNCTIONS
    ########################################################
    # FUNCTION TO SETUP ALGORITHM CLASS
    def __init__(self, positions):
        # Initialise data stores:
        # Historical data of all instruments
        self.data = {}
        # Initialise position limits
        self.positionLimits = {}
        # Initialise the current day as 0
        self.day = 0
        # Initialise the current positions
        self.positions = positions
    # Helper function to fetch the current price of an instrument
    def get_current_price(self, instrument):
        # return most recent price
        return self.data[instrument][-1]
    ########################################################

    # RETURN DESIRED POSITIONS IN DICT FORM
    def get_positions(self):
        # Get current position
        currentPositions = self.positions
        # Get position limits
        positionLimits = self.positionLimits
        
        # Declare a store for desired positions
        desiredPositions = {}
        # Loop through all the instruments you can take positions on.
        for instrument, positionLimit in positionLimits.items():
            # For each instrument initilise desired position to zero
            desiredPositions[instrument] = 0

        # IMPLEMENT CODE HERE TO DECIDE WHAT POSITIONS YOU WANT 
        #######################################################################
        # Display the current trading day
        # print("Starting Algorithm for Day:", self.day)
        
        # I only want to trade the UQ Dollar
        trade_instruments = ["UQ Dollar"]
        
        # Display the prices of instruments I want to trade
        # for ins in trade_instruments:
        #     print(f"{ins}: ${self.get_current_price(ins)}")
        
        # Start trading from Day 2 onwards. Buy if it goes down, sell if it goes up.
        if self.day >= 2:
            pass
            # for ins in trade_instruments:
            #     # if price has gone down buy
            #     if self.data[ins][-2] > self.data[ins][-1]:
            #         desiredPositions[ins] = positionLimits[ins]
            #     else:
            #         desiredPositions[ins] = -positionLimits[ins]
        # Display the end of trading day
        # print("Ending Algorithm for Day:", self.day, "\n")

        # Only plot once
        if self.day == 1:
            # data = self.store_data()
            # self.plot_all(data)
            # self.compare_data(data)
            # DF_change = self.get_change_or_price(data, "Dawg Food", "price")
            dfs = self.read_pandas_data()
            for df in dfs:
            #     dfs[df].plot(x="Day", y="Price", title=f"{df} Prices")
                pass

            for span in range(1, 11):
                dfs["DawgFood"].ewm().mean()

        #######################################################################
        # Return the desired positions
        return desiredPositions

    def read_pandas_data(self):
        data = {}
        for name, file_name in self.get_files():
            df = pd.read_csv(file_name, usecols=range(2))
            df['Change'] = df['Price'].diff().fillna(0)
            data[name] = df
        return data

    def get_files(self):
        names = ["Dawg Food", "Fintech Token", "Fried Chicken", "Goober Eats", "Purple Elixir", "Quantum", "Rare Watch",
                 "Raw Chicken", "Secret Spices", "UQ Dollar"]
        files = ["data/Dawg Food_price_history.csv", "data/Fintech Token_price_history.csv",
                "data/Fried Chicken_price_history.csv", "data/Goober Eats_price_history.csv",
                "data/Purple Elixir_price_history.csv", "data/Quantum Universal Algorithmic Currency Koin_price_history.csv",
                "data/Rare Watch_price_history.csv", "data/Raw Chicken_price_history.csv",
                "data/Secret Spices_price_history.csv", "data/UQ Dollar_price_history.csv"]
        return zip(names, files)

    def get_change_or_price(self, data: dict[str, dict[int, dict[str, int]]], stock: str, type: str):
        return [day[type] for day in data[stock].values()]

    def plot_all(self, data):
        for stock, days in data.items():
            prices = [day["price"] for day in days.values()]
            plt.title(f"{stock} Prices")
            plt.plot([i for i in range(1, 366)], prices)
            plt.show()


    def store_data(self):
        data = {}
        for name, file_name in self.get_files():
            with open(file_name, 'r') as f:
                data[name] = {}
                for i, line in enumerate(f):
                    if i == 0:
                        continue
                    line = line.strip().strip(',').split(',')
                    if len(line) == 2:
                        day, price = line
                        data[name][i] = {}
                        data[name][i]['day'] = int(day)
                        data[name][i]['price'] = float(price)
                        if day == '0':
                            data[name][i]['change'] = 0
                        else:
                            data[name][i]['change'] = float(price) - data[name][i - 1]['price']
                    else:
                        day, price, change = line
                        data[name][i] = {}
                        data[name][i]['day'] = int(day)
                        data[name][i]['price'] = float(price)
                        data[name][i]['change'] = float(change)
        return data

    def compare_data(self, data):
        pass



