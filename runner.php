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
    <select class="selectpicker" multiple data-live-search="false" width='100%'>
      <option>Mustard</option>
      <option>Ketchup</option>
      <option>Relish</option>
    </select>
     <div class="topnav"> 
      <a class="active" href="#home">Specials</a>
     <div id='search' class='hi'> </div >
    <div class="well">
	<form class="form-inline">
		<label class="radio-inline">
			<input type="radio" name="status" id="status_none" value="none" checked>
			None
		</label>
		<label class="radio-inline">
			<input type="radio" name="status" id="status_active" value="christmas">
			Christmas
		</label>
		<label class="radio-inline">
			<input type="radio" name="status" id="status_disabled" value="meat">
                        Meat
		<label class="radio-inline">
			<input type="radio" name="status" id="status_suspended" value="deli-chilled-foods">
			bakery
		</label>
		<label class="radio-inline">
			<input type="radio" name="status" id="status_suspendedd" value="deli-chilled-foods">
			bakery
		</label>
	</form>
</div>
    </div>
    <?php include 'functions2.php'; ?>	
    	<div class="limiter">
		<div class="container-table100">

            <table id="domainsTable" class="footable" data-paging='true' data-sorting='true'  data-paging-size='100' data-filter-container= "#search" data-filtering='true'>
                    <thead>
                            <tr class="table100-head">
                                    <th class="column1">Name</th>
                                    <th class="column2">Brand</th>
                                    <th class="type">Type</th>
                                    <th class="digits" data-type="number">OrigPrice</th>
                                    <th class="digits" data-type="number">SalePrice</th>
                                    <th class="digits" data-type="number">Volume Size</th>
                                    <th class="digits" data-type="number">Discount</th>
                                    <th class="end" data-type="number">MarkDown</th>
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
                                            <td class="end">$$<?php echo sprintf('%0.2f', (1-($row["salePrice"] / $row["origPrice"]))*100 + "%"); ?></td>

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
    $('.selectpicker').selectpicker();

    //on change function i need to control selected value
    $('select.selectpicker').on('change', function(){
       var filtering = FooTable.get('#domainsTable').use(FooTable.Filtering) // get the filtering component for the table
       var filter = $('.selectpicker option:selected').val();
       filtering.addFilter('name', filter, [2], true, false);
    });
        } 
    );
    </script>
    <script>
    $('[name=status]').on('change', function(){
	var filtering = FooTable.get('#domainsTable').use(FooTable.Filtering), // get the filtering component for the table
		filter = $(this).val(); // get the value to filter by
	if (filter === 'none'){ // if the value is "none" remove the filter
		filtering.removeFilter('name');
	} else { // otherwise add/update the filter.
		filtering.addFilter('name', filter, [2], true, false);
	}
	filtering.filter();
});
    </script>
    </body>
</html>
