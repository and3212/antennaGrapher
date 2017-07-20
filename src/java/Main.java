import java.util.Scanner;

/* Author: Liam Lawrence
 * Date: July 19, 2017
 * Takes our CSV data and graphs it in Polar Coordinates
 */

public class Main {

    // For elevation scans
    static void elevationParser(double angle, Data data, double offset) {
        Data validData = new Data();

        // Lists out the data points your using
        System.out.println("Using the following data points");
        System.out.println("| dBm | Azimuth | Elevation |");
        System.out.println("----------------------");
        for(int i = 0; i < data.elevation.size(); i++) {
            if(data.elevation.get(i).equals(angle)) {
                validData.power.add(data.power.get(i) + offset);
                validData.azimuth.add(data.azimuth.get(i));
                validData.elevation.add(data.elevation.get(i));

                System.out.print(data.power.get(i) + " | ");
                System.out.print(data.azimuth.get(i) + " | ");
                System.out.print(data.elevation.get(i));
                System.out.println("");
            }
        }
        System.out.println("----------------------");
        // Creates the graphs
        GraphManager manager = new GraphManager(validData.azimuth, validData.power);
        manager.spawnDialog();
    }

    // For azimuth scans
    static void azimuthParser(double angle, Data data, double offset) {
        Data validData = new Data();

        // Lists out the data points your using
        System.out.println("Using the following data points");
        System.out.println("| dBm | Azimuth | Elevation |");
        System.out.println("----------------------");
        for(int i = 0; i < data.azimuth.size(); i++) {
            if(data.azimuth.get(i).equals(angle)) {
                validData.power.add(data.power.get(i) + offset);
                validData.azimuth.add(data.azimuth.get(i));
                validData.elevation.add(data.elevation.get(i));

                System.out.print("| " + data.power.get(i) + " | ");
                System.out.print(data.azimuth.get(i) + " | ");
                System.out.print(data.elevation.get(i) + " |");
                System.out.println("");
            }
        }
        System.out.println("----------------------");
        // Creates the graphs
        GraphManager manager = new GraphManager(validData.elevation, validData.power);
        manager.spawnDialog();
    }

    // Main method with lots of user interface stuff
    public static void main(String[] args) throws Exception {
        Data data = Data.fromFile("../../res/data.csv");
        double angle;

        Scanner reader = new Scanner(System.in);  // Reading from System.in
        System.out.print("Azimuth or Elevation scan [A/e] ");

        // Parse an Elevation from 0 - 75 degrees
        if (reader.next().toLowerCase().equals("e")) {
            System.out.print("What angle would you like to scan [0/15/30/45/60/75] ");
            angle = reader.nextInt();

            // Checks to see if anything is invalid
            if (angle > 75 || angle % 15 != 0 || angle < 0) {
                System.out.println("Invalid number, defaulting to 0");
                angle = 0;
            }
            // Parse the elevation
            elevationParser(angle, data, 100);

            // Parse an Azimuth from -90 to 90
        } else {
            System.out.print("What angle would you like to scan [-90/-75/-60/-45/-30/-15/0/15/30/45/60/75/90] ");
            angle = reader.nextInt();

            // Checks to see fi anything is invalid
            if (angle > 90 || angle % 15 != 0 || angle < -90) {
                System.out.println("Invalid number, defaulting to 0");
                angle = 0;
            }
            // Parse the azimuth
            azimuthParser(angle, data, 100);
        }
    }
}
