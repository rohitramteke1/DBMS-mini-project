// Importing module
var mysql = require("mysql");

// Connecting to database
var connection = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "password",
    database: "db",
});

function connectTodb() {
    connection.connect((err) => {
        if (err) {
            console.log("Error in the connection");
            console.log(err);
        } else {
            console.log(`Database Connected...`);
        }
    })
};

// connectTodb();
module.exports = connectTodb;