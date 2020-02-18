public class Q3_SquareArray{

	public static int[] createArray(int size) {
		//this method creates an array by making each value in the array its index's square
    int[] anArray;
    anArray = new int[size + 1];
		for (int i = 0; i < anArray.length ; i++) {
      anArray[i] = i * i;
    }
    return anArray;
	}

	public static void main(String[] args){
		//main method that prints the list of squared numbers
    int[] arrayToPrint = createArray(12);
    for (int i = 0; i < arrayToPrint.length; i++) {
      System.out.println("The square of " + i + " is: " + arrayToPrint[i]);
    }
	}
}
