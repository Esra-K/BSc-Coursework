package main;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Created by hp on 11/6/2017.
 */
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String string = scanner.nextLine();
        //System.out.println(string);
        String info = scanner.nextLine();
        String[] infos = info.split(" ");
        double info1 = toRadian(Double.parseDouble(infos[0]));
        double info2 = toRadian(Double.parseDouble(infos[1]));
        int shelterCount = Integer.parseInt(infos[2]);
        int preyNum = Integer.parseInt(scanner.nextLine());
        ArrayList<Prey> preyArrayList = new ArrayList<Prey>();
        ArrayList<Integer> reservedShelters = new ArrayList();
        int counter = 0;
        for (counter = 0; counter< preyNum; counter++){
            Prey prey = new Prey();
            String input = scanner.nextLine();
            //System.out.println("man daram prey migiram" + counter);
            String[] inputInProcess = input.split(" ");
            prey.setName(inputInProcess[0]);
            prey.setVelocity(Double.parseDouble(inputInProcess[1]));
            if(reservedShelters.contains(Integer.parseInt(inputInProcess[2]))){
                System.out.println("Amngah "+ inputInProcess[2]+ " pore");
            }
            else if(Integer.parseInt(inputInProcess[2]) <= shelterCount && Integer.parseInt(inputInProcess[2]) > 0){
                System.out.println(prey.getName() + " raft to Amngah " + inputInProcess[2]);
                reservedShelters.add(Integer.parseInt(inputInProcess[2]));
            }
            preyArrayList.add(counter, prey);
        }
        //System.out.println("they are the hunters we are the foxes");
        String justInCaseThisWasTheBug = scanner.nextLine();
        int hunterNum = Integer.parseInt(justInCaseThisWasTheBug);
        ArrayList<Hunter> hunterArrayList = new ArrayList<Hunter>();
        for (counter = 0; counter< hunterNum; counter++){
            Hunter hunter = new Hunter();
            String input = scanner.nextLine();
            String[] inputInProcess = input.split(" ");
            hunter.setName(inputInProcess[0]);
            hunter.setLat(Double.parseDouble(inputInProcess[1]));
            hunter.setLon(Double.parseDouble(inputInProcess[2]));
            hunter.setVision(Double.parseDouble(inputInProcess[3]));
            hunterArrayList.add(counter, hunter);
        }
        justInCaseThisWasTheBug = scanner.nextLine();
        int routeNum = Integer.parseInt(justInCaseThisWasTheBug);
        //System.out.println(justInCaseThisWasTheBug + "  justInCaseThisWasTheBug");
        List<Integer> integerArrayList = new ArrayList<Integer>();
        for (counter = 0; counter < routeNum; counter++){
            String input = scanner.nextLine();
            String[] inputInProcess = input.split(" ");
            int counter2 = 0;
            for (counter2 = 0; counter2 < preyNum; counter2++){
                if(inputInProcess[0].equals(preyArrayList.get(counter2).getName())){
                    preyArrayList.get(counter2).setAngle(Double.parseDouble(inputInProcess[1]));
                    preyArrayList.get(counter2).setTime(Double.parseDouble(inputInProcess[2]));
                    integerArrayList.add(counter2);
                }
            }
        }
        for (counter = 0; counter < preyNum; counter++){
            if(integerArrayList.contains(counter)){
                Double lat2 = lat2(info1,preyArrayList.get(counter).getVelocity()*preyArrayList.get(counter).getTime(), preyArrayList.get(counter).getAngle());
                Double lon2 = lon2(info2, info1, lat2,preyArrayList.get(counter).getVelocity()*preyArrayList.get(counter).getTime(), preyArrayList.get(counter).getAngle());
                preyArrayList.get(counter).setFinalLat(lat2);
                preyArrayList.get(counter).setFinalLon(lon2);
                int counter3;
                for(counter3 = 0; counter3 < hunterNum; counter3++){
                    double distance = distance(preyArrayList.get(counter).getFinalLat(), preyArrayList.get(counter).getFinalLon(),hunterArrayList.get(counter3).getLat(),hunterArrayList.get(counter3).getLon() );
                    if(hunterArrayList.get(counter3).getVision() < toDegree(distance)){
                        System.out.println(hunterArrayList.get(counter3).getName() + " " + preyArrayList.get(counter).getName() + " ro gereft");
                    }
                }
            }
        }
    }
    static double distance(double lat1 , double lon1 , double lat2 , double lon2){
        return 6371 * Math.acos((Math.sin(lat1)*Math.sin(lat2))+(Math.cos(lat1)*
                Math.cos(lat2)*Math.cos(lon2 - lon1)));
    }
    static double lat2(double lat1 , double distance , double t){
        return Math.asin((Math.sin(lat1)*Math.cos(distance /6371)) + Math.cos(lat1)
                *Math.sin(distance /6371)*Math.cos(t));
    }
    static double lon2(double lon1 , double lat1 , double lat2 , double distance , double t){
        return lon1 + Math.atan2(Math.sin(t)*Math.sin(distance /6371)*Math.cos(lat1
        ),Math.cos(distance /6371) -(Math.sin(lat1)*Math.sin(lat2)));
    }
    static double toRadian(double d){
        return d*Math.PI/180;
    }
    static double toDegree(double d){
        return d*180/Math.PI;
    }
}
class Prey{
    String name;
    int shelterIndex;
    double velocity;
    double angle;
    double time;
    double finalLat;
    double finalLon;

    public void setFinalLat(double finalLat) {
        this.finalLat = finalLat;
    }

    public void setFinalLon(double finalLon) {
        this.finalLon = finalLon;
    }

    public double getFinalLat() {
        return finalLat;
    }

    public double getFinalLon() {
        return finalLon;
    }

    public void setAngle(double angle) {
        this.angle = toRadian(angle);
    }

    public void setTime(double time) {
        this.time = time;
    }

    public double getAngle() {
        return angle;
    }

    public double getTime() {
        return time;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setShelterIndex(int shelterIndex) {
        this.shelterIndex = shelterIndex;
    }

    public void setVelocity(double velocity) {
        this.velocity = velocity;
    }

    public String getName() {
        return name;
    }

    public double getVelocity() {
        return velocity;
    }

    public int getShelterIndex() {
        return shelterIndex;
    }
    static double toRadian(double d){
        return d*Math.PI/180;
    }
    static double toDegree(double d){
        return d*180/Math.PI;
    }
}
class Hunter{
    String name;
    double lat;
    double lon;
    double vision;

    public void setName(String name) {
        this.name = name;
    }

    public void setLat(double lat) {
        this.lat = toRadian(lat);
    }

    public void setLon(double lon) {
        this.lon = toRadian(lon);
    }

    public void setVision(double vision) {
        this.vision = vision;
    }

    public String getName() {
        return name;
    }

    public double getLat() {
        return lat;
    }

    public double getLon() {
        return lon;
    }

    public double getVision() {
        return vision;
    }
    static double toRadian(double d){
        return d*Math.PI/180;
    }
    static double toDegree(double d){
        return d*180/Math.PI;
    }
}
