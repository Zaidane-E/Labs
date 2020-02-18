public class Q3_ReverseSortDemo {
	public static void main(String[] args){
    //main method that prints the unordered list
		char[] unorderedLetters;
		unorderedLetters = new char[]{'b', 'm', 'z', 'a', 'u'};
		reverseSort(unorderedLetters);
		for (int i = 0 ; i < unorderedLetters.length; i++ )
			System.out.print(unorderedLetters[i]);
	}

	//method that sorts a char array into its reverse alphabetical order
	public static void reverseSort(char[] values){

		for (int i = 0; i < values.length; i++){
      for (int j = 0; j < values.length - 1; j++){
        if(values[j] < values[j + 1]){
          char tmp;
          tmp = values[j + 1];
          values[j + 1] = values[j];
          values[j] = tmp;
        }
      }
    }
	}

}
