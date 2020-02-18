import java.util.Scanner;

class Q6 {
	public static void main(String[] args) {
    //main method that takes 10 inputs and prints the average, median, and the number of people who passed/failed the test
    System.out.println("Veuillez entrez vos 10 notes");
    double notes[];
    notes = new double[10];

    for (int i = 0; i < notes.length; i++) {
      Scanner sc = new Scanner(System.in);
      double note = sc.nextDouble();
      notes[i] = note;
    }

    System.out.println("La moyenne des notes est de: " + calculateAverage(notes));
    System.out.println("La mediane est de: " + calculateMedian(notes));
    System.out.println(calculateNumberFailed(notes) + " personnes ont echouee(s) le test.");
    System.out.println(calculateNumberPassed(notes) + " personnes ont passee(s) le test.");

	}

	public static double calculateAverage(double[] notes) {
    //this method calculates the average of the list of int in its parameters
      double sum;
      sum = 0;
      for (int i = 0; i < notes.length; i++){
        sum = sum + notes[i];
      }
      sum = sum / notes.length;
      return sum;
	}

	public static double calculateMedian(double[] notes) {
    //this method calculates the median of the list of int in its parameters
    for (int i = 0; i < notes.length; i++){
      for (int j = 0; j < notes.length - 1; j++){
        if(notes[j] > notes[j + 1]){
          double tmp;
          tmp = notes[j + 1];
          notes[j + 1] = notes[j];
          notes[j] = tmp;
        }
      }
    }
    double mediane;
    mediane = notes[4] + notes[5];
    mediane = mediane / 2;
      return mediane;
	}

	public static int calculateNumberFailed(double[] notes) {
    //this method counts the number of people who failed the test
      int numEchecs;
      numEchecs = 0;
      for(int i = 0; i < notes.length; i++){
        if(notes[i] < 50.0){
          numEchecs = numEchecs + 1;
        }
      }

      return numEchecs;
	}

	public static int calculateNumberPassed(double[] notes) {
    //this method counts the number of people who passed the test
	    int numPass;
      numPass = 0;
      for(int i = 0; i < notes.length; i++){
        if(notes[i] > 50){
          numPass = numPass + 1;
        }
      }
      return numPass;
	}

}
