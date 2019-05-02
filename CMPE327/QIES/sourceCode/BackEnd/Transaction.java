package BackEnd;

import java.util.HashSet;
import java.util.Scanner;
import java.util.ArrayList;
import javax.print.attribute.standard.Severity;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public abstract class Transaction {

	public abstract boolean isValid(String string);
	
	public void sendTransactionToCSF(String mtsfLine) {
		String[] incomingParameters = mtsfLine.split(" ");
		BackEndSystem.getCSF().updateCSF(incomingParameters);
	}
}