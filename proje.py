from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.ml import Pipeline
from pyspark.ml.feature import Tokenizer, StopWordsRemover, HashingTF
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

# Spark başlat
spark = SparkSession.builder \
    .appName("E-Ticaret ML") \
    .getOrCreate()

# CSV oku
df = spark.read.csv(
    "turkce_e_ticaret_veriseti_800.csv",
    header=True,
    inferSchema=True
)

# Label kolonu
df = df.withColumnRenamed("puan", "label")

# Boş yorumları at
df = df.filter(df.kisa_yorum.isNotNull())

# Label tipini garanti altına al
df = df.withColumn("label", col("label").cast("double"))

# Train / Test
train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)

# Pipeline
tokenizer = Tokenizer(
    inputCol="kisa_yorum",
    outputCol="tokens"
)

stopwords = StopWordsRemover(
    inputCol="tokens",
    outputCol="filtered"
)

tf = HashingTF(
    inputCol="filtered",
    outputCol="features",
    numFeatures=1000
)

lr = LinearRegression(
    featuresCol="features",
    labelCol="label"
)

pipeline = Pipeline(stages=[
    tokenizer,
    stopwords,
    tf,
    lr
])

# Model eğit
model = pipeline.fit(train_df)

# Tahmin
predictions = model.transform(test_df)

# Metrikler
rmse = RegressionEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="rmse"
).evaluate(predictions)

r2 = RegressionEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="r2"
).evaluate(predictions)

print("RMSE:", rmse)
print("R2:", r2)

# Örnek çıktı
predictions.select(
    "kisa_yorum", "label", "prediction"
).show(10, truncate=False)