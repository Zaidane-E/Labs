public class ComputerRandomPlayer implements Player {

    public void play(TicTacToeGame game) {

        if ( game.getGameState() == GameState.PLAYING ) {
            
            System.out.println("Player 2's turn.");
            int value, nEmptyCells = 0;
            for ( int i = 0 ; i < game.lines*game.columns ; i++ ) {
                if ( game.valueAt(i) == CellValue.EMPTY ) {
                    nEmptyCells++;
                }
            }

            int[] emptyCells = new int[nEmptyCells];
            
            int j = 0;
            while ( j < emptyCells.length ) {
                for ( int i = 0 ; i < game.lines*game.columns ; i++ ) {
                    if ( game.valueAt(i) == CellValue.EMPTY ) {
                        emptyCells[j] = i;
                        j++;
                    }
                }
            }

            value = emptyCells[Utils.generator.nextInt(emptyCells.length)];
            game.play(value);

        } else {
            System.out.println("Error: this game is not playable.");
        }

    }

}