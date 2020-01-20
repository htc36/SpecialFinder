<head>

    <!-- Style -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.4.1/css/bootstrap.min.css" rel="stylesheet" />
    <link href="specialFinder/fresh-bootstrap-table-master/assets/css/fresh-bootstrap-table.css" rel="stylesheet" />

    <!-- Fonts and icons -->
    <link href="https://use.fontawesome.com/releases/v5.6.3/css/all.css" rel="stylesheet">
    <link href="http://fonts.googleapis.com/css?family=Roboto:400,700,300" rel="stylesheet" type="text/css">

</head>
<?php include 'specialFinder/server/functions.php'; ?>

<div class="fresh-table toolbar-color-blue">
  <!--
    Available colors for the full background: full-color-blue, full-color-azure, full-color-green, full-color-red, full-color-orange
    Available colors only for the toolbar: toolbar-color-blue, toolbar-color-azure, toolbar-color-green, toolbar-color-red, toolbar-color-orange
  -->

  <div class="toolbar">
    <button id="alertBtn" class="btn btn-default">Alert</button>
    <select id = "hi" onchange="dateOfData(this)" > 
        <?php while($row = $tableNames->fetch_assoc()) { ?>
        <option> <?php echo $row["table_name"]; ?> </option>
        <?php }; ?>
        <option> None </option>
        <option> hit </option>
    </select>

    <select id = "types" onchange="typeOfData(this)"> 
        <option>None</option>
        <?php while($row = $type->fetch_assoc()) { ?>
        <option> <?php echo $row["type"]; ?> </option>
        <?php }; ?>
    </select>
    


  </div>

  <table id="fresh-table" class="table"
        data-side-pagination="server"
        data-show-extended-pagination="true"
        data-query-params="queryParams"
        >
    <thead>
        <th data-field="name" data-sortable="true">Name</th>
        <th data-field="brand" data-sortable="true">Brand</th>
        <th data-field="type" data-sortable="true">Type</th>
        <th data-field="origPrice" data-sortable="true">Original Price</th>
        <th data-field="salePrice" data-sortable="true">Sale Price</th>
        <th data-field="volSize" data-sortable="true">Volume Size</th>
        <th data-field="discount" data-sortable="true">Discount</th>
        <th data-field="markDown" data-sortable="true">Mark Down</th>

    </thead>
  </table>
</div>
<!-- Javascript -->
<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.4.1/js/bootstrap.min.js"></script>
<script src="https://unpkg.com/bootstrap-table/dist/bootstrap-table.min.js"></script>

<script type="text/javascript">
  var $table = $('#fresh-table')
  var $alertBtn = $('#alertBtn')

  window.operateEvents = {
    'click .like': function (e, value, row, index) {
      alert('You click like icon, row: ' + JSON.stringify(row))
      console.log(value, row, index)
    },
    'click .edit': function (e, value, row, index) {
      alert('You click edit icon, row: ' + JSON.stringify(row))
      console.log(value, row, index)
    },
    'click .remove': function (e, value, row, index) {
      $table.bootstrapTable('remove', {
        field: 'id',
        values: [row.id]
      })
    }
  }

  function operateFormatter(value, row, index) {
    return [
      '<a rel="tooltip" title="Like" class="table-action like" href="javascript:void(0)" title="Like">',
        '<i class="fa fa-heart"></i>',
      '</a>',
      '<a rel="tooltip" title="Edit" class="table-action edit" href="javascript:void(0)" title="Edit">',
        '<i class="fa fa-edit"></i>',
      '</a>',
      '<a rel="tooltip" title="Remove" class="table-action remove" href="javascript:void(0)" title="Remove">',
        '<i class="fa fa-remove"></i>',
      '</a>'
    ].join('')
  }
    function queryParams(params) {
    params.dateOfSpecials = document.getElementById("hi").value 
    params.type = document.getElementById("types").value
    return params
      }

    function dateOfData(selectObj) {
       var selectIndex=selectObj.selectedIndex;
       var selectValue=selectObj.options[selectIndex].text;
       $('#fresh-table').bootstrapTable('refresh', {
            query: {
            dateOfSpecials: selectValue
            }
        });
    };

    function typeOfData(selectObj) {
       var selectIndex=selectObj.selectedIndex;
       var selectValue=selectObj.options[selectIndex].text;
       $('#fresh-table').bootstrapTable('refresh', {
            query: {
            type: selectValue
            }
        });
    };


  $(function () {
    $table.bootstrapTable({
      classes: 'table table-hover table-striped',
      toolbar: '.toolbar',
      url: 'specialFinder/server/connect.php',
      
      search: true,
      showRefresh: true,
      showToggle: true,
      showColumns: true,
      pagination: true,
      striped: true,
      sortable: true,
      pageSize: 8,
      pageList: [8, 10, 25, 50, 100],

      formatShowingRows: function (pageFrom, pageTo, totalRows) {
        return ''
      },
      formatRecordsPerPage: function (pageNumber) {
        return pageNumber + ' rows visible'
      }
    })

    $alertBtn.click(function () {
      alert('You pressed on Alert')
    })
  })

  $('#fresh-table').on('click-row.bs.table', function (row, $element, field) {
    window.open("http://www.countdownspecials.xyz/specialFinder/tableTest.php?prodNum="+$element.code, '_blank');
    alert($element.code)

	
	
})

</script>

      
