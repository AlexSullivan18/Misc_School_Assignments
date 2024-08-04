import static org.junit.jupiter.api.Assertions.*;

import java.sql.SQLException;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

class ChinookAppTest {

	private static ChinookApp app;
	
	@BeforeAll
	static void setup() throws ClassNotFoundException, SQLException {
		String DB_PATH = ChinookApp.class.getResource("Chinook_Sqlite_AutoIncrementPKs.sqlite").getFile();

		app = new ChinookApp(DB_PATH);
	}
	

	@Test
	void testCustomers() throws SQLException {
		assertEquals(app.customers("USA"), 13);
		assertEquals(app.customers("Brazil"), 5);
		assertEquals(app.customers("Belgium"), 1);
		assertEquals(app.customers("United Kingdom"), 3);
		assertEquals(app.customers("Canada"), 8);
		assertEquals(app.customers("USSR"), 0);
	}

	@Test
	void testEmployees() throws SQLException {
		final String result = 
				"1. Andrew Adams (General Manager)\n" + 
				"2. Nancy Edwards (Sales Manager)\n" +
				"3. Jane Peacock (Sales Support Agent)\n" +
				"4. Margaret Park (Sales Support Agent)\n" +
				"5. Steve Johnson (Sales Support Agent)\n" +
				"6. Michael Mitchell (IT Manager)\n" +
				"7. Robert King (IT Staff)\n" +
				"8. Laura Callahan (IT Staff)\n";
			
			assertEquals(app.employees(), result);
	}

	@Test
	void testSupportedCustomers() throws SQLException {
		assertEquals(app.supportedCustomers(0), 0);
		assertEquals(app.supportedCustomers(1), 0);
		assertEquals(app.supportedCustomers(2), 0);
		assertEquals(app.supportedCustomers(3), 21);
		assertEquals(app.supportedCustomers(4), 20);
		assertEquals(app.supportedCustomers(5), 18);
		assertEquals(app.supportedCustomers(6), 0);
		assertEquals(app.supportedCustomers(7), 0);
		assertEquals(app.supportedCustomers(8), 0);
		assertEquals(app.supportedCustomers(9), 0);	}

