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

    // Script for toasts
    document.addEventListener('DOMContentLoaded', function() {
        var toastElements = document.querySelectorAll('.toast');
        toastElements.forEach(function(toastElement) {
            var toast = new bootstrap.Toast(toastElement);
            toast.show();
        });
    });

    // Mailchimp
 (function($) {
    window.fnames = new Array(); 
    window.ftypes = new Array();
    fnames[0]=EMAIL;
    ftypes[0]=merge;
    fnames[1]=FNAME;
    ftypes[1]=merge;
    fnames[2]=LNAME;
    ftypes[2]=merge;
    fnames[3]=ADDRESS;
    ftypes[3]=merge;
    fnames[4]=PHONE;
    ftypes[4]=merge;
    fnames[5]=BIRTHDAY;
    ftypes[5]=merge;
    false;
}(jQuery));
