console.log("Custom JS loaded!");

// Handle sidebar toggle using event delegation (more reliable)
document.addEventListener('click', function(e) {
    const toggleButton = e.target.closest('button.sidebar-toggle.primary-toggle');

    if (toggleButton) {
        e.preventDefault();
        e.stopPropagation();

        const sidebar = document.querySelector('.bd-sidebar-primary');
        if (sidebar) {
            sidebar.classList.toggle('show');
            document.body.classList.toggle('sidebar-visible');
            const isExpanded = sidebar.classList.contains('show');
            toggleButton.setAttribute('aria-expanded', isExpanded);
        }
        return false;
    }

    // Close sidebar when clicking outside
    const sidebar = document.querySelector('.bd-sidebar-primary');
    if (sidebar && document.body.classList.contains('sidebar-visible')) {
        if (!sidebar.contains(e.target) && !e.target.closest('button.sidebar-toggle.primary-toggle')) {
            sidebar.classList.remove('show');
            document.body.classList.remove('sidebar-visible');
        }
    }
}, true);

// ---- SINGLE DOMContentLoaded handler ----
document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM ready!");

    // Thebe activation detection
    var thebeActivated = false;

    var activationObserver = new MutationObserver(function() {
        if (thebeActivated) return;
        if (document.querySelector('.thebelab-run-button')) {
            thebeActivated = true;
            activationObserver.disconnect();
            document.body.classList.add('thebe-is-active');
            console.log("[fix B] Thebe detected — added thebe-is-active to body");

            document.querySelectorAll('.thebelab-run-button').forEach(function(btn) {
                btn.addEventListener('click', function() {
                    var cell = btn.closest('.cell');
                    if (cell && !cell.classList.contains('tag_hide-input')) {
                        cell.classList.add('cell-has-run');
                        console.log("[fix B] Marked cell-has-run for", cell.id);
                    }
                });
            });
        }
    });
    activationObserver.observe(document.body, { childList: true, subtree: true });

    // Exercise counter labels
    const exercises = document.querySelectorAll('div.cell.tag_thebe-interactive');
    const total = exercises.length;

    exercises.forEach((exercise, index) => {
        const counter = index + 1;
        const label = document.createElement('div');
        label.className = 'exercise-label';
        label.innerHTML = `✏️ Interactive Exercise ${counter}/${total}`;
        label.style.cssText = `
            display: block;
            font-size: 0.85em;
            color: #AD2327;
            font-weight: bold;
            margin-bottom: 8px;
        `;
        exercise.insertBefore(label, exercise.firstChild);
    });
});