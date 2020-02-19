import java.util.ArrayList;

public class Library {

    private ArrayList<Book> library = new ArrayList<Book>();

    public Book getBook(int i) {
      return library.get(i);
    }

    public int getSize() {
      return library.size();
    }

    public void addBook (Book b) {
        library.add(b);
    }

    public void sort() {
        java.util.Comparator<Book> compare = new BookComparator();
        int i, j, argMin;
  			Book tmp;
  			for ( i = 0 ; i < getSize() - 1 ; i++ ) {
  				argMin = i;
  				for ( j = i + 1 ; j < getSize() ; j++ ) {
  					if ( compare.compare(library.get(j), library.get(argMin)) < 0 ) {
  						argMin = j;
  					}
  				}
    			tmp = library.get(argMin);
    			library.set(argMin, library.get(i));
    			library.set(i, tmp);
  		  }
    }

    public void printLibrary() {
        sort();
        System.out.println(library);
    }

}
