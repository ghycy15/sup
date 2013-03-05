/*
 * LCF 2011-2013
 * created Feb 2 2013
 * Author @ huyue gu
 * 
 * 
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLConnection;
import com.google.gson.Gson;

public class ListIP {

 /**
  * @param args
  */
	static {
	    //for localhost testing only
	    javax.net.ssl.HttpsURLConnection.setDefaultHostnameVerifier(
	    new javax.net.ssl.HostnameVerifier(){
 
	        public boolean verify(String hostname,
	                javax.net.ssl.SSLSession sslSession) {
	            if (hostname.equals("dazzlepod.com")) {
	                return true;
	            }
	            return false;
	        }
	    });
	}
// public static void main(String[] args) {
//  // TODO Auto-generated method stub  
//	 String ip = ListIP.getWebIp("http://www.ip138.com/ips1388.asp");
//  System.out.println("IP is£º"+ip);
//   String json = ListIP.getIpInfo("https://dazzlepod.com/ip/"+ip+".json");
//  System.out.println(json);
//   IPDATA data = readjson( json);
//   System.out.println("Position: ("+data.latitude+","+data.longitude+")");
// }

 
 public static IPDATA readjson(String json){
	 
	 IPDATA data = new Gson().fromJson(json, IPDATA.class);
	 
	 return data;
 }
 
 
 public static String getWebIp(String strUrl) {
  try {

   URL url = new URL(strUrl);

   BufferedReader br = new BufferedReader(new InputStreamReader(url

   .openStream()));

   String s = "";

   StringBuffer sb = new StringBuffer("");
   
   String webContent = "";

   while ((s = br.readLine()) != null) {
    sb.append(s + "\r\n");

   }

   br.close();
   webContent = sb.toString();
   int start = webContent.indexOf("http://www.gongju.com/");
   int end = webContent.indexOf("/*ip138-ips-468*60*/");
   webContent = webContent.substring(start,end);
   start = webContent.indexOf("[")+1;
   end = webContent.indexOf("]");
   webContent = webContent.substring(start,end);
   return webContent;

  } catch (Exception e) {
   e.printStackTrace();
   return "error open url:" + strUrl;

  }
 }
 
 public static String getIpInfo(String strUrl) {
	 String inputLine = null;
	
	 BufferedReader reader = null;
	 try {
		 URL url = new URL(strUrl);
		 HttpURLConnection httpcon = (HttpURLConnection) url.openConnection();
		 httpcon.addRequestProperty("User-Agent", "Mozilla/4.76"); 
		 //System.out.print("here");
	     reader = new BufferedReader(new InputStreamReader(httpcon.getInputStream(), "UTF-8"));

	     for (String line; (inputLine = reader.readLine()) != null;) {
	        // System.out.println(inputLine);
	         return inputLine;
	     }
	 } catch (UnsupportedEncodingException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	} catch (IOException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	} finally {
	     if (reader != null) try { reader.close(); } catch (IOException ignore) {}
	 }
	return inputLine;
 }
	 
 
}

class IPDATA{
	String country;
	String city;
	String latitude;
	String ip;
	String region;
	String longitude;
	

}