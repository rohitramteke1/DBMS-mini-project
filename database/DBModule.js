var mysql = require("mysql");

// Creating the database
class ConnectToDB {
    constructor() {
        // Connecting to database
        this.connection = mysql.createConnection({
            host: "localhost",
            user: "root",
            password: "password",
            database: "db",
        });
    }

    // Connect to database function
    connectToDatabase() {
        this.connection.connect((err) => {
            if (err) {
                console.log("Error in the connection");
                console.log(err);
            } else {
                console.log(`Database Connected...`);
            }
        })
    }

    // Adding items to database
    addQueryToDatabase(sql_query) {
        console.log("QUERY: ", sql_query);

        this.connection.query(sql_query,(err, result) => {
            if (err) throw err;
            else console.log(result);
        })
    }
}

module.exports = ConnectToDB;