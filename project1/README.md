# Steps of the project 1:

We will follow the IBM Master plan methodology "The Foundational Methodology":

![image](https://github.com/AhmedRebai/fin_ml_projects_polytechnique_tunisie_option_eges/assets/13001763/1b2c0de7-05da-4872-8060-b5e1be3ca7b3)

My video that explains the implementation of this data science methdology: 

https://www.youtube.com/watch?v=t_Rp8rMeYBk



# 1 - Business Understanding:

In this section, provide an introduction to algorithmic trading in the Forex markets. Explain the relevance and importance of the project.


## Project Overview:

In the realm of quantitative finance, the project's objective is to develop an algorithmic trading strategy for the Forex (FX) market, focusing on a basket of currency pairs, namely EURUSD, USDJPY, USDGBP, and USDCHF. This project aims to harness financial data and quantitative techniques to generate trading signals and optimize portfolio allocation for potential profitability.

## Forex Market Significance:

The Forex market is the largest financial market globally, with daily trading volumes exceeding trillions of dollars. Currency pairs are constantly influenced by various economic, geopolitical, and macroeconomic factors. Algorithmic trading in this market offers a unique opportunity to exploit price discrepancies and market inefficiencies efficiently.

## Data Collection:
The project's first phase involves obtaining historical market data with time granularities ranging from 1 minute to daily, spanning three years from October 12, 2023. Data collection will be facilitated through the MetaTrader 5 (MT5) software, enabling access to reliable real-time data. This data will serve as the foundation for generating alpha signals.

## Phase 1: Alpha Signal Generation:
In Phase 1, we will focus on one specific currency pair within the basket. The goal is to design and implement trading algorithms capable of identifying alpha signals, which are market insights that can potentially lead to profitable trades. These signals may arise from technical, fundamental, or quantitative analyses. Successful signal generation is crucial, as it is the basis for any profitable trading strategy.

## Phase 2: Portfolio Allocation:
In Phase 2, we will delve into portfolio management techniques to optimize the allocation of capital across the basket of currency pairs. Three portfolio allocation methods will be explored:

* Markowitz Portfolio Method: This classic approach aims to construct portfolios that maximize returns for a given level of risk. It is based on the principles of diversification and risk-reward trade-offs.

* Equally Risk Parity: This method allocates capital to assets to ensure an equal contribution to portfolio risk. It offers a balanced risk exposure across the basket.

* Hierarchical Risk Parity (HRP) and HERC: These innovative methods use hierarchical clustering techniques to create portfolios that are resilient to market shocks and provide an optimal risk allocation.

## Project Goals:

* Develop an in-depth understanding of the Forex market, currency pairs, and their interdependencies.
* Master data collection using MetaTrader 5, with a comprehensive dataset covering various time granularities.
* Create and test trading algorithms to identify alpha signals and trading opportunities.
* Implement and evaluate portfolio allocation methods to optimize risk and return for the basket of currency pairs.
* Achieve a practical, implementable trading strategy that can be deployed for real trading, with an emphasis on robust risk management.

## Educational Value:
This project aims to provide a valuable learning experience for engineering students, helping them gain hands-on experience in quantitative finance, algorithmic trading, and portfolio optimization. It equips them with the skills and knowledge needed to tackle real-world financial challenges, making them well-prepared for careers in the finance and technology sectors.

By progressing through these project phases, students will gain a deep understanding of algorithmic trading strategies, portfolio management, and the quantitative finance domain, thereby enhancing their expertise and practical problem-solving capabilities.

# 2 - Analytic Approach:

Describe the approach you will take to solve the problem. This could include an overview of the data science and machine learning techniques you plan to use.

# 3 - Data Requirements:

List the data you need for your project, such as historical Forex market data, currency pair prices, and any other relevant data sources.

# 4 - Data Collection:

Show how to collect data for your project. You might want to provide Python code examples for data retrieval, using libraries like Pandas or APIs for financial data.

![Capture d'écran 2023-10-12 161510](https://github.com/AhmedRebai/fin_ml_projects_polytechnique_tunisie_option_eges/assets/13001763/7923cd6e-1178-4ec3-9feb-bb75bb5ea6d5)

![Capture d'écran 2023-10-12 161455](https://github.com/AhmedRebai/fin_ml_projects_polytechnique_tunisie_option_eges/assets/13001763/9bd88f77-5b1b-476b-be5f-3b1f618bbf4e)

![Capture d'écran 2023-10-12 160044](https://github.com/AhmedRebai/fin_ml_projects_polytechnique_tunisie_option_eges/assets/13001763/e287282c-7c8c-4c82-9f47-43a5cf054d6c)

![Capture d'écran 2023-10-12 160100](https://github.com/AhmedRebai/fin_ml_projects_polytechnique_tunisie_option_eges/assets/13001763/9bd16ee0-4a0a-4c69-a592-85d24510e2dd)





# 5 - Data Understanding (for time series):

Utilize econometric tools, time series analysis, and statistical tests to explore the data. Provide code examples for performing these tasks.

* EDA on Financial Time Series
* Features Extraction (an ensemble of important features for Beta Strategies)
* Book about ARIMA model for time series
* Implementation of the ADF statistical test (Augmented Dickey-Fuller)
* Implementation of the statistical test (KPSS) Kwiatkowski-Phillips-Schmidt-Shin
* Implementation of the Phillips-Perron (PP) statistical test
* Checking for autocorrelation in residuals
* Determine if there is heteroscedasticity in the error
* Analysis of partial autocorrelations (ACF PACF)
* Tail Risk Modeling (VaR , CVaR )
* Examine seasonality in data (seasonal decomposion)
* Identify trends and detect trend changes
* Verification of the normality of the errors otherwise normalization of the errors

# 6 - Data Preparation:

Discuss data preprocessing steps, including data cleaning, missing value handling, and feature scaling.

# 7 - Features Extraction:

Explain how to extract relevant features from the data, which will be used as inputs for your machine learning models.

# 8 - Modeling:

Present the mathematical models you mentioned (multilinear regression, k-Nearest Neighbors, decision trees, random forests, XGBoost, deep learning with LSTM and transformers). Provide code examples for training and testing these models.

# 9 - Model Evaluation:

Describe the evaluation metrics you'll use to assess the performance of your models. Present results for each model, including accuracy, precision, recall, etc.

# 10 - Inserting Models into a Trading Strategy:

Explain how to integrate the machine learning models into a trading strategy. Provide code for generating trade signals based on model predictions.

# 11 - Backtesting:

Show how to backtest your trading strategies using the Backtrader library. Discuss the performance of your strategies.

# 12 - Deployment with Flask and Dash-Plotly:

Describe how to deploy your model and trading strategy using Flask and Dash-Plotly. This may include creating a web application for live trading or strategy monitoring.
