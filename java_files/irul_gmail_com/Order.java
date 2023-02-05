package irul_gmail_com; 

public class Order {
	public static void main(String[] args) {
		double itemCost = 30.99;
		String order;
		if(itemCost > 24.00) {
			order = "High Value Item!";
		} else {
			order = "Low Value Item!";
		}
		System.out.print(order);
	}
}