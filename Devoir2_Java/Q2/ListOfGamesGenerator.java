import java.util.LinkedList;

public class ListOfGamesGenerator {
	

   /**
	* generates all different games for the specified
	* parameters. Each game is recorded only once. 
	* once a game is finished, it is not extended further
	* @param lines
    *  the number of lines in the game
    * @param columns
    *  the number of columns in the game
    * @param sizeWin
    *  the number of cells that must be aligned to win.
    * @return
    * a list of lists of game instances, ordered by levels
  	*/
	public static LinkedList<LinkedList<TicTacToeGame>> generateAllGames(int lines, int columns, int winLength){

      LinkedList<LinkedList<TicTacToeGame>> allGames = new LinkedList<LinkedList<TicTacToeGame>>();
      LinkedList<TicTacToeGame> gamesList = new LinkedList<TicTacToeGame>();
      TicTacToeGame newGame = new TicTacToeGame(lines, columns, winLength);
      gamesList.add(0, newGame);
      allGames.add(0, gamesList);

      boolean generate = true;

      while ( generate ) {
         
         generate = false;
         LinkedList<TicTacToeGame> list = new LinkedList<TicTacToeGame>();

         for( TicTacToeGame game: gamesList ) {

            for ( int i = 0 ; i < lines*columns ; i++ ) {

               if ( game.valueAt(i) == CellValue.EMPTY && game.getGameState() == GameState.PLAYING ) {

                  newGame = new TicTacToeGame(game, i);
                  boolean valid = true;

                  for ( TicTacToeGame otherGame: list ) {

                     if ( newGame.equals(otherGame) ) {
                        valid = false;
                        break;
                     }

                  }

                  if ( valid ) {
                     list.add(newGame);
                  }

                  if ( newGame.getGameState() == GameState.PLAYING ) {
                     generate = true;
                  }

               }

            }

         }

         gamesList = list;
         allGames.addLast(gamesList);

      }

      return allGames;

	}
}