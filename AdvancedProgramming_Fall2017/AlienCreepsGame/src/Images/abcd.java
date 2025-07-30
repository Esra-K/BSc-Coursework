package Images; /**
 * Created by hp on 1/28/2018.
 */



import javafx.application.Application;
import javafx.application.Platform;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.geometry.Rectangle2D;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.*;
import javafx.scene.media.Media;
import javafx.scene.media.MediaPlayer;
import javafx.scene.paint.Color;
import javafx.scene.shape.Line;
import javafx.scene.text.Text;
import javafx.scene.transform.Rotate;
import javafx.stage.Screen;
import javafx.stage.Stage;

import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;
import javafx.scene.layout.Background;
import javafx.scene.layout.BackgroundFill;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.CornerRadii;
import javafx.scene.layout.FlowPane;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.StackPane;
import javafx.scene.layout.VBox;
import javafx.scene.media.Media;

public class abcd extends Application {

    int i = 0;
    int keyT = 200;
    Rotate rot;
    int scrMaxWidth = 1188;
    int scrMaxHeight = 680;
    GridPane mainPane;
    Label currentTimeLable;
    //Label totalScoreLable;
    public int Score = 0;
    int currentTime = 0;
    boolean isGameOvered=true;
    boolean isPaused=true;
    Button startButton;
    Button resume;
    Button exit;
    Scene menuScene;

    @Override
    public void start(Stage primaryStage) {

        BorderPane root = new BorderPane();

        Scene scene = new Scene(root, scrMaxWidth, scrMaxHeight);

        mainPane = new GridPane();
        mainPane.setPrefSize(scrMaxWidth - (scrMaxWidth / 6), scrMaxHeight);//1000
        Color color = Color.rgb(255, 255, 255, 0.75);
////        Color color = Color.rgb(0, 0, 0, 0.75);
        BackgroundFill fill = new BackgroundFill(color, CornerRadii.EMPTY, Insets.EMPTY);
        Background background = new Background(fill);
        mainPane.setBackground(background);

        VBox leftPane = new VBox();
        leftPane.setAlignment(Pos.CENTER);
        leftPane.setPrefSize(scrMaxWidth / 6, scrMaxHeight);//200

//        mainPane.setPadding(new Insets(50, 50, 50, 50));
        root.setCenter(mainPane);
        root.setLeft(leftPane);
        Button btn = new Button();
        btn.setText("Pause");
        btn.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
//                if(!isGameOvered){
                isPaused=true;
                primaryStage.setScene(menuScene);
                Rectangle2D primScreenBounds = Screen.getPrimary().getVisualBounds();

                primaryStage.show();

                primaryStage.setX((primScreenBounds.getWidth() - primaryStage.getWidth()) / 2);
                primaryStage.setY((primScreenBounds.getHeight() - primaryStage.getHeight()) / 2);
//            }
            }
        });

        currentTimeLable = new Label("Elapsed Time: "+String.valueOf(currentTime));
        //totalScoreLable= new Label("Your Score: "+String.valueOf(Score));

        //totalScoreLable.setStyle("-fx-text-fill: green;"+
        //"-fx-font-weight: bold;"+
        // "-fx-font-size: 24;");
        currentTimeLable.setStyle("-fx-text-fill: orange;"+
                "-fx-font-weight: bold;"+
                "-fx-font-size: 20;");

        btn.setPrefSize(100,40);
        btn.setStyle( "-fx-font-weight: bold;-fx-font-size: 16;");
//        currentTimeLable.setPrefSize(300, 200);
//        currentTimeLable.setOpacity(1);

        //leftPane.getChildren().add(totalScoreLable);
        leftPane.getChildren().add(currentTimeLable);
        leftPane.getChildren().add(btn);

        leftPane.setSpacing(80);
        leftPane.setPadding(new Insets(50, 10, 50, 10));
        color = Color.rgb(100, 0, 34, 0.749);
        BackgroundFill fill2 = new BackgroundFill(color, CornerRadii.EMPTY, Insets.EMPTY);
        Background background2 = new Background(fill2);
        leftPane.setBackground(background2);
