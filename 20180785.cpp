//TSP 문제 시작 도시 0번
//초기세대 100 개  
#define N 1000
#define K 999
#include<iostream>
#include<fstream>
#include<cmath>
#include<string>
#include<cstdlib>
#include<ctime>
#include<time.h>
using namespace std;
struct city{
	float x;
	float y;
};
struct tcity{
	string tx;
	string ty;
};
struct p{
	int n[K];
	int cost;
}; // 해집단 
p path[100]; // 현재세대 5개 
p path1[6]; // 교차연산을 위한 6개의 집단 
p path2[3];// 교차연산을 통해 나온 새로운 3개의 집단  
p path3[100];
city cities[N]; // 도시의 좌표  
tcity tcities[N];
int point1, point2;
float totalcost;
float dis[N][N]; // 각 city에서의 거리 인접행렬 계산
void infile() {
	fstream fs;
	string buf1,buf2,buf3;
    fs.open("TSP.csv",ios::in);
    for(int i=0;i<N;i++) {
    	getline(fs,buf1,',');
    	tcities[i].tx = buf1;
        
    	getline(fs,buf2,'\n');
    	tcities[i].ty = buf2;
	}
    fs.close();
} // city 좌표 읽기 
void convert() {
	for(int i=0;i<N;i++) {
		cities[i].x = ceil(stof(tcities[i].tx));
		cities[i].y = ceil(stof(tcities[i].ty));
	}
} // string->float로 변환 
void distance() {	
	for(int i=0;i<N;i++) {
		for(int j=0;j<N;j++)
			dis[i][j] = ceil(sqrt(pow((cities[i].x - cities[j].x),2) + pow((cities[i].y - cities[j].y),2)));
	}
} // 각 city에서의 거리 인접행렬 계산
void makecost() {
	int start = 0;
    int end = 0;
    
    for(int i=0;i<100;i++) {
		for(int j=0;j<K;j++)
		{
			end = path[i].n[j];
			path[i].cost += dis[start][end];
			start = end;
		}
		path[i].cost += dis[start][0];
	}
}
void makecost1(int count) {
	int start = 0;
    int end = 0;
    	
	for(int j=0;j<K;j++)
	{
		end = path2[count].n[j];
		path2[count].cost += dis[start][end];
		start = end;
	}
	path2[count].cost += dis[start][0];
}
void makeGeneration() {
	srand((unsigned int)time(NULL));
    int x;
    int start = 0;
    int end = 0;
    
	for(int i=0;i<100;i++) {
		for(int j=0;j<K;j++)
			path[i].n[j] = j+1;
	}
	
	for(int i=0;i<100;i++) {
		for(int j=0;j<K;j++) {
			x = (double)rand()/RAND_MAX*K;
      		if(x!=j)
     			swap(path[i].n[x], path[i].n[j]);
		}	
	}
	makecost();
} // 초기 해집단 100개 생성 및 총 cost 계산
void selection() {
	int r1, r2;;
	int r3;
	int count=0;
	for(int i=0;i<3;i++) {
		r1 = rand()%100;
		r2 = rand()%100;
		while(1) {
			if(r1==r2)
				r2 = rand()%100;
			else
				break;
		}
		for(int j=0;j<K;j++) {
			path1[count].n[j] = path[r1].n[j];
			path1[count+1].n[j] = path[r2].n[j];
		}
		count+=2;
	}
} //토너먼트 선택 
void ordercrossover(int m, int count2) {
	int count=0, temp;
	
	path2[m].n[0] = path1[count2].n[0];
	for(int i=0;i<100;i++){
		for(int j=0;j<K;j++){
			if(path1[count2+1].n[count] == path1[count2].n[j])	{
				path2[m].n[j] = path1[count2].n[j];
				count=j;
			}
		}	
	}
	for(int i=0;i<K;i++){
		if(path2[m].n[i]==0){
			temp = i;
			break;
		}
	}
	path2[m].n[temp] = path1[count2+1].n[temp];
	for(int i=0;i<10;i++){
		for(int j=0;j<K;j++){
			if(path1[count2].n[temp] == path1[count2+1].n[j])	{
				path2[m].n[j] = path1[count2+1].n[j];
				temp=j;
			}
		}
	}		
	for(int i=0;i<K;i++){		
		if(path2[m].n[i]==0)
			path2[m].n[i]=path1[count2].n[i];
		}
} 
void replacement() {
	for(int i=0;i<K;i++)
		path[point1].n[i] = path2[point2].n[i];
	path[point1].cost = path2[point2].cost;
}
void maxmin() {
	int max=path[0].cost;
	int minn=path2[0].cost;
	for(int i=0;i<5;i++)
	{
		if(path[i].cost>max)
			max = path[i].cost;
	}
	for(int i=0;i<5;i++)
		if(max==path[i].cost)
			point1 = i;
	for(int i=1;i<3;i++)
		if(minn>path2[i].cost)
			minn = path2[i].cost;
	for(int i=0;i<3;i++)
		if(minn==path2[i].cost)
			point2 = i;
}
void reset() {
	for(int i=0;i<3;i++)
    	path2[i].cost = 0;
}
int stop()
{
	int count = 0;
	for(int i=0;i<100;i++)
		path3[i].cost = path[i].cost;
	for(int i=0;i<100;i++)
		if(path[i].cost == path3[i].cost)
			count++;
	if(count==10)
		return 9999;
}
void mutation()
{
	int r,r1,r2;
	int temp;
	r = rand()%10000000000;
	r1 = rand()%4+1;
	r2 = r1-1;
	if(r=9999)
	{
		for(int i=0;i<5;i++)
		{
			temp = path[i].n[r1];
			path[i].n[r1] = path[i].n[r2];
			path[i].n[r2] = temp; 
		}
	}
}
int main(int argc, char *argv[]) {
	srand((unsigned int)time(NULL));
	ofstream outFile;
	outFile.open("output.txt");
	infile(); // city 좌표 읽기 
	convert(); // string->float로 변환 
	distance(); // 각 city에서의 거리 인접행렬 계산
	makeGeneration(); // 초기 해집단 생성
	int stoppoint;
	for(int m=1;m<100;m++)
	{
		cout<<"=========================================="<<m<<"세대=========================================="<<endl; 
		for(int i=0;i<10;i++)
			cout<<path[i].cost<<" ";
		selection();
		for(int i=0;i<3;i++) {
			ordercrossover(i,i*2);
			makecost1(i);
		}
		cout<<endl;
		maxmin();
		replacement();
		reset();
		mutation();
		stoppoint = stop();
		if(stoppoint==9999)
			break;
	}
	cout<<"==========================================최종해=========================================="<<endl;
	int minn=path[0].cost;
	int point;
	for(int i=1;i<100;i++)
		if(minn>path[i].cost)
			minn = path[i].cost;
	for(int i=0;i<100;i++)
		if(minn==path[i].cost)
			point = i;
	
	for(int i=0;i<K;i++)
		outFile<<path[point].n[i]<<endl;
	
	
    return 0;
}
