import pandas as pd
import bar_chart_race as bcr

# Sample data (replace with actual data)
data = {
    'Year': [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Windows': [40, 38, 35, 32, 30, 28, 25, 23, 20, 18],
    'MacOS': [20, 22, 25, 28, 30, 32, 35, 38, 40, 42],
    'Linux': [10, 12, 15, 18, 20, 22, 25, 28, 30, 32],
    'iOS': [15, 18, 20, 22, 25, 28, 30, 32, 35, 38],
    'Android': [15, 15, 15, 15, 15, 15, 15, 15, 15, 15],
}

# Create DataFrame
df = pd.DataFrame(data)

# Set the 'Year' column as the index
df.set_index('Year', inplace=True)

# Create the bar chart race with a slower speed
bcr.bar_chart_race(df, 'best_os_over_10_years_slow.gif', n_bars=5, steps_per_period=10, period_length=1000)

print("bar chart race created. Check 'best_os_over_10_years_slow.gif'")
