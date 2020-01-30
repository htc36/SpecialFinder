<head>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.4.1/css/bootstrap.min.css" rel="stylesheet"
     />
         <link href="specialFinder/fresh-bootstrap-table-master/assets/css/fresh-bootstrap-table.css" rel="stylesheet" />

             <!-- Fonts and icons -->
                 <link href="https://use.fontawesome.com/releases/v5.6.3/css/all.css" rel="stylesheet">
                     <link href="http://fonts.googleapis.com/css?family=Roboto:400,700,300" rel="stylesheet" type="text/css">
</head>

<table
  id="table"
  data-toggle="table"
  data-height="460"
  data-ajax="ajaxRequest"
  data-search="true"
  data-side-pagination="server"
  data-pagination="true">
  <thead>
    <tr>
      <th data-field="id">ID</th>
      <th data-field="name">Item Name</th>
      <th data-field="price">Item Price</th>
    </tr>
  </thead>
</table>

<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.4.1/js/bootstrap.min.js"></script>
<script src="https://unpkg.com/bootstrap-table/dist/bootstrap-table.min.js"></script>
<script>

  // your custom ajax request here
  function ajaxRequest(params) {
    var url = 'http://45.76.124.20:8080/api/products'
    $.get(url + '?' + $.param(params.data)).then(function (res) {
      params.success(res)
    })
  }
</script>
