# Steps of the project 1: Implementing a systematic strategy in the FX market (alpha signals research and dynamic diversification)


In this project, we are collaborating with Value Digital Services, a leading provider of artificial intelligence solutions for the financial industry. Value Digital Services brings its cutting-edge artificial intelligence platform to train students from the Ecole Polytechnique de Tunisie.

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

Data preprocessing is a critical phase in the financial project, and it involves several essential steps to ensure that the data used for analysis and modeling is accurate, reliable, and well-suited for the task at hand. This section outlines the key data preparation steps, with a focus on the specific requirements of the financial domain:

## 1 - Data Cleaning:

* Handling Missing Data: Financial datasets often contain missing values, which can have a significant impact on analysis. Implement strategies such as imputation, interpolation, or removal of incomplete data points to ensure data completeness.
* Outlier Detection and Treatment: Identify and handle outliers that can distort financial models. Techniques like Z-score analysis or the IQR method can be employed to detect and address outliers appropriately.
* Data Validation: Ensure that the data adheres to the defined schema and business rules. Validate data types, ranges, and constraints to maintain data integrity.

## 2. Feature Engineering:

* Creating Relevant Features: Generate additional features that might be useful for modeling. In financial projects, this could involve creating technical indicators (e.g., moving averages, RSI) or extracting relevant financial metrics (e.g., Price-to-Earnings ratio).
* Dimensionality Reduction: Use techniques like Principal Component Analysis (PCA) to reduce the dimensionality of the dataset while preserving essential information, which can enhance the performance of models.

## 3. Time Series Preprocessing:

* Temporal Aggregation: Aggregating data over different time frames (e.g., daily to monthly) may be necessary to align with trading or investment strategies.
* Resampling: Ensure that time series data is consistently sampled and properly aligned. You may need to use resampling techniques like forward-filling, backward-filling, or interpolation.

## 4. Normalization and Scaling:

* Standardize or scale the features appropriately to ensure that they are on a similar scale. This step is particularly crucial when working with different financial instruments or variables with different units and magnitudes.

## 5. Handling Categorical Data:

* If your dataset contains categorical data, transform it into a format suitable for machine learning models. Common techniques include one-hot encoding or label encoding.

## 6. Data Splitting:

* Divide the dataset into training, validation, and test sets to assess model performance. Given the time-series nature of financial data, be mindful of temporal ordering when splitting the data.

## 7. Imbalance Handling:

* In financial datasets, class imbalances are common, especially in the case of binary classification tasks (e.g., buy or sell). Consider techniques like oversampling, undersampling, or using specialized algorithms for imbalanced data.

8. Feature Selection:

    Employ feature selection techniques to identify the most relevant features for your model. This reduces the dimensionality of the dataset and can lead to improved model performance.

## 9. Data Quality Assurance:

* Continuously monitor data quality throughout the project's lifecycle. Establish processes for detecting and correcting errors that may arise during data collection or preprocessing.

# 7 - Features Extraction:

Explain how to extract relevant features from the data, which will be used as inputs for your machine learning models.

Feature extraction is a crucial step in preparing the financial data for machine learning models. In the context of this project, we'll focus on extracting relevant features from the data to serve as inputs for our algorithmic trading models. The extracted features will include information about historical price movements, patterns, and support/resistance levels. Here's a breakdown of the feature extraction process:

## 1. Lag Features:

* Price Lag: Calculate lag features by shifting historical prices forward or backward in time. These features capture the historical price behavior at different time intervals, such as one-hour lag, one-day lag, and so on.
* Return Lag: Compute lagged returns to capture historical return patterns. These features can help identify momentum or mean-reversion signals.

## 2. Technical Analysis Indicators:

* Moving Averages: Calculate different moving averages (e.g., Simple Moving Average, Exponential Moving Average) for various timeframes (e.g., 10-day, 50-day, 200-day). Moving averages help identify trends and crossovers.
* Relative Strength Index (RSI): RSI is a momentum oscillator that measures the speed and change of price movements. It can indicate overbought or oversold conditions.
* Moving Average Convergence Divergence (MACD): MACD is a trend-following momentum indicator that provides insights into potential trend changes.
* Bollinger Bands: Bollinger Bands provide information about price volatility and potential breakouts.
* Stochastic Oscillator: The Stochastic Oscillator helps identify overbought and oversold conditions, often used in conjunction with other indicators.

## 3. Support and Resistance Levels:

* Pivot Points: Calculate daily, weekly, or monthly pivot points based on the previous high, low, and closing prices. Pivot points help identify key support and resistance levels.
* Fibonacci Retracement: Use Fibonacci retracement levels to identify potential support and resistance areas based on the Fibonacci sequence.
* Chart Patterns: Identify and label common chart patterns such as head and shoulders, double tops, and double bottoms. These patterns can indicate potential reversals or continuations in price movements.

