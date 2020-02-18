public class Combination {

    // Instance variables.
    int num1;
    int num2;
    int num3;

    // Constructor
    public Combination( int first, int second, int third ) {
        num1 = first;
        num2 = second;
        num3 = third;
    }

    // An instance method that compares this object
    // to other.
    // Always check that other is not null, i)
    // an error would occur if you tried to
    // access other.first if other was null, ii)
    // null is a valid argument, the method should
    // simply return false.

    public boolean equals( Combination other ) {
      if(other == null || this.num1 != other.num1 || this.num2 != other.num2 || this.num3 != other.num3){
        return false;
      }
      return true;
    }

    // Returns a String representation of this Combination.

    public String toString() {
        return num1 + ":" + num2 + ":" + num3;
    }

}
