public class HumanPlayer implements Player {

    public void play(TicTacToeGame game) {

        if ( game.getGameState() == GameState.PLAYING ) {
            
            System.out.println("Player 1's turn.");

            boolean validCell = false;
            while ( !validCell ) {

                System.out.println(game);
                System.out.print(game.nextCellValue() + " to play: ");
                String answer = Utils.console.readLine();
                int value;
                
                value = Integer.parseInt(answer)-1;
            
                if(value < 0 || value >= (game.lines*game.columns)){
                    System.out.println("The value should be between 1 and " + (game.lines*game.columns));
                } else if(game.valueAt(value) != CellValue.EMPTY) {
                    System.out.println("This cell has already been played");
                } else {
                    game.play(value);
                    validCell = true;
                }
                
            }
        } else {
            System.out.println("Error: this game is not playable.");
        }

    }

}