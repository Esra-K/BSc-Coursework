import javafx.scene.Group;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.Pane;

/**
 * Created by hp on 11/18/2017.
 */
// Takhire sarbazan: sathe 1: 6s  sathe 2: 4s  sathe3: 2s;
public class Soldier extends SpriteBase{
    int ID;
    int Experience;
    double shootingSpeed;
    double Radius;
    int bulletPower;
    public Soldier(int i, Group root, Image image,Double Width, Double Height, Double x, Double y, Double r, Double dx, Double dy, Double dr, Double health, Double damage){
        super(root, image,Width, Height,x, y, r, dx, dy, dr, health, damage);
        this.setID(i);
        this.setHealth(150.0);
        this.setShootingSpeed(5);
        this.setBulletPower(10);
        this.setAntiSpeed(100);
        this.setRadius(0.5);
    }

    public void Update(Player hero){
        double x = hero.getX();
        double y = hero.getY();
        switch (this.getID()){
            case 0:
                this.x = x;
                this.y = y + 87;
                break;
            case 1:
                this.x = x + (Math.pow(3, 0.5)/2)*100;
                this.y = y - 50;
                break;
            case 2:
                this.x = x - (Math.pow(3, 0.5)/2)*100;
                this. y = y - 50;
                break;
        }
        updateUI();
    }
    public void setID(int ID) {
        this.ID = ID;
    }

    public int getID() {
        return ID;
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





    @Override
    public boolean collidesWith(SpriteBase otherSprite) {
        return false;
    }

    @Override
    public void checkRemovability() {
            if(this.health <= 0.){
                this.getView().setVisible(false);
                try {
                    Thread.sleep(6 - 2*(Player.level - 1));
                } catch (InterruptedException e) {
                    System.out.println("JDK keili gij ast");
                }
            }
    }
}
