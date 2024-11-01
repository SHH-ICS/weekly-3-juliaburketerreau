<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-pink.min.css">
    <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>
    <title>Welcome Page</title>
  </head>

  <body>
    
    <?php
    $pizza = "";
    if ( isset( $_POST['pizza'] ) ){
      $pizza = $_POST['pizza'];
    }
    $toppings = "";
    if (isset($_POST['toppings'])) {
      $toppings = $_POST['toppings'];
    }
echo "Large or Extra Large?";
if ($pizza == "Large") {
  echo "That costs $6";
    $large = 6;
  echo "How many toppings, 1, 2, 3 or 4?";
    $toppings = $_POST['toppings'];
    if toppings == "1";
        $top_cost = 1
    elif $toppings == "2";
        $top_cost = 1.75
    elif $toppings == "3";
        $top_cost = 2.50
    elif $toppings == "4";
        $top_cost = 3.35
}



    echo "<h1>My Program</h1>\n";
    echo "<p>My Variable is = ".$pizza."</p>\n";
    ?>
    
  </body>
  
</html>