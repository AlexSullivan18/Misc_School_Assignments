import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

/**
 * Application for a set of queries on the Chinook database
 * 
 * Name: YOUR NAME HERE
 * 
 * @author Seikyung Jung
 */
public class ChinookApp {
	Connection connection;
	String sql;
	
	/**
	 * ChinookApp constructor
	 * @param path
	 * @throws ClassNotFoundException cannot find JDBC driver
	 * @throws SQLException SQL gone bad
	 */
	public ChinookApp(String path) throws ClassNotFoundException, SQLException {
		// load the sqlite-JDBC driver using the current class loader
		Class.forName( "org.sqlite.JDBC" );
		connection = DriverManager.getConnection("jdbc:sqlite:" + path);
	}

	/**
	 * 
	 * @param country
	 * @return
	 * @throws SQLException
	 * customersInCountry
	 * 1) How many customers live in country [parameter value]?
	 */
	public int customers(String country) throws SQLException {

	}
	/**
	 * 
	 * @return
	 * @throws SQLException
	 * 2) List all employees (sort by employee id)
	 */
	public String employees() throws SQLException {

	}
	/**
	 * 
	 * @param supportRepId
	 * @return
	 * @throws SQLException
	 * 3) How many customers have been supported by employee id [parameter value]?
	 */
	public int supportedCustomers(int supportRepId) throws SQLException {
	
	}
	
	/**
	 * 
	 * @return
	 * @throws SQLException
	 * 4) List all customers (sort by customer id)
	 */
	public String customerList() throws SQLException {

	}
	
	/**
	 * 
	 * @param customerId
	 * @return
	 * @throws SQLException
	 * 5) List all invoices for customer #[parameter value] (sort by invoice id, each line by invoice line id)
	 */
	public String invoices(int customerId) throws SQLException {

	}
}
