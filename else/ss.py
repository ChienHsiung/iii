from pyspark import SparkContext, SparkConf
from pyspark.sql import HiveContext
import os
os.environ['SPARK_HOME'] = "C:/spark-2.1.1-bin-hadoop2.7/bin"
if __name__ == '__main__':
    conf = SparkConf()
    conf.set('spark.executor.memory', '16g')
    sc = SparkContext('spark://127.0.0.1:7077', appName='test', conf=conf)
#     sc.setLogLevel('ERROR')
#     hiveContext = HiveContext(sc)
#     hiveContext.setConf('hive.metastore.uris', 'thrift://127.0.0.1:9083')
#     hiveContext.setConf('io.compression.codecs', 'org.apache.hadoop.io.compress.SnappyCodec')
#     hiveContext.sql('use default')
#     hiveContext.sql("select * from table").show()