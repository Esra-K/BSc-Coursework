/**
 * Created by ftehr on 1/29/2018.
 */
public class StartUpStartUpTest {
    public static void main(String[] args) {
        new Thread() {
            @Override
            public void run() {
                javafx.application.Application.launch(StartUpTest.class);
            }
        }.start();/*
        StartUpTest startUpTest = StartUpTest.waitForStartUpTest();
        startUpTest.printSomething();*/
    }
}