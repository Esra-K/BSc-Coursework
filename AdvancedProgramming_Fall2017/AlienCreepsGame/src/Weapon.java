
import Images.Images;
import javafx.scene.Group;
import javafx.scene.image.Image;
import javafx.scene.layout.Pane;

import java.util.List;

/**
 * Created by hp on 11/18/2017.
 */
public class Weapon extends SpriteBase {
    String name;
    int shootingSpeed;
    int airPower;
    int landPower;
    int price;
    int counterSpeed;
    double radius;

    public Weapon(int i, Group root, Image image,Double Width, Double Height, double x, double y, double r, double dx, double dy, double dr, double health, double damage, double speed) {
        super(root, image,Width, Height, x, y, r, dx, dy, dr, health,damage);
        this.imageView.setFitHeight(150);
        this.imageView.setFitWidth(100);
        this.speed = 0.;
        switch (i){
            case 0:
            {
                this.setName("Rocket");
                this.setSpeed(3);
                this.setAirPower(10);
                this.setLandPower(20);
                this.setPrice(180);
                this.setCounterSpeed(0);
                this.setRadius(2);
            }
            case 1:{
                this.setName("AntiAircraft");
                this.setSpeed(15);
                this.setAirPower(12);
                this.setPrice(180);
                this.setCounterSpeed(20);
                this.setRadius(1.5);
            }
            case 2:{
                this.setName("Freezer");
                this.setSpeed(5);
                this.setAirPower(3);
                this.setLandPower(5);
                this.setPrice(170);
                this.setCounterSpeed(60);
                this.setRadius(1);
            }
            case 3:{
                this.setName("Laser");
                this.setSpeed(7);
                this.setAirPower(7);
                this.setLandPower(10);
                this.setPrice(150);
                this.setCounterSpeed(40);
                this.setRadius(1.5); //TODO: IN CHI BOOD?
            }
            case 4:{
                this.setName("Machine_Gun");
                this.setSpeed(10);
                this.setAirPower(5);
                this.setLandPower(10);
                this.setPrice(100);
                this.setCounterSpeed(0);
                this.setRadius(1);
            }
        }
    }
    public void setLandPower(int landPower) {
        this.landPower = landPower;
    }

