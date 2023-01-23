package adminku_gmail_com; 

public class OrderCase {
	boolean isFilled;
	  double billAmount;
	  String shipping;
	  
	  public OrderCase(boolean filled, double cost, String shippingMethod) {
	    isFilled = filled;
	    billAmount = cost;
	    shipping = shippingMethod;
	  }
	  
	  public void ship() {
	    if (isFilled) {
	      System.out.print("Shipping cost: " + calculateShipping());
	    } else {
	      System.out.print("Order not ready");
	    }
	  }
	  
	  public double calculateShipping() {
	    double shippingCost;
	    // declare switch statement here
	      switch (shipping) {
	      case "Regular": 
	        shippingCost = 0;
	        break;
	      case "Express": 
	        shippingCost = 1.75;
	        break;
	      default:
	    	shippingCost = 0.50;
	    }
	    
	    return shippingCost;
	  }
	  
	  public static void main(String[] args) {
	    // do not alter the main method!
	    OrderCase book = new OrderCase(true, 9.99, "Express");
	    
	    book.ship();
	  }
}