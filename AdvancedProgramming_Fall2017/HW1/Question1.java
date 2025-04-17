import java.util.Scanner;

/**
 * Created by hp on 10/14/2017.
 */
public class Question1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Integer numOfConditions = scanner.nextInt();
        //System.out.println(numOfConditions);
        int counter0, counter1, counter2, counter3, counter4, counter5;
        String string = "";
        for (counter0 = 0; counter0< numOfConditions; counter0++){
         string = string.concat(scanner.next()).concat(" ");
            //System.out.println(string);
        }
        String[] separatedString = string.split(" ");
        //System.out.println(separatedString.length);
        for (counter1 = 0; counter1 < separatedString.length; counter1++){
            separatedString[counter1] = separatedString[counter1].replaceAll(" ","");
            //for (counter2 = 0;counter2 < separatedString[counter1].length(); counter2++)
            //System.out.println("counter1: "+ counter1 + " counter2: " + counter2 + " " + separatedString[counter1].charAt(counter2));
        }
        Integer[] minimums = new Integer[separatedString.length];
        Integer[] maximums = new Integer[separatedString.length];
        counter3 = 0;
        for (String inProgress : separatedString) {
            int i = inProgress.indexOf("x");
            //System.out.println(i);
            if (i == 0){
                Character character = inProgress.charAt(1);
                if (character.equals('>')){
                    minimums[counter3] = Integer.parseInt(inProgress.substring(2,inProgress.length()));
                    maximums[counter3] = 9999999;
                }
                else if (character.equals('<')){
                    maximums[counter3] = Integer.parseInt(inProgress.substring(2,inProgress.length()));
                    minimums[counter3] = -9999999;
                }
            }
            else {
                maximums[counter3] = Integer.parseInt(inProgress.substring(i + 2, inProgress.length()));
                minimums[counter3] = Integer.parseInt(inProgress.substring(0, i - 1));
            }
            counter3++;
        }
        Integer min = minimums[0], max = maximums[0];
        for (counter4 = 0; counter4 < separatedString.length; counter4++){
            if(minimums[counter4] > min)
                min = minimums[counter4];
            if(maximums[counter4] < max)
                max = maximums[counter4];
        }
        if(max == 9999999){
            System.out.println("x>" + min);
            return;
        }
        if (min == -9999999){
            System.out.println("x<" + max);
            return;
        }
        if(min > max){
            System.out.println("0");
            return;
        }
        System.out.println(min + "<x<" + max);
    }
}