//        Media sound = new Media(this.getClass().getResource("Game_Start.wav").toString());
//        MediaPlayer mediaPlayer = new MediaPlayer(sound);


        Thread timerThread = new Thread(new Runnable() {
            @Override
            public void run() {
                while (true) {
//                    System.out.println(".run()");
                    if(!isGameOvered && !isPaused){
//                        System.out.println("Paused");
                        try {
                            //if not Game Over
                            //if not Paused
                            Thread.sleep(1000);

                        } catch (InterruptedException ex) {
                            System.out.println(ex.getMessage());
                        }

                        currentTime++;

                        Platform.runLater(new Runnable() {
                            @Override
                            public void run() {
                                currentTimeLable.setText("Elapsed Time: "+String.valueOf(currentTime));
                                if (currentTime % 20 == 0) {
                                    System.out.println("20 ta gozasht ke!");
                                    if(isGameOvered){
                                        Media sound = new Media(this.getClass().getResource("gameover.wav").toString());
                                        MediaPlayer mediaPlayer = new MediaPlayer(sound);
                                        mediaPlayer.play();
                                    }
                                    Media sound = new Media(this.getClass().getResource("row.wav").toString());
//                                Media sound = new Media(this.getClass().getResource("start.mp3").toString());

                                    MediaPlayer mediaPlayer = new MediaPlayer(sound);
                                    mediaPlayer.setVolume(.2);


                                    mediaPlayer.play();
                                }
                            }
                        });

                    }else{

                        try {
                            //if not Game Over
                            //if not Paused
                            Thread.sleep(50);

                        } catch (InterruptedException ex) {
                            System.out.println(ex.getMessage());
                        }


                    }

                }
            }
        });
        timerThread.start();


        rot = new Rotate(0);
        rot.setPivotX(500);
        rot.setPivotY(scrMaxHeight);


        btn.setOnKeyPressed((event) -> {

            VBox vbox = new VBox(new Text("Hi"), new Button("Ok."));
            vbox.setAlignment(Pos.CENTER);
            vbox.setPadding(new Insets(95));
            primaryStage.setScene(new Scene(vbox));
            Rectangle2D primScreenBounds = Screen.getPrimary().getVisualBounds();
            primaryStage.setX((primScreenBounds.getWidth() - primaryStage.getWidth()) / 2);
            primaryStage.setY((primScreenBounds.getHeight() - primaryStage.getHeight()) / 2);

            if (i < 5) {
                System.out.println("i : " + i);
            }else{

                isGameOvered=true;
                Media sound = new Media(this.getClass().getResource("gameover.wav").toString());
                MediaPlayer mediaPlayer = new MediaPlayer(sound);

                mediaPlayer.play();

            }
        });


        mainPane.setAlignment(Pos.TOP_CENTER);


        primaryStage.setTitle("ShootBall");


        primaryStage.setResizable(false);
/*
        Media start = new Media(this.getClass().getResource("start.mp3").toString());
        MediaPlayer mediaPlayer = new MediaPlayer(start);
        mediaPlayer.setVolume(.8);
        mediaPlayer.play();*/
        resume=new Button("Resume");
        resume.setPrefSize(200,60);
        resume.setStyle( "-fx-font-weight: bold;-fx-font-size: 30;");
        startButton=new Button("Start");
        startButton.setPrefSize(200,60);
        startButton.setStyle( "-fx-font-weight: bold;-fx-font-size: 30;");
        exit=new Button("Exit");
        exit.setPrefSize(200,60);
        exit.setStyle( "-fx-font-weight: bold;-fx-font-size: 30;");



        exit.setOnMouseClicked(e->{
            Platform.exit();
            System.exit(0);
        });

        resume.setOnMouseClicked(e->{


            if(isPaused){
                primaryStage.setScene(scene);
                Rectangle2D primScreenBounds = Screen.getPrimary().getVisualBounds();
                primaryStage.setX((primScreenBounds.getWidth() - primaryStage.getWidth()) / 2);
                primaryStage.setY((primScreenBounds.getHeight() - primaryStage.getHeight()) / 2);
                isPaused=false;

            }
            else if(isPaused && isGameOvered){}



        });

        startButton.setOnMouseClicked(e->{
            primaryStage.setScene(scene);
            Rectangle2D primScreenBounds = Screen.getPrimary().getVisualBounds();
            primaryStage.setX((primScreenBounds.getWidth() - primaryStage.getWidth()) / 2);
            primaryStage.setY((primScreenBounds.getHeight() - primaryStage.getHeight()) / 2);
            isPaused=false;
            isGameOvered=false;
            startButton.setDisable(true);
            //mediaPlayer.stop();
        });

//    VBox vbox = new VBox(new Text("Hi"), startButton);
        VBox vbox = new VBox();
        vbox.getChildren().add(startButton);
        vbox.getChildren().add(resume);
        vbox.getChildren().add(exit);
        vbox.setSpacing(80);
        vbox.setAlignment(Pos.CENTER);
        vbox.setPadding(new Insets(150, 80, 150, 80));
        vbox.setBackground(background2);
        menuScene=new Scene(vbox);
        primaryStage.setScene(menuScene);
        Rectangle2D primScreenBounds = Screen.getPrimary().getVisualBounds();

        primaryStage.show();

        primaryStage.setX((primScreenBounds.getWidth() - primaryStage.getWidth()) / 2);
        primaryStage.setY((primScreenBounds.getHeight() - primaryStage.getHeight()) / 2);

        primaryStage.setOnCloseRequest(e->{
            Platform.exit();
            System.exit(0);

        });
    }
    public static void main(String[] args) {
        launch(args);
    }
}
