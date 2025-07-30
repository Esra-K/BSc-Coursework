import javafx.scene.image.Image;
import javafx.stage.Screen;

/**
 * Created by hp on 1/22/2018.
 */
public class Settings {

    public static double SCENE_WIDTH = Screen.getPrimary().getVisualBounds().getHeight()*1.618;
    public static double SCENE_HEIGHT = Screen.getPrimary().getVisualBounds().getHeight();

    public static double PLAYER_SHIP_SPEED = 4.0;
    public static double PLAYER_SHIP_HEALTH = 100.0;

    public static double PLAYER_MISSILE_SPEED = 4.0;
    public static double PLAYER_MISSILE_HEALTH = 200.0;
    public  static final double[][] WEAPONS_PLACE = {{562, 594}, {824, 399}, {996,613}, {1320, 516}, {950, 152}};
    public static int ENEMY_SPAWN_RANDOMNESS = 200;
}