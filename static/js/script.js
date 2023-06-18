    // Filter button click event handler
    document.querySelectorAll('.filter-button').forEach(function(button) {
        button.addEventListener('click', function() {
            var filter = this.dataset.filter;
            filterGallery(filter);
        });
    });

    // Filter gallery based on the body part
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

    // Filter products based on art type
    function filterProducts() {
        const filterType = document.getElementById('filter-select').value;
        const url = new URL(window.location);
        const params = new URLSearchParams(url.search);
        
        if (filterType) {
            params.set('filter', filterType);
        } else {
            params.delete('filter');
        }
        
        window.location.href = url.pathname + '?' + params.toString();
    }

