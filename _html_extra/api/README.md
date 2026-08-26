# Python Quiz API

This directory is copied into the published Jupyter Book by `./deploy`.

## Endpoint

`POST /api/v1/quiz-attempts.php`

`POST /api/v1/lab-attempts.php`

Stores and grades a quiz or lab attempt. If Canvas settings and Canvas IDs are available, the endpoint also attempts grade sync. Otherwise the attempt is saved with `pending` sync status.

The Chapter 01 preview and lab pages post each student attempt to these endpoints. The browser does not contain the answer key; grading happens on the server. The lab grader checks final submitted values rather than executing student code on the server.

Saved fields include:

- quiz ID, chapter, and assignment slug
- student identifier
- Canvas course, assignment, and user IDs when provided
- score and maximum score
- submitted answers and per-question feedback as JSON
- Canvas sync status and sync error
- submission timestamp, IP address, and user agent

## Production Configuration

Do not commit production secrets. Put configuration outside the repository, then point `PY_QUIZ_CONFIG` to it or use the default path:

`/var/www/py_private/quiz_config.php`

On the current production server, `/home/tychen/py_private/quiz_config.php` is also supported. Keep that directory outside the public web root and grant Apache read access with a narrow ACL.

Do not point the Python API at DSM's private config in production. The code only considers `/var/www/dsm_private/quiz_config.php` when `PY_ALLOW_DSM_CONFIG_FALLBACK` is explicitly set to `1`, `true`, or `yes`; that fallback is for emergency local migration only. Use a Python-specific config so admin sessions, database credentials, Canvas settings, and LTI settings stay isolated from DSM.

Example:

```php
<?php
return [
    'database' => [
        'driver' => 'mysql',
        'dsn' => 'mysql:host=127.0.0.1;dbname=py_quiz;charset=utf8mb4',
        'username' => 'py_quiz',
        'password' => 'CHANGE_ME',
    ],
    'canvas' => [
        'base_url' => 'https://YOUR_CANVAS_DOMAIN',
        'access_token' => 'CHANGE_ME',
        'enabled' => true,
    ],
    'lti' => [
        'enabled' => true,
        'issuer' => 'https://canvas.instructure.com',
        'client_id' => 'CANVAS_DEVELOPER_KEY_CLIENT_ID',
        'deployment_ids' => ['CANVAS_DEPLOYMENT_ID'],
        'auth_login_url' => 'https://sso.canvaslms.com/api/lti/authorize_redirect',
        'jwks_url' => 'https://sso.canvaslms.com/api/lti/security/jwks',
        'redirect_uri' => 'https://thinkpy.org/api/lti/launch.php',
        'default_target_link_uri' => 'https://thinkpy.org/chapters/01-intro/assignments/preview.html',
    ],
    'auth' => [
        'bootstrap_admins' => [
            [
                'email' => 'you@example.edu',
                'display_name' => 'Your Name',
                'password_hash' => 'PASTE_PASSWORD_HASH_HERE',
            ],
        ],
    ],
];
```

Create the password hash on the server:

```bash
php -r 'echo password_hash("CHANGE_ME", PASSWORD_DEFAULT), PHP_EOL;'
```

For local development, if no config is found, the API tries SQLite at `/tmp/py_quiz_attempts.sqlite`. If the server does not have the needed PDO driver, the endpoint falls back to a newline-delimited JSON file at `/var/www/py_private/py_quiz_attempts.jsonl` so student submissions are still captured.

The JSONL fallback is a safety net, not the preferred production store. Configure MySQL/MariaDB before using the Canvas sync job for a class.

## Admin Gradebook

After the database and admin bootstrap config are in place, open:

`/api/admin/`

The admin module supports:

- password-protected admin login
- score table with student identifier, quiz, score, Canvas status, and submitted answers
- detailed CSV export
- Canvas-ready CSV export keyed by `SIS Login ID`
- manual sync of pending or failed attempts to Canvas

The admin module requires a working PDO database connection. It does not read from the JSONL fallback store directly.

## Canvas LTI 1.3 Login

The LTI endpoints are:

- Login initiation URL: `https://thinkpy.org/api/lti/login.php`
- Redirect URI: `https://thinkpy.org/api/lti/launch.php`
- Target link URI for Chapter 01 preview: `https://thinkpy.org/chapters/01-intro/assignments/preview.html`

Configure these URLs in a Canvas LTI 1.3 Developer Key. After installing the tool in a course, copy the Canvas client ID and deployment ID into the private `lti` config.

When launched from Canvas, the tool validates the signed Canvas `id_token`, creates or updates a student row in `py_quiz_users`, stores the Canvas identity in a secure LTI session, and saves quiz attempts with that identity. The student-facing quiz page calls `/api/v1/session.php` to fill the student identifier automatically.

## Manual Canvas Workflow

Use this workflow until the Canvas LTI tool is installed by an admin:

1. In Canvas, create assignments named `preview_ch01` and `lab_ch01`.
2. Set points to `10`.
3. Put the Python assignment URLs in the Canvas assignment instructions:
   `https://thinkpy.org/chapters/01-intro/assignments/preview.html`
   `https://thinkpy.org/chapters/01-intro/assignments/lab.html`
4. Ask students to enter their Canvas `SIS Login ID` before submitting.
5. Review submissions in `https://thinkpy.org/api/admin/`.
6. Export Canvas CSV from the admin page and upload it in Canvas Gradebook.

Manual submissions save in MySQL, but they do not automatically verify Canvas identity. LTI launch remains the preferred production identity path.

## Later Canvas Sync

Pending or failed attempts can be synced after submission:

```bash
php /var/www/py/api/cli/sync-canvas.php --limit=100
```

Run the command from cron after production configuration is in place. The script reads the same `PY_QUIZ_CONFIG` file, finds saved attempts with `pending` or `failed` status, sends the saved score to Canvas, and updates each row to `synced`, `failed`, or `skipped`.

Rows can only sync when they include `canvas_course_id`, `canvas_assignment_id`, and `canvas_user_id`. If the book is opened directly without Canvas/LTI launch parameters, attempts still save, but Canvas sync is marked `skipped` until those IDs are available.
