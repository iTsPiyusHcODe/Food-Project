document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Auto-hide alerts after 5 seconds
    setTimeout(function() {
        var alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            var bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);
    
    // Cart quantity controls
    const quantityBtns = document.querySelectorAll('.quantity-btn');
    if (quantityBtns.length > 0) {
        quantityBtns.forEach(btn => {
            btn.addEventListener('click', function() {
                const input = this.parentNode.querySelector('.quantity-input');
                const currentValue = parseInt(input.value);
                
                if (this.classList.contains('increment')) {
                    input.value = currentValue + 1;
                } else if (this.classList.contains('decrement') && currentValue > 1) {
                    input.value = currentValue - 1;
                }
                
                // Update item total
                updateCartItemTotal(input);
            });
        });
        
        // Update totals when quantity inputs change directly
        const quantityInputs = document.querySelectorAll('.quantity-input');
        quantityInputs.forEach(input => {
            input.addEventListener('change', function() {
                if (parseInt(this.value) < 1) {
                    this.value = 1;
                }
                updateCartItemTotal(this);
            });
        });
    }
    
    // Function to update cart item total
    function updateCartItemTotal(input) {
        const cartItem = input.closest('.cart-item');
        if (!cartItem) return;
        
        const price = parseFloat(cartItem.querySelector('.item-price').dataset.price);
        const quantity = parseInt(input.value);
        const totalElement = cartItem.querySelector('.item-total');
        
        if (totalElement) {
            const total = (price * quantity).toFixed(2);
            totalElement.textContent = '$' + total;
            
            // Update cart subtotal and total
            updateCartTotals();
        }
    }
    
    // Function to update cart totals
    function updateCartTotals() {
        const cartItems = document.querySelectorAll('.cart-item');
        let subtotal = 0;
        
        cartItems.forEach(item => {
            const price = parseFloat(item.querySelector('.item-price').dataset.price);
            const quantity = parseInt(item.querySelector('.quantity-input').value);
            subtotal += price * quantity;
        });
        
        const tax = subtotal * 0.1;
        const total = subtotal + tax;
        
        const subtotalElement = document.getElementById('cart-subtotal');
        const taxElement = document.getElementById('cart-tax');
        const totalElement = document.getElementById('cart-total');
        
        if (subtotalElement) subtotalElement.textContent = '$' + subtotal.toFixed(2);
        if (taxElement) taxElement.textContent = '$' + tax.toFixed(2);
        if (totalElement) totalElement.textContent = '$' + total.toFixed(2);
    }
    
    // Recipe filter functionality
    const categoryFilter = document.getElementById('categoryFilter');
    if (categoryFilter) {
        categoryFilter.addEventListener('change', function() {
            const selectedCategory = this.value;
            const recipeCards = document.querySelectorAll('.recipe-card');
            
            recipeCards.forEach(card => {
                if (selectedCategory === 'all' || card.dataset.category === selectedCategory) {
                    card.closest('.col-md-4').style.display = 'block';
                } else {
                    card.closest('.col-md-4').style.display = 'none';
                }
            });
        });
    }
    
    // Add animation classes to elements when they come into view
    const animateElements = document.querySelectorAll('.animate-on-scroll');
    if (animateElements.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-fade-in');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });
        
        animateElements.forEach(element => {
            observer.observe(element);
        });
    }
}); 