	@Test
	void testCustomerList() throws SQLException {
		final String result = 
				"1. Luís Gonçalves (São José dos Campos, SP, Brazil)\n" +
				"2. Leonie Köhler (Stuttgart, Germany)\n" +
				"3. François Tremblay (Montréal, QC, Canada)\n" +
				"4. Bjørn Hansen (Oslo, Norway)\n" +
				"5. František Wichterlová (Prague, Czech Republic)\n" +
				"6. Helena Holý (Prague, Czech Republic)\n" +
				"7. Astrid Gruber (Vienne, Austria)\n" +
				"8. Daan Peeters (Brussels, Belgium)\n" +
				"9. Kara Nielsen (Copenhagen, Denmark)\n" +
				"10. Eduardo Martins (São Paulo, SP, Brazil)\n" +
				"11. Alexandre Rocha (São Paulo, SP, Brazil)\n" +
				"12. Roberto Almeida (Rio de Janeiro, RJ, Brazil)\n" +
				"13. Fernanda Ramos (Brasília, DF, Brazil)\n" +
				"14. Mark Philips (Edmonton, AB, Canada)\n" +
				"15. Jennifer Peterson (Vancouver, BC, Canada)\n" +
				"16. Frank Harris (Mountain View, CA, USA)\n" +
				"17. Jack Smith (Redmond, WA, USA)\n" +
				"18. Michelle Brooks (New York, NY, USA)\n" +
				"19. Tim Goyer (Cupertino, CA, USA)\n" +
				"20. Dan Miller (Mountain View, CA, USA)\n" +
				"21. Kathy Chase (Reno, NV, USA)\n" +
				"22. Heather Leacock (Orlando, FL, USA)\n" +
				"23. John Gordon (Boston, MA, USA)\n" +
				"24. Frank Ralston (Chicago, IL, USA)\n" +
				"25. Victor Stevens (Madison, WI, USA)\n" +
				"26. Richard Cunningham (Fort Worth, TX, USA)\n" +
				"27. Patrick Gray (Tucson, AZ, USA)\n" +
				"28. Julia Barnett (Salt Lake City, UT, USA)\n" +
				"29. Robert Brown (Toronto, ON, Canada)\n" +
				"30. Edward Francis (Ottawa, ON, Canada)\n" +
				"31. Martha Silk (Halifax, NS, Canada)\n" +
				"32. Aaron Mitchell (Winnipeg, MB, Canada)\n" +
				"33. Ellie Sullivan (Yellowknife, NT, Canada)\n" +
				"34. João Fernandes (Lisbon, Portugal)\n" +
				"35. Madalena Sampaio (Porto, Portugal)\n" +
				"36. Hannah Schneider (Berlin, Germany)\n" +
				"37. Fynn Zimmermann (Frankfurt, Germany)\n" +
				"38. Niklas Schröder (Berlin, Germany)\n" +
				"39. Camille Bernard (Paris, France)\n" +
				"40. Dominique Lefebvre (Paris, France)\n" +
				"41. Marc Dubois (Lyon, France)\n" +
				"42. Wyatt Girard (Bordeaux, France)\n" +
				"43. Isabelle Mercier (Dijon, France)\n" +
				"44. Terhi Hämäläinen (Helsinki, Finland)\n" +
				"45. Ladislav Kovács (Budapest, Hungary)\n" +
				"46. Hugh O'Reilly (Dublin, Dublin, Ireland)\n" +
				"47. Lucas Mancini (Rome, RM, Italy)\n" +
				"48. Johannes Van der Berg (Amsterdam, VV, Netherlands)\n" +
				"49. Stanisław Wójcik (Warsaw, Poland)\n" +
				"50. Enrique Muñoz (Madrid, Spain)\n" +
				"51. Joakim Johansson (Stockholm, Sweden)\n" +
				"52. Emma Jones (London, United Kingdom)\n" +
				"53. Phil Hughes (London, United Kingdom)\n" +
				"54. Steve Murray (Edinburgh , United Kingdom)\n" +
				"55. Mark Taylor (Sidney, NSW, Australia)\n" +
				"56. Diego Gutiérrez (Buenos Aires, Argentina)\n" +
				"57. Luis Rojas (Santiago, Chile)\n" +
				"58. Manoj Pareek (Delhi, India)\n" +
				"59. Puja Srivastava (Bangalore, India)\n";
			
			assertEquals(app.customerList(), result);	}

