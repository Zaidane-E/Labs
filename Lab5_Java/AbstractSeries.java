public abstract class AbstractSeries implements Series {

  public double[] take(int k) {

      // implement the method
      double[] sommesPartielles = new double[k];
      for ( int i = 0; i < k ; i++ ) {
        sommesPartielles[i] = next();
      }
      return sommesPartielles;

  }

}
