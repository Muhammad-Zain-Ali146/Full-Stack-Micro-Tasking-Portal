document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('searchInput');

    if (searchInput) {
        searchInput.addEventListener('input', function () {
            // User search text (lowercase & trimmed)
            let filterValue = this.value.toLowerCase().trim();
            
            // All task cards
            let taskCards = document.querySelectorAll('.task-card');
            let visibleCount = 0;

            taskCards.forEach(function (card) {
                // Whole text inside the card (Title + Description + Author)
                let cardText = card.textContent.toLowerCase();

                // Check if search keyword exists inside the card
                if (filterValue === "" || cardText.includes(filterValue)) {
                    card.style.display = 'block'; // Show card
                    visibleCount++;
                } else {
                    card.style.display = 'none';  // Hide card
                }
            });

            // Handle 'No Results Found' message
            let noResultsMsg = document.getElementById('noResults');
            if (noResultsMsg) {
                if (visibleCount === 0 && taskCards.length > 0) {
                    noResultsMsg.style.display = 'block';
                } else {
                    noResultsMsg.style.display = 'none';
                }
            }
        });
    }
});