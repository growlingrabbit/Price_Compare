from pyspark import SparkConf, SparkContext
import os
# import matplotlib as mpl
# mpl.use('TkAgg')
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

os.environ['JAVA_HOME']='/usr/local/jdk1.8'
conf = SparkConf().setAppName('WordCount').setMaster('local')
sc = SparkContext(conf=conf)
file = sc.textFile("file:///home/hadoop/Downloads/PriceCompaer/p_price")
result= file.flatMap(lambda line: line.split("\n")).map(lambda word: (float(word),1)).reduceByKey(lambda x,y:x+y)
result2=result.collect()
print(result2)

x=[]
y=[]
for i in range(len(result2)) :
    for j in range(len(result2[i])):
        x.append(float(result2[i][0]))
        y.append(result2[i][1])

plt.title('Price_Count')
plt.bar(x,y,1)
plt.show()




