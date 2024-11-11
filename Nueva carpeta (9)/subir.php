<?php
// Incluir la biblioteca Python que sube archivos
require_once 'subir_archivo.py';

// Recibir los datos del formulario
$title = $_POST['title'];
$description = $_POST['description'];
$email = $_POST['email'];
$privacy = $_POST['privacy'];
$file = $_FILES['file'];

// Subir el archivo
subir_archivo($file, $title, $description, $email, $privacy);
?>