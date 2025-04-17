import java.util.*;

/**
 * Created by hp on 10/13/2017.
 */
public class Q2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String string = scanner.nextLine();
        String stringeBarax = new StringBuilder(string).reverse().toString();
        //System.out.println(stringeBarax);
        int count = 0, indexes = 0;
        String output = null;
        List<Integer> list = new ArrayList<Integer>();
        for (count = 0; count < string.length()/2; count++){
            if(string.charAt(0) == stringeBarax.charAt(count))
            {
                //System.out.println("meske dare peida mishe" + count);
                list.add(indexes, (count + 1));
                indexes++;
            }
        }
        int count2 = 0;
        for (Integer integer : list) {
            //System.out.println(string.substring(0,integer) + "akharie dorostast");
        }
        avvali:
        for (Integer integer : list) {
            //System.out.println(integer + "ana integer");
            count2 = integer - 1;
            dovvomi:
            for (count = 0; count <integer; count++){
                if(string.charAt(count) != stringeBarax.charAt(count2)){
                    //System.out.println("eva bebakhshid eshteba shod");
                    continue avvali;
                }
                if(count2 > 0)
                count2--;
            }
            output = string.substring(0, integer);
            //System.out.println(output + "ana output");
        }
        if (output == null){
            System.out.println(string);
            return;
        }
        Character[] finalOutput = new Character[output.length()];
        for (count = 0; count < output.length(); count++){
            finalOutput[count] = output.charAt(count);
        }
        Arrays.sort(finalOutput, new Comparator<Character>() {
            public int compare(Character c1, Character c2) {
                int cmp = Character.compare(
                        Character.toLowerCase(c1.charValue()),
                        Character.toLowerCase(c2.charValue())
                );
                if (cmp != 0) return cmp;
                return Character.compare(c1.charValue(), c2.charValue());
            }
        });
        StringBuilder sb = new StringBuilder(finalOutput.length);
        for (char c : finalOutput) sb.append(c);
        output = sb.toString();
        System.out.println(output);
    }
}
