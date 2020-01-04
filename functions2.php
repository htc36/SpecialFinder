<?php
	$servername = "localhost";
	$servername = "45.76.124.20";
	$username = "root";
	$username = "root";
	$password = "Cc5c8cac59";
	$dbname = "specials";

	$conn = new mysqli($servername, $username, $password, $dbname);
	if ($conn->connect_error) {
        	die("Connection failed: " . $conn->connect_error);
        }

        $tableNameQuery = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'specials' order by table_name DESC";  
        $tableNames = $conn->query($tableNameQuery);
        $tableNames2 = $conn->query($tableNameQuery);
        $tableRow = $tableNames2->fetch_assoc();
        $tableName = "`".$tableRow['table_name']."`";

        if (isset($_GET["date"])) { $tableName  = "`".$_GET["date"]."`"; } ;

        $sql = "SELECT * FROM ".$tableName;
        $rs_result = $conn->query($sql);
        $typeQuery = "select distinct type FROM ".$tableName;
        $type = $conn->query($typeQuery);
        
        
        



	global $conn, $rs_result, $type, $tableNames, $tableName;




?>

