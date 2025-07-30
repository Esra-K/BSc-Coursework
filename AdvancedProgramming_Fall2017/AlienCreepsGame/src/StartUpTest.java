/**
 * Created by ftehr on 1/29/2018.
 */
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

import java.util.concurrent.CountDownLatch;

public class StartUpTest extends Application {
    public static final CountDownLatch latch = new CountDownLatch(1);
    public static StartUpTest startUpTest = null;

    public static StartUpTest waitForStartUpTest() {
        try {
            latch.await();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return startUpTest;
    }

    public static void setStartUpTest(StartUpTest startUpTest0) {
        startUpTest = startUpTest0;
        latch.countDown();
    }

    public StartUpTest() {
        setStartUpTest(this);
    }

    public void printSomething() {
        System.out.println("You called a method on the application");
    }

    @Override
    public void start(Stage stage) throws Exception {
        BorderPane pane = new BorderPane();
        Scene scene = new Scene(pane, 500, 500);
        stage.setScene(scene);

        Label label = new Label("Hello");
        pane.setCenter(label);

        stage.show();
    }

    public static void main(String[] args) {
        Application.launch(args);
    }
}
