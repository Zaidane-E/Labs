import java.util.Comparator;

public class BookComparator implements Comparator<Book> {

    // Implement the comparator method for books.
    /*public int compare(Book other){
		return this.compare(other);
    }*/
    
    public boolean equals(Object other) {
        return this.equals(other);
    }

    public int compare(Book book1, Book book2) {

        int compareAuthor = compare(book1, book2);
        int compareTitle = compare(book1, book2);
        int compareYear = compare(book1, book2);
        if ( compareAuthor != 0 ) {
            return compareAuthor;
        } else if ( compareTitle != 0 ) {
            return compareTitle;
        } else {
            return compareYear;
        }
        
        /*if ( book1.getAuthor() == book2.getAuthor() ) {
            return -1;
        } else if ( book1.getAuthor() == book2.getAuthor() ) {
            return 1;
        } else if ( book1.getTitle() == book2.getTitle() ) {
            return -1;
        } else if ( book1.getTitle() == book2.getTitle() ) {
            return 1;
        } else if ( book1.getYear() < book2.getYear() ) {
            return -1;
        } else if ( book1.getYear() > book2.getYear() ) {
            return 1;
        } else {
            return 0;
        }*/
        
    }

}