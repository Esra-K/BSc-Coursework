
import com.sun.xml.internal.ws.api.config.management.policy.ManagedServiceAssertion;
import javafx.scene.Group;
import javafx.scene.image.Image;

/**
 * Created by hp on 1/22/2018.
 */
public class Enemy extends SpriteBase {
    public static boolean GAMEOVER;
    public static int GameOverCountDown;
    double[][] path;
    int pathSegment;
    double pathPointer;
    boolean self_defense;
    String name;
    double soratTirandazi;
    int ghodrat;
    int shomareMasir;

    public Enemy(int i, Group root, Image image,Double Width, Double Height, double x, double y, double r, double dx, double dy, double dr, double health, double damage, double speed) {
        super(root, image,Width, Height,x,y, r, dx, dy, dr, health,damage);
        switch (i){
            case 0:{
                this.setName("Activionion");
                //this.setImageView(Images.Images.Act[0]);
                this.setHealth(400.);
                this.setSpeed(2.);
                this.setSoratTirandazi(2);
                this.setGhodrat(40);
            }
            case 1:{
                this.setName("Aironion");
                //this.setImageView(Images.Images.Air[0]);
                this.setHealth(200.);
                this.setSpeed(5.);
                this.setGhodrat(5);
                this.setSoratTirandazi(20);
            }
            case 2:{
                this.setName("Albertonion");
                //this.setImageView(Images.Images.Alb[0]);
                this.setHealth(250.);
                this.setSpeed(8.);
                this.setSoratTirandazi(5);
                this.setGhodrat(7);
            }
            case 3:{
                this.setName("Algwasonion");
                //this.setImageView(Images.Images.Alg[0]);
                this.setHealth(150.);
                this.setSpeed(4.);
                this.setSoratTirandazi(10);
                this.setGhodrat(25);
            }
        }
        self_defense = false;
        pathPointer = 0.;
        pathSegment = 1;
    }

    @Override
    public void checkRemovability() {
        if( Double.compare( getY(), Settings.SCENE_HEIGHT ) > 0) {
            setRemovable(true);
        }
    }

    public boolean isSelf_defense() {
        return self_defense;
    }

    public void setSelf_defense(boolean self_defense) {
        this.self_defense = self_defense;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getSoratTirandazi() {
        return soratTirandazi;
    }

    public void setSoratTirandazi(double soratTirandazi) {
        this.soratTirandazi = soratTirandazi;
    }

    public int getGhodrat() {
        return ghodrat;
    }

    public void setGhodrat(int ghodrat) {
        this.ghodrat = ghodrat;
    }

    public int getShomareMasir() {
        return shomareMasir;
    }

    public void setShomareMasir(int shomareMasir) {
        this.shomareMasir = shomareMasir;
    }

    public double[][] getPath() {
        return path;
    }

    public void setPath(double[][] path) {
        this.path = path;
    }


    public int getPathSegment() {
        return pathSegment;
    }

    public void setPathSegment(int pathSegment) {
        this.pathSegment = pathSegment;
    }

    public double getPathPointer() {
        return pathPointer;
    }

    public void setPathPointer(double pathPointer) {
        this.pathPointer = pathPointer;
    }

    @Override
    public void move(){
        if(pathSegment >= path.length){
            Enemy.GameOverCountDown++;
            this.getView().setVisible(false);
            if(Enemy.GameOverCountDown >= 5){
                System.out.println("Shoma Bakhtid");
                Enemy.GAMEOVER = true;
                return;
            }
            removable = true;
            return;
        }
         if(Math.abs(pathPointer) > Math.abs(H(path[pathSegment][0])*path[pathSegment][0] + H((path[pathSegment][1]))*path[pathSegment][1])) {
             //this.removable = true;
             //this.getView().setVisible(false);
             pathSegment++;
             pathPointer = 0.;
             return;
         }
         dx = H(path[pathSegment][0]) * this.speed;
         dy = H(path[pathSegment][1]) * this.speed;
        pathPointer = pathPointer + (dx + dy);
         super.move();

    }

    int H(double d){
        if(d < -0.01)
            return -1;
        else if(0.01 > d && d > -0.01)
            return 0;
        else
            return 1;
    }
    @Override
    public boolean collidesWith(SpriteBase otherSpriteBase){
        return false;
    }
    public void shoot(Player player){
        player.health -= this.soratTirandazi*this.ghodrat;

        for(Soldier soldier: player.soldiers){
            soldier.health -= this.soratTirandazi*this.ghodrat;
            if(player.health <= 0){
                soldier.imageView.setVisible(false);
                double t = System.nanoTime();
                while (true){
                    double a = System.nanoTime();
                    if(a - t >= 6000000000.){
                        soldier.imageView.setVisible(false);
                    }
                }
            }
        }
    }
}