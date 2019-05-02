package BackEnd;

public class CHGTransaction extends Transaction {
	public boolean isValid(String mtsfLine) {
		try {
			String[] components = mtsfLine.split(" ");
			String transactionCode = components[0];
			String serviceNumber = components[1];
			int numTickets = Integer.parseInt(components[2]);
			String serviceNumber2 = components[3];

			if (components.length != 6) {
				System.out.println("ERROR: Invalid merged transaction summary file line format");
				System.out.println("Transaction: " + mtsfLine + " is not valid");
				return false;
			} else if (!transactionCode.equals("CHG")) {
				System.out.println("ERROR: Wrong transaction code for class CHG Transaction");
				System.out.println("Transaction: " + mtsfLine + " is not valid");
				return false;
			} else if (!CSF.services.containsKey(serviceNumber)) {
				System.out.println("ERROR: Service " + serviceNumber + "is not in CSF");
				System.out.println("Transaction: " + mtsfLine + " is not valid");
				return false;
			} else if (!CSF.services.containsKey(serviceNumber2)) {
				System.out.println("ERROR: Service " + serviceNumber2 + "is not in CSF");
				System.out.println("Transaction: " + mtsfLine + " is not valid");
				return false;
			} else {
				int ticketsSold = Integer.parseInt(CSF.services.get(serviceNumber)[2]);
				int ticketsSoldService2 = Integer.parseInt(CSF.services.get(serviceNumber2)[2]);
				int capacityService2 = Integer.parseInt(CSF.services.get(serviceNumber2)[1]);

				if (ticketsSold - numTickets < 0) {
					System.out.println(
							"ERROR: Number of Tickers transferred cannot be greater than the number of tickets currently sold which is "
									+ ticketsSold);
					System.out.println("Transaction: " + mtsfLine + " is not valid");
					return false;
				} else if (capacityService2 - ticketsSoldService2 - numTickets < 0) {
					System.out.println("ERROR: Number of Tickers transferred cannot be greater than the capacity");
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
