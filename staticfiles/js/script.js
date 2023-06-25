    // Filter button click event handler
    document.querySelectorAll('.filter-button').forEach(function(button) {
        button.addEventListener('click', function() {
            var filter = this.dataset.filter;
            filterGallery(filter);
        });
    });

    // Filter gallery based on the selected category
    function filterGallery(category) {
        var galleryItems = document.querySelectorAll('.card');
        galleryItems.forEach(function(item) {
            var itemCategory = item.dataset.category;
            if (category === 'all' || itemCategory === category) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    }

    