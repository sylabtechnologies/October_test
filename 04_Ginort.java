/*

Lift from ginorts.py <<###

*/
package ginorts;
import java.util.*;

public class Ginorts {
    public static void main(String[] args) {
        
        ConsoleInput inp = new ConsoleInput('>');
        
        while (inp.hasNext())
        {
            StringBuilder lcase = new StringBuilder();
            StringBuilder ucase = new StringBuilder();
            StringBuilder oddig = new StringBuilder();
            StringBuilder evdig = new StringBuilder();

            String myline = inp.next();
            for (char x : myline.toCharArray())
            {
                if  (x >= 'a' && x <= 'z')
                    lcase.append(x);
                else if (x >= 'A' && x <= 'Z')
                    ucase.append(x);
                else
                {
                    int i = (int)x; i -= (int)'0';

                    if (i % 2 == 1)
                        oddig.append(x);
                    else
                        evdig.append(x);
                }
                
            }

            // Make conversions
            StringBuilder result = new StringBuilder((new Sorted(lcase)).toString());
            result.append(new StringBuilder((new Sorted(ucase)).toString()));
            result.append(new StringBuilder((new Sorted(oddig)).toString()));
            result.append(new StringBuilder((new Sorted(evdig)).toString()));
            
            System.out.println(result);
        }
    }

}
