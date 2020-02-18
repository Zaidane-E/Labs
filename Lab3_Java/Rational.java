public class Rational {

    private int numerator;
    private int denominator;

    // constructors

    public Rational(int numerator) {
	     this.numerator = numerator;
       denominator = 1;
    }

    public Rational(int numerator, int denominator) {
	     this.numerator = numerator;
       this.denominator = denominator;
       this.reduce();
    }

    // getters

    public int getNumerator() {
	     return numerator;
    }

    public int getDenominator() {
	     return denominator;
    }

    // instance methods

    public Rational plus(Rational other) {
      Rational sum = new Rational(this.numerator * other.denominator + other.numerator * this.denominator, this.denominator * other.denominator);
      return sum;
    }

    public static Rational plus(Rational a, Rational b) {
      Rational sum = new Rational(a.numerator * b.denominator + b.numerator * a.denominator, a.denominator * b.denominator);
    	return sum;
    }

    // Transforms this number into its reduced form

    private void reduce() {
      int gcd = gcd(this.numerator, this.denominator);
      this.numerator = this.numerator / gcd;
      this.denominator = this.denominator / gcd;
    }

    // Euclid's algorithm for calculating the greatest common divisor
    private int gcd(int a, int b) {
      // Note that the loop below, as-is, will time out on negative inputs.
      // The gcd should always be a positive number.
      // Add code here to pre-process the inputs so this doesn't happen.
      if ( a < 0 ) {
        a = - a;
      }
      if ( b < 0 ) {
        b = - b;
      }

    	while (a != b)
    	    if (a > b)
    		     a = a - b;
    	    else
    		     b = b - a;
    	return a;
    }

    public int compareTo(Rational other) {
      if ( this.equals(other) ) {
        return 0;
      } else if ( this.numerator * other.denominator < other.numerator * other.denominator ) {
        return -1;
      } else {
        return 1;
      }
    }

    public boolean equals(Rational other) {
      return ( this.numerator * other.denominator == other.numerator * this.denominator );
    }

    public String toString() {
    	String result;
      result = "";
    	if (denominator == 1) {
    	    result += numerator;
    	} else {
    	    result = numerator + "/" + denominator;
    	}
    	return result;
    }

}
