import java.util.*;

/**
 * Created by hp on 10/13/2017.
 */
    import java.util.*;

    /**
     * Created by hp on 10/12/2017.
     */
    public class Q3 {
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            Integer numOfNums = scanner.nextInt();
            scanner.nextLine();
            //System.out.println(numOfNums);
            Integer[] array = new Integer[numOfNums];
            Integer cnt = 0;
            for (cnt = 0; cnt <numOfNums; cnt++){
                array[cnt] = scanner.nextInt();
                //System.out.println("man daram migiram");
                //scanner.nextLine();
            }
            Integer panjia = 0, haftia = 0, tafazol = 0, nokhodia = 0;
            Integer[] array2 = new Integer[numOfNums];
            Set set = new TreeSet<Integer>();
            for (cnt = 0; cnt < numOfNums; cnt++){
                if ((array[cnt] % 5 == 0) && (array[cnt] % 7 != 0)){
                    panjia+= array[cnt];
                    //System.out.println("panjie ro gerftam");
                }
                else if ((array[cnt] % 7 == 0) && (array[cnt] % 5 != 0)){
                    haftia+= array[cnt];
                    //System.out.println("haftie ro gerftam");
                }
                else {
                    set.add(array[cnt]);
                    nokhodia+= array[cnt];
                    //System.out.println("nokhodio gereftam");
                }
            }
            tafazol = panjia - haftia;
            Set<Set<Integer>> powersets = powerSet(set);
            //Set<Integer> subSets = new TreeSet<Integer>();
            for ( Set<Integer> subSets : powersets){
                Integer sum = 0;
                //Integer n = 0;
                for(Integer n : subSets){
                    sum+= n;
                }
                Integer tafazol2 = nokhodia - (sum * 2);
                if (tafazol == tafazol2){
                    System.out.println("true");
                    //System.out.println("man too halgheam");
                    return;
                }


            }
            System.out.println("false");
        }
        public static Set<Set<Integer>> powerSet(Set<Integer> originalSet) {
            Set<Set<Integer>> sets = new HashSet<Set<Integer>>();
            if (originalSet.isEmpty()) {
                sets.add(new HashSet<Integer>());
                return sets;
            }
            List<Integer> list = new ArrayList<Integer>(originalSet);
            Integer head = list.get(0);
            Set<Integer> rest = new HashSet<Integer>(list.subList(1, list.size()));
            for (Set<Integer> set : powerSet(rest)) {
                Set<Integer> newSet = new HashSet<Integer>();
                newSet.add(head);
                newSet.addAll(set);
                sets.add(newSet);
                sets.add(set);
                //System.out.println("man too tabeam");
            }
            return sets;
        }
    }


