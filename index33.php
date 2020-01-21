<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Hello, Bootstrap Table!</title>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css" integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/" crossorigin="anonymous">
    <link rel="stylesheet" href="https://unpkg.com/bootstrap-table@1.15.5/dist/bootstrap-table.min.css">
    <link rel="stylesheet" type="text/css" href="specialFinder/css/style.css">
  </head>
  <body>
     <?php include 'specialFinder/server/functions.php'; ?>
     <div class="topnav"> 
      <a class="active" href="#home">Specials</a>
	<div class ="combo">
            <select id = "hi" onchange="dateOfData(this)" > 
                <?php while($row = $tableNames->fetch_assoc()) { ?>
                    <option> <?php echo $row["table_name"]; ?> </option>
                <?php }; ?>
            <option> None </option>
            <option> hit </option>
        </select>
            <select id="types">  <option> hhhhhhhhhhhhhh </option>
        </select>
	</div>
    </div>
    	<div class="limiter">
              <table data-toggle="table" 
                id = "table"
                data-url="specialFinder/server/connect.php" 
                data-height="100%"
                data-search="true"
                data-pagination="true"
                data-side-pagination="server"
                data-query-params="queryParams"
                data-sortable="true"
                data-page-size="25"
		data-mobile-responsive="true"
                >
              <thead>
                  <tr>
                      <th data-field="name" data-sortable="true">Name</th>
                      <th data-field="brand" data-sortable="true">Brand</th>
                      <th data-field="origPrice" data-sortable="true">Original Price</th>
                      <th data-field="salePrice" data-sortable="true">Sale Price</th>
                      <th data-field="volSize" data-sortable="true">Volume Size</th>
                      <th data-field="discount" data-sortable="true">Discount</th>
                      <th data-field="markDown" data-sortable="true">Mark Down</th>
                  </tr>
              </thead>
          </table>
        </div>
  
  <script>
      function queryParams(params) {
	params.search = 8
        return params
      }
      function dateOfData(selectObj) {
           var selectIndex=selectObj.selectedIndex;
           var selectValue=selectObj.options[selectIndex].text;
           $('#table').bootstrapTable('refresh', {
                query: {
                dateOfSpecials: selectValue
                }
            });
        };


</script>


    <script src="https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <script src="https://unpkg.com/bootstrap-table@1.15.5/dist/bootstrap-table.min.js"></script>
	<script src="https://unpkg.com/bootstrap-table@1.15.5/dist/extensions/mobile/bootstrap-table-mobile.min.js"></script>
  </body>
</html>
