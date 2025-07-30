/**
 * Created by hp on 1/27/2018.
 */



import javafx.animation.AnimationTimer;
import javafx.animation.KeyFrame;
import javafx.animation.KeyValue;
import javafx.animation.Timeline;
import javafx.application.Application;
import static javafx.application.Application.launch;
import javafx.event.EventHandler;
import javafx.scene.Node;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.paint.ImagePattern;
import javafx.scene.shape.Rectangle;
import javafx.scene.shape.Shape;
import javafx.stage.Stage;
import javafx.util.Duration;

//http://clipart-library.com/image_gallery2/Bart-Simpson-Free-Download-PNG.png

/**
 *
 * @author Cory
 */
public class GamePlay extends Application {

    private static double W = 800, H = 560;

    private static  String HERO_IMAGE_LOC =
            "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Ash_Tree_-_geograph.org.uk_-_590710.jpg/440px-Ash_Tree_-_geograph.org.uk_-_590710.jpg";


    private Image heroImage;
    private Node  hero;
    private Image heroImage1;
    private Node  hero1;
    BorderPane root = new BorderPane();
    boolean running, goNorth, goSouth, goEast, goWest, shoot;

    @Override
    public void start(Stage stage) throws Exception {
        heroImage = new Image(HERO_IMAGE_LOC , 100 , 100 , false , false);
        hero = new ImageView(heroImage);

        Pane dungeon = new Pane(hero);

        root.getChildren().add(dungeon);

        moveHeroTo(W / 2, H / 2);

        Scene scene = new Scene(root, W, H);
        /*final Rectangle rectBasicTimeline = new Rectangle(510, 0, 50, 50);
        rectBasicTimeline.setFill(Color.RED);*//*
        final Timeline timeline = new Timeline();
        timeline.setCycleCount(1);
        timeline.setAutoReverse(false);
        //final KeyValue kv = new KeyValue(rectBasicTimeline.yProperty(), 600);
        final KeyFrame kf = new KeyFrame(Duration.millis(13000), kv);


        root.getChildren().add(rectBasicTimeline);
        timeline.getKeyFrames().add(kf);
        timeline.play();*/



        scene.setOnKeyPressed(new EventHandler<KeyEvent>() {
            @Override
            public void handle(KeyEvent event) {
                switch (event.getCode()) {
                    case UP:    goNorth = true; break;
                    case DOWN:  goSouth = true; break;
                    case LEFT:  goWest  = true; break;
                    case RIGHT: goEast  = true; break;
                    case SHIFT: running = true; break;
                    case SPACE:
                        shoot = true;
                        break;
                }
            }
        });

        scene.setOnKeyReleased(new EventHandler<KeyEvent>() {
            @Override
            public void handle(KeyEvent event) {
                switch (event.getCode()) {
                    case UP:    goNorth = false; break;
                    case DOWN:  goSouth = false; break;
                    case LEFT:  goWest  = false; break;
                    case RIGHT: goEast  = false; break;
                    case SHIFT: running = false; break;
                    case SPACE:
                        shoot = false;
                        break;
                }
            }
        });

        stage.setScene(scene);
        stage.show();

        AnimationTimer timer = new AnimationTimer() {
            @Override
            public void handle(long now) {
                int dx = 0, dy = 0;

                if (goNorth) dy -= 3;
                if (goSouth) dy += 3;
                if (goEast)  dx += 4;
                if (goWest)  dx -= 4;

                moveHeroBy(dx, dy);

                /*if (shoot == true){
                    shoot(rectBasicTimeline, hero.getLayoutX(), hero.getLayoutY());
                }*/

            }
        };
        timer.start();
    }
    public void shoot(Shape i, double x, double y){

        Rectangle rectBasicTimeline = new Rectangle(hero.getLayoutX(), hero.getLayoutY(), 50, 50);

        Timeline timeline = new Timeline();
        timeline.setCycleCount(1);
        timeline.setAutoReverse(false);

        KeyValue kv = new KeyValue(rectBasicTimeline.yProperty(), -100);
        KeyFrame kf = new KeyFrame(Duration.millis(2600), kv);


        root.getChildren().add(rectBasicTimeline);
        timeline.getKeyFrames().add(kf);

        timeline.play();

    }

    private void moveHeroBy(int dx, int dy) {
        if (dx == 0 && dy == 0) return;

        final double cx = hero.getBoundsInLocal().getWidth()  / 2;
        final double cy = hero.getBoundsInLocal().getHeight() / 2;

        double x = cx + hero.getLayoutX() + dx;
        double y = cy + hero.getLayoutY() + dy;

        moveHeroTo(x, y);
    }

    private void moveHeroTo(double x, double y) {
        final double cx = hero.getBoundsInLocal().getWidth()  / 2;
        final double cy = hero.getBoundsInLocal().getHeight() / 2;

        if (x - cx >= 0 &&
                x + cx <= W &&
                y - cy >= 0 &&
                y + cy <= H) {
            hero.relocate(x - cx, y - cy);
        }
    }

    public static void main(String[] args) { launch(args); }
}


