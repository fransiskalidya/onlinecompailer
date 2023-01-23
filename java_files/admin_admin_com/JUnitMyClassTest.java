package admin_admin_com;

import static org.junit.Assert.assertEquals;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class JUnitMyClassTest {
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
	public void isMyClassTest() {
		admin_admin_com.MyClass.Double(35.5);
		assertEquals("Is Double Result", "Result = 35.5", outputStream.toString());
		
	}
}
