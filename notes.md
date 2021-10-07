If you originally created your database without nullable=False (or created it in some other way, separate from SQLAlchemy, without NOT NULL on that column), then your database column doesn't have that constraint information. This information lives in reference to the database column, not to a particular instance you are creating/inserting.


Changing the SQLAlchemy table creation, without rebuilding your tables, means changes will not be reflected. As a link in a comment explains, SQLAlchemy is not doing the validation at that level (you would need to use the @validates decorator or some other such thing).

If your database schema has a column which cannot be NULL, you must put something (i.e. not None) into there. Or change your schema to allow NULL in those columns.

All string columns are not nullable by default.

questions: if column input is nullable in the db, does it matter how info is passed into crud? do i have to include the info for the function?