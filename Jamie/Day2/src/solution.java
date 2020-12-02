import java.io.IOException;
import java.io.RandomAccessFile;
import java.util.ArrayList;


public class solution {
    public static void main(String[] args) throws IOException {
        ArrayList<String> input = stringParser();
        System.out.println("P1:" + part1(input));
        System.out.println("P1:" + part2(input));
    }

    // Day 2, Part 1
    public static int part1(ArrayList<String> input){
        int bigCount = 0;
        for(String i : input) {
            long count = getString(i).codePoints().filter(ch -> ch == getAlphabet(i)).count();
            int[] range = getRange(i);
            if (count >= range[0]  && count <= range[1]) {bigCount++; }
        }
        return bigCount;
    }

    // Day 2, Part 2
    public static int part2(ArrayList<String> input){
        int lilCount = 0;
        for(String i : input) {
            int[] range = getRange(i);
            char expectedChar = getAlphabet(i);
            if((getString(i).charAt(range[0]) == expectedChar) ^ (getString(i).charAt(range[1]) == expectedChar)){ lilCount++; }
        }
        return lilCount;
    }

    // Get string, alphabet and range
    public static String getString(String input){ String[] myOutput = input.split(":");return myOutput[1]; }
    public static char getAlphabet(String input){ int index = input.indexOf(":");return input.charAt(index-1); }
    public static int[] getRange(String input){
        String values = input.substring(0,5).replace("-", " ");
        String[] range = values.split(" ");
        int[] theRange = {Integer.parseInt(range[0]), Integer.parseInt(range[1])};
        return theRange;
    }

    // Random string parser to get my input
    public static ArrayList<String> stringParser() throws IOException {
        RandomAccessFile file = new RandomAccessFile("src/puzzleinput.txt", "r");
        ArrayList<String> arr = new ArrayList<String>();
        String value;
        while ((value = file.readLine()) != null) {arr.add(value);}
        return arr;
    }
}
