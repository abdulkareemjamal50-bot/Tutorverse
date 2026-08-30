import {
    initializeApp
} from "https://www.gstatic.com/firebasejs/12.18.0/firebase-app.js";

import {
    getAuth,
    GoogleAuthProvider,
    signInWithRedirect,
    getRedirectResult
} from "https://www.gstatic.com/firebasejs/12.18.0/firebase-auth.js";


const firebaseConfig = {
    apiKey: "AIzaSyBN5yK7jnD0bZmHPQGcUVbkyyIKkuGNCYU",
    authDomain: "tutorverse-3f818.firebaseapp.com",
    projectId: "tutorverse-3f818",
    storageBucket: "tutorverse-3f818.firebasestorage.app",
    messagingSenderId: "909560975681",
    appId: "1:909560975681:web:c4bc3b45ab625c5cd791c0",
    measurementId: "G-6GHMYT5F2Q"
};


console.log("🔥 TutorVerse Firebase JS LOADED");


const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const googleProvider = new GoogleAuthProvider();


const googleButton =
    document.getElementById("google-signin-btn");

const googleButtonText =
    document.getElementById("google-btn-text");

const googleError =
    document.getElementById("google-error");


if (googleButton) {

    googleButton.addEventListener("click", async function () {

        console.log("🔥 Google button clicked");

        if (googleError) {
            googleError.style.display = "none";
        }

        googleButton.disabled = true;

        if (googleButtonText) {
            googleButtonText.textContent =
                "Connecting to Google...";
        }

        try {

            console.log("🔥 Starting Google redirect...");

            await signInWithRedirect(
                auth,
                googleProvider
            );

        } catch (error) {

            console.error(
                "❌ Google redirect error:",
                error
            );

            showError(error.message);
        }

    });

}


async function handleGoogleRedirect() {

    console.log("🔥 Checking for Google redirect result...");

    try {

        const result =
            await getRedirectResult(auth);


        console.log(
            "🔥 getRedirectResult result:",
            result
        );


        if (!result) {

            console.log(
                "⚠️ No Google redirect result found."
            );

            return;
        }


        console.log(
            "✅ Google authentication successful!"
        );

        console.log(
            "Google user:",
            result.user
        );


        const idToken =
            await result.user.getIdToken();


        console.log(
            "✅ Firebase ID token received"
        );


        console.log(
            "🔥 Sending token to Django..."
        );


        const response =
            await fetch(
                "/accounts/firebase-login/",
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken":
                            getCookie("csrftoken")
                    },

                    body: JSON.stringify({
                        idToken: idToken
                    })
                }
            );


        console.log(
            "🔥 Django response status:",
            response.status
        );


        const data =
            await response.json();


        console.log(
            "🔥 Django response:",
            data
        );


        if (
            response.ok &&
            data.success
        ) {

            console.log(
                "🎉 DJANGO LOGIN SUCCESS!"
            );

            window.location.href =
                data.redirect_url;

            return;
        }


        throw new Error(
            data.error ||
            "Django could not complete Google Sign-In."
        );


    } catch (error) {

        console.error(
            "❌ Google redirect processing error:",
            error
        );

        showError(
            error.message ||
            "Google Sign-In failed."
        );
    }

}


function showError(message) {

    if (googleError) {

        googleError.textContent =
            message;

        googleError.style.display =
            "block";
    }

    if (googleButton) {
        googleButton.disabled = false;
    }

    if (googleButtonText) {
        googleButtonText.textContent =
            "Continue with Google";
    }
}


function getCookie(name) {

    let cookieValue = null;

    if (
        document.cookie &&
        document.cookie !== ""
    ) {

        const cookies =
            document.cookie.split(";");

        for (
            let cookie of cookies
        ) {

            cookie = cookie.trim();

            if (
                cookie.substring(
                    0,
                    name.length + 1
                ) === name + "="
            ) {

                cookieValue =
                    decodeURIComponent(
                        cookie.substring(
                            name.length + 1
                        )
                    );

                break;
            }
        }
    }

    return cookieValue;
}


handleGoogleRedirect();