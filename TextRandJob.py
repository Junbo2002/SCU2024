from pyspark.sql.context import HiveContext

from SparkSessionBase import SparkSessionBase


class TextRandJob(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'TextRandJob'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()
        self.spark.sparkContext.setLogLevel("ERROR")

    def start(self):
        # XXX 大数据分析代码
        sql = "show databases"
        hc = HiveContext(self.spark.sparkContext)
        res = hc.sql(sql)
        # # 将DataFrame保存为JSON格式的文件
        # res.write.format("json").mode("overwrite").save("test")
        # # 将DataFrame保存为hdfs上的csv格式的文件
        # res.write.csv("sample_file.csv", header=True)
        # # 将DataFrame保存为本地的csv格式的文件
        # res.toPandas().to_csv("sample_file.csv", header=True)
        res.show()
        # b_df = hc.table('business')
        # b_df.limit(10).show()


TextRandJob().start()
