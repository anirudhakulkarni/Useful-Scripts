import java.io.*;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.HashMap;
class Graph {
    HashMap<String, Integer > map = new HashMap<>();
    LinkedList<Edge>[] adj;
    int size;
    vertex[] Vert;
    public Graph (int size) {
        this.adj=new LinkedList[size];
        this.size=size;
        this.Vert=new vertex[size];
    }
    void addEdge(String source, String destination, int weight){
        int source_i=this.map.get(source);
        int dest_i=this.map.get(destination);
        this.adj[source_i].add(new Edge(dest_i, weight));
        this.Vert[source_i].nghbrs++;
        this.Vert[source_i].weights_sum+=weight;
        this.adj[dest_i].add(new Edge(source_i, weight));
        this.Vert[dest_i].nghbrs++;
        this.Vert[dest_i].weights_sum+=weight;
    }
    void addVertex(String label,int index){
        this.map.put(label,index);
        this.Vert[index]=new vertex(label,index, 0, 0);
        if (adj[index] == null) {
            adj[index] = new LinkedList<Edge>();
        }
    }
    void average(){
        float ans=0;
        for (int ii = 0; ii < this.size; ii++) {
            ans+=this.Vert[ii].nghbrs;
        }
        ans/=this.size;
        System.out.printf("%.2f", ans);
        System.out.println();
    }
    void rank(){
        vertex[] occur=this.Vert.clone();
        MergeSort.sort(occur, 0, this.size-1);
        for (int ii = 0; ii < occur.length-1; ii++) {
            System.out.print(occur[ii].label+",");
        }
        System.out.println(occur[occur.length-1].label);
    }
    void independant_storylines_dfs(){
        boolean visited[]=new boolean[this.size];
        ArrayList<vertex[] > CompList = new ArrayList<vertex[] >(); 
        vertex[] occur=this.Vert.clone();
        for (int ii = 0; ii < occur.length; ii++) {
            if(!visited[ii]){
                //System.out.println(ii);
                ArrayList<vertex> component=new ArrayList<>();
                this.dfs(component,this,ii,visited,occur);
                vertex[] acomponent=new vertex[component.size()];
                acomponent=component.toArray(acomponent);
                MergeSortSize.sort(acomponent, 0, acomponent.length-1);
                CompList.add(acomponent);
            }
        }
        vertex[][] CompArr=new vertex[CompList.size()][];
        CompArr=CompList.toArray(CompArr);
        MergeSortArr.sort(CompArr, 0, CompArr.length -1);
        //printing
        for (int ii = 0; ii < CompArr.length; ii++) { 
            for (int j = 0; j < CompArr[ii].length-1 ; j++) { 
                System.out.print(CompArr[ii][j].label+"," ); 
            }
            System.out.print(CompArr[ii][CompArr[ii].length-1].label );
            System.out.println(); 
        } 

    }
    void dfs(ArrayList component,Graph graph,int ii,boolean visited[],vertex occur[]){
        visited[ii]=true;
        component.add(occur[ii]);
        for (Edge e : adj[ii]) {
            if(!visited[e.vertexId])
            dfs(component, graph, e.vertexId, visited, occur);
        }
    }
}
class vertex{
    public int nghbrs;
    public int weights_sum;
    public int index;
    public String label;
    public vertex(String label,int index, int nghbrs, int weights_sum) {
        this.nghbrs = nghbrs;
        this.weights_sum = weights_sum;
        this.index=index;
        this.label=label;
    }
}
class Edge
{
    public int vertexId;
    public int weight;
    public Edge(int vertexId, int weight) {
        this.vertexId = vertexId;
        this.weight = weight;
    }
}


