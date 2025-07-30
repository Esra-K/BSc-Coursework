
import Images.Images;
import javafx.scene.Group;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.stage.Screen;

import java.util.ArrayList;
import java.util.List;


/**
 * Created by hp on 1/22/2018.
 */
public class Player extends SpriteBase {
    List<Soldier> soldiers = new ArrayList<Soldier>();
    double playerShipMinX;
    double playerShipMaxX;
    double playerShipMinY;
    double playerShipMaxY;

    Input input;


    int Experience;
    double shootingSpeed;
    double Radius;
    int bulletPower;


    int victim;
    static int money;
    static int level;
    boolean MouseEntered;
    // Be vasileye Hero
    boolean shekarchiAzam;
    boolean jeneKhoob;
    boolean elaheShekar;
    boolean chesheOghab;
    // Be vasileye Taslihat
    boolean shellikKonandeBirahm;
    boolean jangavereDelavar;
    boolean sallakh;
    boolean khoonkhar;

    public Player(Group root, Image image,Double Width, Double Height, double x, double y, double r, double dx, double dy, double dr, double health, double damage, double speed, Input input, List<Soldier> soldiers) {
        super(root, image, Width, Height, x, y, r, dx, dy, dr, health,damage);
        Player.level = 1;
        Falsify();
        this.health = 100.0;
        this.speed = speed;
        this.input = input;
        init();
        this.setLevel(1);
        this.setMoney(0);
        this.setShootingSpeed(7);
        this.setBulletPower(20);
        this.setAntiSpeed(100);
        this.setRadius(0.5);
        MouseEntered = false;
    }

    public double getPlayerShipMinX() {
        return playerShipMinX;
    }

    public void setPlayerShipMinX(double playerShipMinX) {
        this.playerShipMinX = playerShipMinX;
    }

    public double getPlayerShipMaxX() {
        return playerShipMaxX;
    }

    public void setPlayerShipMaxX(double playerShipMaxX) {
        this.playerShipMaxX = playerShipMaxX;
    }

    public double getPlayerShipMinY() {
        return playerShipMinY;
    }

    public void setPlayerShipMinY(double playerShipMinY) {
        this.playerShipMinY = playerShipMinY;
    }

    public double getPlayerShipMaxY() {
        return playerShipMaxY;
    }

    public void setPlayerShipMaxY(double playerShipMaxY) {
        this.playerShipMaxY = playerShipMaxY;
    }

    public Input getInput() {
        return input;
    }

    public void setInput(Input input) {
        this.input = input;
    }

    public void setSpeed(double speed) {
        this.speed = speed;
    }

    public int getExperience() {
        return Experience;
    }

    public void setExperience(int experience) {
        Experience = experience;
    }

    public double getShootingSpeed() {
        return shootingSpeed;
    }

    public void setShootingSpeed(double shootingSpeed) {
        this.shootingSpeed = shootingSpeed;
    }

    public double getRadius() {
        return Radius;
    }

    public void setRadius(double radius) {
        Radius = radius;
    }

    public int getBulletPower() {
        return bulletPower;
    }

    public void setBulletPower(int bulletPower) {
        this.bulletPower = bulletPower;
    }

    public int getVictim() {
        return victim;
    }

    public void setVictim(int victim) {
        this.victim = victim;
    }

    public int getMoney() {
        return money;
    }

