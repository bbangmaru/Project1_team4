from sklearn.cluster import KMeans

# head_cluster_city: 중심점의 좌표값 저장
# child_city_idxs: 중심점과 연관되어 있는 도시들의 index 정보
# child_cluster_city: 중심점과 연관되어 있는 도시들의 좌표값 저장
class Clustering:

    @staticmethod
    def clusterTSP(df, k):# k는 군집의 수를 의미
        sub = KMeans(n_clusters = k) # k개의 집단으로 분할
        sub.fit(df) # fit 시키기 - clustering 진행
        labels = sub.predict(df) # 시각화시 필요
        df["cluster"] = sub.labels_ # data frame에 cluster열 추가, 0~k-1까지의 인덱스 형태를 지님
        center = sub.cluster_centers_ # 10개의 center -> sub 생성시 생성, 2차원 ndarray 형태, 중심점은 평균값
        # 중심점과, 자식 도시들을 head와 child에 추가
        head_city = center # 중심점 저장
        child_idx = [] # 중심 주변의 군집화된 도시 index
        for i in range(k): #0~9
            head = []
            for x in df[df["cluster"] == i].index:
                head.append(x)
            child_idx.append(head) # 리스트 통째로 넣기

        '''
        #Clustering 추가
        plt.scatter(df.x, df.y, c=labels, s=10, alpha=0.5) # c 값으로 각각의 sample이 속해있는 cluster index 별로 색상 나누기, labels에는 인덱스 저장되어 있음
        plt.scatter(center[:, 0], center[:, 1], color="RED", s=100, marker='*') # 별은 중심점을 의미
        plt.title("CITY CLUSTER")
        plt.show()
        plt.close()
        '''
        return head_city, child_idx


