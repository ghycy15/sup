/*
 * LCF 2011-2013
 * created Feb 2 2013
 * Author @ huyue gu
 * 
 * 
 */

import java.io.File;
import java.util.Iterator;
import java.util.List;

import org.scribe.builder.ServiceBuilder;
import com.google.gson.Gson;
import org.scribe.model.OAuthRequest;
import org.scribe.model.Response;
import org.scribe.model.Token;
import org.scribe.model.Verb;
import org.scribe.oauth.OAuthService;

import com.google.gson.Gson;
import com.google.gson.JsonSyntaxException;
import com.yelp.v2.Business;
import com.yelp.v2.YelpSearchResult;

public class YelpConnection {

	public void start(String ip, String cat,String dist) {
		// Define your keys, tokens and secrets. These are available from the
		// Yelp website.
		String CONSUMER_KEY = "-hXkAOq4tlFshumHKMVAjA";
		String CONSUMER_SECRET = "XXl8I1DB2ygKPLDOsRllyaVAYYI";
		String TOKEN = "h7zadWUyf5BGcKCb2tSiqJK4AFJotbLz";
		String TOKEN_SECRET = "96Ey1twvJEcEKv4Xpon8vwkGemg";
		/*
		 * 
		 * Consumer Key	-hXkAOq4tlFshumHKMVAjA
Consumer Secret	XXl8I1DB2ygKPLDOsRllyaVAYYI
Token	h7zadWUyf5BGcKCb2tSiqJK4AFJotbLz
Token Secret	96Ey1twvJEcEKv4Xpon8vwkGemg
		 * new key: Consumer Key IEnQZlSRf1Lp4CrQ55YS0w Consumer Secret
		 * Wu4B2agSfXC3i2mcoIZk8h5adKY Token DPACv1RddYrdBDAnA7mIph493P_2KGZb
		 * Token Secret wbr0ndsjWQYXigYpynPrClz1heM
		 * Consumer Key	wLx6D1CmwtdmGes38Hv9Ow
Consumer Secret	NuV9Op1FfNPKbX9PA-EfGM7D6xk
Token	zrxMhSsw6OcyqXZqR6M2I2UNVrCIZkgn
Token Secret	jWT5_SGoPHYBl704RdOjV5T5Gqo
Consumer Key	hu3fzmww77D7TA527vzpDQ
Consumer Secret	2IQZ-lkKF_eKioJA5FJtvX10wGw
Token	y5ASmvNiFPtaXqC4FZw9pdQEooXirrbv
Token Secret	Jogj33qWDWk7isDVYKfK-YbAWZk
		 */
		// Some example values to pass into the Yelp search service.

		// String ip = ListIP.getWebIp("http://www.ip138.com/ips1388.asp");
		// System.out.println("IP is: "+ip);
		String json = ListIP.getIpInfo("https://dazzlepod.com/ip/" + ip
				+ ".json");
		System.out.println(json);
		System.out.println("Dataset");
		IPDATA data = ListIP.readjson(json);
		// System.out.println("Position: ("+data.latitude+","+data.longitude+")");
		String lat = data.latitude;
		String lng = data.longitude;
		OAuthService service = new ServiceBuilder().provider(YelpV2API.class)
				.apiKey(CONSUMER_KEY).apiSecret(CONSUMER_SECRET).build();
		Token accessToken = new Token(TOKEN, TOKEN_SECRET);
		OAuthRequest request = new OAuthRequest(Verb.GET,
				"http://api.yelp.com/v2/search");
		if (cat.equals("eat")) {
			
			request.addQuerystringParameter("category_filter","restaurants");
		} else if (cat.equals("play")) {
			request.addQuerystringParameter("category_filter",
					"active,arts,beautysvc,nightlife,shopping");

		} else {
			
			request.addQuerystringParameter("category_filter",
					cat);
			
		}
		// Execute a signed call to the Yelp service.

		request.addQuerystringParameter("ll", lat + "," + lng);
		// request.addQuerystringParameter("category_filter", category);
		request.addQuerystringParameter("radius_filter", dist);

		service.signRequest(accessToken, request);
		Response response = request.send();
		String rawData = response.getBody();

		// Sample of how to turn that text into Java objects.
		try {
			YelpSearchResult places = new Gson().fromJson(rawData,
					YelpSearchResult.class);
			// System.out.println(places.);
			System.out.println("Your search found " + places.getTotal()
					+ " results.");
			System.out.println("Yelp returned " + places.getBusinesses().size()
					+ " businesses in this request.");
			System.out.println();

			for (Business biz : places.getBusinesses()) {
				System.out.println("Dataset");
				System.out.println(biz.getName() + "data");
				for (String address : biz.getLocation().getAddress()) {
					System.out.println("  " + address);
				}
				System.out.println("data  " + biz.getLocation().getCity());
				System.out.println("data" + biz.getUrl());
				// System.out.println(biz.toString());
				// System.out.println(biz.getReviewCount());
				// System.out.println(biz.getRatingImgUrl());
				System.out.println("data" + biz.getDistance());
				List<List<String>> cats = biz.getCategories();
				System.out.println("data");
				Iterator<List<String>> iter = cats.iterator();
				while (iter.hasNext()) {
					System.out.print(iter.next() + ",");
				}
				System.out.println("data" + biz.getImageUrl());
				// System.out.println(biz.setRatingImgUrl(ratingImgUrl));
				System.out.println();
			}
			System.out.println("Dataset");

		} catch (Exception e) {
			System.out.println("Error, could not parse returned data!");
			System.out.println(rawData);
		}

	}

	private static void add_to_file(String to_do) {
		File file = new File("tododata.sup");

	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String ip = args[0];
		if (args.length > 0) {
			if (args[1] == "stay") {

			} else if (args[1].equals("eat")) {
				new YelpConnection().start(ip, "restaurant",args[2]);
			} else if (args[1].equals("play")) {
				new YelpConnection().start(ip, "play",args[2]);
			} else {
				new YelpConnection().start(ip, args[1],args[2]);
			}

		}

	}

}
