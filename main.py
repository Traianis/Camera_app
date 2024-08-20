import streamlit as st
import streamlit.components.v1 as components

st.title("Flux video live folosind HTML și JavaScript")

# Cod HTML și JavaScript pentru accesarea camerei și afișarea fluxului video
html_code = """
    <div>
        <video id="video" width="100%" height="auto" autoplay></video>
        <button id="capture">Capturează imagine</button>
        <canvas id="canvas" style="display:none;"></canvas>
        <img id="captured-image" style="display:none;" alt="Captured Image"/>
    </div>

    <script>
    // Accesăm camera
    var video = document.getElementById('video');
    var canvas = document.getElementById('canvas');
    var context = canvas.getContext('2d');
    var capturedImage = document.getElementById('captured-image');

    // Inițializăm fluxul video
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function(stream) {
            video.srcObject = stream;
        })
        .catch(function(err) {
            console.log("Eroare: " + err);
        });

    // Capturăm imaginea la apăsarea butonului
    document.getElementById('capture').addEventListener('click', function() {
        // Setăm dimensiunea canvas-ului la dimensiunile video-ului
        //canvas.width = video.videoWidth;
        //canvas.height = video.videoHeight;
        
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
