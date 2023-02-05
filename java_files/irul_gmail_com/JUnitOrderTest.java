package irul_gmail_com;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.Test;

public class JUnitOrderTest {
	private final ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
	  private final PrintStream oPrintStream = System.out;

	  @Before
	  public void setUpStream() {
	    System.setOut(new PrintStream(outputStream));
	  }

	  @After
	  public void restoreStream() {
	    System.setOut(oPrintStream);
	  }
	    @Test
	    public void myResultTest() {
	    	irul_gmail_com.Order.main(null);
		    assertEquals("itemCost Condition not same", "High Value Item!", outputStream.toString());

			String result = irul_gmail_com.Order.condition(null);
	    	assertEquals("is result = High Value Item!", "High Value Item!", String.valueOf(result));
	    }

}
