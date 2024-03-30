const textarea = document.getElementById('js-text');
const qrDiv = document.getElementById('js-qr');
const submitBtn = document.getElementById('js-submit');

submitBtn.addEventListener('click', () => {
    const text = textarea.value;
    const url = `/qrcode?text=${encodeURIComponent(text)}`;

    fetch(url)
        .then(response => {
            if (response.ok) {
                return response.text();
            } else {
                try {
                    throw new Error(response.text());
                } catch (error) {
                    throw new Error('Failed to generate QR code');
                }
            }
        })
        .then(data => {
            qrDiv.innerHTML = `<img src="${data}" alt="QR Code">`;
        })
        .catch(error => {
            qrDiv.textContent = error.message;
        });
});