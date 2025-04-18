/******************************************************************************

							  Online C++ Compiler.
			   Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include<bits/stdc++.h> 
using namespace std;
# define INF 0x3f3f3f3f 
struct Edge
{
	int u;
	int v;
	int weight;
};
bool global = false;
class Graph
{
	int V;
	list < pair <int, int > >*adj;

	vector < Edge > edge;

public:
	Graph(int V)
	{
		this->V = V;
		adj = new list < pair <int, int > >[V];
	}

	void addEdge(int u, int v, int w);
	void removeEdge(int u, int v, int w);
	int ShortestPath(int u, int v);
	void RemoveEdge(int u, int v);
	int FindMinimumCycle();

};

void Graph::addEdge(int u, int v, int w)
{
	adj[u].push_back(make_pair(v, w));
	adj[v].push_back(make_pair(u, w));

	Edge e{ u, v, w };
	edge.push_back(e);
}

void Graph::removeEdge(int u, int v, int w)
{
	adj[u].remove(make_pair(v, w));
	adj[v].remove(make_pair(u, w));
}

int Graph::ShortestPath(int u, int v)
{
	set< pair<int, int> > setds;

	vector<int> dist(V, INF);

	setds.insert(make_pair(0, u));
	dist[u] = 0;

	while (!setds.empty())
	{
		pair<int, int> tmp = *(setds.begin());
		setds.erase(setds.begin());

		int u = tmp.second;

		list< pair<int, int> >::iterator i;
		for (i = adj[u].begin(); i != adj[u].end(); ++i)
		{
			int v = (*i).first;
			int weight = (*i).second;

			if (dist[v] > dist[u] + weight)
			{
				if (dist[v] != INF)
					setds.erase(setds.find(make_pair(dist[v], v)));

				dist[v] = dist[u] + weight;
				setds.insert(make_pair(dist[v], v));
			}
		}
	}
	return dist[v];
}
int Graph::FindMinimumCycle()
{
	int min_cycle = INT_MAX;
	int E = edge.size();
	for (int i = 0; i < E; i++)
	{
		Edge e = edge[i];

		removeEdge(e.u, e.v, e.weight);
		int vistance = ShortestPath(e.u, e.v);
		if (vistance + e.weight < INF) {
			global = true;
		}
		min_cycle = min(min_cycle, vistance + e.weight);
		addEdge(e.u, e.v, e.weight);
	}
	return min_cycle;
}

int main()
{
	int V;
	int m;
	cin >> V;
	cin >> m;
	Graph g(V);
	int i;
	for (i = 0; i < m; i++) {
		int u;
		int v;
		int weight;
		cin >> u;
		cin >> v;
		cin >> weight;
		g.addEdge(u - 1, v - 1, weight);
	}
	int ans = g.FindMinimumCycle();
	if (!global) {
		cout << "-1" << endl;
	}
	else {
		cout << ans << endl;
	}
	return 0;
}
