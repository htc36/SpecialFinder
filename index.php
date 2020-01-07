<html>
<head>
    <title>Tablesorter Demo - Jeff Reifman</title>
    <script src="vendor/jquery/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="foo/js/footable.min.js"></script>

    <link rel="stylesheet" type="text/css" href="foo/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="foo/css/footable.standalone.min.css" type="text/css" media="print, projection, screen" />
    <link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
	<link rel="stylesheet" type="text/css" href="css/util.css">
	<link rel="stylesheet" type="text/css" href="css/main.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.13.1/css/bootstrap-select.css" />
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.bundle.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.13.1/js/bootstrap-select.min.js"></script>




  </head>
    <body>
    <?php include 'functions2.php'; ?>	
     <div class="topnav"> 
      <a class="active" href="#home">Specials</a>
            <div class="combo">
            <select id = "hi" class="selectpicker" data-live-search="false" > <option> None </option>
            <?php
                while($row2 = $type->fetch_assoc()) {
            ?>
                    <option><?php echo $row2["type"]; ?> </option> 
            <?php
                };
            ?>
        </select>
            <select id="types"  class="selectpicker" data-live-search="false" > 
            <?php
                while($row3 = $tableNames->fetch_assoc()) {
                    if ( substr($tableName, 1, 8) == $row3["table_name"] ) { ?>
                        <option selected><?php echo $row3["table_name"]; ?> </option> 
                    <?php }else { ?>
                        <option><?php echo $row3["table_name"]; ?> </option> 
                    <?php }; ?>

            <?php
                };
            ?>
        </select>
            </div>
     <div id='search' class='hi'> </div >
    </div>
    	<div class="limiter">
		<div class="container-table100">

            <table id="domainsTable" class="footable" data-paging='true' data-sorting='true'  data-paging-size='100' data-filter-container= "#search" data-filtering='true'>
                    <thead>
                            <tr class="table100-head">
                                    <th class="column1">Name</th>
                                    <th class="column2">Brand</th>
                                    <th class="type">Type</th>
                                    <th class="digits" data-type="number">OrigPrice($)</th>
                                    <th class="digits" data-type="number">SalePrice($)</th>
                                    <th class="digits" data-type="number">Volume Size</th>
                                    <th class="digits" data-type="number">Discount($)</th>
                                    <th class="digits" data-type="number">MarkDown(%)</th>
                                    <th class="end">Website Link</th>
                                    
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
                                            <td class="digits"><?php echo (printf('%0.1f',$row["origPrice"] - $row["salePrice"])); ?></td>
                                            <td class="digits">$$<?php echo sprintf('%0.2f', (1-($row["salePrice"] / $row["origPrice"]))*100 + "%"); ?></td>
                                            <td class="end"><a href="https://shop.countdown.co.nz/shop/productdetails?stockcode=<?php echo ($row["code"]); ?>" target="_blank">click here </a></td>

                                    </tr>
                                    <?php
                                        };
                                    ?>


                                    
                    </tbody>
                    </div>
                    </div>
            </table>
    </div>
</body>

    <script>
    $(document).ready(function() 
        { 
            $("#domainsTable").footable(); 
            //inicialization of select picker

            $('.selectpicker').selectpicker('val', '<?php echo substr($tableName, 1, 8) ?>' );
        } 
    );
    </script>
    <script>
    $('select.selectpicker').on('change', function(){
	var filtering = FooTable.get('#domainsTable').use(FooTable.Filtering), // get the filtering component for the table
		filter = $(this).val(); // get the value to filter by
	if (filter === 'None'){ // if the value is "none" remove the filter
		filtering.removeFilter('name');
                alert('filter removed');
        }else if(filter[0] <='9' && filter[0] >='0') {
            var hi = "do"//
            window.location.search = '?date=' + filter;
        }else { // otherwise add/update the filter.
		filtering.addFilter('name', filter, [2], true, false);
	}
	filtering.filter();
});
    </script>
    </body>
</html>
