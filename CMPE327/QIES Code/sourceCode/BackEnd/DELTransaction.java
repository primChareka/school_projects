package BackEnd;

public class DELTransaction extends Transaction {
	public boolean isValid(String mtsfLine) {
		try {
			String[] components = mtsfLine.split(" ");
			String transactionCode = components[0];
			String serviceNumber = components[1];
			String name = components[4];
			
			if(components.length!=6) {
				System.out.println("ERROR: Invalid merged transaction summary file line format");
				System.out.println("Transaction: " + mtsfLine + " is not valid");
				return false;
			} else if (!transactionCode.equals("DEL")) {
				System.out.println("ERROR: Wrong transaction code for class SEL Transaction");
				return false;	
			} else if (!CSF.services.containsKey(serviceNumber)) {
				System.out.println("ERROR: Service is not in CSF");
				System.out.println("Transaction: " + mtsfLine + " is not valid");
				return false;
			} else {
				int ticketsSold = Integer.parseInt(CSF.services.get(serviceNumber)[2]);
				String csfName = CSF.services.get(serviceNumber)[3];
				
				if(ticketsSold!=0) {
					System.out.println("ERROR: Number of Tickets sold cannot be greater than the 0");
					System.out.println("Transaction: " + mtsfLine + " is not valid");
					return false;
				}else if(!csfName.equals(name)) {
					System.out.println("ERROR: Service name must match service name in CSF: " +csfName);
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
