<?php
        $servername = "localhost";
        #$servername = "45.76.124.20";
        $username = "root";
        $password = "pebble29er";
        $dbname = "specials3";
        $conn = new mysqli($servername, $username, $password, $dbname);
        mysqli_set_charset($conn, "utf8");
        if ($conn->connect_error){
                die("Connection failed: " . $conn->connect_error);
        }
	$tableNameQuery = "SELECT STR_TO_DATE(table_name, '%d/%m/%y') as test, table_name FROM information_schema.tables WHERE table_schema = 'specials3' ORDER by test asc";
        $dataPoints = array();
        $tableNames = $conn->query($tableNameQuery);
        $firstItem = true;

        //This adds a date colum to all colums in the database
        //while($row = $tableNames->fetch_assoc()) { 
        //    $handle = 'ALTER TABLE `'.$row["table_name"].'` ADD `date` DATE NULL DEFAULT NULL AFTER `code`'; 
        //    $graphPoints = $conn->query($handle);
        //};

        //This sets the date colum to the name of the table
        //while($row = $tableNames->fetch_assoc()) { 
        //    $s = $row["table_name"];
        //    $dateTime = datetime::createfromformat('d/m/y',$s);
        //    $correctDate = $dateTime->format('Y-m-d');
        //    $next = "UPDATE `".$row["table_name"]."` SET date = '".$correctDate."'";
        //    $graphPoints = $conn->query($next);
        //};

//This adds the contents of all tables from the 31/01/20 to the allData table around 3 million records !
//        $count = 0;
//        while($row = $tableNames->fetch_assoc()) { 
//            $s = $row["table_name"];
//            $count = $count + 1;
//            if ($s != "allData" && $count > 13 ) {
//                echo $s."\n";
//                $query = "INSERT INTO allData (name, brand, origPrice, salePrice, volSize, saleType, minAmount, type, barcode, code, date) SELECT name, brand, origPrice, salePrice, volSize, saleType, minAmount, type, barcode, code, date FROM `".$s."`";
//                $graphPoints = $conn->query($query);
//            }

//This adds the contents of all tables from the 31/01/20 to the distinct products, only select values go through
//        $count = 0;
//        while($row = $tableNames->fetch_assoc()) { 
//            $s = $row["table_name"];
//            $count = $count + 1;
//            if ($s != "allData" && $count > 13 ) {
//                echo $s."\n";
//                $query = "INSERT IGNORE INTO distinctProducts (name, brand, volSize, type, barcode, code) SELECT name, brand, volSize, type, barcode, code FROM `".$s."`";
//                $graphPoints = $conn->query($query);
//            }
//        };

//This adds the contents of all tables from the 31/01/20 to the distinct products, only price values and such like go in
//        $count = 0;
//        while($row = $tableNames->fetch_assoc()) { 
//            $s = $row["table_name"];
//            $count = $count + 1;
//            if ($s != "allData" && $count > 13 ) {
//                echo $s."\n";
//                $query = "INSERT IGNORE INTO priceOnDate (origPrice, salePrice, saleType, minAmount, barcode, date) SELECT origPrice, salePrice, saleType, minAmount, barcode, date FROM `".$s."`";
//                $graphPoints = $conn->query($query);
//            }
//        };

        echo("hi");

#                    
#
?>
