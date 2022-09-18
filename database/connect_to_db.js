// Import the module
const ConnectToDatabase = require('./DBModule');

// Creating an object of class ConnectToDatabase()
connector = new ConnectToDatabase();

// Connect to database
connector.connectToDatabase();

connector.addQueryToDatabase("SHOW DATABASES");
connector.addQueryToDatabase("USE db");
connector.addQueryToDatabase("SHOW TABLES");
connector.addQueryToDatabase("SELECT * FROM student");
