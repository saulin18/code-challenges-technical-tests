#include <bits/stdc++.h>

using namespace std;

namespace structures
{
    // Segment tree with lazy propagation for range additions.
    // Queries a single position after applying deferred updates.
    class segment_tree_lazy
    {
    public:
        int n;
        vector<int> tree;
        vector<int> lazy;

        segment_tree_lazy(const vector<int> &arr)
        {
            n = arr.size();
            tree.resize(4 * n);
            lazy.resize(4 * n);
            build(arr, 1, 0, n - 1);
        }

        int query(int index)
        {
           
            return aux_query(1, 0, n - 1, index);
        }

        void update(int left, int right, int value)
        {

            aux_update(1, 0, n - 1, left, right, value);
        }

    private:
        void build(const vector<int> &arr, int node, int t_left, int t_right)
        {
            if (t_left == t_right)
            {
                tree[node] = arr[t_left];
                return;
            }

            int mid = (t_left + t_right) / 2;

            build(arr, 2 * node, t_left, mid);
            build(arr, 2 * node + 1, mid + 1, t_right);

            tree[node] = 0;
            lazy[node] = 0;
        }

        int aux_query(int node, int t_left, int t_right, int index)
        {
            if (t_left == t_right)
            {
                return tree[node] + lazy[node];
            }

            int mid = (t_left + t_right) / 2;

            push_down(node);
            if (index <= mid)
            {
                return tree[node]  + aux_query(2 * node, t_left, mid, index);
            }
            else
            {
                return tree[node] + aux_query(2 * node + 1, mid + 1, t_right, index);
            }
        }

        void aux_update(int node, int t_left, int t_right, int left, int right, int value)
        {
            if (right < t_left || t_right < left)
            {
                return;
            }

            if (left <= t_left && right >= t_right)
            {
                lazy[node] += value;
              
                return;
            }

            int mid = (t_left + t_right) / 2;

            push_down(node);
            aux_update(2 * node, t_left, mid, left, right, value);
            aux_update(2 * node + 1, mid + 1, t_right, left, right, value);
        }

        void push_down(int node)
        {
            if (lazy[node] != 0)
            {
            
                lazy[2 * node] += lazy[node];
                lazy[2 * node + 1] += lazy[node];
                lazy[node] = 0;
            }
        }
    };
}
