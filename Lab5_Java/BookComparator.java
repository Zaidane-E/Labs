import java.util.Comparator;

public class BookComparator implements Comparator<Book> {

    // Implement the comparator method for books.
    public boolean equals(Object other) {
      return this.equals(other);
    }

    public int compare(Book book1, Book book2) {
      Book firstBook = (Book) book1;
      Book secondBook = (Book) book2;
      int compareAuthor = firstBook.getAuthor().compareTo(secondBook.getAuthor());
      int compareTitle = firstBook.getTitle().compareTo(secondBook.getTitle());
      int compareYear = 0;
      if ( firstBook.getYear() < secondBook.getYear() ) {
        compareYear = -1;
      } else if ( firstBook.getYear() > secondBook.getYear() ) {
        compareYear = 1;
      }
      if ( compareAuthor != 0 ) {
          return compareAuthor;
      } else if ( compareTitle != 0 ) {
          return compareTitle;
      } else {
          return compareYear;
      }
    }

}
