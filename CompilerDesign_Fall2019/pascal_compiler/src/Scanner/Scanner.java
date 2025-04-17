package scanner;

import scanner.Token;

/**
 * This is the template of class 'scanner'. You should place your own 'scanner class here and
 * your scanner should match this interface. 
 *
 */
public interface Scanner
{
	int lineNumber = 1;

	public Token NextToken();
	public Token CurrentToken();

	
}
