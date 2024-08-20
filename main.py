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
    <p id="permission-message" style="color: red; display: none;"></p> <!-- Afișare mesaj de permisiune -->
    </div>

    <script>
    var video = document.getElementById('video');
    var canvas = document.getElementById('canvas');
    var context = canvas.getContext('2d');
    var capturedImage = document.getElementById('captured-image');
    var permissionMessage = document.getElementById('permission-message');

    // Verificăm permisiunile înainte de a cere acces la cameră
    navigator.permissions.query({ name: 'camera' }).then(function(permissionStatus) {
        if (permissionStatus.state === 'denied') {
            // Dacă permisiunea a fost refuzată
            permissionMessage.innerText = "Permisiunea de a accesa camera a fost refuzată. Vă rugăm să o permiteți din setările browserului.";
            permissionMessage.style.display = 'block';
        } else if (permissionStatus.state === 'prompt') {
            // Dacă permisiunea nu a fost încă acordată
            permissionMessage.innerText = "Browserul va solicita permisiunea de a accesa camera.";
            permissionMessage.style.display = 'block';
        }
    });

    // Funcția pentru accesarea camerei
    function startCamera() {
        navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } })
            .then(function(stream) {
                video.srcObject = stream;
                permissionMessage.style.display = 'none'; // Ascundem mesajul dacă permisiunea este acordată
            })
            .catch(function(err) {
                console.log("Eroare la accesarea camerei: " + err);
                permissionMessage.innerText = "Nu s-a putut accesa camera. Verificați permisiunile.";
                permissionMessage.style.display = 'block';
            });
    }

    // Începem camera automat când pagina este încărcată
    startCamera();

    // Capturăm imaginea la apăsarea butonului
    document.getElementById('capture').addEventListener('click', function() {
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        context.drawImage(video, 0, 0, canvas.width, canvas.height);

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
