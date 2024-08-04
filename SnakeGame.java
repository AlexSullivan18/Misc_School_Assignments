

/*
Alexander Sullivan this is assignment 1 for comp 250 it is the classic videogame snake where a dot eats pellets in order
to grow in size if it eats poison it dies. this classes utilizes gui to create user interface and linkedlist in order to
grow an
I have implemented the poison pellet linked list
I have implemented the game won mechanic with a simple if statement checking snake size
I have implemented the snake eating itself mechanic where the game ends if the snake comes in contact with itself
I have implemented the snake speed increase as the size increases

most of these implimentations where simply completed by adding an if statement usually in the move method checking a parameter and comparing the snakes position to another entitiy
the speed one evertime the snake eats a pellet the delay decreases by 10
the poison the last added poison pellet is randomized everytime the snake eats regular food by removing the last node in the hitFood function and adding a new random coordnate to the first node
the snake eating itself just checks the newhead position against the other locations occupied by the rest of the snake using snake.getLast()
and the game won just checks if snake.size() is greater than 20

the major issue i seem to find is that the delay starts to break as the snake speeds up and the screens refresh rate starts to bug out

I did not implement the more food pellets becuase everytime I tried to implement them via linkedList it would not register the other 4 food pellets as entities and the snake would pass
right through them. So i decided after alot of time tinkering with it that all the changes to the existing code and new lines to be added for the new and randomized pellets proved to be to difficult for me
 */
import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.LinkedList;
import java.util.Random;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.Timer;
/**
 * Written by Seikyung Jung
 * Warning:
 * You must not post this code online.
 * You must not share this code without permission from the author
 *
 * Current:
 * One snake and one food, No poison
 * The snake does not die when it bumps into itself
 * when the snake grows, it does not move faster

 */
public class SnakeGame extends JFrame {
    // A snake is just a list of coordinates (java.util.LinkedList, not our LinkedList)
    private LinkedList<Coordinate> snake = new LinkedList<Coordinate>();
    // The snake grows when it eats food
    private Coordinate food = new Coordinate();
    private LinkedList<Coordinate> foodList = new LinkedList <Coordinate>();
    private LinkedList <Coordinate> poison = new LinkedList<Coordinate>();
    Coordinate newPoison= new Coordinate();


    // The game is on or over
    private static enum Game { ON, OVER,WON};
    private Game status = Game.ON;

    // Repeatedly moves the snake
    private Timer timer;

    // The snake can move in one of 4 directions
    public static enum Direction { UP, DOWN, LEFT, RIGHT };
    // The snake's current direction (heading). Default: moving right
    private Direction heading = Direction.RIGHT;

    /**
     * 	An (x,y) coordinate in a 64 by 48 grid
     */
    public static class Coordinate {
        public final int x;
        public final int y;
        // By default, construct a random coordinate not too far from the wall
        Coordinate() {
            this.x = new Random().nextInt(60) + 2;
            this.y = new Random().nextInt(40) + 2;
        }
        Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    // The snake can't switch to the opposite direction
    public boolean oppositeDirection(Direction newHeading) {
        return (heading == Direction.UP && newHeading == Direction.DOWN) ||
                (heading == Direction.DOWN && newHeading == Direction.UP) ||
                (heading == Direction.LEFT && newHeading == Direction.RIGHT) ||
                (heading == Direction.RIGHT && newHeading == Direction.LEFT);
    }

    // Update the heading based on the new heading
    public void changeHeading(Direction newHeading) {
        if (!oppositeDirection(newHeading)) {
            heading = newHeading;
        }
    }

    /**
     * 	Handle keyboard input (arrows change the snake's heading)
     */
    private class KeyControl implements KeyListener {
        @Override
        public void keyTyped(KeyEvent e) {}

        @Override
        public void keyPressed(KeyEvent e) {
            Direction newHeading = heading;

            switch(e.getKeyCode()) {
                case KeyEvent.VK_LEFT: case KeyEvent.VK_KP_LEFT:
                    newHeading = Direction.LEFT; break;
                case KeyEvent.VK_RIGHT: case KeyEvent.VK_KP_RIGHT:
                    newHeading = Direction.RIGHT; break;
                case KeyEvent.VK_UP: case KeyEvent.VK_KP_UP:
                    newHeading = Direction.UP; break;
                case KeyEvent.VK_DOWN: case KeyEvent.VK_KP_DOWN:
                    newHeading = Direction.DOWN; break;
            }
            changeHeading(newHeading);
        }

        @Override
        public void keyReleased(KeyEvent e) {
        }
    }


    @Override
    // This view renders the snake and food
    // Each snake coordinate is a 10x10 pixel square
    // This method is called from repaint() from AWT
    public void paint(Graphics g) {
        g.clearRect(0, 0, 640, 480);
        Color green = new Color(0,128,0);
        g.setColor(green);

        for (Coordinate c : snake) {
            g.fillRect(c.x*10, c.y*10, 10, 10);
        }
       // for(Coordinate f : foodList) {
            g.setColor(Color.BLUE);
            g.fillOval(food.x * 10, food.y * 10, 10, 10);
       // }
        for (Coordinate p: poison) {
            g.setColor(Color.RED);
            g.fillOval(p.x * 10, p.y * 10, 10, 10);
        }
    }

