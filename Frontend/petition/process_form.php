<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  // Process form data
  $name = $_POST["name"];
  $email = $_POST["email"];
  $message = $_POST["message"];

  // Handle file upload
  $fileUploaded = false;
  $uploadDir = "uploads/";
  $uploadedFile = $uploadDir . basename($_FILES["file"]["name"]);

  if (move_uploaded_file($_FILES["file"]["tmp_name"], $uploadedFile)) {
    $fileUploaded = true;
  }

  // Save data to database or perform any other required actions

  // Redirect to a success page or display a success message
  header("Location: success.html");
  exit;
}
?>
