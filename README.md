# Change Point Analysis and Statistical Modelling of Brent Oil Prices

This project focuses on detecting changes and associating causes in the time series data of Brent oil prices, specifically how significant political and economic events impact these prices.

## Overview

The goal is to analyze the effects of significant political and economic events on Brent oil prices. The insights derived from this analysis aim to help investors, policymakers, and energy companies make informed decisions.

## Objectives

- Identify key events that have significantly impacted Brent oil prices over the past decade.
- Measure the extent of these impacts on price changes.
- Provide clear, data-driven insights to guide investment strategies, policy development, and operational planning.

## Data

The dataset contains daily prices of Brent oil from May 20, 1987, to September 30, 2022. Each record includes:
- **Date**: Date of the recorded price (`day-month-year` format).
- **Price**: Price of Brent oil in USD per barrel.

## Methodology

- Utilize statistical and econometric models, including ARIMA and GARCH, to analyze the data.
- Consider advanced models like VAR and Markov-Switching ARIMA for deeper insights.
- Implement additional statistical analysis involving Monte Carlo Markov Chain and Bayesian inference methods.

## Installation

Ensure you have Python installed, then clone this repository and run:

```bash
pip install -r requirements.txt
```

This will install PyMC3 among other necessary packages used in this project.

## Usage

To run the analysis, execute the Python scripts located in the `src` directory. Example:

```bash
python src/main_analysis.py
```

## Dashboard

An interactive dashboard is developed using Flask and React, enabling dynamic exploration of how various events affect Brent oil prices. To set up the dashboard:

1. Navigate to the `dashboard` directory.
2. Run `npm install` to install dependencies.
3. Start the backend server:
   ```bash
   python app.py
   ```
4. Launch the frontend in development mode:
   ```bash
   npm start
   ```
![Dashboard](/dashboard/dashboard.png)

## Contributions

Contributions are welcome. Please create a pull request with your proposed changes.

## License

Distributed under the MIT License. See `LICENSE` for more information.
