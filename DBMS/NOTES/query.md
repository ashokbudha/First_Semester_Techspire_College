# DDL Commands


## Create

1. Create database

```sql
     create database univerity;
```

2. Create table

```sql 
    create table student;
```




##  Alter

1. Add a new column

You can add new column.
```sql
    Alter table student
    add address varchar(50);
```
2. Modify a existing column

You can modify the datatype of the column.

```sql
    Alter table student
    modify address varchar(100);
``` 

3. Rename a column

```sql 
    Alter table student
    rename column address to full-address;
```

4. Drop a column

It is used to delete a column.
```sql
    Alter table student
    drop column full-address;
```

5. Rename a table

```sql 
    Alter table student
    Rename to university-student;
```


## Drop 

It removes data and table structure
```sql
    drop table student;
```


## Truncate

Removes all rows from a table but keeps the structure of the table intact for future use
```sql
    truncate table student;
```


## Rename
```sql 
    rename table studnet to university-student;
```

# DML

## Insert

The INSERT statement is used to add new rows of data into a table.

Syntax
```sql
    INSERT INTO table_name (column1, column2, ...) 
    VALUES (value1, value2, ...);
```

Example:
```sql
    INSERT INTO employees (id, name, age, department)
    VALUES 
    (2, 'Jane Smith', 25, 'Finance'),
    (3, 'Samuel Lee', 35, 'IT');
```

## Update

The UPDATE statement modifies existing data within a table. You should always include a WHERE clause to specify which rows to update, otherwise, all rows will be updated.

Syntax:
```sql 
    UPDATE table_name   
    SET column1 = value1, column2 = value2, ...
    WHERE condition;
```


Example:
```sql
    UPDATE employees 
    SET age = 31 
    WHERE id = 1;
```

## Delete

The DELETE statement removes rows from a table. Like UPDATE, you should use a WHERE clause to specify the rows to delete.

Syntax
```sql
    DELETE FROM table_name
    WHERE condition;
```

Example:
```sql
    DELETE FROM employees 
    WHERE id = 2;
```

Delete All Rows:  If you omit the WHERE clause, all rows will be deleted.

```sql 
    DELETE FROM employees;
```


## Select

Syntax

```sql 
    SELECT column1, column2, ... FROM table_name WHERE condition;
```

Example

```sql
    SELECT * FROM employees;
```

```sql
    SELECT name, age FROM employees WHERE department = 'HR';
```











































































