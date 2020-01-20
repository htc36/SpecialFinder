<?php
        include 'functions.php';
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
        $tableNameQuery = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'specials' order 
by table_name DESC";
        $tableNames = $conn->query($tableNameQuery);
        $tableRow = $tableNames->fetch_assoc();
        $latestDate = $tableRow['table_name'];


        if (isset($_GET['dateOfSpecials'])) {
            $FROM = "FROM `".$_GET['dateOfSpecials']."` ";
        } else {
            $FROM = "FROM `".$latestDate."` ";
        }

        if (isset($_GET['search'])) {
            $WHERE = ' WHERE name LIKE "%'.$_GET['search'].'%" ';
            if ($_GET['type'] != 'None') {
                $WHERE .= "and type = '".$_GET['type']."' ";
            }
        }

        if (isset($_GET['sort'])) {
            $ORDERBY = "ORDER BY ".$_GET['sort']." ".$_GET['order'];
        } else {
            $ORDERBY = NULL;
        }
        $tableNameQuery = "SELECT name, brand, origPrice, salePrice, volSize, origPrice - salePrice AS discount, ROUND(((1 -(salePrice / origPrice))*100),2) as markDown, type, code ".$FROM . $WHERE." ".$ORDERBY." LIMIT ".$_GET['offset'].",".$_GET['limit'];



        $tableNames = $conn->query($tableNameQuery);
        while($row = mysqli_fetch_assoc($tableNames)){
            $rows[]=$row;
        }
        $countQuery = "SELECT COUNT(*) as total ".$FROM;
        $totalRowForm = $conn->query($countQuery);
        $total = ($totalRowForm->fetch_assoc())['total'];
        #echo $data;
        $data['total'] = $total;
        $data['rows'] = $rows;
       # echo $tableNameQuery;

        echo json_encode($data);



