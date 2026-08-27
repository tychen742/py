<?php
declare(strict_types=1);

require_once __DIR__ . '/../lib/quiz-app.php';

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

$config = py_load_config();
$pdo = py_database_ready($config);
$user = py_current_student_user($pdo, $config);

if ($user === null) {
    echo json_encode([
        'ok' => true,
        'authenticated' => false,
    ], JSON_UNESCAPED_SLASHES);
    exit;
}

echo json_encode([
    'ok' => true,
    'authenticated' => true,
    'identity' => [
        'student_user_id' => $user['student_user_id'] ?? null,
        'student_identifier' => $user['student_identifier'] ?? '',
        'canvas_user_id' => $user['canvas_user_id'] ?? '',
        'display_name' => $user['display_name'] ?? '',
        'email' => $user['email'] ?? '',
        'lti_context_id' => $user['lti_context_id'] ?? '',
        'lti_resource_link_id' => $user['lti_resource_link_id'] ?? '',
        'lti_lineitem_url' => $user['lti_lineitem_url'] ?? '',
    ],
], JSON_UNESCAPED_SLASHES);