## 4. Graphical Charts:

* Candlestick Patterns: Recognize and categorize candlestick patterns such as doji, engulfing patterns, hammers, and shooting stars. These patterns provide visual insights into market sentiment.
* Trendlines: Draw trendlines on price charts to visualize trends and potential breakout points.
* Volume Analysis: Include volume information on the price charts to assess the strength of price movements.

## 5. Volatility Measures:

* Historical Volatility: Calculate historical volatility as a feature to measure the level of price fluctuations.
* Implied Volatility: Incorporate implied volatility data, if available, which reflects market expectations of future price movements.

## 6. Sentiment Indicators:

* News and Social Media Sentiment: If applicable, use sentiment analysis of news articles or social media content to gauge market sentiment and incorporate sentiment scores as features.

## 7. Economic Indicators:

* Macroeconomic Indicators: Consider adding macroeconomic indicators such as interest rates, inflation, GDP, and unemployment rates as features if they are expected to influence asset prices.

Feature extraction transforms raw financial data into a set of informative features that can be used for predictive modeling and trading signal generation. It's essential to choose features that align with the objectives of the trading strategy and to continually assess and update the feature set as market conditions change.

# 8 - Modeling:

Present the mathematical models you mentioned (multilinear regression, k-Nearest Neighbors, decision trees, random forests, XGBoost, deep learning with LSTM and transformers). Provide code examples for training and testing these models.

In this phase of the project, we will delve into the application of various mathematical models to fulfill the objectives of the financial project. We will explore the role of each machine learning algorithm, both in regression and classification tasks, to aid in trading signal generation and portfolio optimization.
Regression Models:

Regression models are used to predict a continuous target variable, such as stock prices or returns. Here, we will discuss the role and application of specific algorithms in regression tasks.

## 1. Multilinear Regression:

* Role: Multilinear regression aims to establish a linear relationship between one or more predictor variables and the target variable. It can be used to model the influence of various features on financial metrics, such as predicting stock prices based on fundamental factors.

## 2. k-Nearest Neighbors (KNN):

* Role: KNN is often used for similarity-based regression. Given a new data point, it finds the k-nearest data points in the training set and calculates an average or weighted average of their target values. It can be applied to time series data for predicting future price movements based on historical patterns.

##  3. Decision Trees:

* Role: Decision trees can be used for regression tasks to create a hierarchical decision structure based on features. They can help identify optimal entry and exit points for trading based on historical price patterns.

## 4. Random Forests:

* Role: Random forests extend decision trees by creating an ensemble of decision trees. They are effective in reducing overfitting and can be applied to regression tasks, such as predicting stock returns, where multiple decision trees contribute to the prediction.

## 5. XGBoost:

* Role: XGBoost is a gradient boosting algorithm capable of regression tasks. It's particularly useful for modeling complex relationships between features and predicting financial metrics with high accuracy.

## 6. Deep Learning with LSTM (Long Short-Term Memory):

* Role: LSTM is a type of recurrent neural network (RNN) suitable for sequential data like time series. In financial applications, LSTMs can be used for time series forecasting, including predicting stock prices or portfolio returns over time.

## 7. Transformers:

* Role: Transformers are highly versatile models known for their performance in sequence-to-sequence tasks. In financial projects, transformers can be applied to tasks like volatility prediction, where capturing complex dependencies in financial time series data is essential.

Classification Models:

Classification models are used to predict categorical outcomes, such as whether to buy, sell, or hold a particular asset. Here, we will discuss the role and application of specific algorithms in classification tasks.

## 1. k-Nearest Neighbors (KNN):

* Role: KNN can be adapted for classification tasks by determining the most common class among the k-nearest neighbors. It can be used for sentiment analysis and market sentiment classification based on textual data.

## 2. Decision Trees:

* Role: Decision trees are valuable for classification tasks, such as categorizing assets into buy, sell, or hold classes based on technical and fundamental indicators.

## 3. Random Forests:

* Role: Random forests excel in classification tasks, particularly when dealing with imbalanced datasets. They can be used to classify assets into different investment categories or risk levels.

## 4. XGBoost:

* Role: XGBoost's classification capabilities make it a powerful tool for tasks like identifying market regimes or classifying trading signals into actionable categories.

## 5. Deep Learning with LSTM (Long Short-Term Memory):

* Role: LSTMs can be applied to sentiment analysis and market sentiment classification using textual data from news and social media sources.

## 6. Transformers:

* Role: Transformers can be employed for classification tasks involving market sentiment analysis and trend classification in financial time series data.

## 7. Ensemble Methods:

* Role: In both regression and classification, ensemble methods, such as AdaBoost or Gradient Boosting, can be used to combine the strengths of multiple models and enhance predictive performance

# 9 - Model Evaluation:

