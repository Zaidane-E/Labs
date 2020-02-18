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
        // Your code here
        library.add(b);
    }

    public void sort() {
        // Your code here
        java.util.Comparator<Book> compare;
        compare = new BookComparator();
        Book tmp;
        for ( int i = 0 ; i < library.size() - 1 ; i++ ) {
            for ( int j = i + 1 ; j < library.size() ; j++ ) {
                if ( compare.compare(library.get(i), library.get(j)) < 0 ) {
                    tmp = library.get(j);
                    library.set(i, library.get(j));
                    library.set(j, tmp);
                }
            }
        }
        
    }


    public void printLibrary() {
        // Your code here
        sort();
        System.out.println(library);
    }
}