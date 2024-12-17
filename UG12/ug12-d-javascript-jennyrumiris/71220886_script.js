// Script buat ganti warna
const bodyElement = document.body;
const colors = ['lightblue', 'lightgreen', 'pink', 'silver', 'white'];
let colorIndex = 0;
    function gantiWarnaRandom() {
        bodyElement.style.backgroundColor = colors[colorIndex];
        colorIndex = (colorIndex + 1) % colors.length;
    }

// Script buat ganti tulisan header
const headerElement = document.querySelector('.header h1');
const texts = [
    'Hello World!',
    'Coding is Fun!',
    'I love JS!',
    'Welcome to My WebPage!',
    'Enjoy Your Visit!'
];
let textIndex = 0;
    function gantiTeks() {
        headerElement.textContent = texts[textIndex];
        textIndex = (textIndex + 1) % texts.length;
    }    