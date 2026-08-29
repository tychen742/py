<?php
declare(strict_types=1);

require_once __DIR__ . '/../lib/quiz-app.php';

$config = py_load_config();
$error = null;
$target = py_safe_target((string) ($_GET['next'] ?? $_POST['next'] ?? '/'));
$token = (string) ($_GET['token'] ?? $_POST['token'] ?? '');
$userId = (int) ($_GET['uid'] ?? $_POST['uid'] ?? 0);

try {
    $pdo = py_database_ready($config);
} catch (Throwable $exception) {
    http_response_code(500);
    echo '<!doctype html><meta charset="utf-8"><title>Create Password</title>';
    echo '<h1>Create Password</h1>';
    echo '<p>Database is not configured.</p>';
    echo '<pre>' . py_h($exception->getMessage()) . '</pre>';
    exit;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $newPassword = (string) ($_POST['new_password'] ?? '');
    $confirmPassword = (string) ($_POST['confirm_password'] ?? '');
    if ($newPassword !== $confirmPassword) {
        $error = 'Passwords do not match.';
    } elseif (strlen($newPassword) < 10) {
        $error = 'Password must be at least 10 characters.';
    } else {
        $identifier = py_verify_student_email_token($pdo, $token, $newPassword, $userId > 0 ? $userId : null);
        if ($identifier !== null && py_login_student($pdo, $config, $identifier, $newPassword)) {
            header('Location: ' . $target);
            exit;
        }
        $error = 'This link is invalid or expired. Request a new verification email.';
    }
}

?>
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Create Password</title>
  <style>
body { margin: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; color: #24292f; background: #f6f8fa; }
.shell { max-width: 440px; margin: 0 auto; padding: 32px; }
h1 { margin: 0 0 8px; font-size: 28px; }
p { color: #57606a; }
form { display: grid; gap: 16px; padding: 20px; border: 1px solid #d8dee4; border-radius: 8px; background: white; }
label { display: grid; gap: 6px; font-weight: 600; }
input { padding: 10px; border: 1px solid #d0d7de; border-radius: 6px; font: inherit; }
button { padding: 10px 14px; border: 1px solid #0969da; border-radius: 6px; background: #0969da; color: white; font-weight: 700; cursor: pointer; }
.alert { padding: 12px 14px; border-radius: 6px; font-weight: 600; background: #ffebe9; color: #cf222e; }
  </style>
</head>
<body>
  <main class="shell">
    <h1>Create Password</h1>
    <p>Set a password with at least 10 characters.</p>
    <?php if ($error !== null): ?><p class="alert"><?php echo py_h($error); ?></p><?php endif; ?>
    <form method="post">
      <input type="hidden" name="token" value="<?php echo py_h($token); ?>">
      <input type="hidden" name="uid" value="<?php echo py_h($userId); ?>">
      <input type="hidden" name="next" value="<?php echo py_h($target); ?>">
      <label>New Password <input type="password" name="new_password" autocomplete="new-password" minlength="10" required></label>
      <label>Confirm Password <input type="password" name="confirm_password" autocomplete="new-password" minlength="10" required></label>
      <button type="submit">Set password and sign in</button>
    </form>
  </main>
</body>
</html>
