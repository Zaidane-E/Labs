public class Arithmetic extends AbstractSeries {

    // instance variables
    private double k = 1;
    private double s = 0;

    // implement the method
    public double next() {
        s = s + k;
        k = k + 1;
        return s;
    }

}
