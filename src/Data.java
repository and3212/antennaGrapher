import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

/* Author: Liam Lawrence
 * Date: July 19, 2017
 * Reads in our CSV file and sorts it
 */

public class Data {
    // Three columns from our CSV file
    public ArrayList<Double> power = new ArrayList<>();
    public ArrayList<Double> azimuth = new ArrayList<>();
    public ArrayList<Double> elevation = new ArrayList<>();

    // Read in our data from a file
    public static Data fromFile(String filePath) throws Exception {
        boolean firstPass = false;
        Data data = new Data();
        String line;

        // Read in our file and sort it into the proper ArrayLists
        BufferedReader buff = new BufferedReader(new FileReader(filePath));
        while((line = buff.readLine()) != null){
            if(firstPass) {
                String[] splitStrings = line.split(",");
                data.power.add(Double.parseDouble(splitStrings[0]));
                data.azimuth.add(Double.parseDouble(splitStrings[1]));
                data.elevation.add(Double.parseDouble(splitStrings[2]));
            }
            firstPass = true;
        }
        buff.close();
        return data;
    }
}