# CS5262-50 Project

# Project Metrics

### Background

Just for a quick summary, our goal of our ML model is to predict whether or not, using a specific trading strategy, we will make money from the stock market or not. The trading strategy we will focus on initially will be to simply buy a stock at the end of one day and sell it the next. This will drastically limit the scope in which we have to research and refine our  model. Additionally, since we can only buy/sell a single stock with our model, we will define a spread of money we are willing to invest across multiple stocks, this will simulate diversifying our portfolio to limit outlier days where either some extraordinary social, political, or economic event happens that greatly affects the stock price. 

We will define some terms that we will use for the rest of this project for clarity:

* Purchase Close Event (PCE): This refers to the event of buying stock at close of a particular day. 
* Sell Close Event (SCE): This refers to the event of selling a stock at the close of a particular day. 
* Trade Window: The amount of time (we'll measure in days, initially) between a purchase event and a sell event.


### Metrics

The metrics for success and failure, are rather quite simple, since unlike other problems such as creating a ML model for the prediction of whether or not someone is sick or not, our will not require much additional research into the penantly for getting the prediction wrong. 

The main goal of this project is to simply make more money from the stock market than that of a trading algorithm that randomly selects whether or not initiate a purchase close event on day 1 and a sell close event on day 2. Its Important to note here that our trade window will be static at 1 day, at least initially. 

Furthermore, we will define a static amount of money we will invest over different stocks to simulate diversity. Lastly, although not as important, we will define a static amount of total money invested, that will be spread across all stocks. Although static, it would be important to note this as a variable as some algorithmic trading strategies do not work at scale. 

We'll define total amount initial amount invested as: 

$$
T_0
$$

 Well define the amount invested in each stock, $x$ , at a time $i$ to be:

$$
SI_{x,i} = {T_i \over |S_x|}
$$

Where $S_x$ is the collection of the growth rate of the stocks we are focsing on and $|S_x|$ is the cardinality of $S_x$, the number of stocks we will invest in. $T_i$ is the amount of money that we have at a time $i$. 

Next, we'll want to define an terms and expressions to show the amount of money we made/loss starting at an initial day $i$.

$$
T_{i+1} = \sum_{x=X} (P_{x,i} + 1)(SI_{x,i}) + \sum_{w=W} (1.00)(SI_{w,i}) = PL_{sum} + NT_{sum}
$$

Where $P_{x,i}$ s.t p ε $P_{x,i}$ and -1 <= $p$ <= 1 at a time $i$ for a stock $x$ , is the set of percentage differentials from the beginning and end of the trade window for our stocks. $SI_{x,i}$ is the amount of money invested in that particular stock, $x$ , at a time $i$. $X$ will be the set of indices of the stock that we chose to invest, while $W$ will be the indices of the stock that we chose not to invest.

The first summation will be all stocks that we chose to invest, while the second summation are the stocks that we chose not to invest (therefore did not lose money or gain money). We'll call these two summations $PL_{sum}$ for profit loss, and $NT_{sum}$ for no trade. 

So for a group of trades, we can define it our ending amount with profits/losses over a time period $n$ as: 

$$
T_{i} = T_0 + \sum_{i=0}^n(\sum_{x=X} (P_{x,i} + 1)(SI_{x,i}) + \sum_{w=W} (1.00)(SI_{w,i}))
$$

We'll also want to consider opportunity cost in the event that our business has a reliable way of making money. In this case, we can define $O_{cost}$ as opportunity cost rate or the average return of a reliable source of income for capital that was left available from not investing. We'll refine the above expression to find our actual profit/loss, $PL_{actual}$ , we can earn: 


$$
PL_{actual} = \sum_{i=0}^n \sum_{x=X} P_{x,i} • SI_{x,i} + \sum_{w=W}  SI_{w,i} • O_{cost}  
$$

And to factor in opportunity cost, we'll have to subtract the opportunity that we missed which will give us an adjusted profit/loss, $PL_{adj}$ that represents the actual net gain/loss of using our model. This is because if we had not invested in any stock, and our business has a reliable opportunity to invest that capital, then we would see a net gain from that opportunity alone. We can define $PL_{adj}$:

$$
PL_{adj} = T_0 + \sum_{i=0}^n(\sum_{x=X} ( P_{x,i} • SI_{x,i} ) - ( O_{cost} • SI_{x,i} ) + \sum_{w=W} SI_{w,i} • O_{cost} )
$$

$$
= \sum_{i=0}^n(\sum_{x=X} ( ( 1 + P_{x,i}) • SI_{x,i} ) - ( O_{cost} • SI_{x,i} ) + \sum_{w=W} SI_{w,i} • ( 1 + O_{cost} ) )
$$


This can be used for both our model and our random algorithm. 

Let $TM_{end}$ be the end amount we get from our ML model, and $TR_{end}$ be the end amount we get from our randomized algorithm.

If,

$$
	TM_{end} > (TR_{end})(ε) 
$$

For some arbitrary small $\epsilon$ 
Then we have shown that our model has outperformed our random algorithm by a factor of $\epsilon$. But we must also confirm: 

$$
	TM_{end} > T_0
$$

To show that the money we end up with after trading is greater than not trading at all.


## Confusion Matrix

#### False Positives
In stock trading, a false positive would mean that our trading model advised us to invest but it shouldnt have. This outcome is worst than a false negative, since there is not a floor to how much money we could lose. In theory, when we sell our stock, the stock could have crashed to $0, or lost 100% of its value. 

Its pertinent for our model that we air on the side of caution and bias our model to not invest if there is not a strong indication that the stock will go up. By not investing, we guarantee that we keep that money instead of losing it all.

One factor we must also consider is the compounding nature of profit and losses. For each profit we make on a day, we are able to invest even more the following day. However, as stated earlier, there is huge potential for losses if the stock crashes that day. So these two factors must be weighed and considered.

Lastly, we must consider opportunity costs of other potential investments, if we invest within the trading window, we can assume that our capital will be unavailable for other types of investment and will need to be considered. This would rely on the business, however, since there are few ways to make substantial amounts of money in such a short amount of time, and most of them require large amounts of capital.

#### False Negatives
For our stock trader, a false negative would mean our model advised not to invest, but should have. Although not as volatile as a false positives, we ideally want to ensure that we are choosing to invest on some days, even if they are few.  We are comfortable with choosing to invest fewer days rather than more since we want to minimize the amount of false positives that we get. Furthermore, unlike false positives, false negatives would still allow us to trade in the future since the amount of money we have has not been depleted. Conversely, false positives will quickly drain our amount of money we have to invest, and if we get to zero, we are no longer able to invest.

A potential upside to false negatives is leveraging opportunity under certain conditions. If we choose not to invest, we can assume that we have that capital in our broker account and available for investment, if our business had a very reliable way of making money with our capital within the trading window, then we can factor this in and consider it to offset the cost of a false negative, atleast somewhat. 

## Conclusion

We have demonstrated the mathematical expressions that we will use to as metrics for our ML model, as well as how we plan on using these metrics to determine success/failure, and finally, we have shown the impacts to the business of false negatives and false positives and how we plan on prioritizing both. 

#### Data
https://archive.ics.uci.edu/ml/datasets/CNNpred%3A+CNN-based+stock+market+prediction+using+a+diverse+set+of+variables
