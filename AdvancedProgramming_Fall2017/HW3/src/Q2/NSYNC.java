package Q2;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Random;
import java.util.Scanner;
import java.util.concurrent.CyclicBarrier;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.SynchronousQueue;

//import static Q2.NSYNC.cyclicBarrier;
import static Q2.NSYNC.money;

/**
 * Created by hp on 12/15/2017.
 */
public class NSYNC {
    public static int money = 5000;
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int counter;
        int bros = Integer.parseInt(scanner.nextLine());
        ExecutorService executorService = Executors.newFixedThreadPool(bros);
        BrosThread[] Bros = new BrosThread[bros];
        for (counter = 0; counter < bros; counter++){
            Bros[counter] = new BrosThread(counter);
            //System.out.println("make the bros");
        }
        int commands = Integer.parseInt(scanner.nextLine());
        for (counter = 0; counter < commands; counter++){
            String s1 = scanner.nextLine();
            String[] s2 = s1.split(" ");
            Bros[Integer.parseInt(s2[0])].arrayList.add(Integer.parseInt(s2[1]));
            //System.out.println(Integer.parseInt(s2[1]) + " add shod be " + Integer.parseInt(s2[0]) );
        }
        for (counter = 0; counter < bros; counter++){
            executorService.execute(Bros[counter]);
            //System.out.println(counter + " dare Execute mishe");
        }
        executorService.shutdown();
    }
}
class BrosThread extends Thread{
    int id;
    ArrayList<Integer> arrayList = new ArrayList<Integer>();
    int check;
    BrosThread(int id){
        this.id = id;
        check = 0;
    }
    public synchronized void update(int a){
        //System.out.println("UPDATED");
        money += a;
        System.out.println(id + " " + money + " " + a);
        randomWait();
    }

    @Override
    public synchronized void run() {
            try {
                    for(int counter = 0; counter < arrayList.size(); counter++){
                        update(arrayList.get(counter));
                        //System.out.println("try catch");
                        //System.out.println(id + "");
                    }
            } catch (Exception e) {
                e.printStackTrace();
            }
    }
    private void randomWait() {
        try {
            //System.out.println("WAIT!");
            sleep((long)(3000*Math.random()));
        } catch (InterruptedException x) {
            x.printStackTrace();
        }
    }
}