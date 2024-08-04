/**
 *
 * @param <E>
 */

public class SinglyLinkedList <E> {
	
	private Node<E> head = null;	// head node of the list
	private Node<E> tail = null;	// last node of the list
	private int size = 0;
	
	/**
	 * returns the number of elements in the list
	 * @return
	 */
	public int size() {
		
	}
	/**
	 * returns true if the list is empty, and false otherwise
	 * @return
	 */
	public boolean isEmpty() {
		
	}
	/**
	 * returns (but does not remove) the first element in the list
	 * @return
	 */
	public E first(){
		
        
        
        
	}
	/**
	 * returns (but does not remove) the last element in the list
	 * @return
	 */
	public E last(){
	
        
        
        
	}
	/**
	 * adds a new element to the front of the list
	 * @param e
	 */
	public void addFirst (E e){

        
        
        
        
        
        
        
	}
	/**
	 * adds a new element to the end of the list
	 * @param e
	 */
	public void addLast(E e) {

        
        
        
        
        
        
        
        
        
	}
	/**
	 * removes and returns the first element of the list
	 * @return
	 */
	public E removeFirst()
	{

        
        
        
        
        
        
        
        
        
        
	}
	
	/**
	 * Inner class (or nested class) for encapsulation.
	 * Shielding users of our class from the underlying details about nodes and links
	 * @param <E>
	 */
	private static class Node<E> 
	{
		private E element;
		private Node<E> next = null;

		public Node (E e) {
			element = e;
		}

	}
}
