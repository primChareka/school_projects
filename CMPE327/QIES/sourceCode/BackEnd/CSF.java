package BackEnd;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
import javax.print.attribute.standard.Severity;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.File;
import java.io.PrintWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
/**
 *
 * @author primrosechareka
 *
 */
public class CSF {
	// ----- Class Variables ----- //
	BufferedReader fileReader;
	PrintWriter fileWriter;
	public static HashMap<String, String[]> services = new HashMap<String, String[]>();
	public static HashMap<String, String[]> newServices = new HashMap<String, String[]>();

	public CSF(String filename) {
		// Create IO for file
		try {
			//This class requires the input CSF filename to be in the form CSF_000.txt
			this.fileReader = new BufferedReader(new FileReader(filename));
			createInitialServices();
			int filenumber = Integer.parseInt(filename.substring(filename.length()-7,filename.length()-4));
			filenumber++;
			String num= String.format("%03d", filenumber);
			filename = filename.substring(0, filename.length()-7) + num + ".txt";
			System.out.println("New CSF file name is "+filename);
			this.fileWriter = new PrintWriter(filename);

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}
	
	/* ---- INCOMING PARAMS ----
	 * COMMAND  			[0]
	 * SOURCE NUMBER 	[1]
	 * TICKETS 			[2]
	 * DEST. NUMBER 		[3]
	 * NAME				[4]
	 * DATE				[5]
	 */
	
	// Handle all possible correct commands
	public void updateCSF(String[] incomingParameters) {
		try {
			switch (incomingParameters[0]) {
			case "CRE":
				addService(incomingParameters);
				break;
			case "SEL":
				sellService(incomingParameters);
				break;
			case "DEL":
				removeService(incomingParameters[1]);
				break;
			case "CHG":
				changeService(incomingParameters);
				break;
			case "CAN":
				cancelService(incomingParameters);
				break;
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public void createInitialServices(){
		String currentLine;
		String[] parameters;

		try {
			currentLine = fileReader.readLine();
			// Read each line and get all current services, add to map
			while(currentLine != null) {
				parameters = currentLine.split(" "); // Get all parameters from String
				// Add to HashMap
				services.put(parameters[0], parameters);
				currentLine = fileReader.readLine();
			}
			fileReader.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	/* ---- CSF details ----
	 * NUMBER 	[0]
	 * CAPACITY [1]
	 * TICKETS 	[2]
	 * NAME 	[3]
	 * DATE 	[4]
	 */

	// Remove service from HashMap (DEL)
	public void removeService(String serviceNumber) {
		services.remove(serviceNumber);
	}

	// Add new service (CRE)
	public void addService(String[] parameters) {
		// Remove transaction command "CRE" from parameters
		String[] details = new String[5];
		details[0] = parameters[1];
		details[1] = parameters[2];
		details[2] = "0";
		details[3] = parameters[4];
		details[4] = parameters[5];
		newServices.put(details[0], details);
	}

	// Sell tickets for service (SEL)
	public void sellService(String[] parameters) {
		// Get correct service
		String[] details = services.get(parameters[1]);
		// Get new tickets for service (old plus new transaction)
		int tickets = Integer.parseInt(details[2]) + Integer.parseInt(parameters[2]);
		details[2] = Integer.toString(tickets); // Set new value in service
		services.replace(parameters[1], details); // Replace old service values
	}

	// Cancel tickets for service (CAN)
	public void cancelService(String[] parameters) {
		// Get correct service
		String[] details = services.get(parameters[1]);
		// Get new tickets for service (old minus new transaction)
		int tickets = Integer.parseInt(details[2]) - Integer.parseInt(parameters[2]);
		details[2] = Integer.toString(tickets); // Set new value in service
		services.replace(parameters[1], details); // Replace old service values
	}

	// Change tickets for service (CHG)
	public void changeService(String[] parameters) {
		// Get correct source / dest services
		String[] sourceDetails = services.get(parameters[1]);
		String[] destinationDetails = services.get(parameters[3]);

		// Get new tickets for source service
		int tickets = Integer.parseInt(sourceDetails[2]) - Integer.parseInt(parameters[2]);
		sourceDetails[2] = Integer.toString(tickets); // Set new value in service

		// Get new tickets for dest service
		tickets = Integer.parseInt(destinationDetails[2]) + Integer.parseInt(parameters[2]);
		destinationDetails[2] = Integer.toString(tickets); // Set new value in service

		// Replace values
		services.replace(parameters[1], sourceDetails);
		services.replace(parameters[3], destinationDetails);
	}

	// Close the CSF
	public void makeNewCSFFile() {
		// Get all services from HashMap and print
		ArrayList<String> keys = new ArrayList<String>();
		keys.addAll(services.keySet());
		keys.addAll(newServices.keySet());
		Collections.sort(keys);


		// Get all services from HashMap and print to file
		for (String key: keys) {
			String[] parameters = services.get(key);
			if(parameters==null){
				parameters = newServices.get(key);
			}
			StringBuilder serviceDetails = new StringBuilder();
			// Concatinate service details
			for (int i = 0; i < parameters.length; i++) {
				serviceDetails.append(parameters[i] + " ");
			}

			// Start overwriting CSF
			fileWriter.write(serviceDetails.toString().trim() + "\n");
		}

		fileWriter.close();
	}

	// Close the CSF
	public void makeNewVSList(String partialPath) {
System.out.println(partialPath);
		int filenumber = Integer.parseInt(partialPath.substring(partialPath.length()-7,partialPath.length()-4));
		filenumber++;
		String num= String.format("%03d", filenumber);
		String validServicesFile = partialPath.substring(0, partialPath.length()-12) + "/VSF_" + num + ".txt";

		try {
			fileWriter = new PrintWriter(validServicesFile);
			ArrayList<String> keys = new ArrayList<String>();
			keys.addAll(services.keySet());
			keys.addAll(newServices.keySet());
			Collections.sort(keys);


			// Get all services from HashMap and print to file
			for (String key: keys) {
				fileWriter.write(key+ "\n");
			}

			fileWriter.write("00000");
			fileWriter.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}//makeNewVSList

}
