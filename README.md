# assignment-2-1-

1. Introduction

The original StudentRecords table contained update,
insert and delete anomalies due to partial and transitive dependencies.

2. Functional Dependencies

student_id →
student_name, department, advisor_name, enrollment_year

advisor_name →
advisor_email

course_code →
course_name, instructor_name

instructor_name →
instructor_email

3. BCNF Decomposition

Students
Courses
Advisors
Instructors
Enrollments

4. Design Decisions

INT for IDs
VARCHAR for text
DECIMAL(5,2) for marks
CHECK constraint for marks
DEFAULT enrollment_year = 2025
Foreign keys enforce referential integrity.

5. Transaction Analysis

The enrollment transfer is wrapped in a transaction using BEGIN, COMMIT, and ROLLBACK to ensure atomicity. Non-repeatable reads are prevented by REPEATABLE READ, overbooking-style write skew is prevented by SERIALIZABLE, and MVCC allows reporting transactions to read a consistent snapshot even while concurrent updates commit.
