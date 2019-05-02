package BackEnd;

import java.util.HashSet;
import java.util.Scanner;
import java.util.ArrayList;
import javax.print.attribute.standard.Severity;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class CRETransaction extends Transaction {
	// ----- Class Variables ----- //
	public CRETransaction() {
		super();
	}

	public boolean isValid(String mtsfLine) {
		try {
			String[] components = mtsfLine.split(" ");
			String transactionCode = components[0];
			String serviceNumber = components[1];
			int capacity = Integer.parseInt(components[2]);
			
			if(components.length!=6) {
				System.out.println("ERROR: Invalid merged transaction summary file line format");
				System.out.println("Transaction: " + mtsfLine + " is not valid");
				return false;
			} else if (!transactionCode.equals("CRE")) {
				System.out.println("ERROR: Wrong transaction code for class CRE Transaction");
				System.out.println("Transaction: " + mtsfLine + " is not valid");
				return false;
			} else if (CSF.services.containsKey(serviceNumber)||CSF.newServices.containsKey(serviceNumber)) {
				System.out.println("ERROR: Service is already in CSF");
				System.out.println("Transaction: " + mtsfLine + " is not valid");
				return false;	
			}else if(capacity<0||capacity>1000) {
				System.out.println("ERROR: Specified capacity is not between 0 or 1000");
				System.out.println("Transaction: " + mtsfLine + " is not valid");		
				return false;
			}
		} catch (Exception e) {
			System.out.println(5);
			e.printStackTrace();
			return false;
		}
		return true;
	}
	
}