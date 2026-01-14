
class Edge{
    Vertex v1;
    Vertex v2;

    Edge(Vertex v1, Vertex v2){
        this.v1 = v1;
        this.v2 = v2;
    }

    public Vertex getV1() { return v1; }

    public Vertex getV2() { return v2; }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Edge other = (Edge) o;
        return (v1.equals(other.v1) && v2.equals(other.v2)) || (v1.equals(other.v2) && v2.equals(other.v1));
    }

    @Override
    public int hashCode() {
        return v1.hashCode() + v2.hashCode();
    }
}