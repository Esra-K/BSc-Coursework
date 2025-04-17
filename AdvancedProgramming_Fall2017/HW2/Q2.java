package main;

import java.util.*;

/**
 * Created by hp on 10/31/2017.
 */
class User{
    private String name;
    private int age;
    private String city;
    private List<String> album;
    User(){
        //System.out.println("ana user constructor");
        album = new ArrayList<String>();
    }
    public void removeLastElement(ArrayList arrayList){
        arrayList.remove(arrayList.size() - 1);
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public List<String> getAlbum() {
        return album;
    }

    public void setAlbum(List<String> album) {
        this.album = album;
    }
}
class Album{
    private String name;
    private String artist;
    private String genre;
    private int songCount;
    Album(){
       // System.out.println("ana album constructor");
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setGenre(String genre) {
        this.genre = genre;
    }

    public String getGenre() {
        return genre;
    }

    public void setArtist(String artist) {
        this.artist = artist;
    }

    public String getArtist() {
        return artist;
    }

    public void setSongCount(int songCount) {
        this.songCount = songCount;
    }

    public int getSongCount() {
        return songCount;
    }
}
public class Main {
    public static void main(String[] args) throws Exception{
        Scanner scanner = new Scanner(System.in);
        int userCount = Integer.parseInt(scanner.nextLine());
        int albumCount = 0;
       // System.out.println("userCount: " + userCount);
        User[] users = new User[userCount];
        int counter;
        String getName = scanner.nextLine();
        for(counter = 0; counter < userCount; counter++){
            users[counter] = new User();
            users[counter].setName(getName.substring(8));
            //System.out.println(users[counter].getName());
            users[counter].setAge(Integer.parseInt(scanner.nextLine().substring(5)));
            //System.out.println(users[counter].getAge());
            users[counter].setCity(scanner.nextLine().substring(6));
            //System.out.println(users[counter].getCity());
            List<String> list = new ArrayList<String>();
            String string  = scanner.nextLine();
            string = scanner.nextLine();
            while (string.length() >= 8 ? !(string.substring(0,8).equals("- name: ")) : !(isInt(string))){
                list.add(string.substring(2));
                string = scanner.nextLine();
            }
            if(string.length() >= 8 ? string.substring(0,8).equals("- name: "): false){
                getName = string;
                //list.remove(list.size() - 1);
                users[counter].setAlbum(list);
                //System.out.println(users[counter].getAlbum());
                continue;
            }
            albumCount = Integer.parseInt(string);
            //System.out.println(albumCount);
            //list.remove(list.size() - 1);
            users[counter].setAlbum(list);
            //System.out.println(users[counter].getAlbum());
        }
        Album[] albums = new Album[albumCount];
        for (counter = 0;counter < albumCount; counter++){
            albums[counter] = new Album();
            albums[counter].setName(scanner.nextLine().substring(8));
            //System.out.println(albums[counter].getName());
            albums[counter].setArtist(scanner.nextLine().substring(8));
            //System.out.println(albums[counter].getArtist());
            albums[counter].setGenre(scanner.nextLine().substring(7));
            //System.out.println(albums[counter].getGenre());
            albums[counter].setSongCount(Integer.parseInt(scanner.nextLine().substring(8)));
            //System.out.println(albums[counter].getSongCount());
        }
        int questionCount = Integer.parseInt(scanner.nextLine());
        //Thread.sleep(3000);
        //System.out.println("man shomare soalato gereftam");
        //Thread.sleep(1000);
        String [] strings = new String[questionCount];
        int output = 0;
        for (counter = 0; counter < questionCount; counter++){
            String string = scanner.nextLine();
            String[] splitString = string.split(" ");
            int whatQuestion = Integer.parseInt(splitString[0]);
            int Counter2 = 0, Counter3 = 0, Counter4 = 0;
                if(whatQuestion == 1 || whatQuestion == 2){
                    for (Counter2 = 0; Counter2 < userCount; Counter2++) {
                        if (users[Counter2].getName().equals(splitString[1])){
                           for (Counter3 = 0; Counter3<albumCount; Counter3++){
                               if(users[Counter2].getAlbum().contains(albums[Counter3].getName()))
                               {
                                   if(whatQuestion%2 == 1 && albums[Counter3].getArtist().equals(splitString[2]))
                                   output+= albums[Counter3].getSongCount();
                                   if(whatQuestion%2 == 0 && albums[Counter3].getGenre().equals(splitString[2]))
                                       output+= albums[Counter3].getSongCount();
                               }
                           }
                           }
                        }
                    }
                if(whatQuestion == 3 || whatQuestion == 4){
                    for (Counter2 = 0; Counter2 < userCount; Counter2++) {
                        if (users[Counter2].getAge() == (Integer.parseInt(splitString[1]))){
                            for (Counter3 = 0; Counter3<albumCount; Counter3++){
                                if(users[Counter2].getAlbum().contains(albums[Counter3].getName()))
                                {
                                    if(whatQuestion%2 == 1 && albums[Counter3].getArtist().equals(splitString[2]))
                                        output+= albums[Counter3].getSongCount();
                                    if(whatQuestion%2 == 0 && albums[Counter3].getGenre().equals(splitString[2]))
                                        output+= albums[Counter3].getSongCount();
                                }
                            }
                        }
                    }
                }
                if(whatQuestion == 5 || whatQuestion == 6){
                    for (Counter2 = 0; Counter2 < userCount; Counter2++) {
                        if (users[Counter2].getCity().equals(splitString[1])){
                            for (Counter3 = 0; Counter3<albumCount; Counter3++){
                                if(users[Counter2].getAlbum().contains(albums[Counter3].getName()))
                                {
                                    if(whatQuestion%2 == 1 && albums[Counter3].getArtist().equals(splitString[2]))
                                        output+= albums[Counter3].getSongCount();
                                    if(whatQuestion%2 == 0 && albums[Counter3].getGenre().equals(splitString[2]))
                                        output+= albums[Counter3].getSongCount();
                                }
                            }
                        }
                    }
                }
        }
        System.out.println(output);
    }
    public static boolean isInt(String string){
       return string != null && string.matches("[-+]?\\d*\\.?\\d+");
    };
}

