import java.io.Console;

public class TicTacToe{

   /**
     * <b>main</b> of the application. Creates the instance of  GameController 
     * and starts the game. If two parameters line  and column
     * are passed, they are used. 
     * Otherwise, a default value is used. Defaults values are also
     * used if the paramters are too small (less than 2).
     * 
     * @param args
     *            command line parameters
     */
     public static void main(String[] args) {

        StudentInfo.display();

        TicTacToeGame game;
        int lines = 3;
        int columns = 3;
        int win = 3;

   
        try{
            if (args.length >= 2) {
                lines = Integer.parseInt(args[0]);
                if(lines<2){
                    System.out.println("Invalid argument, using default...");
                    lines = 3;
                }
                columns = Integer.parseInt(args[1]);
                if(columns<2){
                    System.out.println("Invalid argument, using default...");
                    columns = 3;
                }
            }
            if (args.length >= 3){
                win = Integer.parseInt(args[2]);
                if(win<2){
                    System.out.println("Invalid argument, using default...");
                    win = 3;
                }
            } 
            if (args.length > 3){
                System.out.println("Too many arguments. Only the first 3 are used.");
            } 

        } catch(NumberFormatException e){
            System.out.println("Invalid argument, using default...");
            lines   = 3;
            columns  = 3;
            win = 3;
        }
        
        Player[] players;
        players = new Player[2];

        Console console = System.console();

        HumanPlayer human = new HumanPlayer();
        ComputerRandomPlayer computer = new ComputerRandomPlayer();

        players[0] = human;
        players[1] = computer;

        game = new TicTacToeGame(lines, columns,win);
        boolean playGame = true;
        int firstPlayer, playerTurn;
        firstPlayer = playerTurn = Utils.generator.nextInt(2);

        while ( playGame ) {

            playerTurn = firstPlayer;

            while ( game.getGameState() == GameState.PLAYING ) {

                players[playerTurn].play(game);
                playerTurn += ( playerTurn == 0 ) ? 1 : -1;
                
            }

            System.out.println("Game Over.");
            System.out.println(game);
            System.out.println("Result: " + game.getGameState());
            System.out.print("Play again (Y)?: ");
            String answer = console.readLine();
            if ( answer.toLowerCase().equals("y") && game.getGameState() != GameState.PLAYING ) {
                game = new TicTacToeGame(lines, columns,win);
                firstPlayer += ( firstPlayer == 0 ) ? 1 : -1;
            } else {
                playGame = false;
            }

        }

    }

}