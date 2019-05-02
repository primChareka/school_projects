package BackEnd;

import java.util.HashSet;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.HashMap;

import javax.print.attribute.standard.Severity;

import FrontEnd.TSF;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class BackEndSystem {
	// ----- Class Variables ----- //
	private static CSF csf = null;

	// ----- Main Execution of Back End System ----- //
	public static void main(String[] args) throws IOException {
		// Get the input files and create a new CSF object and then read and process the
		// MTS file
		String mtsfFilePath =  args[0];
		String csfFilePath =   args[1];

		csf = new CSF(csfFilePath);

		Transaction transaction = null;
		String transactionType; // First 3 letters of mtsfLine, should be: CRE or DEL or SEL....

		// Read until end of mergerd transaction summary file
		FileReader mtsf = new FileReader(mtsfFilePath);
		BufferedReader mtsfBuffer = new BufferedReader(mtsf);
		String mtsfLine = mtsfBuffer.readLine();

		while (mtsfLine != null) {
			mtsfLine = mtsfLine.trim();
			transactionType = mtsfLine.substring(0, 3);

			if (transactionType.equals("CRE")) {
				transaction = new CRETransaction();
			} else if (transactionType.equals("SEL")) {
				transaction = new SELTransaction();
			} else if (transactionType.equals("DEL")) {
				transaction = new DELTransaction();
			} else if (transactionType.equals("CHG")) {
				transaction = new CHGTransaction();
			} else if (transactionType.equals("CAN")) {
				transaction = new CANTransaction();
			} else if (transactionType.equals("EOS")) {
				break;
			}
			BackEndSystem.updateCSF(transaction, mtsfLine);
			mtsfLine = mtsfBuffer.readLine();
		}

		csf.makeNewCSFFile();
		csf.makeNewVSList(csfFilePath);
	}// End Main

	/**
	 * Checks to make sure that the given merged transaction summary file line has valid
	 * contents and then passes the line to the CSF class to update the CSF.txt file
	 * accordingly depending on the transaction type
	 *
	 * @param transaction
	 *            an object inheritred from the Transaction class representing the
	 *            type of transaction being processed
	 * @param mtsfLine
	 *            a String representing a line read from the merged transaction
	 *            summary file
	 */
	public static void updateCSF(Transaction transaction, String mtsfLine) {
		if (transaction.isValid(mtsfLine)) {
			transaction.sendTransactionToCSF(mtsfLine);
		}
	}

	/**
	 * Getter method for the BackEndSystem class's static CSF object
	 *
	 * @return The static CSF object belonging to the BackEndSystem class
	 */
	public static CSF getCSF() {
		return csf;
	}
}
