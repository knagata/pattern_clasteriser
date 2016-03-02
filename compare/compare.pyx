from Cluster import *

def compare(clusters):
    scores = []
    for i in range(len(clusters)):
        for j in range(i+1,len(clusters)):
            score = clusters[i].similarity(clusters[j])
            scores.append((i,j, score))
    scores = sorted(scores,key=lambda x: x[2])
    return scores[0]