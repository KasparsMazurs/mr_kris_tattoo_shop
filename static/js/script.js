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

    // delite product from cart
    function deleteProduct(item_id) {
        // Send an AJAX request to update the quantity to 0 for the specified product item
        // You can use the item_id to identify the product in the backend and update the quantity
    
        // Example AJAX request using jQuery
        $.ajax({
            url: '/delete/' + item_id + '/',  // URL to your delete view
            type: 'POST',
            data: { quantity: 0 },  // Set the quantity to 0
            success: function(response) {
                // Handle the response if needed, e.g., remove the deleted product item from the DOM
                // Example: $('#item_' + item_id).remove();
            },
            error: function(xhr, errmsg, err) {
                // Handle the error if needed
            }
        });
    }