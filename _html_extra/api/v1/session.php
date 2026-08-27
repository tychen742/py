<?php
declare(strict_types=1);

require_once __DIR__ . '/../lib/quiz-app.php';

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

$config = py_load_config();
$pdo = py_database_ready($config);
$student = null;
$admin = null;

$studentSessionName = (string) ($config['student_auth']['session_name'] ?? 'py_student');
if (isset($_COOKIE[$studentSessionName])) {
    $student = py_current_student_user($pdo, $config);
    if (session_status() === PHP_SESSION_ACTIVE) {
        session_write_close();
        $_SESSION = [];
    }
}

$adminSessionName = (string) ($config['auth']['session_name'] ?? 'py_quiz_admin');
if (isset($_COOKIE[$adminSessionName])) {
    py_start_admin_session($config);
    $admin = py_current_admin($pdo);
    if (session_status() === PHP_SESSION_ACTIVE) {
        session_write_close();
        $_SESSION = [];
    }
}

if ($admin !== null) {
    echo json_encode([
        'ok' => true,
        'authenticated' => true,
        'role' => 'admin',
        'identity' => [
            'admin_user_id' => $admin['id'] ?? null,
            'display_name' => $admin['display_name'] ?? '',
            'email' => $admin['email'] ?? '',
        ],
    ], JSON_UNESCAPED_SLASHES);
    exit;
}

if ($student === null) {
    echo json_encode([
        'ok' => true,
        'authenticated' => false,
    ], JSON_UNESCAPED_SLASHES);
    exit;
}

echo json_encode([
    'ok' => true,
    'authenticated' => true,
    'role' => 'student',
    'identity' => [
        'student_user_id' => $student['student_user_id'] ?? null,
        'student_identifier' => $student['student_identifier'] ?? '',
        'canvas_user_id' => $student['canvas_user_id'] ?? '',
        'display_name' => $student['display_name'] ?? '',
        'email' => $student['email'] ?? '',
        'lti_context_id' => $student['lti_context_id'] ?? '',
        'lti_resource_link_id' => $student['lti_resource_link_id'] ?? '',
        'lti_lineitem_url' => $student['lti_lineitem_url'] ?? '',
    ],
], JSON_UNESCAPED_SLASHES);
