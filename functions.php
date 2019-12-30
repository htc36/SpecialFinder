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

	$datatable = "products2";
        $results_per_page = 100; // number of results per page
        if (isset($_GET["page"])) { $page  = $_GET["page"]; } else { $page=1; };
        if (isset($_GET["filter"])) { $filter  = $_GET["filter"]; } else { $filter="1"; };
        if (isset($_GET["order"])) { $order  = $_GET["order"]; } else { $order="asc"; };
        if (isset($_GET["search"])) { $search  = $_GET["search"]; } else { $search=""; };
        $start_from = ($page-1) * $results_per_page;
        if ($search == "") {
                $searchQuery = "";
        } else {
                $searchQuery = " where name LIKE('%".$search."%')";
        }

        switch ($filter) {
                case "1":
                        $sql = "SELECT * FROM ".$datatable.$searchQuery." ORDER BY id ".$order." LIMIT $start_from, ".$results_per_page;
                        $comboBoxText = "";
                        break;
                case "price":
                        $sql = "SELECT * FROM ".$datatable.$searchQuery." ORDER BY salePrice ".$order." LIMIT $start_from, ".$results_per_page;
                        $comboBoxText = "Price";
                        break;
                case "moneyOff":
                        $sql = "SELECT * FROM ".$datatable.$searchQuery." ORDER BY origPrice - salePrice ".$order." LIMIT $start_from, ".$results_per_page;
                        $comboBoxText = "Money Off";
                        break;
                case "markdown":
                        $sql = "SELECT * FROM ".$datatable.$searchQuery." ORDER BY 1 - (origPrice / salePrice) ".$order." LIMIT $start_from, ".$results_per_page;
                        $comboBoxText = "Markdown";
                        break;
        }

        $rs_result = $conn->query($sql);
        #select * FROM itemsTest where itemsTest.name LIKE('%butter chicken%')
	global $conn, $rs_result;




?>

