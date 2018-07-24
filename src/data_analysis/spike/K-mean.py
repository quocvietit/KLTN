"""
@name: K-mean
@author: Vuong Quoc Viet
@version: 1.0
@since: Apr 22, 2018
"""

import sys

reload(sys)
sys.setdefaultencoding('utf8')

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import codecs
import os
import re
from sklearn.metrics import adjusted_rand_score


def start():
	file_paths = get_paths()

	doc_complete = []
	for file_path in file_paths:
		fp = codecs.open(file_path, 'r', 'utf-8')
		doc_content = fp.read()
		dicts = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', doc_content)
		for dict in dicts:
			doc_content.replace(dict," ")
		doc_complete.append(doc_content)

	# print(doc_complete)
	return doc_complete


def get_paths():
	file_paths = [os.path.join("../../data/post_contents", p) for p in os.listdir("../../data/post_contents")]
	return file_paths

documents = start()

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

true_k = 10
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
	print("Cluster %d:" % i),
	for ind in order_centroids[i, :10]:
		print(' %s' % terms[ind]),
	print

print("\n")
print("Prediction")

Y = vectorizer.transform(["chrome browser to open."])
prediction = model.predict(Y)
print(prediction)

Y = vectorizer.transform(["My cat is hungry."])
prediction = model.predict(Y)
print(prediction)
