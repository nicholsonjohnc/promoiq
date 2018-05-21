from pyspark.ml.feature import OneHotEncoder
from log_feature import LogFeature
from lag_feature import LagFeature
from pyspark.ml.feature import VectorAssembler
from pyspark.ml import Pipeline

class PipelineBuilder(object):
    
    def __init__(self, spark_session, model, item, cross_items, memory):
        self.spark_session = spark_session
        self.model = model
#         self.transactions.registerTempTable('transactions')
        self.item = item
        self.cross_items = cross_items
        self.memory = memory
        
    def build(self):
        stages = []
        input_cols = []

        ###########
        # Inputs
        ###########



        # Log price.
        stages.append(LogFeature(inputCol='price_{}'.format(self.item), outputCol='log_price_{}'.format(self.item)))
        input_cols.append('log_price_{}'.format(self.item))
        
        # One hot encoded month.
        stages.append(OneHotEncoder(inputCol='month', outputCol='month_encoded'))
        input_cols.append('month_encoded')

        # Lag log prices.
        for k in range(1, self.memory + 1):
            stages.append(LagFeature(inputCol='log_price_{}'.format(self.item), outputCol='log_price_{}_lag_{}'.format(self.item, k), count=k))
            input_cols.append('log_price_{}_lag_{}'.format(self.item, k))

        # Log cross prices.
        for cross_item in self.cross_items:
            stages.append(LogFeature(inputCol='cross_price_{}'.format(cross_item), outputCol='log_cross_price_{}'.format(cross_item)))
            input_cols.append('log_cross_price_{}'.format(cross_item))

        # Assemble features vector.
        stages.append(VectorAssembler(inputCols=input_cols, outputCol="features"))

        ###########
        # Output
        ###########

        # Log demand.
        stages.append(LogFeature(inputCol='demand_{}'.format(self.item), outputCol='log_demand_{}'.format(self.item)))

        ###########
        # Model
        ###########

        # Add model.
        self.model.setFeaturesCol('features')
        self.model.setLabelCol('log_demand_{}'.format(self.item))
        stages.append(self.model)

        ###########
        # Pipeline
        ###########

        return Pipeline(stages = stages)