	@Test
	void testInvoices() throws SQLException {
		final String result =
				"Invoice #23 ($3.96)\n" + 
				" 117: 'Cotton Fields' on 'Chronicle, Vol. 2' by 'Creedence Clearwater Revival' (1 @ $0.99)\n" + 
				" 118: 'Don't Look Now' on 'Chronicle, Vol. 2' by 'Creedence Clearwater Revival' (1 @ $0.99)\n" + 
				" 119: 'Before You Accuse Me' on 'Chronicle, Vol. 2' by 'Creedence Clearwater Revival' (1 @ $0.99)\n" + 
				" 120: 'Pagan Baby' on 'Chronicle, Vol. 2' by 'Creedence Clearwater Revival' (1 @ $0.99)\n" + "Invoice #45 ($5.94)\n" + 
				" 235: 'Lightning Strikes Twice' on 'Virtual XI' by 'Iron Maiden' (1 @ $0.99)\n" + 
				" 236: 'Don't Look To The Eyes Of A Stranger' on 'Virtual XI' by 'Iron Maiden' (1 @ $0.99)\n" + 
				" 237: 'Night Train' on 'Sex Machine' by 'James Brown' (1 @ $0.99)\n" + 
				" 238: 'It's A Man's Man's Man's World' on 'Sex Machine' by 'James Brown' (1 @ $0.99)\n" + 
				" 239: 'Hey America' on 'Sex Machine' by 'James Brown' (1 @ $0.99)\n" + 
				" 240: 'Get Up Offa That Thing' on 'Sex Machine' by 'James Brown' (1 @ $0.99)\n" + "Invoice #97 ($1.99)\n" + 
				" 530: 'Baltar's Escape' on 'Battlestar Galactica (Classic), Season 1' by 'Battlestar Galactica (Classic)' (1 @ $1.99)\n" + "Invoice #218 ($1.98)\n" + 
				" 1179: 'Gates Of Urizen' on 'Chemical Wedding' by 'Bruce Dickinson' (1 @ $0.99)\n" + 
				" 1180: 'Trupets Of Jericho' on 'Chemical Wedding' by 'Bruce Dickinson' (1 @ $0.99)\n" + "Invoice #229 ($13.86)\n" + 
				" 1238: 'Um Indio' on 'Minha Historia' by 'Chico Buarque' (1 @ $0.99)\n" + 
				" 1239: 'Fora Da Ordem' on 'Minha Historia' by 'Chico Buarque' (1 @ $0.99)\n" + 
				" 1240: 'Chão De Estrelas' on 'Minha História' by 'Os Mutantes' (1 @ $0.99)\n" + 
				" 1241: 'Stormbringer' on 'MK III The Final Concerts [Disc 1]' by 'Deep Purple' (1 @ $0.99)\n" + 
				" 1242: 'Houses Of The Holy' on 'Physical Graffiti [Disc 1]' by 'Led Zeppelin' (1 @ $0.99)\n" + 
				" 1243: 'Mangueira' on 'Sambas De Enredo 2001' by 'Various Artists' (1 @ $0.99)\n" + 
				" 1244: 'Love Of My Life' on 'Supernatural' by 'Santana' (1 @ $0.99)\n" + 
				" 1245: 'El Farol' on 'Supernatural' by 'Santana' (1 @ $0.99)\n" + 
				" 1246: 'Um Love' on 'The Best of Ed Motta' by 'Ed Motta' (1 @ $0.99)\n" + 
				" 1247: 'Jeru' on 'The Essential Miles Davis [Disc 1]' by 'Miles Davis' (1 @ $0.99)\n" + 
				" 1248: 'So What' on 'The Essential Miles Davis [Disc 1]' by 'Miles Davis' (1 @ $0.99)\n" + 
				" 1249: 'Black Satin' on 'The Essential Miles Davis [Disc 2]' by 'Miles Davis' (1 @ $0.99)\n" + 
				" 1250: 'Blue Rythm Fantasy' on 'Up An' Atom' by 'Gene Krupa' (1 @ $0.99)\n" + 
				" 1251: 'Bop Boogie' on 'Up An' Atom' by 'Gene Krupa' (1 @ $0.99)\n" + "Invoice #284 ($8.91)\n" + 
				" 1533: 'Texarkana' on 'Out Of Time' by 'R.E.M. Feat. Kate Pearson' (1 @ $0.99)\n" + 
				" 1534: 'So Central Rain' on 'The Best Of R.E.M.: The IRS Years' by 'R.E.M.' (1 @ $0.99)\n" + 
				" 1535: 'Fall On Me' on 'The Best Of R.E.M.: The IRS Years' by 'R.E.M.' (1 @ $0.99)\n" + 
				" 1536: 'Infeliz Natal' on 'Cesta Básica' by 'Raimundos' (1 @ $0.99)\n" + 
				" 1537: 'Esporrei Na Manivela' on 'Cesta Básica' by 'Raimundos' (1 @ $0.99)\n" + 
				" 1538: 'No Fundo Do Quintal Da Escola' on 'Raul Seixas' by 'Raul Seixas' (1 @ $0.99)\n" + 
				" 1539: 'Que Luz É Essa' on 'Raul Seixas' by 'Raul Seixas' (1 @ $0.99)\n" + 
				" 1540: 'The Power Of Equality' on 'Blood Sugar Sex Magik' by 'Red Hot Chili Peppers' (1 @ $0.99)\n" + 
				" 1541: 'Mellowship Slinky In B Major' on 'Blood Sugar Sex Magik' by 'Red Hot Chili Peppers' (1 @ $0.99)\n";

			assertEquals(app.invoices(59), result);	}

}
