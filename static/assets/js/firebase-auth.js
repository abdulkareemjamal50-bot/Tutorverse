import {
    initializeApp
} from "https://www.gstatic.com/firebasejs/12.18.0/firebase-app.js";

import {
    getAuth,
    GoogleAuthProvider,
    signInWithPopup
} from "https://www.gstatic.com/firebasejs/12.18.0/firebase-auth.js";


// ============================================================
// FIREBASE CONFIGURATION
// ============================================================

// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyBN5yK7jnD0bZmHPQGcUVbkyyIKkuGNCYU",
    authDomain: "tutorverse-3f818.firebaseapp.com",
    projectId: "tutorverse-3f818",
    storageBucket: "tutorverse-3f818.firebasestorage.app",
    messagingSenderId: "909560975681",
    appId: "1:909560975681:web:c4bc3b45ab625c5cd791c0",
    measurementId: "G-6GHMYT5F2Q"
};

// ============================================================
// INITIALIZE FIREBASE
// ============================================================

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const googleProvider = new GoogleAuthProvider();


// ============================================================
// GOOGLE LOGIN BUTTON
// ============================================================

const googleButton = document.getElementById("google-signin-btn");
const googleButtonText = document.getElementById("google-btn-text");
const googleError = document.getElementById("google-error");


if (googleButton) {

    googleButton.addEventListener("click", async function () {

        googleError.style.display = "none";

        googleButton.disabled = true;
        googleButtonText.textContent = "Connecting to Google...";

        try {

            // Open Google sign-in
            const result = await signInWithPopup(
                auth,
                googleProvider
            );


            // Get Firebase ID token
            const idToken = await result.user.getIdToken();


            // Send token to Django
            const response = await fetch(
                "/accounts/firebase-login/",
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": getCookie("csrftoken")
                    },

                    body: JSON.stringify({
                        idToken: idToken
                    })
                }
            );


            const data = await response.json();


            // Django login successful
            if (response.ok && data.success) {

                window.location.href = data.redirect_url;

                return;
            }


            throw new Error(
                data.error ||
                "Django could not complete Google Sign-In."
            );

        }

        catch (error) {

            console.error(
                "Google Sign-In Error:",
                error
            );

            googleError.textContent =
                error.message ||
                "Google Sign-In failed. Please try again.";

            googleError.style.display = "block";

            googleButton.disabled = false;

            googleButtonText.textContent =
                "Continue with Google";
        }

    });

}


// ============================================================
// GET DJANGO CSRF COOKIE
// ============================================================

function getCookie(name) {

    let cookieValue = null;

    if (document.cookie && document.cookie !== "") {

        const cookies = document.cookie.split(";");

        for (let cookie of cookies) {

            cookie = cookie.trim();

            if (
                cookie.substring(
                    0,
                    name.length + 1
                ) === name + "="
            ) {

                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );

                break;
            }
        }
    }

    return cookieValue;
}