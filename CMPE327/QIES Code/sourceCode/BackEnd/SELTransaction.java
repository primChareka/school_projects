package BackEnd;

public class SELTransaction extends Transaction {
	public boolean isValid(String mtsfLine) {
		try {
			String[] components = mtsfLine.split(" ");
			String transactionCode = components[0];
			String serviceNumber = components[1];
			int numTickets = Integer.parseInt(components[2]);

			if (components.length != 6) {
				System.out.println("ERROR: Invalid merged transaction summary file line format");
				System.out.println("Transaction: " + mtsfLine + " is not valid");
				return false;
			} else if (!transactionCode.equals("SEL")) {
				System.out.println("ERROR: Wrong transaction code for class SEL Transaction");
				System.out.println("Transaction: " + mtsfLine + " is not valid");
				return false;
			} else if (!CSF.services.containsKey(serviceNumber)) {
				System.out.println("ERROR: Service is not in CSF");
				System.out.println("Transaction: " + mtsfLine + " is not valid");
				return false;
			} else if (numTickets < 0) {
				System.out.println("ERROR: Number of Tickets sold cannot be negative");
				System.out.println("Transaction: " + mtsfLine + " is not valid");
			} else {
				int capacity = Integer.parseInt(CSF.services.get(serviceNumber)[1]);
				int ticketsSold = Integer.parseInt(CSF.services.get(serviceNumber)[2]);
				if (capacity - ticketsSold - numTickets < 0) {
					System.out.println("ERROR: Number of Tickers sold cannot be greater than the capacity");
					System.out.println("Transaction: " + mtsfLine + " is not valid");
					return false;
				}
			}
		} catch (Exception e) {
			System.out.println(5);
			e.printStackTrace();
			return false;
		}
		return true;
	}
}
