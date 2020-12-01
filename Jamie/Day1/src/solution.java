import java.io.IOException;
import java.io.RandomAccessFile;
import java.util.ArrayList;

public class solution {
    public static void main(String[] args) throws IOException {
        ArrayList<Integer> input = stringPasser();
        System.out.println("P1:" + part1(input));
        System.out.println("P2:" + part2(input));
    }

    // Day 1, Part 1
    public static int part1(ArrayList<Integer> input){
        for(int i : input){
            for(int x : input){
                if((i + x) == 2020){ return i*x;}
            }
        }
        return 0;
    }

    // Day 1 Part 2
    public static int part2(ArrayList<Integer> input) {
        for (int i : input) {
            for (int x : input) {
                for (int y : input)
                    if ((i + x + y) == 2020) { return i * x * y; }
            }
        }
        return 0;
    }

    // Random string parser to get my input
    public static ArrayList<Integer> stringPasser() throws IOException {
        RandomAccessFile file = new RandomAccessFile("src/puzzleinput.txt", "r");
        ArrayList<Integer> arr = new ArrayList<Integer>();
        String value;
        while ((value = file.readLine()) != null) {arr.add(Integer.parseInt(value));}
        return arr;
    }
}