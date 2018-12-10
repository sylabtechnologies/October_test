package ginorts;
import java.util.*;

public class Sorted {
    
    private StringBuilder result;
    
    Sorted(StringBuilder str)
    {
        
        TreeMap<Character, Integer> sorted = new TreeMap<Character, Integer>();        
        
        for (int i = 0; i < str.length(); i++) {
            
            if (sorted.get(str.charAt(i)) == null)
                sorted.put(str.charAt(i), 1);
            else
            {
                int myint = sorted.get(str.charAt(i)) + 1;
                sorted.put(str.charAt(i), myint);
            }
        }
        
        result = new StringBuilder();
        for (Map.Entry<Character,Integer> entry : sorted.entrySet())
            for (int i = 0; i < entry.getValue(); i++)
                result.append(entry.getKey());
        
    }
    
    public String toString() { return result.toString(); }
}
