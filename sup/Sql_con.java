package com.lcf.sql;

import java.sql.*;
import java.io.*;

public class Sql_con {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		try {
			Connection conn = DriverManager.getConnection(
					"jdbc:oracle:thin:@claros.cs.purdue.edu:1524:strep", "gu26@csora",
					"Vkf%1Rt)");
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

}
