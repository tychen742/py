// Dynamically update interactive exercise counters to show X/Total per page
document.addEventListener('DOMContentLoaded', function() {
    // Find all interactive exercise cells
    const exercises = document.querySelectorAll('div.cell.tag_thebe-interactive');
    const total = exercises.length;
    
    // Update each exercise with its number and the total
    exercises.forEach((exercise, index) => {
        const counter = index + 1;
        
        // Create or update the exercise label
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
        
        // Insert at the beginning of the cell
        exercise.insertBefore(label, exercise.firstChild);
    });
});
