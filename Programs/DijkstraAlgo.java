import java.util.*;

class Nod implements Comparator<Nod>
{
    private int v;
    private int weight;

    Nod(int _v, int _w) { v = _v; weight = _w; }

    Nod() {}

    int getV() { return v; }
    int getWeight() { return weight; }

    @Override
    public int compare(Nod node1, Nod node2)
    {
        if (node1.weight < node2.weight)
            return -1;
        if (node1.weight > node2.weight)
            return 1;
        return 0;
    }
}

class DijkstraAlgo
{
    void shortestPath(int s, ArrayList<ArrayList<Nod>> adj, int N)
    {
        int dist[] = new int[N];

        ArrayList<Integer> ar = new ArrayList<>();
        for(int i = 0;i<N;i++) dist[i] = 100000000;
        dist[s] = 0;

        PriorityQueue<Nod> pq = new PriorityQueue<Nod>(N, new Nod());
        pq.add(new Nod(s, 0));

        while(pq.size() > 0) {
            Nod node = pq.poll();
            ar.add(node.getV());

            for(Nod it: adj.get(node.getV()))
            {
                if(dist[node.getV()]  + it.getWeight() < dist[it.getV()]) 
                {
                    dist[it.getV()] = dist[node.getV()] + it.getWeight();
                    pq.add(new Nod(it.getV(), dist[it.getV()]));
                }
            }
        }

        for (int i = 0; i < N; i++)
        {
            System.out.print( dist[i] + " ");
        }
    }
    public static void main(String args[])
    {
        int n = 5;
        ArrayList<ArrayList<Nod> > adj = new ArrayList<ArrayList<Nod> >();

        for (int i = 0; i < n; i++)
            adj.add(new ArrayList<Nod>());

        adj.get(0).add(new Nod(1, 2));
        adj.get(1).add(new Nod(0, 2));

        adj.get(1).add(new Nod(2, 4));
        adj.get(2).add(new Nod(1, 4));

        adj.get(0).add(new Nod(3, 1));
        adj.get(3).add(new Nod(0, 1));

        adj.get(3).add(new Nod(2, 3));
        adj.get(2).add(new Nod(3, 3));

        adj.get(1).add(new Nod(4, 5));
        adj.get(4).add(new Nod(1, 5));

        adj.get(2).add(new Nod(4, 1));
        adj.get(4).add(new Nod(2, 1));

        DijkstraAlgo obj = new DijkstraAlgo();
        obj.shortestPath(0, adj, n);

    }
}
