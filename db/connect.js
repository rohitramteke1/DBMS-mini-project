// Importing module
var mysql = require("mysql");

var connection = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "password",
  database: "db",
});

// Connecting to database
connection.connect(function (err) {
  if (err) {
    console.log("Error in the connection");
    console.log(err);
  } else {
    console.log(`Database Connected...`);

    const sql_query = `SHOW DATABASES`;

    connection.query(sql_query, (err, result) => {
      if (err) {
        console.log(`Error executing the query - ${err}`);
      } else {
		  console.log("Result: ", result);
		} 
			connection.query(`USE db`, (err, result) => {
				console.log("Using database db...");
				if (err) {
					console.log(`Error executing the query - ${err}`);
				}
					// console.log("Result db: ", result);

					connection.query(`SELECT * FROM Persons`, (err, result) => {
					console.log("Using Table Persons");
					if (err) {
						console.log(`Error executing the query - ${err}`);
					}
					console.log("Result db: ", result);

					connection.query(
					`INSERT INTO 
					Persons
						(
							PersonID, 
							LastName, 
							FirstName, 
							Address, 
							City
						)
					VALUES
						(
							2041016, 
							'Panel',
							'Admin',
							'Manhattan',
							'New York'
						)`, (err, result) => {
							console.log("Iserting the data into Persons...");
							if (err) {
								console.log(`Error executing the query - ${err}`);
							}
							console.log("Result db: ", result);
						})
			});
			
      });
    });
  }
});