    public void setAirPower(int airPower) {
        this.airPower = airPower;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public void setCounterSpeed(int counterSpeed) {
        this.counterSpeed = counterSpeed;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }

    public void setSpeed(int speed) {
        this.shootingSpeed = speed;
    }

    public int getPrice() {
        return price;
    }

    public int getCounterSpeed() {
        return counterSpeed;
    }

    public double getRadius() {
        return radius;
    }

    public int getShootingSpeed() {
        return shootingSpeed;
    }

    public int getLandPower() {
        return landPower;
    }

    public int getAirPower() {
        return airPower;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setShootingSpeed(int shootingSpeed) {
        this.shootingSpeed = shootingSpeed;
    }

    @Override
    public boolean collidesWith(SpriteBase otherSprite) {
        return(Math.pow(this.getCenterX() - otherSprite.getCenterX(), 2) + Math.pow(this.getCenterX() - otherSprite.getCenterX(), 2) < Math.pow(this.radius,2));
    }

    @Override
    public void checkRemovability() {

    }
    public void shoot(List<Enemy> enemies){
        for(Enemy enemy: enemies){
            if(this.collidesWith(enemy)){
                switch (this.name){
                    case"Rocket":{
                        switch (enemy.name){
                            case "Activionion":{
                                enemy.shoot(enemy.dx, 20* 7, Images.ActDie1.getImage());
                                System.out.println("///////////////////////////////////////////////");
                                break;
                            }
                            case "Aironion":{
                                enemy.shoot(enemy.dx, 0.,Images.Air1.getImage());
                                System.out.println("//////////////////////////////////////////////////");
                                break;
                            }
                            case "Albertonion":{
                                enemy.shoot(enemy.dx, 20* 7,Images.AlbDie1.getImage());
                                System.out.println("/////////////////////////////////////////////////////");
                                break;
                            }
                            case "Algwasonion":{
                                enemy.shoot(enemy.dx, 20* 7,Images.AlgDie1.getImage());
                                System.out.println("///////////////////////////////////////////////////");
                                break;
                            }
                        }
                        break;
                    }
                    case"AntiAircraft":{
                        switch (enemy.name){
                            case "Activionion":{
                                enemy.shoot(enemy.dx, 20* 7, Images.ActDie1.getImage());
                                System.out.println("///////////////////////////////////////////////");
                                break;
                            }
                            case "Aironion":{
                                enemy.shoot(enemy.dx, 0.,Images.Air1.getImage());
                                System.out.println("//////////////////////////////////////////////////");
                                break;
                            }
                            case "Albertonion":{
                                enemy.shoot(enemy.dx, 20* 7,Images.AlbDie1.getImage());
                                System.out.println("/////////////////////////////////////////////////////");
                                break;
                            }
                            case "Algwasonion":{
                                enemy.shoot(enemy.dx, 20* 7,Images.AlgDie1.getImage());
                                System.out.println("///////////////////////////////////////////////////");
                                break;
                            }
                        }
                        break;
                    }
                    case"Freezer":{
                        switch (enemy.name){
                            case "Activionion":{
                                enemy.shoot(enemy.dx, 20* 7, Images.ActDie1.getImage());
                                System.out.println("///////////////////////////////////////////////");
                                break;
                            }
                            case "Aironion":{
                                enemy.shoot(enemy.dx, 0.,Images.Air1.getImage());
                                System.out.println("//////////////////////////////////////////////////");
                                break;
                            }
                            case "Albertonion":{
                                enemy.shoot(enemy.dx, 20* 7,Images.AlbDie1.getImage());
                                System.out.println("/////////////////////////////////////////////////////");
                                break;
                            }
                            case "Algwasonion":{
                                enemy.shoot(enemy.dx, 20* 7,Images.AlgDie1.getImage());
                                System.out.println("///////////////////////////////////////////////////");
                                break;
                            }
                        }
                        break;
                    }
                    case"Laser":{
                        switch (enemy.name){
                            case "Activionion":{
                                enemy.shoot(enemy.dx, 20* 7, Images.ActDie1.getImage());
                                System.out.println("///////////////////////////////////////////////");
                                break;
                            }
                            case "Aironion":{
                                enemy.shoot(enemy.dx, 0.,Images.Air1.getImage());
                                System.out.println("//////////////////////////////////////////////////");
                                break;
                            }
                            case "Albertonion":{
                                enemy.shoot(enemy.dx, 20* 7,Images.AlbDie1.getImage());
                                System.out.println("/////////////////////////////////////////////////////");
                                break;
                            }
                            case "Algwasonion":{
                                enemy.shoot(enemy.dx, 20* 7,Images.AlgDie1.getImage());
                                System.out.println("///////////////////////////////////////////////////");
                                break;
                            }
                        }
                        break;
                    }
                    case"Machine_Gun":{
                        switch (enemy.name){
                            case "Activionion":{
                                enemy.shoot(enemy.dx, 20* 7, Images.ActDie1.getImage());
                                System.out.println("///////////////////////////////////////////////");
                                break;
                            }
                            case "Aironion":{
                                enemy.shoot(enemy.dx, 0.,Images.Air1.getImage());
                                System.out.println("//////////////////////////////////////////////////");
                                break;
                            }
                            case "Albertonion":{
                                enemy.shoot(enemy.dx, 20* 7,Images.AlbDie1.getImage());
                                System.out.println("/////////////////////////////////////////////////////");
                                break;
                            }
                            case "Algwasonion":{
                                enemy.shoot(enemy.dx, 20* 7,Images.AlgDie1.getImage());
                                System.out.println("///////////////////////////////////////////////////");
                                break;
                            }
                        }
                        break;
                    }
                }
            }
        }
    }

}
