<?php
	$servername = "localhost";
	#$servername = "45.76.124.20";
	$username = "root";
	$password = "pebble29er";
	$dbname = "specials";
	$conn = new mysqli($servername, $username, $password, $dbname);
        mysqli_set_charset($conn, "utf8");
	if ($conn->connect_error) {
        	die("Connection failed: " . $conn->connect_error);
        }
        $rows = array();
        $data = array();

        if (isset($_GET['search'])) {
            $WHERE = ' WHERE name LIKE "%'.$_GET['search'].'%" ';
        } else {
            $WHERE = NULL;
        }
        if (isset($_GET['limit'])) {
            $tableNameQuery = "SELECT name, brand FROM `21/12/19` ".$WHERE." ORDER BY name LIMIT ".$_GET['offset'].",".$_GET['limit'];
        }else {
            $tableNameQuery = "SELECT name, brand FROM `21/12/19` ".$WHERE." ORDER BY name LIMIT 1, 5";
        }


        $tableNames = $conn->query($tableNameQuery);
        while($row = mysqli_fetch_assoc($tableNames)){
            $rows[]=$row;
        }
        $countQuery = "SELECT COUNT(*) as total FROM `21/12/19`";
        $totalRowForm = $conn->query($countQuery);
        $total = ($totalRowForm->fetch_assoc())['total'];
        #echo $data;
        $data['total'] = $total;
        $data['rows'] = $rows;

        echo json_encode($data);



