<?php
        $servername = "localhost";
        #$servername = "45.76.124.20";
        $username = "root";
        $password = "pebble29er";
        $dbname = "specials";
        $conn = new mysqli($servername, $username, $password, $dbname);
        mysqli_set_charset($conn, "utf8");
        if ($conn->connect_error){
                die("Connection failed: " . $conn->connect_error);
        }
	$tableNameQuery = "SELECT STR_TO_DATE(table_name, '%d/%m/%y') as test, table_name FROM information_schema.tables WHERE table_schema = 'specials' ORDER by test asc";
        $dataPoints = array();
        $tableNames = $conn->query($tableNameQuery);
        $firstItem = true;
        while($row = $tableNames->fetch_assoc()) { 
            $handle = 'select salePrice, name from `'.$row["table_name"]."` where code = ".$_GET['prodNum']; 
            $graphPoints = $conn->query($handle);
            $row2 = $graphPoints->fetch_assoc();
            array_push($dataPoints, array("label"=> $row["table_name"], "y"=> floatval($row2['salePrice'])));
            $name = ucwords($row2['name']);
        };

#                    
#
?>
<!DOCTYPE HTML>
<html>
<head>  
<script>
window.onload = function () {
 
var chart = new CanvasJS.Chart("chartContainer", {
	animationEnabled: true,
	exportEnabled: true,
	theme: "light1", // "light1", "light2", "dark1", "dark2"
	title:{
		text: "<?php echo $name ?> "
	},
	data: [{
		type: "line", //change type to bar, line, area, pie, etc  
		dataPoints: <?php echo json_encode($dataPoints, JSON_NUMERIC_CHECK); ?>
	}]
});
chart.render();
 
}
</script>
</head>
<body>
<div id="chartContainer" style="height: 370px; width: 100%;"></div>
<script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
</body>
</html>                              
