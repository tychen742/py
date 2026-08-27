<?php
declare(strict_types=1);

require_once __DIR__ . '/../lib/quiz-app.php';

$config = py_load_config();
$target = py_safe_target((string) ($_GET['next'] ?? '/'));
py_start_student_session($config);
$_SESSION = [];
session_destroy();

header('Location: ' . $target);
exit;
