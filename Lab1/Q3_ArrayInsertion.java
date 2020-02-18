import java.util.Arrays;

public class Q3_ArrayInsertion{

  	public static int[] insertIntoArray(int[] beforeArray, int indexToInsert, int valueToInsert){
      //this method inserts a specified array at the specified index
      int[] tmp;
      tmp = new int[beforeArray.length + 1];
      for (int i = 0; i < indexToInsert; i++){
        tmp[i] = beforeArray[i];
      }
      tmp[indexToInsert] = valueToInsert;
      for (int i = indexToInsert + 1; i <= beforeArray.length; i++){
        tmp[i] = beforeArray[i - 1];
      }
      return tmp;
  	}

  	public static void main(String[] args){
      //this is the main method that prints the array before and after the insertion
  		int[] beforeArray = {1,2,3,4,5,6};
      int indexToInsert = 2;
      int valueToInsert = 15;
      int[] afterArray;
      afterArray = insertIntoArray(beforeArray, indexToInsert, valueToInsert);
      System.out.println("Array avant l'insertion:");
      for (int i = 0; i < beforeArray.length; i++){
        System.out.println(beforeArray[i]);
      }
      System.out.println("Array apres l'insertion de " + valueToInsert + " a la position " + indexToInsert + ":");
      for (int i = 0; i < afterArray.length; i++){
        System.out.println(afterArray[i]);
      }
  	}
  }
