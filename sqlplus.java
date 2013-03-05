import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.File;
import java.util.Map;

public class test1 {
    
    public static void main (String args []) {
        
        test_script();
    }
    
    public static void test_script () {
        
        String fileName = "@test_table.sql";
        String sqlPath = "E:\\";
        
        String sqlCmd = "sqlplus";
        
        String arg1   = "user/password@sid"; -- plug in your user, password and db name
        String arg2   = fileName;
        try {
            String line;
            ProcessBuilder pb = new ProcessBuilder(sqlCmd, arg1, arg2);
            Map<String, String> env = pb.environment();
            env.put("VAR1", arg1);
            env.put("VAR2", arg2);
            pb.directory(new File(sqlPath));
            pb.redirectErrorStream(true);
            Process p = pb.start();
            BufferedReader bri = new BufferedReader
            (new InputStreamReader(p.getInputStream()));
            BufferedReader bre = new BufferedReader
            (new InputStreamReader(p.getErrorStream()));
            while ((line = bri.readLine()) != null) {
                System.out.println(line);
            }
            bri.close();
            while ((line = bre.readLine()) != null) {
                System.out.println(line);
            }
            bre.close();
            System.out.println("Done.");
        }
        catch (Exception err) {
            err.printStackTrace();
        }
        
    }
    
}