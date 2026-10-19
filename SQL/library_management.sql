CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(30)
);

CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(50)
);

CREATE TABLE borrow_records (
    borrow_id INT PRIMARY KEY,
    student_id INT REFERENCES students(student_id),
    book_id INT REFERENCES books(book_id),
    borrow_date DATE
);

INSERT INTO students VALUES (1, 'Aman', 'CSE'), (2, 'Rahul', 'IT'),(3, 'Priya', 'CSE');

INSERT INTO books VALUES(101, 'Python Basilcs', 'John'),(102, 'SQL Guide', 'David'),(103, 'Java Programming', 'James');

INSERT INTO borrow_records VALUES(1, 1, 101, '2026-10-10'),(2, 2, 102, '2026-10-12'),(3, 1, 103, '2026-10-15');

-- SELECT
SELECT * FROM students;

-- WHERE
SELECT * FROM students
WHERE department = 'CSE';

-- ORDER BY
SELECT * FROM books
ORDER BY title ASC;

-- LIMIT
SELECT * FROM books
LIMIT 2;

-- INSERT
INSERT INTO students
VALUES (4, 'Rohan', 'IT');

-- UPDATE
UPDATE students
SET department = 'AIML'
WHERE student_id = 4;

-- DELETE
DELETE FROM students
WHERE student_id = 4;

-- INNER JOIN
SELECT students.name, borrow_records.book_id
FROM students
INNER JOIN borrow_records
ON students.student_id = borrow_records.student_id;

-- LEFT JOIN
SELECT students.name, borrow_records.book_id
FROM students
LEFT JOIN borrow_records
ON students.student_id = borrow_records.student_id;

-- GROUP BY + HAVING + COUNT
SELECT student_id, COUNT(*) AS total_books
FROM borrow_records
GROUP BY student_id
HAVING COUNT(*) > 1;