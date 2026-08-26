<?php
declare(strict_types=1);

require_once __DIR__ . '/../lib/quiz-app.php';

$config = py_load_config();
py_start_admin_session($config);
$_SESSION = [];
session_destroy();

header('Location: /api/admin/');
