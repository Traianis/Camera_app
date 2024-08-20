import streamlit as st
import streamlit.components.v1 as components

st.title("Flux video live folosind HTML și JavaScript - Camera din spate")

# Cod HTML și JavaScript pentru accesarea camerei și afișarea fluxului video
html_code = """
    <!DOCTYPE html>
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
  </style>
</head>
<body>
  <h1>Take a Photo</h1>
  <video id="camera" autoplay playsinline></video>
  <button id="capture-btn">Capture</button>
  <canvas id="canvas"></canvas>

  <script>
    const video = document.getElementById('camera');
    const canvas = document.getElementById('canvas');
    const captureBtn = document.getElementById('capture-btn');

    // Accesarea camerei pentru telefoane mobile
    navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } })
      .then(stream => {
        video.srcObject = stream;
      })
      .catch(err => {
        console.error("Error accessing camera: ", err);
      });

    // Capturarea imaginii și trimiterea acesteia către server
    captureBtn.addEventListener('click', () => {
      const context = canvas.getContext('2d');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      context.drawImage(video, 0, 0, canvas.width, canvas.height);

      // Convertim imaginea într-un Blob și trimitem către server
      canvas.toBlob(blob => {
        const formData = new FormData();
        formData.append('photo', blob, 'photo.png');

        // Trimiterea imaginii folosind Fetch API către pagina "test.com"
        fetch('https://localhost:8000/upload', {
          method: 'POST',
          body: formData
        })
        .then(response => response.text())
        .then(data => {
          console.log('Success:', data);
        })
        .catch(error => {
          console.error('Error:', error);
        });
      }, 'image/png');
    });
  </script>
</body>
</html>

"""

# Integrarea codului HTML și JavaScript în Streamlit
components.html(html_code, height=1000)
if st.button("Închide"):
    st.stop()
