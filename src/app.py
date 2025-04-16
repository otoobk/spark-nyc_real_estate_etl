from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder.appName("nyc_real_estate_ETL").getOrCreate()

    spark.stop()
    
if __name__ == "__main__":
    main()