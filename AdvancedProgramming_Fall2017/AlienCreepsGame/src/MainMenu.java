import com.sun.scenario.Settings;
import javafx.animation.KeyFrame;
import javafx.animation.KeyValue;
import javafx.animation.Timeline;
import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.scene.Cursor;
import javafx.scene.Group;
import javafx.scene.Node;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.effect.BlendMode;
import javafx.scene.effect.BoxBlur;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.*;
import javafx.scene.media.Media;
import javafx.scene.media.MediaPlayer;
import javafx.scene.paint.Color;
import javafx.scene.paint.CycleMethod;
import javafx.scene.paint.LinearGradient;
import javafx.scene.paint.Stop;
import javafx.scene.shape.Circle;
import javafx.scene.shape.Rectangle;
import javafx.scene.shape.StrokeType;
import javafx.scene.text.Font;
import javafx.scene.text.FontPosture;
import javafx.scene.text.FontWeight;
import javafx.scene.text.Text;
import javafx.stage.Screen;
import javafx.stage.Stage;
import javafx.scene.layout.HBox;
import javafx.util.Duration;
import jdk.internal.util.xml.impl.Input;


public class MainMenu extends Application {

    Stage stage;
    Scene startScene = new Scene(new Group(), 1000, 1000);
    Scene custumScene = new Scene(new Group(), 1500, 1500);
    Scene mainScene = new Scene(new Group(), 1500, 1500);
    Scene helpScene = new Scene(new Group(), 1500, 1500);

