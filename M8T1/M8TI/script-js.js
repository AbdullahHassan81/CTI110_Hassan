document.addEventListener('DOMContentLoaded', () => {
    // Race Cars Data
    const raceCars = {
        f1: [
            { name: "Mercedes W14", team: "Mercedes", specs: "Latest F1 car" },
            { name: "Red Bull RB19", team: "Red Bull Racing", specs: "Championship-winning car" }
        ],
        nascar: [
            { name: "Hendrick Motorsports Camaro", team: "Hendrick", specs: "Top-tier NASCAR vehicle" }
        ]
    };

    // Dealerships Data
    const dealerships = {
        online: ["Carvana", "CarMax", "Cars.com"],
        local: ["Local Car Club Meetups", "Regional Car Museums", "Annual Auto Shows"]
    };

    // Maintenance Tools Data
    const maintenanceTools = {
        basic: {
            name: "Basic Toolkit",
            items: ["Wrench Set", "Screwdriver Set", "Jack"],
            cost: "$100-$200"
        },
        advanced: {
            name: "Advanced Toolkit",
            items: ["Diagnostic Scanner", "Torque Wrench", "Oil Filter Wrench"],
            cost: "$300-$500"
        }
    };

    // Populate Race Cars
    function populateRaceCars() {
        const f1Grid = document.getElementById('f1-cars');
        const nascarGrid = document.getElementById('nascar-cars');

        if (f1Grid) {
            raceCars.f1.forEach(car => {
                const carCard = document.createElement('div');
                carCard.classList.add('car-card');
                carCard.innerHTML = `
                    <h4>${car.name}</h4>
                    <p>Team: ${car.team}</p>
                    <p>Specs: ${car.specs}</p>
                `;
                f1Grid.appendChild(carCard);
            });
        }

        if (nascarGrid) {
            raceCars.nascar.forEach(car => {
                const carCard = document.createElement('div');
                carCard.classList.add('car-card');
                carCard.innerHTML = `
                    <h4>${car.name}</h4>
                    <p>Team: ${car.team}</p>
                    <p>Specs: ${car.specs}</p>
                `;
                nascarGrid.appendChild(carCard);
            });
        }
    }

    // Populate Dealerships
    function populateDealerships() {
        const onlineDealershipSection = document.getElementById('online-dealerships');
        const localDealershipSection = document.getElementById('local-dealerships');

        if (onlineDealershipSection) {
            const onlineList = document.createElement('ul');
            dealerships.online.forEach(dealer => {
                const listItem = document.createElement('li');
                listItem.textContent = dealer;
                onlineList.appendChild(listItem);
            });
            onlineDealershipSection.appendChild(onlineList);
        }

        if (localDealershipSection) {
            const localList = document.createElement('ul');
            dealerships.local.forEach(location => {
                const listItem = document.createElement('li');
                listItem.textContent = location;
                localList.appendChild(listItem);
            });
            localDealershipSection.appendChild(localList);
        }
    }

    // Populate Maintenance Tools
    function populateMaintenanceTools() {
        const basicToolkitSection = document.getElementById('basic-toolkit');
        const advancedToolkitSection = document.getElementById('advanced-toolkit');

        if (basicToolkitSection) {
            const basicToolDetails = document.createElement('div');
            basicToolDetails.innerHTML = `
                <h3>${maintenanceTools.basic.name}</h3>
                <p>Estimated Cost: ${maintenanceTools.basic.cost}</p>
                <ul>
                    ${maintenanceTools.basic.items.map(item => `<li>${item}</li>`).join('')}
                </ul>
            `;
            basicToolkitSection.appendChild(basicToolDetails);
        }

        if (advancedToolkitSection) {
            const advancedToolDetails = document.createElement('div');
            advancedToolDetails.innerHTML = `
                <h3>${maintenanceTools.advanced.name}</h3>
                <p>Estimated Cost: ${maintenanceTools.advanced.cost}</p>
                <ul>
                    ${maintenanceTools.advanced.items.map(item => `<li>${item}</li>`).join('')}
                </ul>
            `;
            advancedToolkitSection.appendChild(advancedToolDetails);
        }
    }

    // Contact Form Handling
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Message sent! We will get back to you soon.');
            contactForm.reset();
        });
    }

    // Populate content based on current page
    if (document.body.contains(document.getElementById('f1-cars'))) {
        populateRaceCars();
    }

    if (document.body.contains(document.getElementById('online-dealerships'))) {
        populateDealerships();
    }

    if (document.body.contains(document.getElementById('basic-toolkit'))) {
        populateMaintenanceTools();
    }
});
