document.addEventListener('DOMContentLoaded', (event) => {
    // Set current year in footer
    document.getElementById('current-year').textContent = new Date().getFullYear();

    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Add active class to current navigation item
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    const sections = document.querySelectorAll('main section');

    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (pageYOffset >= sectionTop - sectionHeight / 3) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href').substring(1) === current) {
                link.classList.add('active');
            }
        });
    });

    // Form submission handling with validation
    const contactForm = document.querySelector('.contact-form form');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            if (validateForm()) {
                // Here you would typically send the form data to a server
                // For this example, we'll just show an alert
                alert('Thank you for your message! I will get back to you soon.');
                contactForm.reset();
            }
        });
    }

    // Form validation function
    function validateForm() {
        let isValid = true;
        const name = document.getElementById('name');
        const email = document.getElementById('email');
        const message = document.getElementById('message');

        if (name.value.trim() === '') {
            isValid = false;
            showError(name, 'Name is required');
        } else {
            removeError(name);
        }

        if (email.value.trim() === '') {
            isValid = false;
            showError(email, 'Email is required');
        } else if (!isValidEmail(email.value)) {
            isValid = false;
            showError(email, 'Please enter a valid email address');
        } else {
            removeError(email);
        }

        if (message.value.trim() === '') {
            isValid = false;
            showError(message, 'Message is required');
        } else {
            removeError(message);
        }

        return isValid;
    }

    function showError(input, message) {
        const formGroup = input.closest('.form-group');
        const error = formGroup.querySelector('.invalid-feedback') || document.createElement('div');
        error.className = 'invalid-feedback';
        error.textContent = message;
        if (!formGroup.querySelector('.invalid-feedback')) {
            formGroup.appendChild(error);
        }
        input.classList.add('is-invalid');
    }

    function removeError(input) {
        const formGroup = input.closest('.form-group');
        const error = formGroup.querySelector('.invalid-feedback');
        if (error) {
            formGroup.removeChild(error);
        }
        input.classList.remove('is-invalid');
    }

    function isValidEmail(email) {
        const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(String(email).toLowerCase());
    }
    
});

const toggleButton = document.getElementById('toggle-dark-mode');
const bodyElement = document.body;

toggleButton.addEventListener('click', function() {
  bodyElement.classList.toggle('dark-mode');

  if (bodyElement.classList.contains('dark-mode')) {
    toggleButton.textContent = 'Switch to Light Mode';
  } else {
    toggleButton.textContent = 'Switch to Dark Mode';
  }
});
