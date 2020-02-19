public class Book {

    // Your variables declaration here
    private String author;
    private String title;
    private int year;

    public Book (String author, String title, int year) {
        this.author = author;
        this.title = title;
        this.year = year;
    }

    public String getAuthor() {
        return author;
    }

    public String getTitle() {
        return title;
    }

    public int getYear() {
        return year;
    }

    public boolean equals(Object other) {
        if ( other == null ) {
          return false;
        }
        if ( other == this ) {
          return true;
        }
        if ( getClass() != other.getClass() ){
            return false;
        }
        Book otherBook = (Book) other;
        return (author == otherBook.author
        || author != null && author.equals(otherBook.author))
        && (title == otherBook.title
        || title != null && title.equals(otherBook.title))
        && year == otherBook.year;
    }

    public String toString() {
        return author + ": " + title + " (" + year + ")";
    }

}
