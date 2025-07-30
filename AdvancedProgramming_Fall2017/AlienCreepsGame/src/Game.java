
import Images.Images;
import javafx.animation.AnimationTimer;
import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.*;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.scene.text.Text;
import javafx.stage.Screen;
import javafx.stage.Stage;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Random;

/**
 * Created by hp on 1/22/2018.
 */
public class Game extends Application {
    Random rnd = new Random();;
    BorderPane playfieldLayer;
    Pane scoreLayer;
    Image playerImage;
    List<Soldier> soldiers = new ArrayList<>();;
    List<Enemy> enemies = new ArrayList<>();;
    List<Weapon> weapons= new ArrayList<Weapon>();
    static Player player;
    static Text collisionText = new Text();
    boolean collision = false;
    Scene scene;
    Group root;


    @Override
    public void start(Stage primaryStage) {
        Enemy.GAMEOVER = false;
        Enemy.GameOverCountDown = 0;
        root = new Group();

        scoreLayer = new Pane();

        //root.getChildren().add( playfieldLayer);
        root.getChildren().add( scoreLayer);


        primaryStage.setHeight(Settings.SCENE_HEIGHT);
        primaryStage.setWidth(Settings.SCENE_WIDTH);
        primaryStage.setResizable(false);
        //BorderPane pane = new BorderPane();
        Image img = new Image("naghshe.jpg");
        ImageView imageView = new ImageView(img);

        imageView.setFitWidth(Screen.getPrimary().getVisualBounds().getHeight()*1.618);
        imageView.setFitHeight(Screen.getPrimary().getVisualBounds().getHeight());


       // playfieldLayer.setCenter(imageView);
        scene = new Scene( root, Settings.SCENE_WIDTH, Settings.SCENE_HEIGHT);
        root.getChildren().add(root.getChildren().size() - 1,imageView);
        //primaryStage.alwaysOnTopProperty();


        primaryStage.setScene(scene);
        primaryStage.show();

        loadGame();
        createPlayers();
        createScoreLayer();
        int randomStart = 0;


       AnimationTimer gameLoop = new AnimationTimer() {

            @Override
           public void handle(long now) {

               player.processInput();

               spawnEnemies( true);
               player.move();
               for (Soldier soldier: soldiers){
                   soldier.Update(player);
               }
               enemies.forEach(SpriteBase::move);
               // check collisions
               checkCollisions();

              // update sprites in scene
               player.updateUI();
                enemies.forEach(sprite -> sprite.updateUI());
                player.shoot(enemies);

                // check if sprite can be removedy
               enemies.forEach(sprite -> sprite.checkRemovability());

               removeSprites(enemies);
               for (Enemy enemy: enemies){

                }
                if (Enemy.GAMEOVER){
                    //TODO: go to the gameover Thread
                }
            }
//
        };
       gameLoop.start();
    }

    private void loadGame() {
        playerImage = new Image( getClass().getResource("Images/HeroDown.gif").toExternalForm());
        //enemyImage = new Image( getClass().getResource("").toExternalForm());
    }

    private void createScoreLayer() {

        collisionText.setFont( Font.font( null, FontWeight.BOLD, 64));
        collisionText.setStroke(Color.BLACK);
        collisionText.setFill(Color.RED);

        scoreLayer.getChildren().add(collisionText);

        // TODO: quick-hack to ensure the text is centered; usually you don't have that; instead you have a health bar on top
            collisionText.setText(Double.toString(player.getHealth()));
        double x = (Settings.SCENE_WIDTH - collisionText.getBoundsInLocal().getWidth()) / 2;
        double y = (Settings.SCENE_HEIGHT - collisionText.getBoundsInLocal().getHeight()) / 2;
        collisionText.relocate(x, y);
        collisionText.setText("");
        //collisionText.setBoundsType(TextBoundsType.VISUAL);
    }
    private void createPlayers() {
        Image image2 = new Image("Images/PrivateDown.gif");
        for (int i = 0; i <3; i++){
            Soldier soldier = new Soldier(i,root,image2,67.,100.,0.,0.,0.,0.,0.,0.,150.,0.);

            soldiers.add(soldier);
        }
        // player input
        Input input = new Input(scene);
        // register input listeners
        input.addListeners(); // TODO: remove listeners on game over

        Image image = playerImage;
        // center horizontally, position at 70% vertically
        double x = (Settings.SCENE_WIDTH - image.getWidth()) / 2.0;
        double y = Settings.SCENE_HEIGHT * 0.7;
        // create player
        player = new Player(root, image,67.,100., x, y, 0, 0, 0, 0, 300., 0, Settings.PLAYER_SHIP_SPEED, input, soldiers);
        for (Soldier soldier: soldiers)
            soldier.Update(player);
        player.getView().setOnMouseEntered(event -> collisionText.setText("health :" + Double.toString(player.getHealth())));
        player.getView().setOnMouseExited(event -> collisionText.setText(""));
        Image image1 = new Image("Castle.png");
        for(int i = 0; i < Settings.WEAPONS_PLACE.length; i++){
            Random random = new Random();
            int i1 = (int)random.nextDouble()*5;
            Weapon weapon = new Weapon(i1, root,image1,90.,135.,Settings.WEAPONS_PLACE[i][0],Settings.WEAPONS_PLACE[i][1], 0,100,0, 0, 100,0,0 );
        }
    }

