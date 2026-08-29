<?php
declare(strict_types=1);

require_once __DIR__ . '/../lib/quiz-app.php';

$config = py_load_config();
py_start_admin_session($config);
$target = py_safe_target((string) ($_GET['next'] ?? '/'));
$_SESSION = [];
session_destroy();

header('Location: ' . $target);
exit;
