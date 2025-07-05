document.addEventListener('DOMContentLoaded', function () {
    // Mobile menu toggle
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');

    mobileMenuButton.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            mobileMenu.classList.add('hidden');

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Filter buttons event listeners
    const filterButtons = document.querySelectorAll('.filter-btn');
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            filterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');

            const filter = button.getAttribute('data-filter');
            filterVehicles(filter);
        });
    });

    // Filter vehicles function
    function filterVehicles(filter) {
        const vehicleCards = document.querySelectorAll('.car-card');
        vehicleCards.forEach(card => {
            const typeElement = card.querySelector('.text-gray-400');
            const vehicleType = typeElement.textContent.toLowerCase().trim();

            if (filter === 'all' ||
                (filter === 'sedan' && vehicleType === 'berline') ||
                (filter === 'suv' && vehicleType === 'suv') ||
                (filter === 'truck' && vehicleType === 'camion') ||
                (filter === 'luxury' && vehicleType === 'luxe')) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }

    // File upload display name
    const photoInput = document.getElementById('photo');
    const fileNameDisplay = document.getElementById('file-name');

    if (photoInput && fileNameDisplay) {
        photoInput.addEventListener('change', (event) => {
            const file = event.target.files[0];
            if (file) {
                fileNameDisplay.textContent = file.name;
            } else {
                fileNameDisplay.textContent = 'Téléverser une photo';
            }
        });
    }

    // Form submissions
    const exchangeForm = document.getElementById('exchange-form');
    const contactForm = document.getElementById('contact-form');

    if (exchangeForm) {
        exchangeForm.addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Votre demande d\'échange a été envoyée avec succès. Nous vous contacterons rapidement!');
            exchangeForm.reset();
            if (fileNameDisplay) fileNameDisplay.textContent = 'Téléverser une photo';
        });
    }

    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Votre message a été envoyé avec succès. Nous vous répondrons dès que possible!');
            contactForm.reset();
        });
    }
});
