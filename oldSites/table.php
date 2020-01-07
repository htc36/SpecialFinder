<!DOCTYPE html>
<html>
<body>
    <?php include 'functions.php'; ?>	
    <div class="wrap-table100">
            <div class="table100">
                    <table id="myTable" class="tablesorter">
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
</body>
</html>
