-- 코드를 입력하세요
SELECT book.book_id, author.author_name, date_format(book.published_date, '%Y-%m-%d') as published_date
from book, author
where (book.author_id = author.author_id) and (book.category like '%경제%')
order by published_date;