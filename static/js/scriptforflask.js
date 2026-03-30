console.log("JS loaded");

// ================= PLAY BUTTON =================
const playButton = document.getElementById("play-btn");

if (playButton) {
    playButton.addEventListener("click", () => {
        window.location.href = "/start";
    });
}


// ================= POPUPS =================
const difficultyPopup = document.getElementById("difficulty-popup");
const instructionsPopup = document.getElementById("instructions-popup");
const hintPopup = document.getElementById("hint-popup");

const difficultyBtn = document.getElementById("difficulty-btn");
const instructionsBtn = document.getElementById("instructions-btn");
const hintBtn = document.getElementById("hint-btn");

const difficultyOptions = document.querySelectorAll(".difficulty-option");
const display = document.getElementById("difficulty-display");

// OPEN POPUPS
if (difficultyBtn) {
    difficultyBtn.addEventListener("click", () => {
        difficultyPopup.classList.add("active");
    });
}

if (instructionsBtn) {
    instructionsBtn.addEventListener("click", () => {
        instructionsPopup.classList.add("active");
    });
}

if (hintBtn) {
    hintBtn.addEventListener("click", () => {
        hintPopup.classList.add("active");
    });
}

// CLOSE POPUPS
[difficultyPopup, instructionsPopup, hintPopup].forEach(popup => {
    if (popup) {
        popup.addEventListener("click", (e) => {
            if (e.target === popup) {
                popup.classList.remove("active");
            }
        });
    }
});


// ================= DIFFICULTY =================
difficultyOptions.forEach(button => {
    button.addEventListener("click", () => {
        const level = button.textContent.trim(); // "Easy", "Medium", "Hard"

        if (display) {
            display.textContent = "Difficulty Level: " + level;
        }

        fetch("/set_difficulty", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ difficulty: level })
        });

        difficultyPopup.classList.remove("active");
    });
});


// ================= QUIZ =================
const options = document.querySelectorAll(".options");
const nextBtn = document.getElementById("next-btn");
const prevBtn = document.getElementById("prev-btn");

// OPTION CLICK
options.forEach((option, index) => {
    option.addEventListener("click", () => {

        fetch("/answer", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ answer: index })
        });

        options.forEach(opt => opt.style.backgroundColor = "");
        option.style.backgroundColor = "lightblue";
    });
});


// ================= NAVIGATION =================
if (nextBtn) {
    nextBtn.addEventListener("click", () => {
        fetch("/next", { method: "POST" })
        .then(() => {
            window.location.href = "/quiz";
        });
    });
}

if (prevBtn) {
    prevBtn.addEventListener("click", () => {
        fetch("/prev", { method: "POST" })
        .then(() => {
            window.location.href = "/quiz";
        });
    });
}


const reviewNextBtn = document.getElementById('review-next-btn')
const reviewPrevBtn = document.getElementById('review-prev-btn')


// ================= QUIZ =================
const reviewOptions = document.querySelectorAll(".review-options");

// OPTION CLICK
reviewOptions.forEach((option, index) => {
    option.addEventListener("click", () => {

        fetch("/answer", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ answer: index })
        });

        options.forEach(opt => opt.style.backgroundColor = "");
        option.style.backgroundColor = "lightblue";
    });
});


if (reviewNextBtn) {
    reviewNextBtn.addEventListener("click", () => {
        fetch("/review_next", { method: "POST" })
        .then(() => {
            window.location.href = "/review";
        });
    });
}

if (reviewPrevBtn) {
    reviewPrevBtn.addEventListener("click", () => {
        fetch("/review_prev", { method: "POST" })
        .then(() => {
            window.location.href = "/review";
        });
    });
}


// ================= FINAL PAGE =================
const returnBtn = document.getElementById("return-btn");
const reviewBtn = document.getElementById("review-btn")


if (returnBtn) {
    returnBtn.addEventListener("click", () => {
        window.location.href = "/";
    });
}

if (reviewBtn) {
    reviewBtn.addEventListener("click",()=>{
        window.location.href = "/review";
    })
}

// ================= REVIEW PAGE =================

