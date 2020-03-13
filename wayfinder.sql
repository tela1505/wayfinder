BEGIN TRANSACTION;
DROP TABLE IF EXISTS "posts";
CREATE TABLE IF NOT EXISTS "posts" (
	"postId"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"content"	TEXT NOT NULL,
	"title"	TEXT NOT NULL,
	"date"	TEXT NOT NULL,
	"tags"	TEXT NOT NULL,
	"likes"	INTEGER,
	"posterId"	INTEGER NOT NULL,
	FOREIGN KEY("posterId") REFERENCES "users"("userId")
);
DROP TABLE IF EXISTS "users";
CREATE TABLE IF NOT EXISTS "users" (
	"username"	TEXT NOT NULL,
	"password"	TEXT NOT NULL,
	"userId"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"name"	TEXT NOT NULL,
	"age"	INTEGER NOT NULL,
	"university"	TEXT NOT NULL,
	"email"	TEXT NOT NULL
);
DROP TABLE IF EXISTS "grade_measurements";
CREATE TABLE IF NOT EXISTS "grade_measurements" (
	"userId"	INTEGER NOT NULL,
	"gradeEntryId"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"gradeSubject"	TEXT NOT NULL,
	"grade"	INTEGER NOT NULL,
	"date"	TEXT NOT NULL,
	FOREIGN KEY("userId") REFERENCES "users"("userId")
);
DROP TABLE IF EXISTS "sleep_measurements";
CREATE TABLE IF NOT EXISTS "sleep_measurements" (
	"userId"	INTEGER NOT NULL,
	"sleepEntryId"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"sleep"	INTEGER NOT NULL,
	"date"	TEXT NOT NULL,
	FOREIGN KEY("userId") REFERENCES "users"("userId")
);
DROP TABLE IF EXISTS "weight_measurements";
CREATE TABLE IF NOT EXISTS "weight_measurements" (
	"userId"	INTEGER NOT NULL,
	"weightEntryId"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"weight"	INTEGER NOT NULL,
	"date"	TEXT NOT NULL,
	FOREIGN KEY("userId") REFERENCES "users"("userId")
);
DROP TABLE IF EXISTS "comments";
CREATE TABLE IF NOT EXISTS "comments" (
	"commentId"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"commenterId"	INTEGER NOT NULL,
	"commentedPostId"	INTEGER NOT NULL,
	"content"	TEXT NOT NULL,
	"date"	TEXT NOT NULL,
	FOREIGN KEY("commenterId") REFERENCES "users"("userId"),
	FOREIGN KEY("commentedPostId") REFERENCES "posts"("postId")
);
COMMIT;
