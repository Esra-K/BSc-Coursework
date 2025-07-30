import javafx.scene.Group;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.Pane;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by hp on 1/22/2018.
 */
public abstract class SpriteBase{

    Image image;
    ImageView imageView;
    double speed;
    Group root;
    final double WhenIWasFine; //healthe avvalie
    double antiSpeed;
    Double x;
    Double y;
    Double r;

    Double dx;
    Double dy;
    Double dr;

    Double health;
    Double damage;

    boolean removable = false;

    Double w;
    Double h;

    boolean canMove = true;

    public SpriteBase(Group root, Image image, Double Width, Double Height, Double x, Double y, Double r, Double dx, Double dy, Double dr, Double health, Double damage){//, Double antiSpeed
        //this.antiSpeed = antiSpeed;
        double time = System.nanoTime();
        WhenIWasFine = health;
        this.health = health;
        this.root = root;
        this.image = image;
        this.x = x;
        this.y = y;
        this.r = r;
        this.dx = dx;
        this.dy = dy;
        this.dr = dr;

        this.health = health;
        this.damage = damage;

        this.imageView = new ImageView(image);
        this.imageView.setFitHeight(Height);
        this.imageView.setFitWidth(Width);
        this.imageView.relocate(x, y);
        this.imageView.setRotate(r);
        //imageView.setOnMouseEntered(event -> System.out.println("I'M WORKING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"));
        this.w = image.getWidth(); // imageView.getBoundsInParent().getWidth();
        this.h = image.getHeight(); // imageView.getBoundsInParent().getHeight();

        addToLayer();
    }

    public void addToLayer() {
        this.root.getChildren().add(this.imageView);
    }

    public void removeFromLayer() {
        this.root.getChildren().remove(this.imageView);
    }

    public Image getImage() {
        return image;
    }

    public void setImage(Image image) {
        this.image = image;
    }

    public ImageView getImageView() {
        return imageView;
    }

    public void setImageView(ImageView imageView) {
        this.imageView = imageView;
    }

    public Group getRoot() {
        return root;
    }

    public void setRoot(Group root) {
        this.root = root;
    }

    public Double getW() {
        return w;
    }

    public void setW(Double w) {
        this.w = w;
    }

    public Double getH() {
        return h;
    }

    public void setH(Double h) {
        this.h = h;
    }

    public boolean isCanMove() {
        return canMove;
    }

    public void setCanMove(boolean canMove) {
        this.canMove = canMove;
    }

    public Double getX() {
        return x;
    }

    public void setX(Double x) {
        this.x = x;
    }

    public Double getY() {
        return y;
    }

    public void setY(Double y) {
        this.y = y;
    }

    public Double getR() {
        return r;
    }

    public void setR(Double r) {
        this.r = r;
    }

    public Double getDx() {
        return dx;
    }

    public void setDx(Double dx) {
        this.dx = dx;
    }

    public Double getDy() {
        return dy;
    }

    public void setDy(Double dy) {
        this.dy = dy;
    }

    public Double getDr() {
        return dr;
    }

    public void setDr(Double dr) {
        this.dr = dr;
    }

    public Double getHealth() {
        return health;
    }

    public Double getDamage() {
        return damage;
    }

    public void setDamage(Double damage) {
        this.damage = damage;
    }

    public void setHealth(Double health) {
        this.health = health;
    }

    public boolean isRemovable() {
        return removable;
    }

    public void setRemovable(boolean removable) {
        this.removable = removable;
    }

    public void move() {
        if( !canMove)
            return;
        x += dx;
        y += dy;
        r += dr;
        updateUI();
    }

    public boolean isAlive() {
        return Double.compare(health, 0) > 0;
    }

    public ImageView getView() {
        return imageView;
    }

    public void updateUI() {
        imageView.setImage(image);
        imageView.relocate(x, y);
        imageView.setRotate(r);

    }

    public Double getWidth() {
        return w;
    }

    public Double getHeight() {
        return h;
    }

    public Double getCenterX() {
        return x + w * 0.5;
    }

    public Double getCenterY() {
        return y + h * 0.5;
    }

    // TODO: per-pixel-collision
    public abstract boolean collidesWith( SpriteBase otherSprite);

    public void getDamagedBy( SpriteBase sprite) {
        health -= sprite.getDamage();
    }

    public void kill() {
        setHealth( 0.);
        this.getView().setVisible(false);
    }

    public void remove() {
        setRemovable(true);
    }

    public void stopMovement() {
        this.canMove = false;
    }

    public abstract void checkRemovability();
    public void shoot(double speedLoss, double energyLoss, Image image){
        speed-= speedLoss;
        if(speed <0){speed = 0.;}
        health -= energyLoss;
        if(health <= WhenIWasFine/2){
            this.image = image;
            updateUI();
        }
        if(health <= 0){
            kill();
        }
    }

    public Double getSpeed() {
        return speed;
    }

    public void setSpeed(Double speed) {
        this.speed = speed;
    }

    public double getWhenIWasFine() {
        return WhenIWasFine;
    }

    public double getAntiSpeed() {
        return antiSpeed;
    }

    public void setAntiSpeed(double antiSpeed) {
        this.antiSpeed = antiSpeed;
    }
}