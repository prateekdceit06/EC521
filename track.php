<?php
// Check if form is submitted with POST method
if ($_SERVER["REQUEST_METHOD"] == "POST") {

  // Get the data from the form
  $key = $_POST["payload"];
  echo "$key"


  // Create a new file with a unique name
  $filename =  "details.txt";

  // Open the file for writing
  $handle = fopen($filename, "w");

  // Write the data to the file
  fwrite($handle, "Key: \n$key\n");


  // Close the file
  fclose($handle);

  // Output a success message
  echo "Data saved to file!";
}
?>
