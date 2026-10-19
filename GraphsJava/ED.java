import java.util.*;
public class ED {
    HashMap<Double, Double> memoFib;
    HashMap<Double, Double> memoFact;
    public ED(){
        this.memoFib = new HashMap<>();
        this.memoFact = new HashMap<>();
        memoFib.put((double)0,(double) 0);
        memoFib.put((double)1, (double)1);
        memoFact.put((double)0, (double)1);
    }


    public double minCoins(int amount, ArrayList<Integer> coins){
        if(amount == 0) return 0;
        var dp = new double[amount + 1];
        dp[0] = 0;
        for (int i = 1; i <= amount; i++) {
            dp[i] = Float.MAX_VALUE;
        }


        for (int i = 1; i <= amount; i++) {
            for (int j = 0; j < coins.size(); j++) {
                if(i < coins.get(j)){

                    continue;
                } 
                dp[i] = Math.min(dp[i], dp[i - coins.get(j)] + 1);
            }
        }

        return dp[amount] == Float.MAX_VALUE ? -1 : dp[amount];
    }

    public double bs(double left, double right, double value, double[] arr){
        if (left > right) return -1;

        int mid = (int) Math.floor(left + (right - left) / 2);

        if (arr[mid] == value) return value;

        if (arr[mid] > value) {
            return bs(left, mid - 1, value, arr);
        }
        return bs(mid + 1, right, value, arr);
    }

    public double factorial(double num){
        if (this.memoFact.containsKey(num)){
            return this.memoFact.get(num);
        }


        var res = num * factorial(num - 1);
        this.memoFact.put(num, res);
        return this.memoFact.get(num);
    }

    public double fib(double num){
          if (this.memoFib.containsKey(num)){
            return this.memoFib.get(num);
        }

        var res = fib(num - 1) + fib(num - 2);

        this.memoFib.put(num, res);
        return this.memoFib.get(num);

    }

    public void Djikstra(HashMap<Integer, List<List<Integer>>> adjList, int startNode){
    var max = 10 * 8 * (10 * 8);
    var distances = new int[adjList.size()];
    for (int i = 0; i < distances.length; i++) {
        distances[i] = max;
    }
    distances[startNode] = 0;

    var pq = new PriorityQueue<List<Integer>>((arg0, arg1) -> arg0.get(0) - arg1.get(0));
   

    for (int i = 0; i < distances.length; i++) {
        if (i != startNode) {
            pq.add(List.of(max, i));
            continue;
        }
        pq.add(List.of(0, startNode));
    }

    while (!pq.isEmpty()) {
        var distanceAndNode = pq.poll();
        var distance = distanceAndNode.get(0);
        var node = distanceAndNode.get(1);

        for (List<Integer> neigh : adjList.get(node)) {
            var newDistance = distance + neigh.get(0);

            if (newDistance >= distances[neigh.get(1)]){
                continue;
            }
            distances[neigh.get(1)] = newDistance;
            pq.add(List.of(newDistance, neigh.get(1)));
        }
        
    }


   }
    
}
