import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;
import javax.swing.*;
import java.util.List;

/* Author: Liam Lawrence
 * Date: July 19, 2017
 * Graphs our data using JFree Chart
 */

public class GraphManager {
    // Chart variables
    XYSeries dataSeries;
    XYSeriesCollection collection;
    JFreeChart polarChart;

    // Sets up graph
    public GraphManager(List<Double> theta, List<Double> radius) {
        assert theta.size() == radius.size();
        dataSeries = new XYSeries("Series 1");

        // Adds our data into the graphs XYSeries
        for(int i = 0; i < theta.size(); i++) {
            dataSeries.add(theta.get(i), radius.get(i));
        }

        // Sets up polar chart
        collection = new XYSeriesCollection(dataSeries);
        polarChart = ChartFactory.createPolarChart("Polar Chart Example", collection, true, true, false);
    }

    // Creates a JPanel
    public ChartPanel getFrame() {
        return new ChartPanel(polarChart);
    }

    // Creates the final window with the graph on it
    public void spawnDialog() {
        JDialog dialog = new JDialog();
        dialog.add(getFrame());
        dialog.pack();
        dialog.setVisible(true);
    }
}
