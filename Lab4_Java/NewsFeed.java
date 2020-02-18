/* *
 * Use static array for NewsFeed
 * with constant MAX_SIZE
 * */

public class NewsFeed {

    private Post[] messages;
    private int size;
    public static final int MAX_SIZE = 25;

    public NewsFeed() {
    	messages = new Post[MAX_SIZE];
      this.sort();
    }

    public void add(Post message) {
      for ( int i = 0 ; i < size ; i++ ) {
        if ( messages[i] == null ) {
          messages[i] = message;
          break;
        }
      }
    }

    public Post get(int index) {
	     return messages[index];
    }

    public int size() {
	     return size;
    }

	  public void sort(){
			int i, j, argMin;
			Post tmp;
			for (i = 0; i < size - 1; i++) {
				argMin = i;
				for (j = i + 1; j < size(); j++) {
					if (messages[j].compareTo(messages[argMin]) < 0) {
						argMin = j;
					}
				}

  			tmp = messages[argMin];
  			messages[argMin] = messages[i];
  			messages[i] = tmp;
		  }

	  }

  	public NewsFeed getPhotoPost(){
      NewsFeed photoPost = new NewsFeed();
      for ( int i=0 ; i < size ; i++ ){
        if ( messages[i].getClass().getName().equals("PhotoPost") ) {
          photoPost.add(messages[i]);
        }
      }
      return photoPost;
  	}

  	public NewsFeed plus(NewsFeed other){
      NewsFeed feed = new NewsFeed();
  	  for ( int i = 0 ; i < 25 ; i++ ) {
        feed.add(this.messages[i]);
      }
      for ( int i = 25 ; i < 50 ; i++ ) {
        feed.add(other.messages[i]);
      }
      feed.sort();
      return feed;
  	}

}