    // When the snake moves, it can hit the wall, hit the food, poison (not implemented) or itself (not implemented)
    public void move() {
        Coordinate newHead = newHead();


        if(snake.size()>=20) {
            status = Game.WON;
            return;
        }
        if (hitTheWall(newHead)) {
            status = Game.OVER;
            return; // will return back to where this method is called
        }
        if (hitThePoison(newHead,poison.getFirst())){
            status=Game.OVER;
            return;
        }
        if (hitThePoison2(newHead,poison.getLast())){
            status=Game.OVER;
            return;
        }

        if (snakeCollision(newHead,snake.getLast())){
            status=Game.OVER;
            return;
        }


        snake.addFirst(newHead);	// java.util.LinkedList.addFirst()

        if (hitTheFood(newHead)){
            food = new Coordinate();
            newPoison = new Coordinate();
            poison.removeLast();
            poison.addFirst(newPoison);
            if(timer.getDelay()>50)
                timer.setDelay(timer.getDelay()-10);
        }
        else {
            snake.removeLast();
        }
    }

    // The snake's heading determines its new head coordinate
    private Coordinate newHead() {
        Coordinate head, newHead;
        head = snake.getFirst();	// java.util.LinkedList.getFirst()

        switch (heading) {
            case DOWN: newHead = new Coordinate(head.x, head.y + 1); break;
            case LEFT: newHead = new Coordinate(head.x - 1, head.y); break;
            case RIGHT: newHead = new Coordinate(head.x + 1, head.y); break;
            case UP: newHead = new Coordinate(head.x, head.y - 1); break;
            // The default case is never reached because we have only 4 events.
            default: newHead = new Coordinate(); break;
        }
        return newHead;
    }
    private boolean snakeCollision(Coordinate newHead,Coordinate p){
      return (newHead.x== p.x && newHead.y== p.y);
    }
    private boolean hitTheFood(Coordinate newHead) {
        return newHead.x == food.x && newHead.y == food.y;
    }
    public boolean hitThePoison(Coordinate deadHead , Coordinate p){
        return(deadHead.x == p.x && deadHead.y == p.y );

    }
    public boolean hitThePoison2(Coordinate deadhead,Coordinate p2){
        return(deadhead.x==p2.x && deadhead.y==p2.y);
    }

    public boolean hitTheWall(Coordinate head) {
        return (head.x == 64 || head.y == 48 || head.x == 0 || head.y == 0);
    }

    /**
     * The timer moves the snake using this class.
     */
    private class SnakeMover implements ActionListener {
        @Override
        // Listening Action (in this case Timer - every certain millisecond) and execute this method
        public void actionPerformed(ActionEvent e) {
            move();
            repaint();	// from AWT library. It will call paint() automatically
            if(status==Game.WON)
                playAgain("You've won");
            if (status == Game.OVER) {
                playAgain("The snake's dead");
            }
        }
    }

    // Ask the player what to do when the game is over
    private void playAgain(String message) {
        String[] options = new String[] {"Play again","Quit"};
        int choice = JOptionPane.showOptionDialog(null, message, "Game over", JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE,null,options,options[0]);

        if (choice == 0) {
            initialize();
        } else {
            System.exit(0);
        }
    }

    // Initialize game (snake, food, etc)
    private void initialize() {
        status = Game.ON;

        // Make a small snake with 1 node (a 10x10 pixel coordinate)
        foodList.clear();
        poison.clear();
        snake.clear(); // remove all of the elements of the LinkedList
        snake.add(new Coordinate()); // append the new element to the end of the LinkedList

        Coordinate food = new Coordinate();
        foodList.addFirst(food);

        food= new Coordinate();
        foodList.addFirst(food);

        food= new Coordinate();
        foodList.addFirst(food);

        food= new Coordinate();
        foodList.addFirst(food);

        food= new Coordinate();
        foodList.addFirst(food);

        Coordinate newPoison= new Coordinate();
        poison.addFirst(newPoison);

        newPoison= new Coordinate();
        poison.addFirst(newPoison);

    }
    public SnakeGame() {

        setSize(640, 480);	// Window size - pixel
        setTitle("Snake Game");
        setVisible(true);

        // Update the snake's direction using keyboard arrows
        // Event Handler: addKeyListener is from AWT library. This is how to "register" event
        addKeyListener(new KeyControl());

        // Make the snake move every 150 milliseconds
        timer = new Timer(150, new SnakeMover());
        timer.start();

        // Initialize game (snake, food)
        initialize();

    }

    public static void main(String[] args) {
        new SnakeGame();
    }
}
