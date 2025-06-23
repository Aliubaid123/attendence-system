import numpy as np
import matplotlib.pyplot as plt

def main():
    print("=== Simple Stock Price Simulator ===")
    
    # inputs from user
    stock_name = input("Enter stock name : ")
    start_price = float(input("Enter starting price: "))
    days = int(input("Enter days to simulate : "))
    trend = float(input("Enter daily trend : "))
    volatility = float(input("Enter volatility : "))
    
    # Generate random price changes
    daily_returns = np.random.normal(trend, volatility, days)
    prices = [start_price]
    
    # Calculate each day's price
    for ret in daily_returns:
        prices.append(prices[-1] * (1 + ret))
    
    # Calculate 10-day moving average
    ma = [sum(prices[i-10:i])/10 if i >=10 else prices[i] 
          for i in range(len(prices))]
    
    # Plot the results
    plt.figure(figsize=(10,5))
    plt.plot(prices, label='Price', color='blue')
    plt.plot(ma, label='10-Day Avg', linestyle='--', color='orange')
    plt.title(f"{stock_name} Price Simulation")
    plt.xlabel("Days")
    plt.ylabel("Price ($)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()