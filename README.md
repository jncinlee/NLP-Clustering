# NLP-Clustering
Mini project for sentences clustering by NLP, and clustering for different group by TFIDF matrix and K-mean method

The method using is basically follow the steps of NLP operations. First step is Part-of-speech tagging, tag removal, second step is Tokenization, third step is Filtering, stop word removal and last step is Stemming. And the process is selective conducting due to my limited ability on Python.

Based on 3 different situation, I then generate feature matrix Term Frequency-Inverse Document Frequency (TF-IDF) for each document (sentence). First situation “Simple k-mean” is raw text without filtering, the TF-IDF matrix is 40x116. Second situation “Filtered k-mean” is extracting all the Substantive from each document (Capital initial words), and generate the TF-IDF matrix with size 40x49. The third situation I tagging the cluster keyword based on document provided, the TF-IDF size is 40x50

By each acquired TF-IDF feature matrix, I use K-mean method to conduct clustering (k=5 designated). And use standard deviation within each cluster as an easy index to measure the accuracy prediction within each group, since K-mean is random assigning number as cluster in Python. When a number is closer to 0, it means better clustering of certain group. The result could be summarized as below.

![alt tag](https://github.com/jncinlee/NLP-Clustering/blob/master/result.png "Clustering Result")

We could observe that by tagging each document (from providing tags), the result is greatly improved, and is best perform of the other two (5.401, or entropy 25.3 \<27.6 \< 29.8). With smaller TF-IDF matrix size but lower prediction error, it also better perform on Cluster 1&2. 

This tells us that the NLP process should be a major focus for improving clustering. Since I have some technical issue using ParZu package during the Stemming process, I believe this could largely improve the performance of clustering, and should be a key point.
