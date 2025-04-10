<?php
$data = json_decode(file_get_contents("php://input"), true);
$symbol = $data['symbol'];
$labels = $data['labels'];
$prices = $data['prices'];
$volumes = $data['volumes'];

$conn = new mysqli("localhost", "your_username", "your_password", "your_database");
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

for ($i = 0; $i < count($labels); $i++) {
  $time = $conn->real_escape_string($labels[$i]);
  $price = $prices[$i];
  $volume = $volumes[$i];

  $conn->query("INSERT INTO stock_data (symbol, time, price, volume)
                VALUES ('$symbol', '$time', '$price', '$volume')
                ON DUPLICATE KEY UPDATE price='$price', volume='$volume'");
}

$conn->close();
?>
