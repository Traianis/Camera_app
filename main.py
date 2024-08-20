import streamlit as st
import streamlit.components.v1 as components

st.title("Flux video live folosind HTML și JavaScript - Camera din spate")

# Cod HTML și JavaScript pentru accesarea camerei și afișarea fluxului video
html_code = """
    <html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Capture Photo</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 0;
      padding: 0;
    }
    #camera {
      width: 100%;
      max-width: 400px;
      height: auto;
      margin: 20px 0;
    }
    #canvas {
      display: none;
    }
    #capture-btn {
      background-color: #4CAF50;
      color: white;
      border: none;
      padding: 10px 20px;
      text-align: center;
      font-size: 16px;
      margin: 10px 0;
      cursor: pointer;
    }
    #capture-btn:hover {
      background-color: #45a049;
    }
    #captured-image {
      display: none;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <h1>Take a Photo</h1>
  <video id="camera" autoplay playsinline></video>
  <button id="capture-btn">Capture</button>
  <canvas id="canvas"></canvas>
  <img id="captured-image" alt="Captured Image" />

  <script>
    const video = document.getElementById('camera');
    const canvas = document.getElementById('canvas');
    const captureBtn = document.getElementById('capture-btn');
    const capturedImage = document.getElementById('captured-image');

    // Accesarea camerei pentru telefoane mobile
    navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } })
      .then(stream => {
        video.srcObject = stream;
      })
      .catch(err => {
        console.error("Error accessing camera: ", err);
      });

    // Capturarea imaginii și afișarea acesteia pe pagină
    captureBtn.addEventListener('click', () => {
      const context = canvas.getContext('2d');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      context.drawImage(video, 0, 0, canvas.width, canvas.height);

      // Convertim imaginea în format Data URL și o afișăm pe pagină
      const imageDataURL = canvas.toDataURL('image/png');
      capturedImage.src = imageDataURL;
      capturedImage.style.display = 'block'; // Afișăm imaginea capturată
    });
  </script>
</body>
</html>
"""

# Integrarea codului HTML și JavaScript în Streamlit
components.html(html_code, height=1000)
if st.button("Închide"):
    st.stop()
