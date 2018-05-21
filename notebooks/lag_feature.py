from pyspark import keyword_only
from pyspark.ml import Transformer
from pyspark.ml.param.shared import HasInputCol, HasOutputCol, Param
from pyspark.sql.functions import lag, first
from pyspark.sql.window import Window
import sys

class LagFeature(Transformer, HasInputCol, HasOutputCol):

    @keyword_only
    def __init__(self, inputCol=None, outputCol=None, count=None):
        super(LagFeature, self).__init__()
        self.count = Param(self, "count", "")
        self._setDefault(count=1)
        kwargs = self._input_kwargs
        self.setParams(**kwargs)

    @keyword_only
    def setParams(self, inputCol=None, outputCol=None, count=None):
        kwargs = self._input_kwargs
        return self._set(**kwargs)
        
    def setCount(self, value):
        self._paramMap[self.count] = value
        return self

    def getCount(self):
        return self.getOrDefault(self.count)

    def _transform(self, dataset):
        count = self.getCount()
        in_col = self.getInputCol()
        out_col = self.getOutputCol()
        
        w = Window.partitionBy().orderBy(dataset['year'], dataset['week'])
        dataset = dataset.select('*', lag(in_col, count=count).over(w).alias(out_col))
        # Backward fill nulls.
        w = Window.partitionBy().orderBy(dataset['year'], dataset['week']).rowsBetween(0, sys.maxsize)
        return dataset.withColumn(out_col, first(out_col, ignorenulls=True).over(w))
