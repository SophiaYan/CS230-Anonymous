package tests;

import static org.junit.Assert.*;

import java.awt.Color;

import model.Board;

import org.junit.*;


public class BoardTest {

	static Board board;
	
	@Before
	public void setUp() {
		board = new Board();
	}
	
	@Test
	public void emptyConstructor() {
		board = new Board(null);
		assertNull("Board should be null.", board.getPiece(0,0));
	}
	@Test
	public void notInCheck() {
		board.setPiece("King", 0, 0, Color.WHITE);
		board.setPiece("King", 7, 7, Color.BLACK);
		assertFalse("White is not in check.",board.inCheck(Color.WHITE));
		assertFalse("Black is not in check.",board.inCheck(Color.BLACK));
	}
	
	@Test
	public void notInFriendlyCheck() {
		board.setPiece("King", 0, 0, Color.WHITE);
		board.setPiece("Rook", 0, 1, Color.WHITE);
		assertFalse("Not in check with friendly piece.",board.inCheck(Color.WHITE));
	}
	
	@Test
	public void opponentInCheck() {
		board.setPiece("King", 0, 0, Color.WHITE);
		board.setPiece("Rook", 0, 1, Color.BLACK);
		assertTrue("White is in check.",board.inCheck(Color.WHITE));
	}
	
	@Test
	public void moveIntoCheck() {
		board.setPiece("King", 0, 0, Color.WHITE);
		board.setPiece("Rook", 1, 1, Color.BLACK);
		assertFalse("Can't move into check.",board.movePiece(0, 0, 1, 0));
	}
	
	@Test
	public void otherPieceInCheck() {
		board.setPiece("King", 0, 0, Color.WHITE);
		board.setPiece("Rook", 0, 1, Color.BLACK);
		board.setPiece("Rook", 8, 8, Color.WHITE);
		assertTrue("White in check.",board.inCheck(Color.WHITE));
		assertFalse("Need to move king out of check.",board.movePiece(8, 8, 8, 7));
	}
	
	@Test
	public void captureOutofCheck() {
		board.setPiece("King", 0, 0, Color.WHITE);
		board.setPiece("Rook", 0, 1, Color.BLACK);
		board.setPiece("Rook", 1, 1, Color.WHITE);
		assertTrue("White is in check.",board.inCheck(Color.WHITE));
		assertTrue("Captured out of check.",board.movePiece(1,1,0,1));
		assertFalse("White is no longer in check.",board.inCheck(Color.WHITE));
	}
	
	@Test
	public void captureIntoCheck() {
		board.setPiece("King", 0, 0, Color.WHITE);
		board.setPiece("Rook", 1, 0, Color.BLACK);
		board.setPiece("Rook", 1, 1, Color.BLACK);
		assertFalse("Can't capture into check.",board.movePiece(0, 0, 1, 0));	
	}
	
	@Test
	public void emptyBoardCheck() {
		assertFalse("White is not in check.",board.inCheck(Color.WHITE));
		assertFalse("Black is not in check.",board.inCheck(Color.BLACK));
	}
	
	@Test
	public void notInFriendlyCheckmate() {
		board.setPiece("King", 0, 0, Color.WHITE);
		board.setPiece("Rook", 0, 2, Color.WHITE);
		board.setPiece("Rook", 1, 2, Color.WHITE);
		assertFalse("Not in checkmate with friendly pieces.",board.inCheckmate(Color.WHITE));
	}

	@Test
	public void opponentInCheckmate() {
		board.setPiece("King", 0, 0, Color.WHITE);
		board.setPiece("Rook", 0, 2, Color.BLACK);
		board.setPiece("Rook", 1, 2, Color.BLACK);
		assertTrue("White is in check.",board.inCheck(Color.WHITE));
		assertTrue("White in checkmate.",board.inCheckmate(Color.WHITE));
	}
	
	@Test
	public void notInCheckOrCheckMate() {
		board.setPiece("King", 0, 0, Color.WHITE);
		board.setPiece("King", 7, 7, Color.BLACK);
		assertFalse("White is not in checkmate.",board.inCheckmate(Color.WHITE));
		assertFalse("Black is not in checkmate.",board.inCheckmate(Color.BLACK));
	}
	
	@Test
	public void notInCheckMate() {
		board.setPiece("King", 0, 0, Color.WHITE);
		board.setPiece("Rook", 5, 0, Color.BLACK);
		assertTrue("White is in check.",board.inCheck(Color.WHITE));
		assertFalse("White is not in checkmate.",board.inCheckmate(Color.WHITE));
	}
	
	@Test
	public void empytBoardCheckMate() {
		assertFalse("White is not in checkmate.",board.inCheckmate(Color.WHITE));
		assertFalse("Black is not in checkmate.",board.inCheckmate(Color.BLACK));
	}
	
	@Test
	public void inStalemate() {
		board.setPiece("King", 0, 0, Color.WHITE);
		board.setPiece("King", 1, 2, Color.BLACK);
		board.setPiece("Queen", 2, 1, Color.BLACK);
		assertTrue("White is in a stalemate.",board.inStalemate(Color.WHITE));
	}
	
	@Test
	public void emptyBoardStalemate() {
		assertFalse("No one is in stalemate.",board.inStalemate(Color.WHITE));
		assertFalse("No one is in stalemate.",board.inStalemate(Color.BLACK));
	}
	
	@Test
	public void noStalemateInCheck() {
		board.setPiece("King", 0, 0, Color.WHITE);
		board.setPiece("Rook", 0, 1, Color.BLACK);
		assertFalse("White is not in stalemate.",board.inStalemate(Color.WHITE));
	}
	
	@Test
	public void noCheckNoStalemate() {
		board.setPiece("King", 0, 0, Color.WHITE);
		assertFalse("Not in check.",board.inCheck(Color.WHITE));
		assertFalse("Not in stalemate, in check.",board.inStalemate(Color.WHITE));
	}
}
