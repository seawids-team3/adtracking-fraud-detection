#  Reads in the training csv, sorts it first by
#  ip, then by click_time, then writes it out
#  in spark-friendly parquet format

import pyspark

spark = pyspark.sql.SparkSession.builder.getOrCreate()

df = spark.read.csv('../data/train.csv', header=True, inferSchema=True)

df_sort = df.sort(['ip','click_time'])

df_sort.write.parquet('../data/sorted_train.parquet', 
                     mode='overwrite')

spark.stop()

