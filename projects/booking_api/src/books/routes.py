from fastapi import APIRouter, status, HTTPException
from typing import List
from src.books.schemas import Book, BookUpdate
from src.books.data import books

book_router = APIRouter()

@book_router.get("/", response_model=List[Book])
async def get_books():
    return books

@book_router.get("/{book_id}")
async def get_book(book_id: int) -> Book:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_book(book: Book) -> Book:
    new_book = book.model_dump()
    books.append(new_book)
    return new_book

@book_router.patch("/{book_id}")
async def update_book(book_id: int, updated_book: BookUpdate) -> Book:
    for book in books:
        if book["id"] == book_id:
            if updated_book.title is not None:
                book["title"] = updated_book.title
            if updated_book.author is not None:
                book["author"] = updated_book.author
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {"detail": "Book deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")