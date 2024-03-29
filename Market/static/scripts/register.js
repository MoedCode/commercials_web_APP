function displayPhoto(event) {
    const input = event.target;
    if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const preview = document.getElementById('photo-preview');
            preview.src = e.target.result;
            preview.style = "width: 25%; height: 25%;"
            preview.style.display = 'block';
            resizeImage(input.files[0]);
        }
        reader.readAsDataURL(input.files[0]);
    }
}

function resizeImage(file) {
    const maxFileSize = 1024 * 1024; // 1MB
    const maxWidth = 800;
    const maxHeight = 600;

    if (file.size > maxFileSize) {
        console.log("Image size exceeds 1 megabyte. Resizing...");
        // Resize image
        const img = new Image();
        img.onload = function() {
            const canvas = document.createElement('canvas');
            let width = img.width;
            let height = img.height;

            // Resize image if necessary
            if (width > maxWidth || height > maxHeight) {
                if (width / maxWidth > height / maxHeight) {
                    width = maxWidth;
                    height = Math.round(width * img.height / img.width);
                } else {
                    height = maxHeight;
                    width = Math.round(height * img.width / img.height);
                }
            }

            canvas.width = width;
            canvas.height = height;
            const ctx = canvas.getContext('2d');
            ctx.drawImage(img, 0, 0, width, height);
            const resizedDataURL = canvas.toDataURL(file.type);

            // Update preview with resized image
            const preview = document.getElementById('photo-preview');
            preview.src = resizedDataURL;
        };
        img.src = URL.createObjectURL(file);
    }
}