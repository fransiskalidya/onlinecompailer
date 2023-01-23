package adminku_gmail_com;

import static org.junit.Assert.assertEquals;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class JUnitOrderCaseTest {
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
	    public void myOrderCaseResult() {
	    	adminku_gmail_com.OrderCase.main(null);
		    assertEquals("ShippingCost not same", "Shipping cost: 1.75", outputStream.toString());

			double data = adminku_gmail_com.OrderCase.calculateShipping("Express");
		   assertEquals("Result from CalculateShipping", "1.75" ,String.valueOf(data));
	    }
}
