import streamlit as st
import streamlit.components.v1 as components

st.title("Flux video live folosind HTML și JavaScript - Camera din spate")

# Cod HTML și JavaScript pentru accesarea camerei și afișarea fluxului video
html_code = """
    <div style="text-align: center;">
        <video id="video" width="100%" height="auto" autoplay style="border: 1px solid black;"></video>
        <br>
        <button id="capture">Capturează imagine</button>
        <canvas id="canvas" style="display:none;"></canvas>
        <img id="captured-image" style="display:none;" alt="Captured Image"/>
    </div>

    <script>
    // Accesăm camera din spate
    var video = document.getElementById('video');
    var canvas = document.getElementById('canvas');
    var context = canvas.getContext('2d');
    var capturedImage = document.getElementById('captured-image');

    // Inițializăm fluxul video cu suport pentru camera din spate
    navigator.mediaDevices.getUserMedia({ video: { facingMode: { exact: 'environment' } } })
        .then(function(stream) {
            video.srcObject = stream;
        })
        .catch(function(err) {
            console.log("Eroare la accesarea camerei: " + err);
        });

    // Capturăm imaginea la apăsarea butonului
    document.getElementById('capture').addEventListener('click', function() {
        // Setăm dimensiunea canvas-ului la dimensiunile video-ului
        // canvas.width = video.videoWidth;
        // canvas.height = video.videoHeight;

        // Test
        canvas.width = 550;
        canvas.height = 400;
        context.drawImage(video, 0, 0, canvas.width, canvas.height);

        // Convertim imaginea în data URL și o afișăm
        var dataURL = canvas.toDataURL('image/png');
        capturedImage.src = dataURL;
        capturedImage.style.display = 'block';
    });
    </script>
"""

# Integrarea codului HTML și JavaScript în Streamlit
components.html(html_code, height=1000)
if st.button("Închide"):
    st.stop()
