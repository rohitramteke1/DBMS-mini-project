// Import the module
const ConnectToDatabase = require('./DBModule');

// Creating an object of class ConnectToDatabase()
connector = new ConnectToDatabase();

// Connect to database
connector.connectToDatabase();

// connector.addQueryToDatabase("SHOW DATABASES");
// connector.addQueryToDatabase("USE db");
// connector.addQueryToDatabase("SHOW TABLES");
// connector.addQueryToDatabase("SELECT * FROM student");


// connector.addQueryToDatabase("desc student")
connector.addQueryToDatabase("select * from student where E_mail = '2041054@gcoej.ac.in'")