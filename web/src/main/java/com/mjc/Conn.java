package com.mjc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Conn {
	private static Connection conn=null;
	
	public static Connection getInstance() throws SQLException {
		if(conn==null) {
			
			try {
				String connUrl="jdbc:mysql://localhost:3306/example";
				String dbUser="root";
				String dbPassword="123456";
				Class.forName("org.mariadb.jdbc.Driver");
				conn=DriverManager.getConnection(connUrl,dbUser,dbPassword);
			} catch (ClassNotFoundException e) {
				// TODO Auto-generated catch block
				
				e.printStackTrace();
			}
				
		}
		return conn;
	}
	
}
