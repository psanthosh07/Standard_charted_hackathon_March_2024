document.addEventListener("DOMContentLoaded", function() {
    var videoStream;

    function startCamera() {
        if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
            navigator.mediaDevices.getUserMedia({ video: true })
            .then(function(stream) {
                var video = document.getElementById('video');
                videoStream = stream;
                video.srcObject = stream;
                video.play();
            })
            .catch(function(err) {
                console.error('Error accessing the camera:', err);
            });
        }
    }

    var canvas = document.getElementById('canvas');
    var context = canvas.getContext('2d');
    var video = document.getElementById('video');
    var captureButton = document.getElementById('captureButton');
    var retryButton = document.getElementById('retryButton');
    var registerForm = document.getElementById('registerForm');

    captureButton.addEventListener('click', function() {
        // Set canvas dimensions to match video dimensions
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        // Pause the video
        video.pause();
        // Draw the current frame onto the canvas
        context.drawImage(video, 0, 0, canvas.width, canvas.height);
        // Stop the video stream
        if (videoStream) {
            videoStream.getTracks().forEach(track => track.stop());
        }
        // Hide the video element
        video.style.display = 'none';
        // Show the canvas element
        canvas.style.display = 'block';
        // Show the register form
        registerForm.style.display = 'block';
        // Hide the capture button
        captureButton.style.display = 'none';
    });

    retryButton.addEventListener('click', function() {
        // Show video element
        video.style.display = 'block';
        // Hide canvas element
        canvas.style.display = 'none';
        // Show capture button
        captureButton.style.display = 'block';
        // Restart camera
        startCamera();
    });

    // Start the camera initially
    startCamera();
});