Describe the evaluation metrics you'll use to assess the performance of your models. Present results for each model, including accuracy, precision, recall, etc.

evaluate the performance of the machine learning models used for trading signal generation, portfolio allocation, and other tasks. To achieve this, we will employ a variety of evaluation metrics tailored to the specific objectives of each model. Here, we describe the key evaluation metrics that will be utilized to assess model performance:

## For Regression Models (Predicting Continuous Variables):

* Mean Absolute Error (MAE):
** Role: MAE measures the average absolute difference between the predicted and actual values. It provides an indication of the magnitude of prediction errors.
** Use Case: MAE is suitable for assessing models used to predict continuous financial metrics like stock prices or portfolio returns.

* Mean Squared Error (MSE):
** Role: MSE calculates the average squared difference between predicted and actual values. It penalizes larger errors more than MAE.
** Use Case: MSE is effective for quantifying the magnitude of errors in financial predictions.

* Root Mean Squared Error (RMSE):
** Role: RMSE is the square root of the MSE and provides a more interpretable measure of prediction errors. It has the same unit as the target variable.
** Use Case: RMSE is commonly used in financial projects to express the prediction error in the same units as the financial metric being predicted.

## For Classification Models (Categorizing Outcomes):

* Accuracy:
** Role: Accuracy measures the proportion of correctly classified instances. It's a fundamental metric for assessing classification models.
** Use Case: Accuracy is applicable for evaluating models that classify trading signals into buy, sell, or hold categories.

* Precision:
** Role: Precision quantifies the proportion of true positive predictions among all positive predictions. It assesses the model's ability to avoid false positives.
** Use Case: Precision is essential for scenarios where false positives can result in significant losses, such as false buy signals.

* Recall (Sensitivity):
** Role: Recall calculates the proportion of true positive predictions among all actual positive instances. It gauges the model's ability to identify true positives.
** Use Case: Recall is crucial in cases where missing true positives could lead to missed opportunities, e.g., failure to identify profitable trading signals.

* F1-Score:
** Role: The F1-Score is the harmonic mean of precision and recall. It balances the trade-off between precision and recall.
** Use Case: F1-Score provides an overall assessment of classification model performance, especially in scenarios where both false positives and false negatives need to be minimized.

* Area Under the Receiver Operating Characteristic (ROC AUC):
** Role: ROC AUC assesses the model's ability to distinguish between positive and negative classes by measuring the area under the ROC curve.
** Use Case: ROC AUC is valuable for models dealing with binary outcomes, such as classifying trading signals as profitable or not.

## Additional Metrics:

* Profit and Loss (P&L):
** Role: P&L assesses the actual profit or loss generated by trading signals based on the model's recommendations. It provides a real-world measure of model performance.
** Use Case: P&L is crucial for understanding the economic impact of trading strategies and portfolio allocation.

* Sharpe Ratio:
** Role: The Sharpe Ratio assesses the risk-adjusted return of a trading strategy. It considers both returns and volatility.
** Use Case: The Sharpe Ratio is essential for determining the risk-adjusted performance of trading strategies, including portfolio allocation methods.

By utilizing a combination of these evaluation metrics, we can comprehensively assess the performance of machine learning models in our financial project. The choice of metrics will depend on the specific task and the project's objectives, with an emphasis on achieving both accuracy and financial soundness in trading decisions.

# 10 - Inserting Models into a Trading Strategy:

Explain how to integrate the machine learning models into a trading strategy. Provide code for generating trade signals based on model predictions.

# 11 - Backtesting:

Show how to backtest your trading strategies using the Backtrader library. Discuss the performance of your strategies.

** Conduct extensive backtesting to assess the historical performance of the trading strategy. This helps in understanding how the strategy would have performed in the past and identifying potential issues.

** Code Example (using a backtesting library, e.g., Backtrader):



###  Implement a backtesting framework to simulate the trading strategy

import backtrader as bt

class MyStrategy(bt.Strategy):

    #### Define your strategy logic here

cerebro = bt.Cerebro()

cerebro.addstrategy(MyStrategy)

data = bt.feeds.PandasData(dataname=dataframe)

cerebro.adddata(data)

cerebro.run()

cerebro.plot()

## Live trading

If the backtesting results are satisfactory, consider deploying the trading strategy in a live trading environment. Ensure that the infrastructure, risk management, and execution mechanisms are in place for real-time trading.

## Continuous Monitoring and Optimization:

Continuously monitor the performance of the trading strategy in the live environment. Periodically retrain the machine learning models with fresh data and consider reevaluating and updating the strategy parameters for better adaptability to changing market conditions.


# 12 - Deployment with Flask and Dash-Plotly:

Describe how to deploy your model and trading strategy using Flask and Dash-Plotly. This may include creating a web application for live trading or strategy monitoring.