public class A4_2019CS50421 {
    public static void main(String[] args) throws Exception {
        long startTime = System.nanoTime();
        String nodes_csv_loc = args[0];
        String edges_csv_loc = args[1];
        //String function = args[2];

        String line="";
        //input taking
        FileReader nodesF;
        BufferedReader br,br2;
        int num_lines=0;
        try {
            nodesF=new FileReader(nodes_csv_loc);
            LineNumberReader count = new LineNumberReader(new FileReader(nodes_csv_loc));
            count.skip(Long.MAX_VALUE);
            num_lines=count.getLineNumber()-1;
            
            br=new BufferedReader(nodesF);
            br2=new BufferedReader(new FileReader(edges_csv_loc));
            int index=0;
            Graph graph=new Graph(num_lines);
            //exact input
            while ((line=br.readLine())!=null) {
                String[] values=line.split(",(?=([^\"]*\"[^\"]*\")*[^\"]*$)");
                if(values[1].charAt(0)=='"'){values[1]=values[1].substring(1,values[1].length()-1);}
                //values[1]=values[1].replaceAll("\"", "");
                if(index==0){
                    index++;
                    continue;
                }
                graph.addVertex(values[1], index-1);
                index++;
            }
            while ((line=br2.readLine())!=null) {
                String[] values=line.split(",(?=([^\"]*\"[^\"]*\")*[^\"]*$)");
                if(values[0].charAt(0)=='"'){values[0]=values[0].substring(1,values[0].length()-1);}
                if(values[1].charAt(0)=='"'){values[1]=values[1].substring(1,values[1].length()-1);}
                //uncomment here if "" business is over
                //values[0]=values[0].replaceAll("\"", "");
                //values[1]=values[1].replaceAll("\"", "");
                if(values[2].equals("Weight"))continue;
                graph.addEdge(values[0], values[1], Integer.parseInt(values[2]));
            }
            //graph.printer();
            if(args[2].equals("average")){
                if(graph.size==0){
                    System.out.println("0.00");
                    return;
                }
                graph.average();
            }        
            else if(args[2].equals("rank")){
                //comment here
                //FileOutputStream f = new FileOutputStream("rank.txt");System.setOut(new PrintStream(f));
                if(graph.size==0){
                    System.out.println();
                    return;
                }
                graph.rank();
            }   
            else if(args[2].equals("independent_storylines_dfs")){
                //comment here
                //FileOutputStream f = new FileOutputStream("dfs.txt");System.setOut(new PrintStream(f));
                if(graph.size==0){
                    System.out.println();
                    return;
                }
                graph.independant_storylines_dfs();
            } 
        } 
        catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        //PrintStream consoleStream = new PrintStream(new FileOutputStream(FileDescriptor.out));System.setOut(consoleStream);long stopTime = System.nanoTime();System.out.println((stopTime - startTime)/1000000000.0);  
    }
    
}
class MergeSort {
    static void merge(vertex arr[], int l, int m, int r){
        int n1 = m - l + 1;
        int n2 = r - m;
        vertex L[] = new vertex[n1];
        vertex R[] = new vertex[n2];
        for (int i = 0; i < n1; ++i)
            L[i] = arr[l + i];
        for (int j = 0; j < n2; ++j)
            R[j] = arr[m + 1 + j];
        int i=0,j=0,k=l;
        while(i<n1&&j<n2){
            if (L[i].weights_sum > R[j].weights_sum) {
                arr[k] = L[i];
                i++;
            }
            else if(L[i].weights_sum<R[j].weights_sum) {
                arr[k] = R[j];
                j++;
            }
            else{
                if (L[i].label.compareTo(R[j].label)>0) {
                    arr[k] = L[i];
                    i++;
                }
                else{
                    arr[k] = R[j];
                    j++;
                }
            }
            k++;
        }
        while (i < n1) {
            arr[k] = L[i];
            i++;k++;
        }
        while (j < n2) {
            arr[k] = R[j];
            j++;k++;
        }
    }
    static void sort(vertex arr[], int l, int r){
        if (l < r) {
            int m = (l + r) / 2;
            sort(arr, l, m);
            sort(arr, m + 1, r);
            merge(arr, l, m, r);
        }
    }
}

class MergeSortArr {
    static void merge(vertex arr[][], int l, int m, int r){
        int n1 = m - l + 1;
        int n2 = r - m;
        vertex[][] L = new vertex[n1][];
        vertex[][] R = new vertex[n2][];
        for (int i = 0; i < n1; ++i)
            L[i]=arr[l + i];
        for (int j = 0; j < n2; ++j)
            R[j]= arr[m + 1 + j];
        int i = 0, j = 0;
        int k = l;
        while (i < n1 && j < n2) {
            if (L[i].length > R[j].length) {
                arr[k] = L[i];
                i++;
            }
            else if(L[i].length<R[j].length) {
                arr[k] = R[j];
                j++;
            }
            else{
                int ii=0;
                while(ii<L[i].length){
                    if (L[i][ii].label.compareTo(R[j][ii].label)>0) {
                        arr[k] = L[i];
                        i++;
                        break;
                    }
                    else if(L[i][ii].label.compareTo(R[j][ii].label)<0){
                        arr[k] = R[j];
                        j++;
                        break;
                    }      
                    else{
                        ii++;
                    }
                }
            }
            k++;
        }
        while(i<n1){
            arr[k]=L[i];
            i++;k++;
        }
        while(j<n2){
            arr[k]=R[j];
            j++;k++;
        }
    }
 
    static void sort(vertex[] [] arr, int l, int r){
        if(l<r){
            int m=(l+r)/2; 
            sort(arr,l,m);
            sort(arr,m+1,r);
            merge(arr,l,m,r);
        }
    }
}
class MergeSortSize{
    static void merge(vertex arr[], int l, int m, int r){
        int n1=m-l+1;
        int n2=r-m;
        vertex L[]=new vertex[n1];
        vertex R[]=new vertex[n2];
        for (int i=0; i<n1; ++i)
            L[i] = arr[l + i];
        for (int j=0;j<n2;++j)
            R[j]=arr[m+1+j]; 
        int i=0, j=0;
        int k=l;
        while (i < n1 && j < n2) {
            if (L[i].label.compareTo(R[j].label)>0) {
                arr[k] = L[i];
                i++;
            }
            else{
                arr[k] = R[j];
                j++;
            }
            k++;
        }
        while(i<n1) {
            arr[k]=L[i];
            i++;k++;
        }
        while(j<n2) {
            arr[k]=R[j];
            j++;k++;
        }
    }
    static void sort(vertex arr[], int l, int r){
        if(l<r){
            int m=(l+r)/2;
            sort(arr,l,m);
            sort(arr,m+1,r);
            merge(arr,l,m,r);
        }
    }
}