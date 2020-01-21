<?php
    $servername = "localhost";
            #$servername = "45.76.124.20";
            $username = "root";
            $password = "pebble29er";
            $dbname = "specials";

            $conn = new mysqli($servername, $username, $password, $dbname);
            if ($conn->connect_error) {
                    die("Connection failed: " . $conn->connect_error);
            }

            $tableNameQuery = "SELECT STR_TO_DATE(table_name, '%d/%m/%Y') as test, table_name FROM information_schema.tables WHERE table_schema = 'specials' order by test DESC";  
            $tableNames = $conn->query($tableNameQuery);

            $typeQuery = "select distinct type FROM `20/01/20`";
            $type = $conn->query($typeQuery);
            global $tableNames, $type;