    public void makeStartScene() {
        Group root = (Group) startScene.getRoot();
        root.getChildren().clear();

        //set backgrond image
        ImageView backgrond = new ImageView(new Image(getClass().getResourceAsStream("alcreeps.gif")));
        backgrond.setFitHeight(Screen.getPrimary().getVisualBounds().getHeight());
        backgrond.setFitWidth(Screen.getPrimary().getVisualBounds().getHeight() * 1.618);
        root.getChildren().add(backgrond);

        //set start sound
        Media start = new Media(this.getClass().getResource("start.mp3").toString());
        MediaPlayer mediaPlayer = new MediaPlayer(start);
        mediaPlayer.setVolume(.8);
        mediaPlayer.play();

        //play button
        ImageView imageView = new ImageView(new Image(getClass().getResourceAsStream("alien1.jpg")));
        Button btn1 = new Button(null, imageView);
        btn1.setBackground(new Background(new BackgroundFill(Color.GREY, CornerRadii.EMPTY, javafx.geometry.Insets.EMPTY)));
        btn1.setPadding(javafx.geometry.Insets.EMPTY);

        imageView.setPreserveRatio(true);
        imageView.setFitHeight(270);
        imageView.setFitWidth(270);
        btn1.setGraphic(imageView);
        btn1.relocate(150, 800);
        btn1.setCursor(Cursor.OPEN_HAND);
        btn1.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                Button btn1 = (Button) event.getSource();
                btn1.setGraphic(new ImageView());

                stage.setTitle("Welcome to Alien Creeeps");
                custumScene();
                stage.setScene(custumScene);
            }
        });


        //Resume button
        ImageView alien3 = new ImageView(new Image(getClass().getResourceAsStream("alien3.jpg")));
        Button btn2 = new Button(null, imageView);
        btn2.setBackground(new Background(new BackgroundFill(Color.GREY, CornerRadii.EMPTY, javafx.geometry.Insets.EMPTY)));
        btn2.setPadding(javafx.geometry.Insets.EMPTY);

        alien3.setPreserveRatio(true);
        alien3.setFitHeight(270);
        alien3.setFitWidth(270);
        btn2.setGraphic(alien3);
        btn2.relocate(350, 800);
        btn2.setCursor(Cursor.OPEN_HAND);
        //TODO resume button
        btn2.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
            }
        });

        //Exit button
        ImageView alien2 = new ImageView(new Image(getClass().getResourceAsStream("alien2.jpg")));
        Button btn3 = new Button(null, imageView);
        btn3.setBackground(new Background(new BackgroundFill(Color.GREY, CornerRadii.EMPTY, javafx.geometry.Insets.EMPTY)));
        btn3.setPadding(javafx.geometry.Insets.EMPTY);

        alien2.setPreserveRatio(true);
        alien2.setFitHeight(270);
        alien2.setFitWidth(270);
        btn3.setGraphic(alien2);
        btn3.relocate(550, 800);
        btn3.setCursor(Cursor.OPEN_HAND);
        //TODO exit button
        btn3.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                stage.close();
            }
        });

        //help button
        ImageView help = new ImageView(new Image(getClass().getResourceAsStream("alien4.png")));
        Button btn4 = new Button(null, help);
        btn4.setBackground(new Background(new BackgroundFill(Color.GREY, CornerRadii.EMPTY, javafx.geometry.Insets.EMPTY)));
        btn4.setPadding(javafx.geometry.Insets.EMPTY);

        help.setPreserveRatio(true);
        help.setFitHeight(270);
        help.setFitWidth(270);
        btn4.setGraphic(help);
        btn4.relocate(750, 800);
        btn4.setCursor(Cursor.OPEN_HAND);
        btn4.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                helpScene();
                stage.setScene(helpScene);
            }
        });


        //add to root
        //root.getChildren().addAll(btn1, btn2, btn3, btn4);

        //add hbox for these buttons
        // HBox
        HBox hb = new HBox();
        hb.setPadding(new Insets(1300, 750, 300, 690));
        hb.setSpacing(100);

        // Buttons
        hb.getChildren().add(btn1);
        hb.getChildren().add(btn2);
        hb.getChildren().add(btn4);
        hb.getChildren().add(btn3);

        root.getChildren().add(hb);
    }


    //*******************************************************************
    //sakhtane sence ha
    //create main scene for single playing
    public void mainScene() {
        new Thread() {
            @Override
            public void run() {
                javafx.application.Application.launch(Game.class);
            }
        }.start();
    }
        //game.start(stage);

        /*Group root = (Group) custumScene.getRoot();
        root.getChildren().clear();

        ImageView backgrond = new ImageView(new Image(getClass().getResourceAsStream("naghshe.jpg")));
        backgrond.setFitHeight(Screen.getPrimary().getVisualBounds().getHeight());
        backgrond.setFitWidth(Screen.getPrimary().getVisualBounds().getHeight() * 1.618);
        root.getChildren().add(backgrond);*/




    //sence marbot be play
    public void custumScene() {
        Group root = (Group) custumScene.getRoot();
        root.getChildren().clear();

        ImageView backgrond = new ImageView(new Image(getClass().getResourceAsStream("black.jpg")));
        backgrond.setFitHeight(Screen.getPrimary().getVisualBounds().getHeight());
        backgrond.setFitWidth(Screen.getPrimary().getVisualBounds().getHeight() * 1.618);
        root.getChildren().add(backgrond);


        //single button
        ImageView yekNafare = new ImageView(new Image(getClass().getResourceAsStream("single.png")));
        Button b1 = new Button(null, yekNafare);
        b1.setBackground(new Background(new BackgroundFill(Color.GREY, CornerRadii.EMPTY, javafx.geometry.Insets.EMPTY)));
        b1.setPadding(javafx.geometry.Insets.EMPTY);

        yekNafare.setPreserveRatio(true);
        yekNafare.setFitHeight(400);
        yekNafare.setFitWidth(400);
        b1.setGraphic(yekNafare);
        b1.relocate(180 , 400);
        b1.setCursor(Cursor.OPEN_HAND);
        b1.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                mainScene();
                stage.setScene(mainScene);
            }
        });

        //multiple button
        ImageView chandNafare = new ImageView(new Image(getClass().getResourceAsStream("multiple.png")));
        Button b2 = new Button(null, chandNafare);
        b2.setBackground(new Background(new BackgroundFill(Color.GREY, CornerRadii.EMPTY, javafx.geometry.Insets.EMPTY)));
        b2.setPadding(javafx.geometry.Insets.EMPTY);

        chandNafare.setPreserveRatio(true);
        chandNafare.setFitHeight(400);
        chandNafare.setFitWidth(400);
        b2.setGraphic(chandNafare);
        b2.relocate(580 , 400);
        b2.setCursor(Cursor.OPEN_HAND);
        b2.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                //stage.setTitle("Welcome to Alien Creeeps");
                //custumScene();
                //stage.setScene(custumScene);
            }
        });
        HBox hBox = new HBox();
        hBox.setPadding(new Insets(700, 750, 300, 800));
        hBox.setSpacing(400);

        // Buttons
        hBox.getChildren().add(b1);
        hBox.getChildren().add(b2);


        root.getChildren().add(hBox);
    }



    //sence marbot be help
    public void helpScene(){
        Group root = (Group) helpScene.getRoot();
        root.getChildren().clear();

        Group circles=createCircles();
        root.getChildren().add(circles);
        Text text = new Text();

        text.setText("Alien Creeps is a traditional tower defense"+"\n" + "game where players place different defensive"+"\n" +
                "towers in the path of advancing enemies." + "\n" +
                "Their goal is to reach your defensive zone," +"\n" + "while yours is to get rid of all of them"+"\n" +
                "before they succeed. In Alien Creeps, you'll" + " \n" +
                "have a good array of defensive towers to" + "\n" +
                " protect Earth from the alien attack. " + "\n" +
                "In addition to normal towers, you can also " + "\n" +
                "control  heroes. You'll need to be careful with" + "\n" +
                " them, though, because they can die.");

        //setting the position of the text
        text.setX(160);
        text.setY(300);
        text.setFont(Font.font("verdana", FontWeight.BOLD, FontPosture.REGULAR, 100));
        text.setFill(Color.DARKGREEN);

        text.setStrokeWidth(1);

        text.setStroke(Color.GOLD);


        circles.setEffect(new BoxBlur(100, 100, 10));

        Group blendModeGroup=createBlendGroup(helpScene, circles);
        root.getChildren().add(blendModeGroup);

        addAnimation(circles);
        root.getChildren().add(text);
        /*ImageView backgrond = new ImageView(new Image(getClass().getResourceAsStream("help.png")));
        backgrond.setFitHeight(Screen.getPrimary().getVisualBounds().getHeight());
        backgrond.setFitWidth(Screen.getPrimary().getVisualBounds().getHeight() * 1.618);
        root.getChildren().add(backgrond);*/
    }
    Group createBlendGroup(Scene helpscene,Group circles){
        Rectangle colors = new Rectangle(helpscene.getWidth(), helpscene.getHeight(),
                new LinearGradient(0f, 1f, 1f, 0f, true, CycleMethod.NO_CYCLE, new
                        Stop[]{
                        new Stop(0, Color.web("#f8bd55")),
                        new Stop(0.14, Color.web("#c0fe56")),
                        new Stop(0.28, Color.web("#5dfbc1")),
                        new Stop(0.43, Color.web("#64c2f8")),
                        new Stop(0.57, Color.web("#be4af7")),
                        new Stop(0.71, Color.web("#ed5fc2")),
                        new Stop(0.85, Color.web("#ef504c")),
                        new Stop(1, Color.web("#f2660f")),}));



        colors.widthProperty().bind(helpscene.widthProperty());
        colors.heightProperty().bind(helpscene.heightProperty());

        Group blendModeGroup =
                new Group(new Group(new Rectangle(Screen.getPrimary().getVisualBounds().getHeight() * 1.618,
                        Screen.getPrimary().getVisualBounds().getHeight(),
                        Color.BLACK), circles), colors);
        colors.setBlendMode(BlendMode.OVERLAY);
        return blendModeGroup;
    }
    Group createCircles(){
        Group circles = new Group();
        for (int i = 0; i < 30; i++) {
            Circle circle = new Circle(300, Color.web("white", 0.08));
            circle.setStrokeType(StrokeType.OUTSIDE);
            circle.setStroke(Color.web("white", 0.16));
            circle.setStrokeWidth(4);
            circles.getChildren().add(circle);
        }
        return circles;
    }
    void addAnimation(Group circles) {
        Timeline timeline = new Timeline();
        for (Node circle : circles.getChildren()) {
            timeline.getKeyFrames().addAll(
                    new KeyFrame(Duration.ZERO, // set start position at 0
                            new KeyValue(circle.translateXProperty(), Math.random() * 2200),
                            new KeyValue(circle.translateYProperty(), Math.random() * 1700)
                    ),
                    new KeyFrame(new Duration(20000), // set end position at 20s
                            new KeyValue(circle.translateXProperty(), Math.random() * 2200),
                            new KeyValue(circle.translateYProperty(), Math.random() * 1700)
                    )
            );
        }
        // play 20s of animation
        timeline.play();
    }



    public void start(Stage primaryStage){
        stage = primaryStage;
        stage.setHeight(Screen.getPrimary().getVisualBounds().getHeight());
        stage.setWidth(Screen.getPrimary().getVisualBounds().getHeight()*1.618);
        stage.setResizable(false);

        //custumScene();
        helpScene();
        makeStartScene();
        //mainScene();
        stage.setTitle("Alien Creeps");
        stage.setScene(startScene);
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
    /*private void createPlayers() {

        // player input
        Input input = new Input(scene);

        // register input listeners
        input.addListeners(); // TODO: remove listeners on game over

        Image image = playerImage;

        // center horizontally, position at 70% vertically
        double x = (Settings.SCENE_WIDTH - image.getWidth()) / 2.0;
        double y = Settings.SCENE_HEIGHT * 0.7;

        // create player
        Hero hero = new Hero(mainScene, image, x, y, 0, 0, 0, 0, Settings.PLAYER_SHIP_HEALTH, 0, Settings.PLAYER_SHIP_SPEED, input);
        //System.out.println(player.getHealth());
        // register player


    }
*/
}
