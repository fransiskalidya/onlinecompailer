package admin_admin_com;

import static org.junit.Assert.assertEquals;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class JUnitHelloWorldTest {
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
  public void isHelloWorld() {
    admin_admin_com.HelloWorld.main(null);
    assertEquals("Is Hello World not same", "Hello World!", outputStream.toString());
  }
}