    private void spawnEnemies( boolean random) {

        if( random && rnd.nextInt(Settings.ENEMY_SPAWN_RANDOMNESS) != 0) {
            //System.out.println(player.getHealth());
            return;
        }

        // image
        //Image image = enemyImage;
        final double[][] path1 = {{185., 330.}, {440., 0.}, {0., 230.}, {555., 0.}, {0., -90.}, {305., 0.}};
        final double[][] path2 = {{185., 740.}, {580., 0.}, {0., -540.}, {415., 0.}, {0., 135.}, {135., 0.}, {0., 115.}, {170., 0.}};
        // random speed
        int type = (int)(rnd.nextDouble()* 4);
        Random random1 = new Random();
        int shomareMasir = (int)(random1.nextDouble()*2);
        double x, y;
        Enemy enemy;
        switch (shomareMasir) {
            case 0:{
                x = 185. - 20.;
                y = 330. - 30.;
                switch (type){
                    case 0:{
                        enemy = new Enemy(0,root,Images.Act[0].getImage(),67.,100., x, y,0,2,  2,0, 400, 0, 2 );
                        enemy.setPath(path1);
                        enemies.add(enemy);
                        break;
                    }
                    case 1:{
                        enemy = new Enemy(1,root,Images.Air[0].getImage(),67.,100., x, y,0,5,  5,0, 200, 0, 5 );
                        enemy.setPath(path1);
                        enemies.add(enemy);
                        break;
                    }
                    case 2:{
                        enemy = new Enemy(2,root,Images.Alb[0].getImage(),67.,100., x, y,0,8,  8,0, 250, 0, 8 );
                        enemy.setPath(path1);
                        enemies.add(enemy);
                        break;
                    }
                    case 3:{
                        enemy = new Enemy(3,root,Images.Alg[0].getImage(),67.,100., x, y,0,4,  4,0, 150, 0, 4 );
                        enemy.setPath(path1);
                        enemies.add(enemy);
                        break;
                    }
                }
                break;
            }

            case 1:{
                x = 185. - 20.;
                y = 740. - 30.;
                switch (type){
                    case 0:{
                        enemy = new Enemy(0,root, Images.Act[0].getImage(),67.,100., x, y,0,2,  2,0, 400, 0, 2 );
                        enemy.setPath(path2);
                        enemies.add(enemy);
                        break;
                    }
                    case 1:{
                        enemy = new Enemy(1,root,Images.Air[0].getImage(),67.,100., x, y,0,5,  5,0, 200, 0, 5 );
                        enemy.setPath(path2);
                        enemies.add(enemy);
                        break;
                    }
                    case 2:{
                        enemy = new Enemy(2,root,Images.Alb[0].getImage(),67.,100., x, y,0,8,  8,0, 250, 0, 8 );
                        enemy.setPath(path2);
                        enemies.add(enemy);
                        break;
                    }
                    case 3:{
                        enemy = new Enemy(3,root,Images.Alg[0].getImage(),67.,100., x, y,0,4,  4,0, 150, 0, 4 );
                        enemy.setPath(path2);
                        enemies.add(enemy);
                        break;
                    }
                }
                break;
            }
        }
    }

    private void removeSprites(List<? extends SpriteBase> spriteList) {
        Iterator<? extends SpriteBase> iter = spriteList.iterator();
        while( iter.hasNext()) {
            SpriteBase sprite = iter.next();
            if( sprite.isRemovable() || !sprite.getView().isVisible()) {
                // remove from layer
                sprite.removeFromLayer();
                // remove from list
                iter.remove();
            }
        }
    }

    private void checkCollisions() {
        collision = false;

            for( Enemy enemy: enemies) {
                if( player.collidesWith(enemy)) {
                    //enemy.setDx(enemy.getDx() + 1000);
                    collision = true;
                }
            }
       // System.out.println(player.getHealth());
    }

    public static void main(String[] args) {
        launch(args);
    }

}