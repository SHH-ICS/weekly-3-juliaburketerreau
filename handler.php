<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-pink.min.css">
    <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>
    <title>Welcome Page</title>
  </head>

  <body>
    
    <center> 
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
    if ($toppings == "1"){
        $top_cost = 1;
    }
    elseif ($toppings == "2"){
        $top_cost = 1.75;
    }
    elseif ($toppings == "3"){
        $top_cost = 2.50;
    }
    elseif ($toppings == "4"){
      $top_cost = 3.35;
    }
  
}
$subtotal = $large + $top_cost;
        echo"Your subtotal is";
        var_dump(round($subtotal));
        echo"$". $subtotal;
        $tax = 0.13 * $subtotal;
        var_dump(round($tax));
        echo"Your tax is";
        echo"$". $tax;
        $fintot = $tax + $subtotal;
        var_dump(round($fintot));
        echo"Your final cost is";
        echo"$". $fintot;

    if ($pizza == "Extra Large") {
      echo "That costs $6";
      $large = 10;
      echo "How many toppings, 1, 2, 3 or 4?";
      $toppings = $_POST['toppings'];
      if ($toppings == "1") {
        $top_cost = 1;
      } elseif ($toppings == "2") {
        $top_cost = 1.75;
      } elseif ($toppings == "3") {
        $top_cost = 2.50;
      } elseif ($toppings == "4") {
        $top_cost = 3.35;
      }
    }





    echo "<h1>My Program</h1>\n";
    echo "<p>My Variable is = ".$pizza."</p>\n";
    ?>
    
  </body>
  
</html>