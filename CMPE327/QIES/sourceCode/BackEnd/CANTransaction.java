package BackEnd;

public class CANTransaction extends Transaction {
	public boolean isValid(String mtsfLine) {
		try {
			String[] components = mtsfLine.split(" ");
			String transactionCode = components[0];
			String serviceNumber = components[1];
			int numTickets = Integer.parseInt(components[2]);

			if (components.length != 6) {
				System.out.println(1);
				return false;
			} else if (!transactionCode.equals("CAN")) {
				System.out.println("ERROR: Wrong transaction code for class CAN Transaction");
				System.out.println("Transaction: " + mtsfLine + " is not valid");
				return false;
			} else if (!CSF.services.containsKey(serviceNumber)) {
				System.out.println("ERROR: Service is not in CSF");
				System.out.println("Transaction: " + mtsfLine + " is not valid");
				return false;
			} else if (numTickets < 0) {
				System.out.println("ERROR: Number of Tickets canceled cannot be negative");
				System.out.println("Transaction: " + mtsfLine + " is not valid");
			} else {
				int ticketsSold = Integer.parseInt(CSF.services.get(serviceNumber)[2]);
				if (ticketsSold - numTickets < 0) {
					System.out.println(
							"ERROR: Number of Tickers cancelled cannot be greater than the number of tickets currently sold which is "
									+ ticketsSold);
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
