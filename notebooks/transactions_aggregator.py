from pyspark.sql import functions as F 

class TransactionsAggregator(object):
    
    def __init__(self, spark_session, transactions, item, cross_items):
        self.spark_session = spark_session
        self.transactions = transactions
        self.transactions.registerTempTable('transactions')
        self.item = item
        self.cross_items = cross_items
    
    def create_prices(self):
        return self.spark_session.sql('''
            SELECT
                date,
                YEAR(date) AS year,
                MONTH(date) AS month,
                WEEKOFYEAR(date) AS week,
                cost AS cost_{0}, 
                price AS price_{0}, 
                sales AS sales_{0}
            FROM 
                transactions
            WHERE
                item='{0}'
        '''.format(self.item))
        
    def create_cross_prices(self, cross_item):
        return self.spark_session.sql('''
            SELECT DISTINCT
                date, 
                price AS cross_price_{0}
            FROM 
                transactions
            WHERE
                item='{0}'
        '''.format(cross_item))
  
    def create_prices_and_cross_prices(self, prices, cross_prices):
        a = prices.alias('a')
        b = cross_prices.alias('b')
        return a.join(b, F.col('a.date') == F.col('b.date'), how='left').select([F.col('a.' + column) for column in a.columns] + [F.col('b.' + column) for column in b.columns if column != 'date'])

    def create_week_level_features(self, prices_and_cross_prices):
        a = prices_and_cross_prices.alias('a')
        cols = ['date', 'month', 'cost_{}'.format(self.item), 'price_{}'.format(self.item), 'sales_{}'.format(self.item)] + ['cross_price_{}'.format(cross_item) for cross_item in self.cross_items]
        funs = [F.min, F.min, F.avg, F.avg, F.sum] + [F.avg for cross_item in self.cross_items]
        names = ['date', 'month', 'cost_{}'.format(self.item), 'price_{}'.format(self.item), 'demand_{}'.format(self.item)] + ['cross_price_{}'.format(cross_item) for cross_item in self.cross_items]
        exprs = [f(F.col('a.' + c)).alias(n) for c, f, n in zip(cols, funs, names)]
        return a.groupBy("year", "week").agg(*exprs).orderBy("year", "week").drop('date')
        
    def aggregate(self):
        prices = self.create_prices()
        for cross_item in self.cross_items:
            cross_prices = self.create_cross_prices(cross_item)
            prices = self.create_prices_and_cross_prices(prices, cross_prices)
        return self.create_week_level_features(prices)