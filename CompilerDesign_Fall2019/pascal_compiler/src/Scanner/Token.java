package scanner;


public class Token<T>{
    public T lexeme;
    public String type;
    public int lineNumber;

    public Token(T lexeme, String type, int lineNumber) {
        this.lexeme = lexeme;
        this.type = type;
        this.lineNumber = lineNumber;
    }

    @Override
    public String toString() {
        return "Type: " + this.type + ", Lexeme: " + this.lexeme + ", Line number: " + lineNumber;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == null) {
            return false;
        }
        if (!Token.class.isAssignableFrom(obj.getClass())) {
            return false;
        }
        final Token other = (Token) obj;
        return this.lexeme.equals(other.lexeme) && this.type.equals(other.type);
    }
}