    public void setMoney(int money) {
        this.money = money;
    }

    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }

    public boolean isMouseEntered() {
        return MouseEntered;
    }

    public void setMouseEntered(boolean mouseEntered) {
        MouseEntered = mouseEntered;
    }

    public boolean isShekarchiAzam() {
        return shekarchiAzam;
    }

    public void setShekarchiAzam(boolean shekarchiAzam) {
        this.shekarchiAzam = shekarchiAzam;
    }

    public boolean isJeneKhoob() {
        return jeneKhoob;
    }

    public void setJeneKhoob(boolean jeneKhoob) {
        this.jeneKhoob = jeneKhoob;
    }

    public boolean isElaheShekar() {
        return elaheShekar;
    }

    public void setElaheShekar(boolean elaheShekar) {
        this.elaheShekar = elaheShekar;
    }

    public boolean isChesheOghab() {
        return chesheOghab;
    }

    public void setChesheOghab(boolean chesheOghab) {
        this.chesheOghab = chesheOghab;
    }

    public boolean isShellikKonandeBirahm() {
        return shellikKonandeBirahm;
    }

    public void setShellikKonandeBirahm(boolean shellikKonandeBirahm) {
        this.shellikKonandeBirahm = shellikKonandeBirahm;
    }

    public boolean isJangavereDelavar() {
        return jangavereDelavar;
    }

    public void setJangavereDelavar(boolean jangavereDelavar) {
        this.jangavereDelavar = jangavereDelavar;
    }

    public boolean isSallakh() {
        return sallakh;
    }

    public void setSallakh(boolean sallakh) {
        this.sallakh = sallakh;
    }

    public boolean isKhoonkhar() {
        return khoonkhar;
    }

    public void setKhoonkhar(boolean khoonkhar) {
        this.khoonkhar = khoonkhar;
    }

    private void init() {
        // calculate movement bounds of the player ship
        // allow half of the ship to be outside of the screen
        playerShipMinX = 0 - image.getWidth() / 2.0;
        playerShipMaxX = Screen.getPrimary().getVisualBounds().getHeight()*1.618 - image.getWidth() / 2.0;
        playerShipMinY = 0 - image.getHeight() / 2.0;
        playerShipMaxY =  Screen.getPrimary().getVisualBounds().getHeight() - image.getHeight() / 2.0;
    }

    public void processInput() {

        // vertical direction
        if( input.isMoveUp()) {
            this.image = Images.heroUp.getImage();
            //this.imageView = Images.heroUp;
            for(Soldier soldier: soldiers){

                System.out.println("==========================================================================");
            }
            dy = -speed;
        } else if( input.isMoveDown()) {
            this.image = Images.heroDown.getImage();
            //this.imageView = Images.heroDown;
            dy = speed;
            for(Soldier soldier: soldiers)
                soldier.image = Images.PrivateDown.getImage();
        } else {
            dy = 0d;
        }

        // horizontal direction
        if( input.isMoveLeft()) {
            //this.imageView = Images.heroLeft;
            this.image = Images.heroLeft.getImage();
            for(Soldier soldier: soldiers)
                soldier.image = Images.PrivateLeft.getImage();
            dx = -speed;
        } else if( input.isMoveRight()) {
            this.image = Images.heroRight.getImage();
            //this.imageView = Images.heroRight;
            for(Soldier soldier: soldiers)
                soldier.image = Images.PrivateRight.getImage();
            dx = speed;
        } else {
            dx = 0d;
        }

    }

    @Override
    public void move() {
        super.move();
        checkBounds();
    }

    private void checkBounds() {
        if( Double.compare( y, playerShipMinY) < 0) {
            y = playerShipMinY;
        } else if( Double.compare(y, playerShipMaxY) > 0) {
            y = playerShipMaxY;
        }
        if( Double.compare( x, playerShipMinX + 75) < 0) {
            x = playerShipMinX;
        } else if( Double.compare(x, playerShipMaxX + 75) > 0) {
            x = playerShipMaxX;
        }
    }
    @Override
    public boolean collidesWith(SpriteBase otherSprite) {
        return(Math.pow(this.getCenterX() - otherSprite.getCenterX(), 2) + Math.pow(this.getCenterX() - otherSprite.getCenterX(), 2) < Math.pow(25,2));
    }

    @Override
    public void checkRemovability(){

    }
    public void Falsify(){
        shekarchiAzam = false;
        jeneKhoob = false;
        sallakh = false;
        shellikKonandeBirahm = false;
        jeneKhoob = false;
    }
    public void shoot(List<Enemy> enemies){
        for(Enemy enemy: enemies){
            if(this.collidesWith(enemy)){
                switch (enemy.name){
                    case "Activionion":{
                        enemy.shoot(enemy.dx, 20* 7,Images.ActDie1.getImage());
                        enemy.shoot(this);
                        System.out.println("I SET FIRE TO THE GAME");
                        break;
                    }
                    case "Aironion":{
                        enemy.shoot(enemy.dx, 0.,Images.Air1.getImage());
                        enemy.shoot(this);
                        System.out.println("I SET FIRE TO THE GAME");
                        break;
                    }
                    case "Albertonion":{
                        enemy.shoot(enemy.dx, 20* 7,Images.AlbDie1.getImage());
                        enemy.shoot(this);
                        System.out.println("I SET FIRE TO THE GAME");
                        break;
                    }
                    case "Algwasonion":{
                        enemy.shoot(enemy.dx, 20* 7,Images.AlgDie1.getImage());
                        enemy.shoot(this);
                        System.out.println("I SET FIRE TO THE GAME");
                        break;
                    }
                }
            }
        }
    }

}