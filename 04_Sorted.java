package ginorts;
import java.util.*;

public class Sorted {
    
    private StringBuilder result;
    
    Sorted(StringBuilder str)
    {
        TreeSet<Character> sorted = new TreeSet<Character>();
        
        for (int i = 0; i < str.length(); i++) {
            sorted.add(str.charAt(i));
        }
        
        result = new StringBuilder();
        for (Character x : sorted) {
            result.append(x);
        }
    }
    
    public String toString() { return result.toString(); }
}
