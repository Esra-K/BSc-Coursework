package scanner;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class test
{
    public static void main(String[] args) throws IOException {
//        File file = new File();
        FileInputStream fis = new FileInputStream("C:\\Users\\zahra\\Desktop\\compiler\\compiler_project\\src\\scanner\\input.txt");

        InputStreamReader f = (new InputStreamReader(fis));

        MyScanner s = new MyScanner(f);
        while (true){
            Token t = s.NextToken();
            if(t == null)
                return;
            System.out.println(t.toString());
        }
    }
}
