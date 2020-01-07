<!DOCTYPE html>
<html lang="en">
<head>
	<title>Table V01</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
<!--===============================================================================================-->	
	<link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/perfect-scrollbar/perfect-scrollbar.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="css/util.css">
	<link rel="stylesheet" type="text/css" href="css/main.css">
<!--===============================================================================================-->
</head>
<body>
	<?php include 'functions.php'; ?>	
	<div class="limiter">
		<div class="container-table100">
			<div class="wrap-table100">
				<div class="table100">
					<table>
						<thead>
							<tr class="table100-head">
								<th class="column1">Name</th>
								<th class="column2">Brand</th>
								<th class="type">Type</th>
								<th class="digits">OrigPrice</th>
								<th class="digits">SalePrice</th>
								<th class="digits">Volume Size</th>
								<th class="digits">Discount</th>
								<th class="end">MarkDown</th>
							</tr>
						</thead>
						<tbody>
							    	<?php
								    while($row = $rs_result->fetch_assoc()) {
								?>
								<tr>
									<td class="column1"><?php echo $row["name"]; ?> </td>
									<td class="column2"><?php echo $row["brand"]; ?></td>
									<td class="type"><?php echo $row["type"]; ?></td>
									<td class="digits"><?php echo $row["origPrice"]; ?></td>
									<td class="digits"><?php echo $row["salePrice"]; ?></td>
									<td class="digits"><?php echo $row["volSize"]; ?></td>
                                                                        <td class="digits">$<?php echo $row["origPrice"] - $row["salePrice"]; ?></td>
                                                                        <td class="end"><?php echo sprintf('%0.2f', (1-($row["salePrice"] / $row["origPrice"]))*100 + "%"); ?>%</td>

								</tr>
								<?php
								    };
								?>

								
						</tbody>
					</table>
				</div>
			</div>
		</div>
	</div>


	

<!--===============================================================================================-->	
	<script src="vendor/jquery/jquery-3.2.1.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/bootstrap/js/popper.js"></script>
	<script src="vendor/bootstrap/js/bootstrap.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/select2/select2.min.js"></script>
<!--===============================================================================================-->
	<script src="js/main.js"></script>

</body>
</html>
