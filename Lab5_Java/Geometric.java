public class Geometric extends AbstractSeries {

    // instance variables
    private double k = 1;
    private double s = 0;

    // implement the method
    public double next() {
        s = s + (1/k);
        k = k * 2;
        return s;
    }

}
