import scanner.MyScanner;
import scanner.Scanner;
import scanner.Token;

import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Stack;

public class Parser {
    Scanner scanner;
    CodeGenerator cg;
    PTBlock[][] parseTable;
    Stack<Integer> parseStack = new Stack<Integer>();
    String[] symbols;

    public Parser(String inputFile, String[] symbols, PTBlock[][] parseTable) {
        try {
            this.parseTable = parseTable;
            this.symbols = symbols;
            FileInputStream fis = new FileInputStream(inputFile);
            InputStreamReader f = (new InputStreamReader(fis));
            scanner = new MyScanner(f);
            cg = new CodeGenerator(scanner);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public int LineNumber() {
        return scanner.lineNumber; // Or any other name you used in your scanner.Scanner
    }

    public void Parse() {
        try {
            int tokenId = nextTokenID();
            int curNode = 0;
            boolean notAccepted = true;
            while (notAccepted) {
                String token = symbols[tokenId];
                PTBlock ptb = parseTable[curNode][tokenId];
                switch (ptb.getAct()) {
                    case PTBlock.ActionType.Error: {
                        throw new Exception(String.format("Compile Error (" + token + ") at line " + scanner.lineNumber + " @ " + curNode));
                    }
                    case PTBlock.ActionType.Shift: {
                        cg.doSemantic(ptb.getSem());
                        tokenId = nextTokenID();
                        curNode = ptb.getIndex();
                    }
                    break;

                    case PTBlock.ActionType.PushGoto: {
                        parseStack.push(curNode);
                        curNode = ptb.getIndex();
                    }
                    break;

                    case PTBlock.ActionType.Reduce: {
                        if (parseStack.size() == 0) {
                            throw new Exception(String.format("Compile Error (" + token + ") at line " + scanner.lineNumber + " @ " + curNode));
                        }

                        curNode = parseStack.pop();
                        ptb = parseTable[curNode][ptb.getIndex()];
                        cg.doSemantic(ptb.getSem());
                        curNode = ptb.getIndex();
                    }
                    break;

                    case PTBlock.ActionType.Accept: {
                        notAccepted = false;
                    }
                    break;

                }
            }
            cg.FinishCode();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    int nextTokenID() {
        String t = "";
        try {

            Token token = scanner.NextToken();
            t = token.type;
        } catch (Exception e) {
            e.printStackTrace();
        }

        int i;

        for (i = 0; i < symbols.length; i++)
            if (symbols[i].equals(t))
                return i;
        (new Exception("Undefined token: " + t)).printStackTrace();
        return 0;
    }

    public void WriteOutput(String outputFile) // You can change this function, if you think it is not comfortable
    {
        cg.WriteOutput(outputFile);
    }
}


