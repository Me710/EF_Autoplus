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

    // Sample vehicle data
    const vehicles = [
        {
            id: 1,
            name: 'Toyota Camry 2021',
            type: 'sedan',
            price: '25,900$',
            image: 'https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1740&q=80'
        },
        {
            id: 2,
            name: 'Ford Explorer 2022',
            type: 'suv',
            price: '36,500$',
            image: 'https://images.unsplash.com/photo-1606744837616-56c9a5c6a6eb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1742&q=80'
        },
        {
            id: 3,
            name: 'RAM 1500 2020',
            type: 'truck',
            price: '32,700$',
            image: 'https://images.unsplash.com/photo-1570681950018-cc01b0df03a3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1740&q=80'
        },
        {
            id: 4,
            name: 'BMW X5 2022',
            type: 'luxury',
            price: '59,900$',
            image: 'https://images.unsplash.com/photo-1616788494707-ec28f08fd05a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1740&q=80'
        },
        {
            id: 5,
            name: 'Honda Civic 2020',
            type: 'sedan',
            price: '21,300$',
            image: 'https://images.unsplash.com/photo-1558981852-426c6c22a060?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1742&q=80'
        },
        {
            id: 6,
            name: 'Jeep Grand Cherokee 2021',
            type: 'suv',
            price: '38,200$',
            image: 'https://images.unsplash.com/photo-1591462658157-2c227bbf1c50?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1740&q=80'
        },
    ];

    // Render vehicles
    function renderVehicles(filter = 'all') {
        const vehicleGrid = document.getElementById('vehicle-grid');
        vehicleGrid.innerHTML = '';

        const filteredVehicles = filter === 'all'
            ? vehicles
            : vehicles.filter(vehicle => vehicle.type === filter);

        filteredVehicles.forEach(vehicle => {
            const vehicleCard = document.createElement('div');
            vehicleCard.className = 'car-card bg-gray-900 rounded-lg overflow-hidden transition-all duration-300 hover:shadow-xl';

            vehicleCard.innerHTML = `
                <div class="relative overflow-hidden h-48">
                    <img src="${vehicle.image}" alt="${vehicle.name}" class="car-img w-full h-full object-cover transition-transform duration-500">
                    <div class="absolute bottom-0 left-0 bg-red-600 text-white px-4 py-1 text-sm">${vehicle.price}</div>
                </div>
                <div class="p-6">
                    <h3 class="text-xl font-bold mb-2">${vehicle.name}</h3>
                    <div class="flex justify-between items-center">
                        <span class="text-gray-400 text-sm uppercase">${vehicle.type === 'luxury' ? 'Luxe' : vehicle.type === 'truck' ? 'Camion' : vehicle.type === 'suv' ? 'SUV' : 'Berline'}</span>
                        <button class="btn-gradient hover:bg-red-800 text-white font-bold py-2 px-4 rounded transition duration-300 text-sm">
                            Voir détails
                        </button>
                    </div>
                </div>
            `;

            vehicleGrid.appendChild(vehicleCard);
        });
    }

    // Initialize with all vehicles
    renderVehicles();

    // Filter buttons event listeners
    const filterButtons = document.querySelectorAll('.filter-btn');
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            filterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');

            const filter = button.getAttribute('data-filter');
            renderVehicles(filter);
        });
    });

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
